
#tuple
#since tuple is indexed you can access the items with indices (negative or positive)
#once element is defined it cannnot be changed terme is used immutable 
my_tuple = ("yashi","arya","gourav",100,10.1,10+2j)  #in complex we use j in place fo i so keep in mind
print(my_tuple)
print(type(my_tuple))
a = ("python",)  #bracket and in end at comma(,) so it wil comvert the elemets in tuple type 
print(type(a))
print(my_tuple[0]) # we are using square bracket for slicing the list or tuple 
print(my_tuple[-1])
print(my_tuple[0][0])
tup = 10,20,30,40    # if we seperate elemments with commoa so python will understand it is a tuple
print(type(tup)) 
print(tup[1:4])
print(tup[ : ])
my_tuple2 = ("yashi","arya","gourav",100,10.1,10+2j,(10,20,30,40))
print(my_tuple2[6][1])
#example of list
my_list2 = ["yashi","arya","gourav",100,10.1,10+2j,(10,20,30,40)]
print(type(my_list2))
my_list2[3]="mad max"
print(my_list2)
#back to tuple  
print(len(my_tuple))   # len counts the number of element present in the list or tuple
print(tup.count(0))  # check the number specifically present in the element
print(tup.index(20))
tuple3 = my_tuple + my_tuple2   # its add the types of staement 
print(tuple3) 
print(min(tup))      # its check the min value adn how it tell by the ASCII table and itdentity on that
# keep in mind that we can't find min on mix of two different  data type
print(max(tup))
print(sum(tup))
print()
# see the differnce between dot(.)method and difference between methods 
for i in tup:
    print(i)
if 10 in tup:       # memebership programming (it is in membership)
    print("i love you")
else:
    print("bhaag yeah se i dont know")


list = input("enter an integer: ")
i = 0
while len(list) == 0:
    list.append(i)
    i += 1

print(list,"/n")

#set constructor
d = [1,2,3,4,"hi"]
print(type(d))

d = [1,2,3,4,"hi",1,2,3,4]
e = set(d)
print(e)
print(type(e))

t = "python"
e = set(t)
print(e)

t = "pythonp"
e = set(t)
print(e)

A = {1,2,3,4,5}
B = A    #shallow method
print(A)
print(B)

#.add method 
#one element at a time 
A = {1,2,3,4,5}
A.add(6)
B = A 
print(A)
print(B)

#copy()method 
# the method copy() is used to make a copy.deep copy
A = {1,2,3,4,5}
B = A.copy
print(A)
print(B)

#update method 
# it will get update in A not in B 

A = {1,2,3,4,5}
A.update([6,7,8,9])
print(B)


# remove method in set 
A = {1,2,3,4,5}

A.remove(2)
A = B
print(A)
print(B)


# python set operations 
a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
c = {11,333,455,666}
print(a|b) #for union  
print(a.union(b)) # for union  
print(b.union(a))
print(a&b)# intersection
print(a.intersection(b))
print(a&c)
print(a-b)#difference 
print(a.difference(b))
print(b.difference(a))
print(a^b) #set symmetric differnce
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a-b)
print(a)


A = {1,2,3,4,5}
B = {4,5,6,7,8} 
print(A-B)
print(A.difference_update(B)) # remove all the element of other set from this set 
print(B.difference_update(A))
print(A)
print(B)

#set1.isdisjoint(set2) : returns true if two sets have a null intesrection 
x = {11,12,13,14,15}
y = {14,15,16,17,18}
z = {19,20,21,22,23,24}
o = {} #EMPTY SET
print(x.isdisjoint(y))
print(x.isdisjoint(z))
#all(): returns true; if all the elements of the set are true (or if the set is empty)
print(all(x)) # output is true 
print(all(x)) # outpt will be false if we add 0 in set 
print(all(z))
# any();returns true if any elemts of the set is true.if the set is empty,returns false
print(any(x))
print(any(o))
print(max(x))
print(min(x)) # max function returns the largest items in the set
L = {"g","a","o","d"}
print(max(L))
print(min(L)) # min function returns the samllest items in the set 
 
#sorted(): return a new sorted list from elemnts in the set(does not sort the set itself)
a = {1,2,3,4,5,-10,-5,-100}
print(sorted(a))
print(a)
b = {"a","b","c","A","B","C"}
print(sorted(b))
print(b)
print(sum(a)) # sum(): returns the sum of all elements in the set

#frozenset
# new clas that has the cahrectersitics os a set but its elements cannot be cahnged once assigned while tuple are immutable lists,frosets are immutable sets
#frozenset can be created using the frzenset() function
x = frozenset({11,12,13,14,15})
print(x)
print(type(x))
print(x.add(6))
print(x.remove(11))

x = frozenset({11,12,13,14,15})
y = frozenset({14,15,16,17,18})
print(x.copy)
print(x.intersection(y))
print(x.difference(y))

print(x.symmetric_difference(y))
print(x.union(y))

ab = input("enter a list: ")
c = set()
for i in ab:
    c.add(i)
print("the number of unique charater in the string is",len(c))

#---------------------------------------------------
#python dictionary 
"""mutable
unordered
each item has a key-value pair
keys are unique
key are used to acess an item 
usually keys are stings.but it may be numbers also 
each key-value pair is separated by comma(,)
each key is separated from value by: 
key and value are spearted by collan(:)"""

score = {"india":300,"pak":1,"aus":200}
print(score)
print(type(score))
a = {} #empty dic
print(a)
print(type(a))
b = set() #empty set
print(b) 
dic1 = {1:"hello",2:"how are you ?",3:"fine"}
print(dic1)
print(type(dic1))
#remember we can use integer,float ,complex and as well as string
# we can also have a mix
# if we want to update value we can use [i am talking baout below example]
score2 = {"india":300,"pak":1,"aus":200,"india":350}
print(score2)
print(type(score2))
#keys are case sensitive
score3 = {"india":300,"pak":1,"aus":200,"INDIA":"hello"}
print(score3)
print(type(score3))

# accessing dictionary elements 
print(score3["INDIA"])# we are accessing the elments from its key value
# if we have similar key then update value will be printed keep in mind
print(score3.get("pak")) #we are using the .get method 
print(score3.get("INDIA"))
print(score3.get("NZ")) # in get method it will give none for non present element 

#print(score3["NZ"]) # but in this case this will give an error 
score3["SA"]=256 #this line will insert in dictinoary 
print(score3)

#updating elemnts in dictinoary
score3["india"]=588
print(score3)

#del (del is a keywords)
del score3 ["pak"]
print(score3)

# this will only print value 
print(score3.values())

#this will only print keywords 
print(score3.keys())

# display both key and values
print(score3.items())

#len is a function and it will display the length
print(len(score3))

#pop method 
score3.pop("INDIA")
print(score3)

#popitem() will remove the last inserted items from dictionary
score3.popitem()
print(score3)

#clear() clears the item not the dictionary or tuple or set
score3.clear()
print(score3)
print(len(score3))
# print(dic(score3)) = this will give error 

score3 = score #copy the dictionary 
print(score3)
print(score)
# this will be update in both
# shawllow copy 
score3["wz"]=687
score3["bam"]=163
print(score)

#deep copy
# deep copy mai change nahi hota 😁
score = {"india":300,"pak":1,"aus":200}
score4 = dict(score)
print(score4)
score["SA"]=256 
print(score)

#nested dictionary 
x = {"fruit":{"name":"apple","color":"red"},"vegetable":{"name":"chilli","color":"green"}}
print(x)
print(x.get("fruit"))
print((x.get("fruit")).get("color"))
#membership opertor
#the membership opertor in and not in is alos applicable in dictionary
score = {"india":300,"pak":1,"aus":200}
if "india" in score:
    print("yes!!,its a membership opertor")

else:
    print("error")

#now for nested dic
if "color" in x["fruit"]:
    print("yes!!,its a membership opertor")

#   
else:
    print("error")

#
for i in score:
    print(i)

#
for i in score.values():
    print(i)

#
for i in score:
    print(score.get(i))

#
for i,j in score.items():
    print(i,j)

# uniquq character 
#create a program that determines and display the number the number of unique charater in a string entered by the user.
#for exmple.hello,world! has 10 unique charater while zzz has only one unique charater.
#use a dictionary or set to solve this question

string = {"fruit":"apple","vegetable":"chilli"}
dictionary = {}
for char in string:
    if( char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char]=1
for char in dictionary:
    print(char,' -> ',dictionary[char])

assign_number = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1,
                "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3,"Q":10,"R":1, "S":1,
                "T":1, "U":1, "V":4, "W":4, "X":8, "Y":4, "Z":10}
x = 0
m = input("enter a string: ")
for i in m():
    x = x+a[i]
print('{} is the total score of the word {}'.format(x,m))
