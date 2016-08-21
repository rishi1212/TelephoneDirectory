list1=[]
list2=[]
dict1={}
temp=100
n=input("Enter the number of players : ")
for i in range(0,n):
    name1=raw_input("Enter your team name: ")
    num=raw_input("Enter your player name: ")
    list1.extend([name1])
    list2.extend([num])
    dict1=dict(zip(list1,list2))#to convert two list into dictionary
print dict1
print """
    1:Add a player
    2:details of player by giving team name
    """
choice=input("Enter your choice")
def add(dict1):
    name3=raw_input("Enter the team name: ")
    num3=raw_input("Enter player name: ")
    dict1[name3]=num3
    print dict1
def search(dict1,n,list1,temp):
    name2=raw_input("Enter the team name ")
    for i in range(0,n):
        if list1[i]==name2:
            print list2[i]
if (choice==1):
    add(dict1)
elif (choice==2):
   search(dict1,n,list1,temp)