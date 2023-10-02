"""
myList = ["a","b","c"]
print(myList)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is           <ordered> and <changeable>.                     <Allows duplicate members.>
Tuple is a collection which is          <ordered> and <unchangeable>.                   <Allows duplicate members.>
Set is a collection which is            <unordered>, <unchangeable*>, and <unindexed>.  <No duplicate members>.
Dictionary is a collection which is     <ordered**> and <changeable>.                   <No duplicate members>.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

"""

# thislist = list(("apple", "banana", "cherry"))
#
# if "aple" in thislist:
#     print("Yes it has")
# else:
#     print("no")
#
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# thislist[1] = "blackcurrant"
# print(thislist)
#
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist)
# thislist[1:1] = ["blackcurrant", "watermelon"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
for x in thislist:
    print(x)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
for i in range(len(thislist)):
    print(thislist[i])
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop(0)
print(thislist)
del thislist[0]
print(thislist)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
print(thislist)
thislist.clear()
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)