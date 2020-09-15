#2_Module

def inputNum() :
    print("숫자, 연산자, 숫자 입력")
    try :
        a = input()
        b = input()
        c = input()
        return a,b,c
    except :
        print("다시 입력해주세요")

def caculate(a,b,c) :
    try :
        a = int(a)
        c = int(c)
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
        else :
             print("계산할 수 없는 식입니다.")
    except :
        print("계산할 수 없는 식입니다.")
                
        
#5_Module

def addVoca(voca) :
    try :
        a = input("추가(Eng:Kor) : ")
        eng = a.split(":")[0].strip().lower()
        kor = a.split(":")[1].strip().lower()
        if(eng in voca) :
            print("이미 저장되어있습니다.")
        else :
            voca.setdefault(eng, kor)
            print("저장되었습니다.")
    except :
        print("잘못 입력하셨습니다.")

def search(voca) :
    try :
        for key,value in sorted(voca.items()) :
            print(key, ":", value)
    except :
        print("자료가 없습니다.")

def eSearch(voca) :
    eng = input("영어 : ").strip().lower()
    if(eng in voca) :
        print("한글 :", voca.get(eng))
    else :
        print("등록되지 않은 자료입니다.")
    
def kSearch(voca) :
    kor = input("한글 : ").strip()
    if(kor in voca.values()) :
        for key, value in voca.items() :
            if(kor == value) :
                print("영어 :",key)
    else :
        print("등록되지 않은 자료입니다.")

def selectMenu(voca) :
    while(1) :
        print("\nMENU #단어추가 #전체조회 #영어로검색 #한글로검색 #종료")
        a = input("\n# : ")
        if(a == "단어추가") :
            addVoca(voca)
        elif(a == "전체조회") :
            search(voca)
        elif(a == "영어로검색") :
            eSearch(voca)
        elif(a == "한글로검색") :
            kSearch(voca)
        elif(a == "종료") :
            break
        else :
            print("잘못 입력하셨습니다.\n")
