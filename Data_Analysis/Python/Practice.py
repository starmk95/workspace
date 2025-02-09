def ex1_1():
    a = 20
    b = 30
    c = a+b
    print(c)

def ex1_2():
    x=20
    Computer = 'Mac'
    Age = 30
    My_score = 70
    _name = '김민규'
    myBirthYear = 1997
    data2 = 20.3
    print(x, Computer, My_score, _name, myBirthYear, data2)

def ex1_19():
    eng = 100
    result = '영어점수 ' + str(eng) + '점'
    print(result)
    print('영어점수 {}점'.format(eng))

def ex1_29():
    year = 2025
    month = 2
    day = 6
    print(year,month,day, sep='/')
    print(year,f"{month:02d}",f"{day:02d}", sep='/')

def ex1_30():
    a='안녕하세요'
    b='반갑습니다'
    print(a)
    print(b)
    print('\n\n')
    print(a, end=" ")
    print(b)

def ex1_32():
    name = input("이름을 입력하세요 : ")
    print("{}님 반갑습니다.".format(name));

def ex3_5():
    sum=0
    for i in range(1, 101):
        if i%3 ==0:
            sum+=i
    print("1~100에서 3의 배수의 합계 = {}".format(sum))

def ex3_11():
    n1 = int(input("첫 수를 입력하세요 : "))
    n2 = int(input("끝 수를 입력하세요 : "))
    n = int(input("합계를 구하고자 하는 배수를 입력하세요 : "))

    sum = 0
    i = n1
    while i<n2+1:
        if(i%n==0):
            sum+=i
        i+=1
    print("{}부터 {} 사이 중 {}의 배수들의 총 합은 {}입니다".format(n1,n2,n,sum))

def reverse_sentence():
    sentence = input("거꾸로 뒤집을 문장을 입력하세요 : ")
    i = len(sentence)-1
    while(i>=0) :
        print('%s' %sentence[i], end='')
        i-=1
    print()

def ex4_3():
    a = [10,20,30,40,50,60,70,80,90,100]
    x = a.index(30)
    print(x)
    a.pop(x)
    print(a)
    a.remove(90)
    print(a)
    a.clear()
    print(a)

def ex5_2():
    tuple1 = ('a','b','c')
    tuple2 = ('d','e','f')
    tuple3 = tuple1 + tuple2
    print(tuple3)
    print(len(tuple3))
    for x in tuple1:
        print(x)
    del tuple1

def gugudan():
    dans = (2,3,4,5,6,7,8,9)
    print("구구단표")
    print('-'*30)

    for dan in dans:
        for i in range(1,10):
            print('%d x %d = %d' %(dan, i, dan*i))
        print('-'*30)

def matchWord(word, answer):
    if word == answer:
        msg = "맞아용"
    else:
        msg = "ㄴㄴ"
    return msg

def execute_matchWord():
    eng_dict = {'orange' : '오렌지', 'cookie' : '쿠키', 'mother' : '어머니', 'brother' : '형제', 'python' : '파이썬'}
    for key in eng_dict:
        string = input(eng_dict[key] + '에 맞는 영어 단어는? ')
        result = matchWord(string, key)
        print(result)

# ex1_1
# ex1_2()
# ex1_19()
# ex1_29()
# ex1_30()
# ex1_32()
# ex3_5()
# ex3_11()
# reverse_sentence()
# ex4_3()
# ex5_2()
# gugudan()
execute_matchWord()