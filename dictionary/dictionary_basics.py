#create a dictionary
dictionary={'name':'pramod','age':32,'height':5.8,'weight':68}

print(dictionary)

#create using dict function

dict_new=dict(name='Pramod',age=32,weight=67,height=5.8)

print(dict_new)

#keys and values and items

print(dict_new.keys())
print(dict_new.values())
print(dict_new.items())
#accessing values

print(dict_new['name'])

for i in dict_new.values():
    print(i)

#accesing key value in pairs
for x,y in dict_new.items():
    print('key is  :' + str(x) , 'value is : '+ str(y))


#check for key or values or items in dictionary 

print('name' in dict_new)
print('Pramod' in dict_new.values())

print(('name','Pramod') in dict_new.items())