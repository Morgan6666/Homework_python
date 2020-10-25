#Задание №1
file_1 = open("New_file13.txt", 'x', encoding = 'utf-8')
file_1.write(input("Введите значение для ввода:"))
while file_1.write(input("Введите значение для ввода:")) == '':
    file_1.write(input("Введите значение для вввода:"))
file_1.close()
file_1 = open("New_file13.txt", 'r')
file_1.read()

#Задание №2
file_2 = open("My_file.txt", 'r',encoding = 'utf-8')
count_1 = 0
count_2 = 0
for i in file_2.readlines():
    print(i)
    count_1 +=1   
for k in i:
    count_2 += 1
print('Число строк в файле:',count_1)
print('Чсло букв в файле: ', count_2)
file_2.close()


#Задание №3
import pickle
dict_1 = {'Василий Тёмкин':20000,
       "Иван Сусанин": 3000000,
        "Павел Грозный": 210000,
       "Денис Байрамкулов": 2000000000000000,
       "Алексей Пронин":10000}
New_dict = open("My_lesson2.txt", 'wb')
pickle.dump(dict_1, New_dict)
New_dict.close()

with open('My_lesson2.txt','rb') as New_dict:
    New_dict2 = pickle.load(New_dict)
    res = []
    count = 0
    for values in New_dict2:
        res.append(New_dict2[values])
        count += 1
        if New_dict2[values] < 20000:
            print(f"Сотрудники чей оклад менне 20000: {values}")
    print(f'Среднее значение оклада {float(sum(res) / count)}')



#Задаание №5
with open("My_file6.txt", 'w') as my_file6:
    my_file6.write(input("Введите последовательность чисел через пробел: "))
with open("My_file6.txt", 'r') as my_file6:
    res = []
    res_2 =[]
    for i in my_file6:
        for k in i:
            res.append(k)
            if k == ' ':
                res.remove(k)
    for k in res:
        res_2.append(int(k))
        
            
    print(f'Сумма вашей последовательности цифр: {sum(res_2)}')
        