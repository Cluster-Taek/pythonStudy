import random
import time
import datetime
import Practice2_module as m

#1
print("1.")
list = []

for i in range(45) :
    list.append(i + 1)

lotto = random.sample(list, 6)
lotto.sort()
print(lotto,"\n")

#2
print("2.")
if __name__ == "__main__" :
    while 1 :
        list = m.inputNum()
        m.caculate(list[0],list[1],list[2])
        s = input("그만하시겠습니까? y/n : ")
        if(s == "y") :
            break

#3
a = input("3. 문자열 입력 : ")
print("문자열의 개수 :",len(a))
print("가장 큰 문자열 :", max(a))
print("뒤집은 문자열 :", a[::-1],"\n")

#4
print("4.")
dt = datetime.datetime.now()
p = datetime.timedelta(days=49, hours=1, minutes=8, seconds=7)
print("현재 :", dt.strftime("%Y년%m월%d일 %H시%M분%S초"))
print("미래 :", (dt + p).strftime("%Y년%m월%d일 %H시%M분%S초"),"\n")

#5
print("5.")
if __name__ == "__main__" :
    voca = {"apple": "사과", "banana": "바나나","pineapple": "파인애플","koptimizer": "고광종교수님"}
    m.selectMenu(voca)

#End
print("수고하셨습니당~~~!")

    
    
