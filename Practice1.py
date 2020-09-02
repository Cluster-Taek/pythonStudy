import cmath
import math

#변수
print("#변수\n")

#1
kScore = 50
mScore = 80
eScore = 30
print("1.","Avg : %.2f" %((kScore + mScore + eScore) / 3))

#2
num1 = 409298570
if num1 % 2 == 0 :
    print('2.',num1," : 짝수")
else :
    print('2.',num1," : 홀수")

#3
s1 = "국어:수학:영어:프로그래밍"
print('3.',s1.split(':'))

#4
list1 = [1, 70, 3, 80, 5]
list1.reverse()
print('4.',list1)

#5
list2 = ["파이썬은", "정말", "편하다"]
print('5.'," ".join(list2))

#6
list3 = [1, 50, 410, 10, 3, 4, 5]
list3.sort()
print('6.',list3)

#7
s2 =  " I love python "
print('7.',s2.strip())

#제어문
print("\n#제어문\n")

#1
sum1 = 0
for i in range(1, 101) :
    sum1 += i
print('1.',sum1)

#2
sum2 = 0
i = 1
while i < 101 :
    sum2 += i
    i += 1
print('2.',sum2)

#3
sum3 = 0
for i in range(1, 101) :
    if i % 3 == 0 :
        sum3 += i
print('3.',sum3)

#4
list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in range(0, len(list)) :
    sum += list[i]
print('4.',"Avg : %.2f" %(sum/len(list)))

#5
list = [1, 3, 5, 40, 90, 100, 2020]
for i in range(0, len(list)) :
    if list[i] % 2 == 1 :
        list[i] *= 2
print('5.',list)

#6
print('6.')
for i in range(0, 5) :
    for j in range(0, i + 1) :
        print('*', end = '')
    print()

#함수와 입출력
print("\n#함수와 입출력\n")

#1
def gradeResult(score) :
    if score <= 100 and score >= 80 :
        print("A")
    elif score < 80 and score >= 50 :
        print("B")
    elif score < 50 and score >= 30 :
        print("C")
    elif score < 30 and score >= 0 :
        print("F")
    else :
        print("잘못 입력하셨습니다.")
gradeResult(int(input('1. 점수 입력 : ')))

#2
def evenResult(num) :
    if num % 2 == 0 :
        return True
    else :
        return False
print(evenResult(int(input('2. 숫자 입력 : '))))

#3
def personalNum(pNum) :
    if(len(pNum) < 14) :
        return
    print(pNum[:2], end='년생, ')
    if(pNum[7] == '1') :
        print("남자")
    elif(pNum[7] == '2') :
        print("여자")
    else :
        print("알 수 없음")
personalNum(input('3. 주민등록번호 입력 : '))

#4
def calcFunction(num1, sign, num2) :
    if sign == '+' :
        return num1 + num2
    elif sign == '-' :
        return num1 - num2
    elif sign == '*' :
        return num1 * num2
    elif sign == '/' :
        if(num2 == 0) :
            return "0으로는 나눌 수 없습니다."
        return num1 / num2
    elif sign == '%' :
        if(num2 == 0) :
            return "0으로는 나눌 수 없습니다."
        return num1 % num2
    else : 
        return "잘못 입력하셨습니다"
print(calcFunction(int(input('4. 숫자 입력 : ')), input('부호 입력 : '), int(input('숫자 입력 : '))))

#5
def changeFunction(money) :
    list = [50000,10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    for i in range(0,len(list)) :
        print("%d원 : %d개" %(list[i], money / list[i]))
        money = money % list[i]
    
changeFunction(int(input('5. 숫자 입력 : ')))

#6
def equationResult(equation) :
    a = int(equation.split("x^2")[0])
    b = int(equation.split("x^2")[1].split("x")[0])
    c = int(equation.split("x^2")[1].split("x")[1])
    disc = (b * b) - (4 * a * c)
    if disc < 0 :
        x1 = (- b + cmath.sqrt(disc)) / (2 * a)
        x2 = (- b - cmath.sqrt(disc)) / (2 * a)
    else :
        x1 = (- b + math.sqrt(disc)) / (2 * a)
        x2 = (- b - math.sqrt(disc)) / (2 * a)
    print("x1 = ",x1)
    print("x2 = ",x2)
    
equationResult(input('6. 이차방정식 입력 : '))

#CLEAR
print("\n수고하셨습니당")
