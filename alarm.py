#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from collections import OrderedDict
from openpyxl import load_workbook

file_path = r"C:\Users\eamashu\Documents\workspace\Bharti_XLS_Automation\test_inp_file.txt"
celluecnt_file = r"C:\Users\eamashu\Documents\workspace\Bharti_XLS_Automation\celluecnt.txt"
cell_file = r"C:\Users\eamashu\Documents\workspace\Bharti_XLS_Automation\cell.txt"
output_xls_file = r"C:\Users\eamashu\Documents\workspace\Bharti_XLS_Automation\myxls.xlsx"
cmd_dict = {}
with open(file_path, 'rt') as file:
	text = file.read()
	txt_cmd_list = text.split("MML Command-----")[1:]
	for cmd in txt_cmd_list:
		cmd_name=cmd.split(":;")[0]

		if cmd_name in cmd_dict.keys():
			cmd_dict[cmd_name] += cmd
		else:
			cmd_dict[cmd_name] = cmd


df = pd.DataFrame([cmd_dict])
#print(df['DSP CELLUECNT'].values)

np.savetxt(celluecnt_file, df['DSP CELLUECNT'].values, fmt='%s')
np.savetxt(cell_file, df['DSP CELL'].values, fmt='%s')
# for key, val in cmd_dict.items():
    # if key=='DSP CELLUECNT':
        # import pdb;pdb.set_trace()
        # print(val)



def write_xls(f_name, op_name, sheet_name):
    datafile = None
    s = []
    e = []
    tmpdf = None
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
            
        #book = load_workbook(output_xls_file)
        #writer = pd.ExcelWriter(output_xls_file, engine = 'openpyxl')
        #writer.book = book
        if sheet_name == 'DCP CELL':
            book = load_workbook(output_xls_file)
            writer = pd.ExcelWriter(output_xls_file, engine='openpyxl')
            writer.book = book
            writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
            maindf.to_excel(writer, sheet_name = sheet_name, index=False)
            writer.save()
        else:
            maindf.to_excel(output_xls_file, sheet_name = sheet_name, index=False)

        

write_xls(celluecnt_file, 'celluecnt', 'DSP CELLUECNT')
write_xls(cell_file, 'cell', 'DCP CELL')