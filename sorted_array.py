#O(n2) code below 
#======================================
lst = [7, 1, 2, 3, 4, 5, 6]
#op [7,1,6,2,5,3,4]
lst = [1, 6, 9, 4, 3, 7, 8, 2]
#op = [9 1 8 2 7 3 6 4]
lst2=[]
for i in range(0, len(lst)):
  if len(lst) > 0:
    high = max(lst)
    lst2.append(high)
    lst.remove(high)
  if len(lst) > 0:
    low = min(lst)
    print(low)
    lst2.append(low)
    lst.remove(low)

print(lst2)
#========================================
#O(n Log n) code below 

def print_alternate_sorted(arr, n):
  i = 0
  j = n-1
  print(arr,n)
  arr.sort()
  while (i < j):
    print(arr[j])
    j -= 1
    print(arr[i])
    i += 1
  
  if n%2 != 0:
    print(arr[i])

lst = [1, 6, 9, 4, 3, 7, 8, 2,0]
n = len(lst)

print_alternate_sorted(lst,n)
#=========================================
#input: 5,23,1,13,9,3,7,63
#output:1,23,5,13,7,3,9,63

def alternate_sort(arr,n):
  i = 0
  j = n-1

  while(i<j):
    if i%2 == 0:
      print(i,arr[i], arr[i+2])
      if arr[i] > arr[i+2]:
        tmp = arr[i]
        arr[i] = arr[i+2]
        arr[i+2] = tmp
    i += 2
    j -= 1   
  print(arr)

lst = [5,23,1,13,9,3,7,63]
n = len(lst)

alternate_sort(lst, n)
