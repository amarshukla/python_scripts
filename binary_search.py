def binsearch(lst, t):
  big_index = 0 
  end_index = len(lst) - 1
  while big_index <= end_index:
    mid_pos = big_index + (end_index - big_index) //2
    mid_item = lst[mid_pos]

    if t == mid_item:
      return mid_pos
    elif t < mid_item:
      end_index = mid_pos - 1
    else:
      big_index = mid_pos + 1
  return None    
print(binsearch(lst, 4))
