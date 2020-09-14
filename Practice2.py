import random
import time
import datetime

#1
print("1.")
list = []

for i in range(45) :
    list.append(i + 1)

lotto = random.sample(list, 6)
print(lotto,"\n")

#2
print("2.")
while 1 :
    print("숫자, 연산자, 숫자 입력")
    try :
        a = int(input())
        b = input()
        c = int(input())
    except :
        print("다시 입력해주세요")
        continue
    if b == "+" :
        print(a, "+", c, "=", a+c)
    elif b == "-" :
        print(a, "-", c, "=", a-c)
    elif b == "*" :
        print(a, "*", c, "=", a*c)
    elif b == "/" :
        try :
            print(a, "/", c, "=", a/c)
        except ZeroDivisionError as e:
            print("0으로는 나눌 수 없습니다.")
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
voca = {"apple": "사과", "banana": "바나나","pineapple": "파인애플","koptimizer": "고광종교수님"}
def add() :
    try :
        a = input("추가(eng:kor) : ")
        eng = a.split(":")[0].strip()
        kor = a.split(":")[1].strip()
        if(eng in voca) :
            print("이미 저장되어있습니다.")
        else :
            voca.setdefault(eng, kor)
            print("저장되었습니다.")
    except :
        print("잘못 입력하셨습니다.")

def search() :
    try :
        for key,value in voca.items() :
            print(key, ":", value)
    except :
        print("자료가 없습니다.")

def eSearch() :
    eng = input("영어 : ").strip()
    if(eng in voca) :
        print("한글 :", voca.get(eng))
    else :
        print("등록되지 않은 자료입니다.")
    
def kSearch() :
    kor = input("한글 : ").strip()
    if(kor in voca.values()) :
        for key, value in voca.items() :
            if(kor == value) :
                print("영어 :",key)
    else :
        print("등록되지 않은 자료입니다.")

    
    
while(1) :
    print("\nMENU #단어추가 #전체조회 #영어로검색 #한글로검색 #종료")
    a = input("\n# : ")
    if(a == "단어추가") :
        add()
    elif(a == "전체조회") :
        search()
    elif(a == "영어로검색") :
        eSearch()
    elif(a == "한글로검색") :
        kSearch()
    elif(a == "종료") :
        break
    else :
        print("잘못 입력하셨습니다.\n")


    
    
