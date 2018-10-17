playlist={'name':'fun_time',
    'genre':'pop',
    'movie':[
        {'title':'love yatri','year':2018,'actors':['sohail','arbaaz'],'duration':3.5},
        {'title':'sultan','year':2016,'actors':['salman','anushka'],'duration':5.5},
        {'title':'lakshya','year':2007,'actors':['hrithik','preity'],'duration':4.2}
        ]
}

print(playlist)

#print year for each song

for i in playlist['movie']:
    print(i['year'])

#total time of playlist

total_time=0

for i in playlist['movie']:
    
    total_time +=i['duration']

print(total_time)