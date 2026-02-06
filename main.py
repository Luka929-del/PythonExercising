# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. თუ რიცხვი
# დადებითია, დაბეჭდოს ეკრანზე “Number
# is
# positive”.
# a = int(input("Enter a number: "))
# if a > 0 :
#     print("Number is positive")
# else:print("number is not positive")
# from curses.textpad import rectangle

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ
# შეამოწმოს, თუ შეყვანილი რიცხვი 10-ის ჯერადია, დაბეჭდოს “რიცხვი ბოლოვდება 0-ით”, თუ
# არადა დაბეჭდოს “რიცხვი არ ბოლოვდება 0-ით”. (გაითვალისწინეთ: 10-ის ჯერადი ნიშნავს
# რომ 10-ზე გაყოფისას ნაშთი არის 0).

# a = int(input("Enter a number: "))
# if a % 10 == 0:
#     print("რიცხვი ბოლოვდება 0-ით")
# else:
#     print("რიცხვი არ ბოლოვდება 0-ით")

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ორ ნებისმიერ რიცხვს. პროგრამამ
# შეამოწმოს, თუ ორივე შეყვანილი რიცხვი 10-ზე მეტია, დაითვალეთ მათი საშუალო
# არითმეტიკული, თუ არადა დაითვალეთ მათი ნამრავლი. დაბეჭდეთ მიღებული შედეგი.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > 10 and b > 10 :
#     print((a + b)/2)
# else:
#     print(a*b)

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ
# რიცხვი დადებითია, დაბეჭდოს ეკრანზე “Number is positive”, თუ რიცხვი
# უარყოფითია, დაბეჭდოს “Number is negative”, თუ არადა დაბეჭდოს “Number
# is equal to zero”.

# a = int(input("Enter a number: "))
# if a > 0 :
#     print("Number is positive")
# elif a < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ 3 რიცხვს. იპოვეთ ამ რიცხვებს
# შორის მინიმუმი და დაბეჭდეთ ეკრანზე (გამოიყენეთ if ოპერატორი).

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else:
#     print(c)

# დაწერეთ პროგრამა, სადაც შეიტანთ (input) ნებისმიერ რიცხვს 0-დან 100-ის ჩათვლით
# და შედეგად გამოიტანს შეფასების შესაბამის ლათინურ დასახელებას შემდეგი სქემის
# მიხედვით. მაგ. თუ შეიტანთ 45-ს, პროგრამამ უნდა დაბეჭდოს FX.

# a = int(input("Enter a number between 0 and 100: "))
# if 91<=a<=100:
#     print("A")
# elif 81<=a<=90:
#     print("B")
# elif 71<=a<=80:
#     print("C")
# elif 61<=a<=70:
#     print("D")
# elif 51<=a<=60:
#     print("E")
# elif 41<=a<=50:
#     print("FX")
# else:
#     print("Failed")

# დაწერეთ პროგრამა, რომლის გაშვებისას შეიყვანთ ნებისმიერ რიცხვს. იპოვეთ
# შეყვანილი რიცხვის ბოლო ორი ციფრი და დაბეჭდეთ ეკრანზე.

# a = int(input("enter a number: "))
# x = a % 10
# a -= a % 10
# a //= 10
# y = a % 10
# print(y , x)

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ წელს და დაადგენთ არის თუ არა
# შეყვანილი რიცხვი ნაკიანი წელიწადი. მაგ: 2012, 2016 წლები ნაკიანია.
# გაითვალისწინეთ,
# ნაკიანია წელიწადი, რომელიც უნაშთოდ იყოფა ოთხზე, გარდა იმ წლებისა რომლებიც
# იყოფა 100-ზე მაგრამ არ იყოფა 400-ზე. მაგ. 2100, 2200, 2300 წლები არ არის ნაკიანი.
# 2000 წელი ნაკიანია.

# a = int(input("enter year: "))
# if a % 4 == 0 and not (a % 100 == 0 and a % 400 != 0):
#     print("წელი ნაკიანია")
# else:
#     print("წელი არ არის ნაკიანი")

# ახალ ხაზზე გადატანა "\n" (Windows Key ს დახმარებით გამოვიყენებ backslash სიმბოლოს)
# როცა მსურს print ფუნქციის გაშვებისას შედეგი რაიმე კონკრეტულით დაბოლოვდეს ვიყენებ (end="")
# print("Luka", end=", You are not child anymore, grow the f up!")
# print("'\n'6 is\neven number")
# print ფუნქციის გამოყენებისას რამდენიმე ატრიბუტის დაშორება ან space ით ან sep ფუნქციითაა შესაძლებელი
# age = 23
# print("Luka","you are",age,"years old")
# print("You are",age,"years old",sep="!")

# a = "My name is Beyonce"
# age = 43
# print('%d' %age)
# print('%f' %age)
# print('%.3f' %age)
# print('%s' %a)
# # ფორმატირებული ბეჭდვა
# print('Hey, %s and i am %d years old' %(a,age))

# დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.
# for i in range(20,126):
#     if i % 5 == 0:
#         print(i)

# დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.
# for i in range(200,24,-1):
#     if i % 8 ==0:
#         print(i)


# შეიყვანთ 2 რიცხვი. ციკლის გამოყენებით დაბეჭდეთ შეყვანილი რიცხვების საერთო გამყოფები. მაგ. 15-ის და
# 18-ის საერთო გამყოფებია: 1, 3

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# for i in range(1,a+1):
#     if a % i == 0 and b % i == 0 :
#         print(i)

# შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო
# არითმეტიკული.

# x = 0
# sum = 0
# while x<10:
#     a = int(input("Enter number: "))
#     sum += a
#     a == 0
#     x += 1
# print(sum/10)


# დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.

# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# დაბეჭდეთ 1500-დან 2100-ის ჩათვლით რიცხვები რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.

# for i in range(1500,2101):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)

# დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი
# ერთდროულად. დაბეჭდეთ მიღებული შედეგი.

# sum = 0
# for i in range(1500, 2101):
#     if i % 7 == 0 and i % 5 == 0:
#         sum += i
# print(sum)

# დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი
# ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული
# ჯამი ეკრანზე.

# sum = 0
# for i in range(1500, 2101):
#     if i % 7 == 0 and i % 5 == 0:
#         sum += i
#         if sum > 20000: break
# print(sum)

# დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.

# sum = 0
# for i in range(1500, 2101):
#     if i % 5 == 0:
#         sum += 1
# print(sum)

# დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue
# ოპერატორი.

# for i in range(15,150):
#     if i % 5 == 0:
#         if i == 50 or i == 75 or i == 80: continue
#         print(i)

# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
# x = 0
# a = int(input("Enter first integer and positive number: "))
# b = int(input("Enter second integer and positive number: "))
# for i in range(1,a+1):
#     if a % i == 0 and b % i == 0 and i > x:
#         x = i
# print(x)

# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.

# usj = 0
# a = int(input("Enter first integer and positive number: "))
# b = int(input("Enter second integer and positive number: "))
# for i in range(1,a*b+1):
#     if i % a == 0 and i % b == 0:
#         usj = i
#         break
# print(usj)


# შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ.
# თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.
# x = 0
# y = 0
# while x < 10:
#     a = int(input("Enter number: "))
#     if a % 2 != 0 and a > y:
#         y = a
#     x += 1
# if y == 0:
#     print("in entered numbers was not any odd number")
# else:print(y)

# შეიყვანეთ რიცხვი კლავიატურიდან. პროგრამამ უნდა დაბეჭდოს შეყვანილი რიცხვის ყველა გამყოფი. (მაგ.
# 18-ის გამოყოფებია: 1, 2, 3, 6, 9, 18)

# a = int(input("Enter number: "))
# for i in range(1,a+1):
#     if a % i == 0:
#         print(i)

# შეიტანეთ რიცხვი. დაადგინეთ შეტანილი რიცხვი არის თუ არა მარტივი რიცხვი და გამოიტანეთ შესაბამისი
# შეტყობინება (გაითვლისწინეთ: მარტივია რიცხვი, რომელსაც აქვს მხოლოდ ორი გამყოფი: ერთი და თავისი
# თავი).

# sum = 0
# a = int(input("Enter number: "))
# for i in range(1,a+1):
#     if a % i == 0:
#         sum += 1
# if sum == 2:
#     print("entered number is simple")
# else:
#     print("entered number is not simple")

# დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.

# for k in range(2,1000):
#     sum = 0
#     for i in range(1,k+1):
#         if k % i == 0:
#             sum += 1
#     if sum == 2:
#         print(k)
#     else:continue
#     sum = 0

# დაბეჭდეთ 0-დან 100-მდე არსებული ფიბონაჩის რიცხვები (ფიბონაჩის რიცხვებია 0, 1, 1, 2, 3, 5, 8, 13, ...).
# a = 0
# b = 1
# c = a + b
# print(a)
# print(b)
# while c < 100:
#     print(c)
#     a = b
#     b = c
#     c = a + b

# შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ.
# a = int(input("Enter number: "))
# sum = 0
# while a > 0:
#     a -= a % 10
#     a /= 10
#     sum += 1
# print(sum)


# შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა ჯამი და დაბეჭდეთ.

# a = int(input("Enter number: "))
# sum = 0
# while a > 0:
#     sum += a % 10
#     a -= a % 10
#     a /= 10
# print(sum)

# შეიყვანეთ ნებისმიერი რიცხი. დაბეჭდეთ შეტანილი რიცხვი შებრუნებული სახით. (მითითება: მაგ. თუ შეიტანთ
# 1254-ს, დაბეჭდოს 4521)

# a = int(input("Enter number: "))
# b = a
# sum = 0
# while a > 0:
#     a -= a % 10
#     a /= 10
#     sum += 1
#
# newnumber = 0
# while sum > 0:
#     newnumber += 10**sum * (b%10)
#     b -= b % 10
#     b /= 10
#     sum -= 1
# newnumber /= 10
# print(int(newnumber))


# შეიყვანეთ ნებისმიერი რიცხი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი.
# (მითითება: პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად
# იკითხება). მაგ. 12521

# a = int(input("Enter number: "))
# b = a
# x = a
# sum = 0
# while a > 0:
#     a -= a % 10
#     a /= 10
#     sum += 1
#
# newnumber = 0
# while sum > 0:
#     newnumber += 10**sum * (b%10)
#     b -= b % 10
#     b /= 10
#     sum -= 1
# newnumber /= 10
#
# if x == int(newnumber):
#     print("ეს რიცხვი პოლინდრომია")
# else:
#     print("ეს რიცხვი არ არის პოლინდრომი")


# შეიყვანეთ რიცხვი. დათვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგ. 5-ის
# ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5

# a = int(input("Enter number: "))
# faqtoriali = 1
# for i in range(1,a+1):
#     faqtoriali *= i
# print(faqtoriali)

# დაწერეთ პროგრამა რომელიც ეკრანზე გამოიტანს შემდეგ გამოსახულებას. მითითება:
# გამოიყენეთ 2 ჩადგმული for ციკლი.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(6):
#     print(i*"*")
# for j in range(4,0,-1):
#     print(j*"*")

# print(abs(-5.6))
# from math import fabs, factorial, fmod, trunc, sqrt, radians
# import random
#
# print(fabs(-4.567))
# print(factorial(5))
# print(fmod(47,9))
# print(trunc(6.78))
# print(sqrt(64))
# print(radians(60))
#
#
# x = random.random()
# print(x)
# y = random.randint(10,100)
# print(y)
# z = random.randrange(10,100,4)
# print(z)
# k = random.uniform(1,10)
# print(k)

# შეიტანეთ ათწილადი რიცხვი, დაამრგვალეთ ათწილად ნაწილში მეათედის სიზუსტით (1
# ციფრი ათწილად ნაწილში) და დაბეჭდეთ შედეგი. გამოიყენეთ round,
# ceil,
# floor,
# trunc
# ფუნქციები სათითაოდ და შეამოწმეთ შედეგი თითოეულის გამოყენებით.

# from math import  ceil,floor,trunc
# a = float(input("enter number: "))
# print(round(a,1))
# print(ceil(a))
# print(floor(a))
# print(trunc(a))



# შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი. გამოიყენეთ
# max
# ფუნქცია.
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))
# print(max(a,b,c))


# გამოთვალეთ 3**8 ფუნქციის გამოყენებით და დაბეჭდეთ შედეგი. ასევე გამოთვალეთ 2**9, 4**6
# და დაბეჭდეთ მიღებული შედეგი.

# print(pow(3,8))
# print(pow(2,9))
# print(pow(4,6))

# გამოთვალეთ ფესვი შემდეგი გამოსახულების შედეგი ფუნქციის გამოყენებით:
# ა) 225625
# ბ) 4225
# from math import sqrt
# print(sqrt(225625))
# print(sqrt(4225))


# დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი დიაპაზონიდან 0-დან 1-ის
# ჩათვლით. დაამრგვალეთ რიცხვი (3 ციფრი ათწილად ნაწილში) და დაბეჭდეთ.
# import random
# a = random.uniform(0,1)
# print(round(a,3))

# დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი 100-დან 120-მდე.
# დაამრგვალეთ რიცხვი (1 ციფრი ათწილად ნაწილში) და ისე გამოიტანეთ.
# import random
# a = random.uniform(100,120)
# print(round(a,1))

# დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება:
# გამოიყენეთ ციკლის ოპერატორი
# import random
# x = 0
# while x < 10:
#     a = random.randint(1,100)
#     print(a)
#     x += 1


# შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის (დააბრუნებს) მათ
# საშუალო არითმეტიკულს. გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის და დაბეჭდეთ
# შედეგი.

# def sash_arithmetic(a,b):
#     return (a+b)/2
# print(sash_arithmetic(3,7))
# print(sash_arithmetic(45,77))
# print(sash_arithmetic(45,32))


# დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის მათ საშუალო
# არითმეტიკულს და დაბეჭდავს შედეგს (გაითვალისწინეთ რომ დაბეჭდვა უნდა მოხდეს ფუნქციის
# შიგნით - ფუნქცია არ აბრუნებს მნიშვნელობას). გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.

# def sash_arithmetic(a,b):
#     print((a+b)/2)
# sash_arithmetic(34,67)
# sash_arithmetic(39,58)
# sash_arithmetic(89,102)

# შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) არგუმენტად გადაცემული რიცხვის კუბს.
# გამოიძახეთ ფუნქცია რამდენიმეჯერ და დაბეჭდეთ მიღებული შედეგი.

# def ricxvis_kubi(a):
#     return a ** 3
# print(ricxvis_kubi(45))
# print(ricxvis_kubi(33))

# შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) ორ რიცხვს შორის მინიმალურ მნიშვნელობას.
# გამოიძახეთ ფუნქცია და დაბეჭდეთ შედეგი. (პარამეტრად გადაეცით ნებისმიერი ორი რიცხვი).

# def minimal_num(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# print(minimal_num(45,32))


# დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის თუ არა კენტი. თუ
# კენტია, დააბრუნოს მნიშვნელობა True,
# თუ არადა ‐ False.
# შეამოწმეთ რამდენიმე რიცხვისთვის და
# დაბეჭდეთ შედეგი.

# def kenti(a):
#     if a % 2 != 0:
#         return True
#     else:
#         return False
# print(kenti(46))
# print(kenti(37))

# დაწერეთ ფუნქცია, რომელიც დაითვლის (დააბრუნებს) პარამეტრად გადაცემული რიცხვის
# ფაქტორიალს და დაბეჭდეთ შედეგი სხვადასხვა რიცხვებისთვის.

# def faqtoriali(a):
#     namravli = 1
#     for i in range(1,a + 1):
#         namravli *= i
#     return namravli
# print(faqtoriali(5))
# print(faqtoriali(67))

# შეასრულეთ მე-6 სავარჯიშო რეკურსიის გამოყენებით. გაითვალისწინეთ, რეკურსიულია ფუნქცია,
# რომელიც თავის თავს იძახებს.

# def faqtoriali(a):
#     if a == 1:
#         return 1
#     else:
#         return a * faqtoriali(a-1)
# print(faqtoriali(6))

# დაწერეთ უპარამეტრო ფუნქცია რომელიც ეკრანზე ბეჭდავს შემდეგ ტექსტს: “Hello
# World”.
# (გაითვალისწინეთ რომ ფუნქცია არ აბრუნებს მნიშვნელობას).

# def uparametro():
#     print("Hello World")
# uparametro()
# uparametro()


# 9. დაწერეთ ანონიმური ფუნქცია რომელიც დაითვლის რიცხვის კუბს.
# anonimous = lambda a: a ** 3
# print(anonimous(5))

# text = "Hello, World"
# print(text[:])
# print(text[:5])
# print(text[5:])
# print(text[3:7])
# length = len(text)
# # ბოლო სიმბოლოს მივწვდებით ასე:
# print(text[length-1])

# print('n')
# print('/n')

# a = "Computer"
# b = "Science"
# print(a + b)

# print('Darwin\'s')
# print('H2O' * 3)
# print('CO2' * 0)

# დაწერეთ პროგრამა რომლის მეშვებით შეიტანთ ნებისმიერ სტრიქონს (input ბრძანების
# გამოყენებით). დაბეჭდეთ შეყვანილი სტრიოქნის სიგრძე (სიმბოლოების რაოდენობა).

# a = input("Enter text: ")
# print(len(a))

# შეიყვანეთ ნებისმიერი ორი სტრიქონი. ახალ ცვლადში მოახდინეთ მათი შეერთება და
# დაბეჭდეთ შედეგი.

# a = input("Enter first sentence: ")
# b = input("Enter second sentence: ")
# c = a + " " + b
# print(c)

# შეიყვანეთ სტრიქონი. გადაიყვანეთ სტრიქონის ყველა სიმბოლო მაღალ რეგისტრში და
# დაბეჭდეთ შედეგი.

# a = input("Enter text: ")
# print(a.upper())

# შეიყვანეთ სტრიქონი. დაითვალეთ რამდენჯერ შეგხვდათ სიმბოლო “a”
# დაბეჭდეთ
# შედეგი.

# a = input("Enter text: ")
# count = 0
# for i in a:
#     if i == "a":
#         count += 1
# print(count)

# შეიყვანეთ სამი სტრიქონი რომელიც წარმოადგენს სხვადასხვა ხილის დასახელებას
# (მაგ. Banana,
# Watermelon,
# Apple). დაბეჭდეთ ისინი ალფაბეტის ზრდადობის მიხედვით
# (თავდაპირველად წაიკითხეთ სლაიდი “შედარების ოპერაციები სტრიქონებზე”).

# არასრულია
# a = "Banana"
# b = "Watermalon"
# c = "Apple"
# if a>b and b>c:
#     print(c,b,a)
# elif b>a and a>c:
#     print(c,a,b)
# elif c>a and a>b:
#     print(b,a,c)

# text
# ცვლადს მიანიჭეთ სტრიქონი “სწავლის ძირი მწარე არის, კენწეროში
# გატკბილდების”.
# სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ
# შედეგი. დაითვალეთ რამდენჯერ არის ნახსენები სიმბოლო ‘ს’.

# text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
# print(text[:20])
# sum = 0
# for i in text:
#     if i == "ს":
#         sum += 1
# print(sum)

# # text ცვლადს მიანიჭეთ სტრიქონი "Hello, this is example of string. Please, write this text and do some exercises"
# თუ სტრიქონში გვხვდება ტექსტი “is“,
# შეცვლეთ ის “were”-ითდა დაბეჭდეთ შედეგი.

# text = "Hello, this is example of string. Please, write this text and do some exercises"
# if "is" in text:
#     print(text.replace("is", "were"))


# text ცვლადს მიანიჭეთ სტრიქონი "Hello, this is example of string. Please, write this text and do some exercises"
# დაითვალეთ სტრიქონში სიტყვების რაოდენობა. გამოიყენეთ count
# ფუნქცია

# text = "Hello, this is example of string. Please, write this text and do some exercises"
# sum = 1
# for i in text:
#     if i == " ":
#         sum += 1
# print(sum)

# text
# ცვლადს მიანიჭეთ შემდეგი ტექსტი: “Have a nice day".
# დაბეჭდეთ ტექსტის თითოეული სიმბოლო
# ეკრანზე უკუ მიმართულებით ცალ-ცალკე ხაზზე (ანუ პირველად დაბეჭდავ ბოლო სიმბოლოს,
# შემდეგ ბოლოს წინა სიმბოლოს, და ა.შ). გამოიყენეთ while
# ციკლის ოპერატორი

# text = "Have a nice day"
# a = len(text)
# b = -1
# while a > 0:
#     print(text[b])
#     b -= 1
#     a -= 1


# დაითვალეთ რამდენი ციფრისგან შედგება რიცხვი 237645. გამოიყენეთ lenფუნქცია. გამოიყენეთ
# სტრიქონთან სამუშაო ფუნქციები.
# a = str(237645)
# amount = len(a)
# print(amount)

# დაითვალეთ რამდენი ციფრისგან შედგება 2**132 (გაითვალისწინეთ წინა მაგალითი).
# x = 2 ** 132
# print(len(str(x)))

# ტექსტურ ცვლადში ჩაწერეთ თქვენი ემაილი. სტრიქონის ფუნქციების გამოყენებით, იპოვეთ რომელ
# პოზიციაზეა განთავსებული სიმბოლო @.დაბეჭდეთ შედეგი.

# myemail = "lukaanatsvlishvili@gmail.com"
# print(myemail.find("@"))

# დაწერეთ პროგრამა, სადაც user
# შეიყვანს თავის სახელს და გვარს და პროგრამა დაუბეჭდავს
# შესაბამის იმეილის დასახელებას: მაგ: adam.giorgadze@btu.edu.ge

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# print("{}.{}@btu.edu.ge".format(name,surname))

# დაწერეთ პროგრამა, სადაც user
# შეიყვანს (input ბრძანებით) სასურველ პაროლს (ტექსტურ
# მონაცემს). დაადგინეთ შესაძლებელია თუ არა იგი ვარგისი იყოს პაროლად. დაბეჭდეთ შესაბამისი
# პასუხი. გაითვალისწინეთ, პაროლი ვარგისია, თუ იგი შედგება მინიმუმ 8 სიმბოლოსგან,
# აუცილებლად უნდა მონაწილეობდეს როგორც დიდი ლათინური სიმბოლო, ასევე პატარა
# ლათინური სიმბოლო და ციფრი.

# password = input("Enter your password: ")
# if len(password) >= 8 and password.isalnum() == True and password.isalpha() == False and password.islower() == False:
#     print("პაროლი ვარგისია")
# else: print("პაროლი არ არის ვარგისი")

# def tricky_function(x, items=[]):
#     items.append(x)
#     return items
#
# list1 = tricky_function(1)
# list2 = tricky_function(2, [])
# list3 = tricky_function(3)
# list4 = tricky_function(4)
#
# print(list1, list2, list3, list4)


# დაწერეთ პროგრამა, რომლის მეშვეობით შექმნით ფაილს იმავე
# დირექტორიაში (საქაღალდეში), ჩაწერეთ მასში ნებისმიერი ტექსტი და
# დახურეთ ფაილი.
# f = open('text1.txt','w')
# content = f.write('hello, my name is Luka!')
# f.close()

# დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით ფაილს, წაიკითხავთ
# კონტენტს და დაბეჭდავთ ეკრანზე. დაითვალეთ სიმბოლოების რაოდენობა
# ფაილში.
# f = open('text1.txt','r')
# content = f.read()
# count = 0
# for i in content:
#     if i != ' ':
#         count += 1
# print(count)
# f.close()

# დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით უკვე არსებულ ფაილს და
# ბოლოში დაამატეთ თქვენთვის სასურველი ტექსტი.
# f = open('text1.txt','a+')
# f.write(' and i am 23 years old')
# f.close()

# დაწერეთ პროგრამა რომელიც წაიკითხავს ინფორმაციას ერთი ფაილიდან
# და ჩააკოპირებს მეორე (ახალ) ფაილში (შეამოწმეთ ქართულ უნიკოდზეც).
# f = open('text1.txt','r')
# content = f.read()
# f1 = open('text2.txt','a+')
# f1.write(content)
# f.close()
# f1.close()

# დაწერეთ პროგრამა, რომლის მეშვეობით, ორი ფაილის კონტენტს
# გააერთიანებთ მესამე (ახალ) ფაილში.
# f1 = open("text1.txt",'r')
# content1 = f1.read()
# f2 = open("text2.txt",'r')
# content2 = f2.read()
# f3 = open("text3.txt",'a+')
# content3 = f3.write(content1 + content2)
# f1.close()
# f2.close()
# f3.close()

# დაწერეთ პროგრამა რომელიც წაიკითხავს ტექსტს ფაილიდან და დაბეჭდავს
# ეკრანზე მაღალ რეგისტრში.
# f = open('text2.txt','r')
# content = f.read()
# print(content.upper())
# f.close()

# ახალი ფორმატირება
# name = 'Luka'
# age = 23
# print(f'Hello, my name is {name} and i am {age} years old')

# def create_dict(**kwargs):
#     new_dict = {}
#     for atr, val in kwargs.items():
#         new_dict[atr] = val
#     print(new_dict)
# create_dict(name="Luka",surname="Natsvlishvili",age=23)

# def sum_numbers(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# sum_numbers(1,2,3,4,5,45)


# list1 = [34,68,72]
# square = [i**2 for i in list1]
# print(square)



# product_list = {"Shampoo" : "5", "Milk":"4", "Coffee":"5", "Bread":"2"}
# def print_products():
#     for i in product_list:
#         for j in product_list[i]:
#             print(f"{i} - {j}ლ")
# def choose_products():
#         a = input("what do u want to buy? ")
#         if a in product_list:
#             confirm_purchase()
#         else:
#             print("ar aris")
#             choose_products()
# def confirm_purchase():
#     b = input("ნამდვილად გსურთ ყიდვა? ")
#     if b == "Yes":
#         print("Thank u n goodbye")
#     else:
#         c = input("სხვა ნივთის ყიდვა გინდათ? ")
#         if c == "No":
#             print("Goodbye")
#         else:print_products()
# print_products()
# choose_products()
# ფუნქციონალური პროგრამირება
# def print_products():
#     for i in product_list:
#         print(f"{i} - {product_list[i]}ლ")
# print_products()

# def choose_products():
#     while True:
#         a = input("what do u want to buy? ")
#         if a in product_list:
#             break
#
#     print("არის")
# choose_products()


# შექმენით სია numbs ნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების
# ჯამი, მინიმალური, მაქსიმალური და საშუალო არითმეტიკული. ასევე შეასრულეთ
# შემდეგი ოპერაციები:
# • სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# • სიის მესამე ელემენტად ჩასვით რიცხვი 205
# • წაშალეთ სიის მე-4 ელემენტი
# • დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ

# nums = [9,45,68,81,36]
# print(sum(nums),min(nums),max(nums),sum(nums)/len(nums))
# nums.append(102)
# nums.insert(2,205)
# nums.pop(3)
# nums.sort()
# print(nums)

# რიცხვის უკუ მიმართულებით დაწერა!!!
# list1 = []
# a = 234
# for i in str(a):
#     list1.append(i)
# list1.reverse()
# newnum = ""
# for j in list1:
#     newnum += j
# print(int(newnum))

# დაწერეთ პროგრამა, რომლის მეშვეობით შეიყვანთ (input-­‐ით) 10 მონაცემს.
# წარმოადგინეთ და დაბეჭდეთ ისინი სიის ელემენტების სახის.
# list1 = []
# for i in range(10):
#     a = input("Enter data: ")
#     list1.append(a)
# print(list1)

# შექმენით სია fruits, რომელის ელემენტებია: Watermelon,Banana,Apple.დაალაგეთ
# სიის ელემენტები ალფაბეტის უკუ-მიმართულებით და დაბეჭდეთ ისინი.
# fruits = ["Watermelon","Banana","Apple"]
# fruits.sort()
# fruits.reverse()
# print(fruits)


# დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია, დაითვლის სიის
# ელემენტების ნამრავლს და დააბრუნებს შედეგს. გამოიძახეთ ფუნქცია ნებისმიერი
# სიისთვის.
# def namravli(*args):
#     namr = 1
#     for i in args:
#         namr *= i
#     return namr
# print(namravli(4,5))

# დაწერეთ პროგრამა, რომელიც რიცხვითი მნიშვნელობების სიაში ამოშლის კენტ
# რიცხვებს. დაბეჭდეთ მიღებული სია.
# list1 = [9,5,77,44,57,88]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)
#     else:continue
# print(list2)

#შექმენით 5 ელემენტიანი სია (რიცხვითი მნიშვნელობებით). თითოეული ელემენტი
# გაზარდეთ 10-ით და დაბეჭდეთ სია.
# list1 = [4,6,7,8,9]
# list2 = []
# for i in list1:
#     i += 10
#     list2.append(i)
# print(list2)

# my_set = set([2,4,5])
# my_set.add(6)
# print(my_set)
# my_set.update([8,9,7])
# print(my_set)

# my_dict = {1:"Luka", 2: "Nini", 3: "Elene"}
# my_dict.pop(2)
# print(my_dict)

# class Rectangle:
#     def __init__(self,width,length):
#         self.width = width
#         self.length = length
#     def Perimeter(self):
#         return 2*(self.width+self.length)
# obj1 = Rectangle(45,78)
# print(obj1.Perimeter())
# print(Rectangle.Perimeter(obj1))

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def increase_age(self):
#         self.age += 1
# obj1 = Dog("Lycy",12)
# obj1.increase_age()
# print(obj1.age)

# # import sys
# # text = input("write what you whanted to say to me yesterday: ")
# # # sys.exit(0)
# # print(text==5)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = input("Which math operator do you want to use? ")
# if c == "/":
#     print(a / b)
# elif c == "*":
#     print(a * b)
# elif c == "**":
#     print(a ** b)
# elif c == "%":
#     print(a % b)
# elif c == "//":
#     print(a // b)
# elif c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# else:
#     print("You entered wrong math operator")

# class Celsius:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#     def get_temp(self):
#         try:
#             return self.__temperature
#         except AttributeError:
#             return "There is no obj"
#     def set_temp(self,other_temp):
#         self.__temperature = other_temp
#     def del_temp(self):
#         del self.__temperature
#     @property
#     def temperature(self):
#         return f"Today's temperature is {self.__temperature} celsius"
#     @staticmethod
#     def change_celsius_into_f(temp):
#         f = (9/5) * temp + 32
#         return f
#     def sxvaoba(self,other):
#         return self.__temperature - other.__temperature
# temp1 = Celsius(30)
# print(temp1.get_temp())
# temp1.set_temp(50)
# print(temp1.get_temp())
# # temp1.del_temp()
# print(temp1.get_temp())
# print(temp1.temperature)
# print(Celsius.change_celsius_into_f(30))
# print(Celsius.sxvaoba(Celsius(40),Celsius(24)))
# temp1.del_temp()
# print(temp1.get_temp())

# a = [1,2] * 2
# a[1] = 5
# print(a)

# class Student:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     @property
#     def fullname(self):
#         return f"{self.firstname} {self.lastname}"
#     @fullname.setter
#     def fullname(self,name):
#         result = name.split()
#         self.firstname = result[0]
#         self.lastname = result[1]
#     @property
#     def email(self):
#         return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"
# student1 = Student("Luka","Natsvlishvili")
# print(student1.fullname)
# student1.fullname = "Ana Morchiladze"
# print(student1.firstname)
# print(student1.lastname)
# print(student1.email)


# class Employee:
#     organization = 'Google'
#     def __init__(self,name,age,salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#
#     @property
#     def name(self):
#         try:
#             return self.__name
#         except AttributeError:
#             return "There is no such name"
#
#     @name.setter
#     def name(self,other):
#         self.__name = other
#
#     @property
#     def email(self):
#         return f"{self.name}@gmail.com"
#
#     @email.setter
#     def email(self,other):
#         if other.endswith("@gmail.com"):
#             self.name = other.replace("@gmail.com","")
#         else:
#             self.name = other
#
#     def increase_salary(self,addition):
#         self.__salary += addition
#         return self.__salary
#
#     @staticmethod
#     def convert_to_usd(money_amount_in_laris):
#         usd = money_amount_in_laris * 3.1
#         return f"{usd}$"
#
# obj1 = Employee("Luka",23,1200)
# obj2 = Employee("Ana",24,5000)
# print(obj1.name)
# obj2.name = "Irakli"
# print(obj2.name)
# print(obj1.email)
# print(obj2.email)
# print(obj1.increase_salary(3500))
# print(obj2.convert_to_usd(5000))
# obj2.email = "Nini@gmail.com"
# print(obj2.name)
# print(obj2.email)


# class Bank_Account:
#     def __init__(self,account_name,balance=0):
#         self.__account_name = account_name
#         self.__balance = balance
#     @property
#     def name(self):
#         return self.__account_name
#     @name.setter
#     def name(self,other):
#         self.__account_name = other
#     def deposit(self,additional_money):
#         self.__balance += additional_money
#         return f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი"
#     def withdraw(self,withdrawn_money):
#         if withdrawn_money <= self.__balance:
#             self.__balance -= withdrawn_money
#             return f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი"
#         else:
#             return f"ანგარიშზე არაა საკმარისი თანხა. გთხოვთ მიუთითოთ განსხვავებული რაოდენობა"
#
#
# a = input("შეიტანეთ კლიენტის სახელი გვარი: ")
# b = int(input("რა თანხა გაქვთ ამჟამად ანგარიშზე? "))
# bank_account_obj = Bank_Account(a,b)
# c = int(input("შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულებაც გსურთ: \nთანხის შეტანა: 1, თანხის გამოტანა: 2 "))
# if c == 1:
#     d = int(input("რა თანხის შეტანა გსურთ? "))
#     print(bank_account_obj.deposit(d))
# elif c == 2:
#     e = int(input("რა თანხის გამოტანა გსურთ? "))
#     print(bank_account_obj.withdraw(e))
# else:
#     print("გთხოვთ შეიტანოთ 1-იანი ან 2-იანი")


# How to call API in Python

# import requests
# url = 'https://jsonplaceholder.typicode.com/todos/1'
# response = requests.get(url)
# if response.status_code == 200:
#     print('data', response.json())
# else:
#
#     print('There was no data')


# def inverted_string(string):
#     return string[::-1]
# my_string = "Programmer"
# print(inverted_string(my_string))

# a = [10, 20, 30]
# b = a
# b += [40]
# print(a)

# def average(a,b):
#     return (a + b) / 2
# print(average(2,6))
# print(average(4,9))
# print(average(10,45))

# def average(a,b):
#     print((a + b) / 2)
# average(3,6)
# average(76,83)
# average(334,678)

# def cube(a):
#     return a ** 3
# print(cube(45))
# print(cube(5))
# print(cube(56))

# def minimal(a,b):
#     if a > b:
#         return f"{a} is greater than {b}, as a result minimal number is {b}"
#     elif a < b:
#         return f"{a} is minimal number"
#     else:
#         return f"{a} and {b} are equal"
# print(minimal(56,78))
# print(minimal(45,2))
# print(minimal(55,55))

# def is_odd(a):
#     if a % 2 != 0:
#         return True
#     else:
#         return False
# print(is_odd(4))
# print(is_odd(7))

# def factorial(a):
#     if a == 0 or a == 1:
#         return a
#     else:
#         return a * factorial(a-1)
# print(factorial(4))

# def factorial(a):
#     result = 1
#     while(a > 1):
#         result *= a
#         a -= 1
#     return result
# print(factorial(4))

# def hello_func():
#     print("Hello World")
# hello_func()

# cube = lambda x: x ** 3
# print(cube(5))

# i = 0
# while i < 3:
#     if i == 1:
#         break
#     print(i)
#     i += 1
# else:
#     print("Done")

# for i in range(3):
#     x = i
# def test():
#     print(x)
# test()


# x = 1
# def test():
#     global x
#     for x in range(3):
#         pass
# test()
# print(x)

# print({i: i*i for i in range(3)})

# for i in range(3):
#     continue
#     print(i)


# a = [1,3,5,6]
# x = 0
# for i in a:
#     if i > 4: continue
#     x += i
# print(x)

# my_list = [12,34,67,67]
# my_list.append(113)
# print(my_list)
# my_list.insert(1,145)
# print(my_list)
# print(my_list.count(67))
# print(my_list.index(145))
# my_list.pop(3)
# print(my_list)
# my_list.remove(67)
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)
# new_list = my_list.copy()
# print(new_list)
# my_list.clear()
# print(my_list)

# my_str = "Hello"
# print(my_str.upper())
# print(my_str.lower())
# new_str = "hello world"
# print(new_str.capitalize())
# print(new_str.title())
# print(new_str.startswith("he"))
# my_str =  " luka"
# print(my_str.strip())
# print(my_str.endswith("ka"))
# print(new_str.replace(" ","|"))
# print(new_str.split())
# print("-".join(new_str.split()))
# print(my_str.find("l"))
# print(my_str.index("a"))
# print(new_str.count("l"))
# print(new_str.isnumeric())
# print(new_str.isalpha())
# my_new_str = "Ana"
# print(my_new_str.isalpha())

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#     def increase_width(self):
#         self.width += 2
# obj1 = Rectangle(3,4)
# #ატრიბუტის ცვლილება შეგვიძლია ორი გზით
# obj1.width += 3
# obj1.increase_width()
# print(obj1.perimeter())
# #ორგვარად  შემიძლია გამოძახება
# # print(obj1.perimeter())
# # print(Rectangle.perimeter(obj1))
# #
# # print(obj1.length)
# # del obj1.length
# # print(obj1.length)
# #
# # del obj1
# # del Rectangle
# # print(obj1)

# class Dog:
#     """ამ კლასში ხდება ძაღლის სახელისა და ასაკის ინიციალიზაცია"""
#     def __init__(self, name=None, age=0):
#         self.name = name
#         self.age = age
# a = Dog("Jeka", 4)
# b = Dog("Buddy", 3)
#
# print(f"{a.name} is {a.age} years old")
#
# c = Dog()
# c.name = input("Enter your dog's name: ")
# c.age  = int(input("Enter your dog's age: "))
# max_age = max(a.age,b.age,c.age)
# print(f"The oldest dog's age is {max_age}")
#
# print(dir(c))
# print(help(c))
# print(Dog.__doc__)

# class Student:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#     @property
#     def fullname(self):
#         return f"{self.name} {self.surname}"
#     @fullname.setter
#     def fullname(self, new_fullname: str):
#         result = new_fullname.split()
#         self.name = result[0]
#         self.surname = result[1]
#     @property
#     def email(self):
#         return f"{self.name}.{self.surname}.1@btu.edu.ge"
# obj1 = Student("Luka","Natsvlishvili")
# print(obj1.fullname)
# obj1.fullname = "Nini Abramishvili"
# print(obj1.email)

# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("Started")
#         val = func(*args, **kwargs)
#         print("Ended")
#         return val
#     return wrapper
# @f1
# def f(a, b = 9):
#     print(a, b)
#
# @f1
# def add(a, b):
#     return a + b
#
# print(add(10,19))

# def before_after(func):
#     def wrapper(*args):
#         print("before")
#         func(*args)
#         print("after")
#     return wrapper
#
# class Test:
#     @before_after
#     def decorated_method(self):
#         print("run")
#
# t = Test()
# t.decorated_method()

# import time
#
# def timer(func):
#     def wrapper():
#         before = time.time()
#         func()
#         print("Function took:", time.time() - before, "seconds")
#     return wrapper()
# @timer
# def run():
#     time.sleep(2)


# import datetime
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         with open("logs.txt", "a") as f:
#             f.write("called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
#         val = func(*args, **kwargs)
#         return val
#     return wrapper
#
# @log
# def run(a, b, c=9):
#     print(a+b+c)
#
# run(1,3,c=9)

# count = 0
# while count < 5:
#     count += 1
#     if count == 4: continue
#     print(count)


# class Counter:
#     x = 1
#
#     @classmethod
#     def nxt(cls):
#         cls.x *= 2
#         return cls.x
# for _ in range(4):
#     print(Counter.nxt(), end=" ")

# from functools import cache
#
# @cache
# def fibo(n):
#     if n <= 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# print(fibo(499))

# class Student:
#     def __init__(self, firstname, lastname):
#         self.__firstname = firstname
#         self.__lastname = lastname
#     def get_name(self):
#         return self.__firstname
#     def set_name(self, new_name):
#         self.__firstname = new_name
#     def del_name(self):
#         del self.__firstname
#     name = property(get_name, set_name, del_name)
#
# obj1 = Student("Luka","Natsvlishvili")
# print(obj1.name)
# obj1.name = "Levani"
# print(obj1.name)
# del obj1.name


# შექმენით კლასი Student, ატრიბუტებით first, last, fullname, email.
# class Student:
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last
#         self.fullname = self.name + " " + self.last
#         self.email = f"{self.name}.{self.last}.1@btu.edu.ge"
# obj1 = Student("Luka", "Natsvlishvili")
# print(obj1.fullname)
# print(obj1.email)


# class Student:
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last
#     def fullname(self):
#         return self.name + " " + self.last
#     def email(self):
#         return f"{self.name}.{self.last}.1@btu.edu.ge"
# obj1 = Student("Luka", "Natsvlishvili")
# print(obj1.fullname())
# print(obj1.email())

# lst = [1,2,3]
# result = 0
# for i in lst:
#     for j in lst:
#         result += (i == j)
# print(result)

# total = 0
# for i in range(1,4):
#     j = i
#     while j > 0:
#         total += (i + j)
#         j -= 2
# print(total)

# print("Hi", "Luka, you are so generous", sep="! ")
# print("Hello\nWorld")
# print("Luka",end=" :) ")
# print("You are so smart", end=" :)")

# my_str = "Luka"
# a = 5.3
# print("%d" %a)
# print("%5d" %a)
# print("%s" %my_str)
# print("%10s" %my_str)
# print("%f" %a)
# print("%.2f" %a)
# print("Hi %s, nice to meet you. Do you have %.2f dollars?" %(my_str, a))

# import math
# x = math.sqrt(9)
# print(x)


# from math import sqrt, pi
# r = sqrt(9)
# area_of_circle = pi * r**2
# print(area_of_circle)

# from math import *
# a = pi
# print(a)

# import random
# a = random.random()
# print(a)
# b = random.uniform(1,10)
# print(b)
# c = random.randint(1,10)
# print(c)
# m = random.randrange(10)
# n = random.randrange(10,100,2)
# print(m)
# print(n)

# import random
# a = random.randint(10,100)
# print(a)

# double = lambda x: x*2
# print(double(5))

# string slice

# my_text = "Hello World!"
# print(my_text[0:6])
# print(my_text[:6])
# print(my_text[6:])
# print(my_text[:])

# length = len(my_text)
# last_symbol = my_text[length-1]
# print(last_symbol)

# my_text = "Hello World!"
# index = 0
# while index < len(my_text):
#     print(my_text[index])
#     index += 1
#
# for i in my_text:
#     print(i)
#
# res = "ll" in my_text
# print(res)

# my_text = "Hello World!"

# new_str = "J" + my_text[1:]
# print(new_str)

# new_str = my_text.replace("l","k")
# print(new_str)

# a = "hey, it's Lukaa"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.isalpha())
# print(a.isnumeric())
# print(a.isalnum())
# print(a.isdigit())
# print(a.islower())
# print(a.isupper())
#
# print(a.find("s"))
# print(a.find("i",3))
# print(a.count("a"))
# print(a.startswith("hey"))

# f = open('text1.txt','r')
# content = f.read()
# print(content)
# f.close()

# with open('text2.txt','r',encoding='UTF-8') as f:
#     content = f.read()
#     print(content)


# f = open("text2.txt","r",encoding='UTF-8')

# for line in f:
#     print(line)

# print(f.readline())
# print(f.readline())
# print(f.readline(4))

# f = open("text2.txt","a+",encoding='UTF-8')
# content = f.read()
# # f.write("\nLuka Natvlishvili is a great programmer")
# f.seek(5) #კურსორის ადგილმდებარეობის ცვლილება
# pos = f.tell() #კურსორის ადგილმდებარეობის ჩვენება
# print(pos)
# print(f.name)
# f.close()

# import os
# os.rename("text5.txt","my_text.txt")
# os.remove("my_text.txt")

# nested_list = [1,3,5,8,[9,10]]
# print(nested_list[4][1])

# my_list = [2,7,4,9,1,46,32]
# my_list.sort()
# my_list.reverse()
# print(my_list)

# my_txt = "Hello"
# new_list = list(my_txt)
# print(new_list)

# txt = "I love Python programming language"
# s = txt.split()
# print(s)

# txt1 = "I-love-you"
# delimiter = "-"
# s = txt1.split(delimiter)
# print(s)

# my_list = ["Good","morning","America"]
# delimiter = " "
# s = delimiter.join(my_list)
# print(s)

# def avarage_of_nums(*args):
#     return sum(args)/len(args)
# a = avarage_of_nums(1,5,7)
# print(a)

# double = [i*i for i in range(10) if i%2==0]
# print(double)

# my_set = {1,4,2,7}
# my_set.add(9)
# my_set.update([5,9,6])
# print(my_set)
# my_set.discard(10)
# # my_set.remove(10)
# my_set.pop()
# print(my_set)

# my_dict = {1:"Luka", "hey":"world", 5:[1,2,3], 7: {1,5,6}}
# new_dict = my_dict.fromkeys({1,"hey",5},10)
# print(new_dict)
# for i in my_dict.keys():
#     print(i)
# for i in my_dict.values():
#     print(i)
# for i in my_dict.items():
#     print(i)

# print(len(my_dict))
# print(my_dict.get(5,"Not Fount"))
# my_dict["hey"] = "Jupiter"
# print(my_dict)
# del my_dict[1]
# my_dict.pop(5)
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# def print_items(**kwargs):
#     print(kwargs)
# print_items(kwargs_1 = 5, kwargs_2 = "Luka", kwargs_3 = 78)

# def print_items(**kwargs):
#     for key in kwargs:
#         print(key, kwargs[key])
# print_items(kwargs_1 = 5, kwargs_2 = "Luka", kwargs_3 = 78)

# i = 3
# while i > 1:
#     for j in range(2):
#         print(i - j,end=" ")
#     i -= 1


# try:
#     print(5 + 'Luka')
# except TypeError:
#     print("Something went wrong with adding different types of values")
#
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
#
# try:
#     print(a)
# except NameError:
#     print("variable with that name does not exist")

# my_list = [3,6,"Hello","Bye",6]
# try:
#     my_list[5] * 4
#     print(my_list)
# except IndexError:
#     print("Element in list with that index does not exist!")

# try:
#     print(int("Luka"))
# except ValueError:
#     print("something went wrong")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("division by zero is not allowed!")
# except ValueError as v:
#     print(v)
# except:
#     print("any other errors!")
# else:
#     print("this will be printed only if there will be no errors!")
# finally:
#     print("This will be printed in both cases")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     if (b == 0):
#         raise ZeroDivisionError("Division by zero is not allowed")
# except Exception as e:
#     print(e)

# def avg(numbers):
#     assert len(numbers)!=0, "List is empty"
#     print(sum(numbers)/len(numbers))
# t = [1,2,4,5]
# print(avg(t))
# k = []
# print(avg(k))

# t = [3,6,7]
# my_iterator = iter(t)
# try:
#     for i in range(len(t)+1):
#         print(my_iterator.__next__())
# except StopIteration:
#     print("Error")
#
#
# def my_generator():
#     i = 5
#     while True:
#         if i % 5 == 0: yield i
#         i += 5
# a = my_generator()
# for i in range(10):
#     print(next(a))

# მისამართი მეხსიერებაში
# my_list = [1,2,3]
# print(hex(id(my_list)))

# my_tuple = (1,3,[5,7],"Luka",{1:"Hello World"})
# my_tuple = list(my_tuple)
# my_tuple[0] = 5
# my_tuple = tuple(my_tuple)
# print(my_tuple)
# print(hex(id(my_tuple)))
# my_tuple[4][1] = "Goodbye World"
# print(my_tuple)
# print(hex(id(my_tuple)))
# my_tuple[2].append(67)
# print(my_tuple)
# print(hex(id(my_tuple)))

# i = 0
# funcs = []
# while i<5:
#     funcs.append(lambda i=i: i)
#     i += 1
# print([f() for f in funcs])

# arr = [1,2,3]
# for i in arr:
#     arr.remove(i)
# print(arr)

# nums = [1,2,3]
# res = map(lambda x: x + 1, nums)
# for i in res:
#     pass
# print(list(res))


# nums = [1,2,3]
# res = list(map(lambda x: x + 1, nums))
# print(res)


# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)
# print([f() for f in funcs])

# x = {1,2,3,4}
# y = {3,4,5}
# print(x.difference(y))

# a = [1,2,3]
# b = [10,20,30]
# for i,j in zip(a,b):
#     i = i + 100
#     print(j)

# my_str = "python"
# result = my_str[::-2]
# print(result)

# class Counter:
#     count = 0
#     @classmethod
#     def increment(cls):
#         cls.count += 3
# Counter.increment()
# Counter.increment()
# print(Counter.count)

# from functools import reduce
# a = [5]
# for i in range(3):
#     print(reduce(lambda x, y: x + y, a))

# for i in range(1,5):
#     print(i * "*", end="\n")

# for i in range(1,5):
#     print(" " * (5 - i) + i * "*")

# for i in range(5,0,-1):
#     print(i * "*", end="\n")

# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n = 4
# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# clcoding = [1,2,3,4]
# total = 0
# for x in clcoding:
#     total += x
#     clcoding[0] = total
# print(clcoding)

# def f(x):
#     return x + 1
# m = map(f,[1,2,3])
# m = map(f,m)
# print(list(m))

# a = [1,2]
# a.append(a)
# print(len(a))
# print(a)

# my_array = [[1,2,3],[4,5,6]]
# def weird_func(array_2D):
#     total = 0
#     for array in array_2D:
#         for element in array:
#             total += element
#     return total
# print(weird_func(my_array))


# fibonacci_list = [0,1]
#
# a = int(input("how many members do u want with fibonacci func? "))
#
# def fibonacci_func(a):
#     for i in range(a-2):
#         fibonacci_list.append(
#             fibonacci_list[-1] + fibonacci_list[-2]
#         )
#     return fibonacci_list
# print(fibonacci_func(a))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# n = int(input("How many Fibonacci numbers? "))
#
# for i in range(n):
#     print(fibonacci(i), end=" ")

# class A:
#     def __init__(self):
#         return 10
# obj = A()
# print(obj)

# class Car:
#     pass
# car1 = Car()
# print(type(car1) == Car)

# import __hello__
# __hello__.main()

# arr = [1,2,3]
# for i in arr:
#     i = i * 2
# print(arr)

# lst = [1,2,3]
# out = []
# for i in range(len(lst)):
#     out.append(lst[i])
#     break
# print(out)

# print(len("Python" * 2))

# t = (1,(2,3),4)
# s = 0
# for i in t:
#     if type(i) == tuple:
#         s += sum(i)
#     else:
#         s += i
# print(s)

# t = (1,2,3)
# for i in t:
#     i = i * 2
# print(t)

# s = {1,2,3}
# s.add([4,5])
# print(s)

# scores = {"A": 85, "B": 72, "C": 90}
# opt = {"min": 80}
# res = list(filter(lambda k: scores[k] <= opt["min"],scores))
# print(res)

# x = 10
# def outer():
#     x = 5
#     return map(lambda y: y + x, range(3))
# x = 20
# result = list(outer())
# print(result)

# t = (5, -5, 10)
# u = tuple(abs(i) for i in t)
# v = u[::-1]
# x = sum(v[i] for i in range(1, len(v)))
# print(x)

# def func(x, l=[]):
#     l.append((x))
#     return l
# print(func(1))
# print(func(2))

# class Vanish:
#     def __get__(self, obj, owner):
#         del owner.x
#         return 100
# class A:
#     x = Vanish()
# a = A()
# print(a.x, hasattr(A, "x"))
# print(a.x)

# d = {'a': 1}
# k = d.keys()
# d['b'] = 2
# print(list(k))

# x = [i*i for i in range(3)]
# print(list(x), list(x))

# import calendar
# year = 2026
# cal = calendar.TextCalendar(calendar.MONDAY)
# print(cal.formatyear(year))

# t = (1,2,3,4,{5:"Luka"},[1,2,3],{6,7,8})
# for i in t:
#     if i == 3:
#         i = 20
# print(t)
# t[4][5] = "Nini"
# print(t)
# t[5].append(45)
# print(t)
# t[6].add(9)
# print(t)

# arr = [10,20,30]
# for i in arr:
#     i = i * 10
# print(arr)
