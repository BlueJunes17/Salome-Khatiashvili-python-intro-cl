"""დაწერეთ პროგრამა რომელიც დაბეჭდავს გამრავლების ტაბულას 1 და 9 ის ჩათვლით.
ტაბულა უნდა იყოს სვეტებად შედგენილი. 
ოველ მომდევნო სვეტში არ უნდა იყოს გამეორებული ნამრავლი წინა სვეტიდან.
Გავიხილოთ 1x3 ის მაგალითი"""


first_number = 1

while first_number < 10:
    second_number = 1
    while second_number <= first_number:
        if second_number == first_number:
            print(f'{second_number} * {first_number} = {first_number * second_number}')
        else:
            print(f'{second_number} * {first_number} = {first_number * second_number}', end= " ")
        second_number += 1
    first_number += 1