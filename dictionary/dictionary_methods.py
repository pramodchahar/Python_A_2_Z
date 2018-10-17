#methods for dictionary 

my_dict={'name':'ziaan','age':2,'team':'chelsea','loc':'bangalore','food':'fish','player':'hazard'}

#clear

my_dict.clear()

print(my_dict)

#copy
my_dict={'name':'ziaan','age':2,'team':'chelsea','loc':'bangalore','food':'fish','player':'hazard'}

new_dict=my_dict.copy()

print(new_dict)

#get

print(my_dict.get('food'))

#pass any key which is not present , it returns None

print(my_dict.get('new'))


#pop 
#takes the argument as key and removes the key value pair

my_dict.pop('name')

print(my_dict)


#update
#adds the new values to dictionary 

new_dict={'salary':10}


my_dict.update(new_dict)

print(my_dict)

my_dict.update({'test':'cleared'})

print(my_dict)

