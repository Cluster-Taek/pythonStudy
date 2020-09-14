import random
import time
import datetime

#1
list = []

for i in range(45) :
    list.append(i + 1)

lotto = random.sample(list, 6)
print(lotto)

#2


#3
a = input()
print("문자열의 개수 :",len(a))
print("가장 큰 문자열 :", max(a))
print("뒤집은 문자열 :", a[::-1])

#4
dt = datetime.datetime.now()
p = datetime.timedelta(days=49, hours=1, minutes=8, seconds=7)
print("현재 :", dt.strftime("%Y년%m월%d일 %H시%M분%S초"))
print("미래 :", (dt + p).strftime("%Y년%m월%d일 %H시%M분%S초"))

#5
