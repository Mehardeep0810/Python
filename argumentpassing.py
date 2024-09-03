"""
def nameAge(name,age):
    print(f'Name= {name} and age= {age}');
    
"There are 2 types of arguments in python a. positional b. keyword"
    
nameAge(name="abc",age=40)"positional arguments"
nameAge(age=40, name="abc")"positional arguments"

nameAge("abc",40)"keyword arguments"
nameAge(40,"abc")"keyword arguments"
"""

"""
def pos_arg(a=55,b=0,c=0):
    print(f'The value of a is : {a}')
    print(f'The value of a is : {b}')
    print(f'The value of a is : {c}')
def main():
    pos_arg(c=20)
"constructor in python"
if __name__ == '__main__':
    main()
"""

"""
def minus(a,b):
    print(a)
    print(b)
    return a-b
a,b=20,10
result=minus(b,a)
print(result)
"""

"""
def strings(*args):"to call all the values"
    print(args)
def details(**args):"if we want to use 2 method then use **args"
    print(args)
strings(1,2,"Hello","everybody","chitkara")
details(name="chitkara", age=40)
"""

"""
main data types in python

STRING


LIST = ordered changable and allow duplicate values
eg. [1,2,3,4]

a=[1,2,3,4]
a
[1, 2, 3, 4]
type(a)
<class 'list'>
b=(1,2,3,4)
b
(1, 2, 3, 4)
type(b)
<class 'tuple'>
c={1,2,3,4}
c
{1, 2, 3, 4}
type(c)
<class 'set'>

a={1:'a',2:"b",3:"c"}
a
{1: 'a', 2: 'b', 3: 'c'}
type(a)
<class 'dict'>

{1: ['a','x','y'], 2: 'b', 3: 'c'}"To add multiple values in dictionary use [] after key"
type(a)
<class 'dict'>

a=[1,2,3,4]
a[0:3]
[1, 2, 3]

a[0:]
[1, 2, 3, 4]

a[:]
[1, 2, 3, 4]

a[-1]
4

a[:3]
[1, 2, 3]

a[1:4]
[2, 3, 4]

a[1:-2]
[2]

a[-1:-2]
[]

a.append(5)"It is suitable only to add one value at the end"
a
[1, 2, 3, 4, 5]


a.extend([6,7])"This will add 6 and 7 at 2 different indexes"
a
[1, 2, 3, 4, 5, 6, 7]


a.append([8,9])"this will give one index to both"
a
[1, 2, 3, 4, 5, 6, 7, [8, 9]]


a.insert(1,15)"1 is index at which we want to insert, 15 is the value that we want to insert at the 1 index."
a
[1, 15, 2, 3, 4, 5, 6, 7, [8, 9]]

a.pop()"it will remove last element"
[8, 9]


a.remove(1)"The value in  bracket is not index but value"
a.remove(1)
a
[15, 2, 3, 4, 5, 6, 7]


a.insert(6,15)
a
[15, 2, 3, 4, 5, 6, 15, 7]


b= a.copy()
b
[15, 2, 3, 4, 5, 6, 15, 7]


a.count(15)
2


a.reverse()
a
[7, 15, 6, 5, 4, 3, 2, 15]

b "The copied value will not change"
[15, 2, 3, 4, 5, 6, 15, 7]

a.sort()
a
[2, 3, 4, 5, 6, 7, 15, 15]


a[::]
[2, 3, 4, 5, 6, 7, 15, 15]


a[0:7:2]
[2, 4, 6, 15]


a[0:7:3]"initial value: final value: steps"
[2, 5, 15]




TUPLE = unordered unchangable
eg. (1,2,3,4)
//only 2 methods
count
and
index

tuple=(1,2,3,4,5)
type(tuple)
<class 'tuple'>

t1=("apple","mango","apple","orange")
t1
('apple', 'mango', 'apple', 'orange')

t2=(1,"apple",4.5,"a",2,3)
t2
(1, 'apple', 4.5, 'a', 2, 3)

t1.count("apple")
2

t1.index("apple")
0

you can use differnt data types in tuple but cannot change it

SET = ordered and unchangable
will not support duplicate values
the copy method removes the previous value of the set
in deffernce common elements are eleminated, originality of set in not changed
in difference_update method originality of set is changed
eg. {"red","blue","black"}

s1={1,2,3,4,5}
type(s1)
<class 'set'>

s1={1,2,3,4,5}
s2={3,4,"a",4.5}
s3={"apple","orange","grapes"}
s1
{1, 2, 3, 4, 5}
s2
{'a', 3, 4.5, 4}
s3
{'grapes', 'apple', 'orange'}
s3.add("apple")
s3
{'grapes', 'apple', 'orange'}

s3.add("xyz")
s3
{'grapes', 'apple', 'xyz', 'orange'}

s3.add("abc")
s3
{'grapes', 'xyz', 'orange', 'apple', 'abc'}

s4={1,2,3,4}
s4.clear()
s4
set()

s5=set({1,2,3,4})
type(s5)
<class 'set'>

s1
{1, 2, 3, 4, 5}
s2
{'a', 3, 4.5, 4}
s3
{'grapes', 'xyz', 'orange', 'apple', 'abc'}
s4
set()
s2= s1.copy()
s2
{1, 2, 3, 4, 5}
s1
{1, 2, 3, 4, 5}

s2
{1, 2, 3, 4, 5}
s2={4,5,6,7,8}
s2
{4, 5, 6, 7, 8}
s1
{1, 2, 3, 4, 5}
s2.difference(s1)
{8, 6, 7}

s1.difference(s2)
{1, 2, 3}

s1.difference_update(s2)
s1
{1, 2, 3}

s2.discard(8)
s2
{4, 5, 6, 7}

s1
{1, 2, 3}
s2
{4, 5, 6, 7}
s1.intersection(s2)
set()

s1={1,2,3,4}
s1
{1, 2, 3, 4}
s2
{4, 5, 6, 7}
s1.intersection(s2)
{4}

s1.intersection_update(s2)
s1
{4}

s2
{4, 5, 6, 7}
s2.issubset(s2)
True

s2.issubset(s1)
False

s1.issubset(s2)
True

s3
{'grapes', 'xyz', 'orange', 'apple', 'abc'}
s3.pop()
'grapes'

s3
{'xyz', 'orange', 'apple', 'abc'}
s1
{4}

s1={1,2,3,8,9,10}
s2
{4, 5, 6, 7}
s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s2.union(s1)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

DICTIONARY = ordered* (* means in versions after 3.6 dictionary will be ordered in all the versions) changable and do not allow duplicate values
eg. {key:values}

"""
