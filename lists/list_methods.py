
###########################
# Adding Items to List
###########################

#create a sample list
country=['india','uk','usa','china','germany']

#append Vs Extend Vs Insert
# Append adds only one item at a time at the end of list 
# Extend adds multiple items at a time at the end of the list
# Insert items adds one item at a time at any index of the list

country.append('brazil')
print(country)

#country.append('belgium','france')
#returns error

country.append(['belgium','france'])
#add the items as nested list
print(country)

#Extend can add multiple items at a time
country.extend(['belgium','france'])

print(country)

#check len for append vs extend

## Insert 

#insert item at a given postion

country.insert(3,'spain')
print(country)

#insert a nested list (-1) add to second last index as it counts number of records in previous version of list and then adds at that index
country.insert(-1,['germany','austria'])
print(country)


#alternative 
country.insert(len(country),'dubai')
print(country)

###########################
# Deleting Items from List
###########################

# Clear Vs Pop Vs Remove

# clear removes all items of the items 
# Pop removes a single item from the list
# Remove 


#clear example
country.clear()
print(country)

#pop example
#it removes the item at given index and return it 
#if no index is provided , it removes the last item of th list and returns it 

country=['india','uk','usa','china','germany']
print(country.pop())
print(country)

#pop using index
print(country.pop(1))
print(country)

#Remove example
#instead of index , we provide item / value that needs to be removed
#removes the first occurence of the value /item in the list 
country=['india','uk','usa','china','germany']
country.remove('uk')
print(country)

# remove list of items from a list 
#we can use sets,filter,lambda , list comprehension etc

###########################
# Other methods of List
###########################

#Index | Count | Sort | Reverse | Join 

#index
#returns the index of specified value or item in the list 

print(country.index('india'))

#Count
#returns the number of times the item/value occurs in the list

num_list=[1,2,3,4,2,4,5,2,3,4,2,3,4,2,5,5,6]
print(num_list.count(2))

#reverse
#reverses the order of the list 
country=['india','uk','usa','china','germany']
country.reverse()
print(country)

#sort
#sorts the items in ascending (deafult) or descending order
num_list.sort()
print(num_list)


#join (string method)
#mainly used to convert lists into strings /words

word_list=['I' , 'want','to','become','an','expert']

print(' '.join(word_list))

word_list=['I' , 'want','to','become','an','expert']

print('|'.join(word_list))




