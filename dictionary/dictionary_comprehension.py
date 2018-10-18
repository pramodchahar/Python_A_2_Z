# {_:_ for _ in _ }

my_dict={'age':23,'salary':10,'weight':60,'height':5.8}

#using traditional for loop

for key,value in my_dict.items():
    print(value**2)

#using dictionary comprehension

print({key:value**2 for key,value in my_dict.items()})
print({value**2 for key,value in my_dict.items()})


name_1='PRAMOD'
name_2='CHAHAR'

combo={name_1[i]:name_2[i] for i in range(0,len(name_1))}

print(combo)

#uppercase a dictionary

my_dict={'name':'ziaan','team':'chelsea','loc':'bangalore','food':'fish','player':'hazard'}

print({key.upper():value.upper() for key,value in my_dict.items()})


#conditonal logic with dict comprehensions

num_list=[1,2,3,4,5]

#traditional way 
new_dict={}

for i in num_list:
    if i %2==0:
        new_dict.update({i:'even'})
    else:
        new_dict.update({i:'odd'})

print(new_dict)

#using dict comprehension

print({i:('even' if i%2==0 else 'odd') for i in num_list})


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]


for i in range(len(list1)):
    print(list1[i] +':' + list2[i])

#create dictionary using dict comprehension

answer={list1[i]:list2[i] for i in range(len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer={}
for i in person:
    answer.update({i[0]:i[1]})
print(answer)

#using dict comprehension

new_answer={i[0]:i[1] for i in person}

print(new_answer)

#alternate solution

print({k:v for k,v in person})

#other solution

print(dict(person))


#create dictionary like below
#{'a':0,'e':0,'i':0,'o':0,'u':0}

print({i:0 for i in ['a','e','i','o','u']})

print({char:0 for char in 'aeiou'})


#create dictionary to map ASCII keys to characters

answer = {count: chr(count) for count in range(65,91)}

print(answer)


