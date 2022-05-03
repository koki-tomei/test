# -*- coding: utf-8 -*-

#1
print("Welcome to Hagiwara Lab.")

#2
for i in range(1,31):
  if (i%15==0):
    print("FizzBuzz")
  elif(i%3==0):
    print("Fizz")
  elif(i%5==0):
    print("Buzz")
  else:print(i)

#3
print("stressed"[::-1])

#4
print("パタトクカシーー"[::2])
print("パタトクカシーー"[1::2])

#5
li5=[]
for i in range(1,11):
  li5.append(i*i)
print(li5)

#6
print([x*x for x in range(1,11)])

#7
def split_word(sen):
  sen=sen.replace(",","")
  sen=sen.replace(".","")
  words =sen.split(" ")
  return words

words =split_word("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
counts =[len(w) for w in words]
print(counts)

#8
head1_list =[1,5,6,7,8,9,15,16,19]
words=split_word("Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
dic={}
for i in range(len(words)):
  if(i+1 in head1_list):
    v=words[i][0]
  else:
    v=words[i][0:2]
  dic[v] =i+1
print(dic)





