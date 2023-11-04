# modifiable variant type: list, dict,set
# un-modifiable variant type: str,tuple

# str,tuple-- unmodifiable variant copy- shadow copy - only copy the reference address of the variant
# 不可变类型的变量
# copy：只复制变量地址
# deepcopy：
# 如果子对象有可变类型，deepcopy对每一层对象都开辟新的内存空间
# 如果子对象没有可变类型，deepcopy只copy对象的reference地址
from copy import copy, deepcopy

str='laura'
t=(1,2,3,'asdf','asd',{'d':'w'})

print(f'-----string copy----')
str1=copy(str)
print(f' copied str is: {str1}')
print(f' original string id is: {id(str)}')
print(f' copied string id is: {id(str1)}')
print(f'-----tuple copy----')
t1=copy(t)
print(f' copied tuple is: {t1}')
print(f' original tuple id is: {id(t)}')
print(f' copied tuple id is: {id(t1)}')
print(f' original tuple id is: {id(t[5])}')
print(f' copied tuple id is: {id(t1[5])}')
# list,set,dict-- modifiable variant copy- shadow copy - only copy the reference address of the variant
# 可变类型的变量
# copy：对变量开辟新的内存空间，不对子变量开辟
# deepcopy：
# 如果子对象是： 可变类型，deepcopy对每一层对象都开辟新的内存空间
# 如果子对象是：不可变类型，deepcopy只copy对象的reference地址
l=[1,2,3,4]
print(f'-----list copy----')
l1=deepcopy(l)
print(f' copied list is: {l1}')
print(f' original list id is: {id(l)}')
print(f' copied list id is: {id(l1)}')
print(f' original list id is: {id(l[3])}')
print(f' copied list id is: {id(l1[3])}')