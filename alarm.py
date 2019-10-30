#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Author: Amar Shukla (eamashu)

from datetime import date
import pandas as pd
import numpy as np
from collections import OrderedDict
from openpyxl import load_workbook


class AlarmParser:
    """
    This class reads alarm file containing tabular and non-tabular data.
    It creates 2 Ad-hoc files for DSP CELLUECNT and DSP CELL commands.
    It then creates an xls containing tabular data of these 2 Adhoc files in seperate sheets inside same xls.
    Once everything is completed, Adhoc files gets deleted.
    """
    
    def __init__(self, alarm_file_path, celluecnt_file_dir):
        self.alarm_file_path = alarm_file_path
        self.celluecnt_file = celluecnt_file_dir + '\celluecnt.txt'
        self.cell_file = celluecnt_file_dir + '\cell.txt'
        today = str(date.today())
        self.output_xls_file = celluecnt_file_dir + '\alarm_output'+today+'.xlsx'
        self.cmd_dict = {}

    def read_alarm_full_file(self):
        """
        This function reads full alarm file containing data from various commands.
        Creates a dictionary where keys are command names and value is command output.
        """
        
        with open(self.alarm_file_path, 'rt') as file:
            text = file.read()
            txt_cmd_list = text.split("MML Command-----")[1:]
            for cmd in txt_cmd_list:
                cmd_name=cmd.split(":;")[0]

                if cmd_name in self.cmd_dict.keys():
                    self.cmd_dict[cmd_name] += cmd
                else:
                    self.cmd_dict[cmd_name] = cmd

    
    def write_adhoc_files(self):
        """
        Write 2 Adhoc files for 2 DSP commands.
        """
        try:
            self.read_alarm_full_file()
            df = pd.DataFrame([self.cmd_dict])
            np.savetxt(self.celluecnt_file, df['DSP CELLUECNT'].values, fmt='%s')
            np.savetxt(self.cell_file, df['DSP CELL'].values, fmt='%s')
            return 0
        except Exception as e:
            return e


    def write_xls(self, f_name, op_name, sheet_name):
        """
        Write final xls file containing 2 sheets.
        """
        
        datafile = None
        s = []
        e = []
        tmpdf = None
        try:
            with open(f_name) as f:
                datafile = f.readlines()
                for idx,line in enumerate(datafile):

                    if 'Local' in line:
                        s.append(idx)
                    if '(Number of results' in line:
                        e.append(idx)
                maindf = pd.DataFrame()
                for i in range(len(s)):
                    head = list(datafile[s[i]].split("  "))
                    head = [x for x in head if x.strip()]
                    tmpdf = pd.DataFrame(columns=head)
                    for l_ in range(s[i]+1,e[i]):
                        da = datafile[l_]
                        if len(da)>1:
                            data = list(da.split("  "))
                            data =  [x for x in data if x.strip()]
                            tmpdf = tmpdf.append(dict(zip(head,data)),ignore_index=True)
                    maindf = pd.concat([maindf,tmpdf], sort=False)
                try:    
                    if sheet_name == 'DCP CELL':
                        book = load_workbook(output_xls_file)
                        writer = pd.ExcelWriter(output_xls_file, engine='openpyxl')
                        writer.book = book
                        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
                        maindf.to_excel(writer, sheet_name = sheet_name, index=False)
                        writer.save()
                    else:
                        maindf.to_excel(output_xls_file, sheet_name = sheet_name, index=False)
                except Exception as e:
                    return e
        except Exception as e:
            return e
            

    def instantiate_writer(self):
        """
        This function calls file writing function to write xls file with 2 sheets.
        """
        
        res = self.write_adhoc_files()
        if res == 0:
            ret_1 = self.write_xls(self.celluecnt_file, 'celluecnt', 'DSP CELLUECNT')
            ret_2 = self.write_xls(self.cell_file, 'cell', 'DCP CELL')

            if ret_1 or ret_2 is not None:
                print("Error writing file and reason is as below -\n")
                print(ret_1,"\n",ret_2)
        else:
            print("Some error occurred writing adhoc files")
