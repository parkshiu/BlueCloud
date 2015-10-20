decimal = 10
result = ''
while (decimal>0):
    remainder = decimal % 2
    decimal = decimal/2
    result = str(remainder) + result
print result






sentence = "I love you"
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence
print reverse_sentence




print "구구단 몇단을 계산할까요?"
x=1
while(x<>0):
    x=int(raw_input())
    if x==0: break
    if not(1<=x<=9):
        print "잘못입력하셨습니다.","1부터 9사이 숫자를 입력해줏요"
        continue
    else:
        print "구구단 " + str(x) +"단을 계산합니다"
        for i in range(1,10):
            print str(x) +"X"+ str(i) +"="+ str(x*i)
        print "구구단 몇단을 계산할까요(1~9)?"
print "구구단 게임을 종료합니다."



import random
guess_number=random.randint(1,100)
print "숫자를 맞춰보세요(1~100)"
users_input=int(raw_input())
while(users_input<>guess_number):
        if users_input>guess_number:
            print "숫자가 너무 큽니다"
        else:
            print "숫자가 너무 작습니다."
        users_input=int(raw_input())
else: print "게임을 종료합니다."



