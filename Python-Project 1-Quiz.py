q1="""who is the best caption in india ?
a)Rohit sharma
b)virat kohli
c)M.S.Dhoni
d)kapil dev"""
q2="""who is your best friend ?
a)Srikanta
b)Kusuma
c)Suvarna
d)Anil"""
q3="""what is your favourite subject?
a)C
b)C++
c)Java
d)Python"""
q4="""
What is your college name?
a)Aditya
b)IIT Madras
c)Pragati
d)Vishnu"""
q5="""who is your next prime minister in india?
a)Narendra Modi
b)Rahul Gandhi
c)KCR
d)Tagore"""

questions={q1:"a",q2:"b",q3:"d",q4:"c",q5:"a"}

name =input("Hi Whats ur name")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this questions(Yes/No)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow!you got one point")
        score=score+1
        print("Your current score is :",score)
    else:
         print("wrong answer,u lost 1 mark")
         score=score-1
         print("ur current score is",score)
    flag2=input("Do you want to Quit? type (Yes/No)")
    if flag2=="yes":
        break
print("Your total score is",score)
