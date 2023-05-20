import random

def password():
  k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  s = ['1','2','3','4','5','6','7','8','9','0']
  rez = ''
  for i in range(11):
    rez += random.choice(k+a+s)
  return rez

d = password()
print('Пароль:',d)
