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




print "������ ����� ����ұ��?"
x=1
while(x<>0):
    x=int(raw_input())
    if x==0: break
    if not(1<=x<=9):
        print "�߸��Է��ϼ̽��ϴ�.","1���� 9���� ���ڸ� �Է����޿�"
        continue
    else:
        print "������ " + str(x) +"���� ����մϴ�"
        for i in range(1,10):
            print str(x) +"X"+ str(i) +"="+ str(x*i)
        print "������ ����� ����ұ��(1~9)?"
print "������ ������ �����մϴ�."



import random
guess_number=random.randint(1,100)
print "���ڸ� ���纸����(1~100)"
users_input=int(raw_input())
while(users_input<>guess_number):
        if users_input>guess_number:
            print "���ڰ� �ʹ� Ů�ϴ�"
        else:
            print "���ڰ� �ʹ� �۽��ϴ�."
        users_input=int(raw_input())
else: print "������ �����մϴ�."



