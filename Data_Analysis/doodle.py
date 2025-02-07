# class MyClass:
#     def __init__(self, number):  # 생성자 수정
#         self.number = number  # 인스턴스 속성

#     def inc_10(self):
#         self.number += 10

#     def inc_20(self):
#         self.number += 20


# # 첫 번째 객체 생성 및 메서드 호출
# obj1 = MyClass(100)  # 초기값 100
# obj1.inc_10()        # 100 + 10 = 110
# obj1.inc_20()        # 110 + 20 = 130
# print(obj1.number)   # 130 출력

# # 두 번째 객체 생성 및 메서드 호출
# obj2 = MyClass(200)  # 초기값 200
# obj2.inc_10()        # 200 + 10 = 210
# obj2.inc_20()        # 210 + 20 = 230
# print(obj2.number)   # 230 출력


class EngSentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.length = len(self.sentence)

    def reverse(self):
        tmp = ''
        for i in range(self.length):
            tmp += (self.sentence[self.length - 1 - i])
        return tmp

    def insertHyphen(self):
        tmp = ''
        for i in range(self.length):
            if self.sentence[i] == ' ':
                tmp += '-'
            else:
                tmp += self.sentence[i]
        return tmp

a = 'We are the champions!'
eng1 = EngSentence(a)
print("역순 : %s" % eng1.reverse())
print("하이픈(-) 삽입 : %s" % eng1.insertHyphen())
