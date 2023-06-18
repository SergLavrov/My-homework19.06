
# 11.120.
# В массиве хранится информация о росте 35 человек. Определить, сколько
# человек имеют самый большой рост.

someList = [175, 195, 185, 169, 190, 189, 195, 174, 195]
cnt = 0
maxNumber = max(someList)

for index in range(len(someList)):
    if someList[index] == maxNumber:
        cnt += 1
print(cnt)


# 11.132. Дан массив. Определить:

# а) максимальный элемент массива и элемент, являющийся максимальным
#    без учета этого элемента;

someList = [75, 95, 85, 69, 19, 89, 74, 69]

maxNumber = max(someList)
indexMaxNumber = someList.index(maxNumber)

del someList[indexMaxNumber]
maxNumber1 = max(someList)

print(maxNumber)
print(maxNumber1)

# б) минимальный элемент массива и элемент, являющийся минимальным
#    без учета этого элемента;

someList = [75, 95, 85, 69, 19, 89, 74, 69]

minNumber = min(someList)
indexMinNumber = someList.index(minNumber)

del someList[indexMinNumber]
minNumber1 = min(someList)

print(minNumber)
print(minNumber1)


# в) номера максимального элемента массива и элемента, являющегося
#    максимальным без учета этого элемента

someList = [75, 85, 69, 19, 89, 74, 95, 69]

maxNumber = max(someList)
indexMaxNumber = someList.index(maxNumber)
number = indexMaxNumber + 1

del someList[indexMaxNumber]
maxNumber1 = max(someList)
indexMaxNumber1 = someList.index(maxNumber1)
number1 = indexMaxNumber1 + 1

print(number)
print(number1)

# г) номера минимального элемента массива и элемента, являющегося
# минимальным без учета этого элемента

someList = [25, 85, 45, 19, 89, 74, 95, 70]

minNumber = min(someList)
indexMinNumber = someList.index(minNumber)
number = indexMinNumber + 1

del someList[indexMinNumber]
minNumber1 = min(someList)
indexMinNumber1 = someList.index(minNumber1)
number1 = indexMinNumber1 + 1

print(number)
print(number1)


# 11.145. Дан массив из четного числа элементов. Поменять местами:

#  а) его половины;

someList = [25, 85, 45, 19, 89, 74]

halfIndex = int(len(someList)/2 - 1)

result1 = someList[:halfIndex+1]
result2 = someList[halfIndex+1:]

newSomeList = result2 + result1
print(newSomeList)

# или можно так:

someList = [25, 85, 45, 19, 89, 74]

result1 = someList[:int(len(someList)/2)]
result2 = someList[int(len(someList)/2):]

newSomeList = result2 + result1
print(newSomeList)


#  б) первый элемент со вторым, третий — с четвертым и т. д.;

someList = [25, 85, 45, 19, 89, 74, 15, 10]

someList1 = someList[1::2]
index = 0
index1 = 1

while index < len(someList):
    someList1.insert(index1, someList[index])
    index += 2
    index1 +=2

print(someList1)


#  1.173.
#  Переставить последний элемент массива на место первого. При этом
#  первый, второй, ..., предпоследний элементы сдвинуть вправо на 1 позицию.

someList = [25, 85, 45, 19, 89, 74, 95, 70]
someList.insert(0, someList[-1])
del someList[-1]
print(someList)


