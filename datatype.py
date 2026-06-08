J = {'name': 'Mohan','sport':'kabaddi','strength': 7,'role': 'defender'}
print(J['role'] == 'rider' )
# print(J['role'].update('rider'))
J['role'] = 'rider'
print(J['role'] == 'rider' )

list
a=[1,2,3,4,5]
print(a)

b=['vanaja','aneesha','sneha','sri']
print(b)

#positive index
a=['python','java','c++','ruby']
print(a[0])

#negative index
print(a[-1])

b=[1,2,3,4,5]
print(b[1:4])
print(b[1:])
print(b[:4])
print(b[:])

#list=['python','sql','ai']
a[1]='power bi'
print(a)

append_list=['sql','ai']
a.append(append_list)
print(a)

insert_list=['ai','ml']
a.insert(2,insert_list)
print(a)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list = list1 + list2

list.remove(3)
list.pop(2)
print(list)
del list[0]
print(list)
list.clear()
print(list)
print(len(list))
list=[1,2,3,4,5]
print(list.count(2))
list.index(4)
number=[3,4,5]
number.sort()
print(number)
number.sort(reverse=True)
print(number)
list.reverse()
list[::-1]
print(list)
new_list = list.copy()
print(new_list)

for i in range(len(list)):
    print(list[i])

for i in range(1,11):
    print(i)
    