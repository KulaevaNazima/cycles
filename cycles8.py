# 8. Есть переменная которая хранит в себе число:
#    Необходимо написать следующие условия для проверки переменной:
#        1. Это число трёхзначное?
#        2. Это число положительное и чётное?
#        3. Это число делится на 31 без остатка?
#        4. Если это число больше 100 и оно делится на 17 без остатка 
# или это число больше 150 и равно 13**2 тогда показать что это за число
a = int (input("Vvedite chislo: "))
if a>100 and a <1000:
    print ("3 значное")
if a >0 and (a%2)==0:
    print ("Polozhitelnoe i chetnoe")
if a%31==0:
    print ("Delitsa na 3 bez ostatka")
if a>100 and a%17==0:
    print (a)
if a>150 and a ==13**2:
    print (a)