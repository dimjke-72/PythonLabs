# Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзначное число: "))
 
d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
 
print("Сумма цифр числа:", number + d1 + d2)