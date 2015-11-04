a = 23
print a, hex(a), bin(a)


a = 1.2
b = 2.0
print a. is_integer(), b.is_integer()



import math
print round(a), math.ceil(a), math.floor(a)



a = "abcde"
print a[0], a[4]
print a[-1], a[-5]


a = "Gachon University"
print a[0:6], " AND ", a[-9:]
print a[:]
print a[-50:50]
print a[::2], " AND ", a[::-1]


f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while 1: #1은 무한반복
    line = f.readline()
    if not line : break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
print "Number of A Wolrd 'Yesterday'", n_of_yesterday


f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while 1: #1은 무한반복
    line = f.readline()
    if not line : break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
n1_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
n2_of_yesterday = yesterday_lyric.count("Yesterday")
n3_of_yesterday = yesterday_lyric.count("yesterday")
print "Number of A Wolrd 'Yesterday'", n1_of_yesterday
print "Number of A Wolrd 'Yesterday'", n2_of_yesterday
print "Number of A Wolrd 'Yesterday'", n3_of_yesterday



colors = ['red', 'blue', 'green']
print colors[0]
print colors[2]
print len(colors)



a = [5,3,4,1,2]
a.index(2)
print a
a.count(5)
print a
a.sort()
print a
a.reverse()
print a
b = sorted(a)
print b



t = [1, 2, 3]
a, b, c = t
print t, a, b, c




kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print midterm_score[0][2]



student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print student_average




a = [1, 2, 3, 4, 5]
a.append(10)
a.append(20)
print a.pop()
print a.pop()


b = "Shingu University"
a = list(b)
for i in range(len(a)):
    print a.pop()


s = set([1, 2, 3])
s.add(1)
print s
s.remove(1)
print s
s.update([1, 4, 5, 6, 7])
print s
s.discard(3)
print s
s.clear()
print s
