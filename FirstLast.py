#Дано число. Выведите в консоль первую цифру этого числа.
#Дано число. Выведите в консоль последнюю цифру этого числа
#Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
#Дано число. Выведите количество цифр в этом числе.



number = input('Введите любое число: ')
string_num = str(number)
mapObject = map(int, string_num)
separate_digit_list = list(mapObject)
sumfl=separate_digit_list[0]+separate_digit_list[-1]
print('Первое число: ', separate_digit_list[0])
print('Последнее число: ', separate_digit_list[-1])
print('Сумма первого и последнего числа: ', sumfl)
print('Количество цифр в числе: ', len(separate_digit_list))
