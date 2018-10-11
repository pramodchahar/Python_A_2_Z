###########################
# Slicing of List
###########################

# makes new lists using slices or parts of original lists 

# list_name[start:end:step]

 #sort of similar to range(start,end,step size)


num_list=[11,22,33,44,55,66,77,88,99]

print(num_list[3:])

print(num_list[5:])

print(num_list[-1:])

print(num_list[-3:])

print(num_list[:])

print(num_list[:3])

print(num_list[4:7])

print(num_list[-4:8])

print(num_list[::3])

print(num_list[::-3])



# modify part of list

num_list[2:5]=['a','b','c']

print(num_list)
