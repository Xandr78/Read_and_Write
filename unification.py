# Задание №3 объединить содержимое файлов в один 
dict_fails = {}
sort_dict = {}
with open('file_1.txt', 'r', encoding='utf-8') as f1:
    count1 = len(f1.readlines())
    dict_fails['file_1.txt'] = count1 
    
with open('file_2.txt', 'r', encoding='utf-8') as f2:
    count2 = len(f2.readlines())
    dict_fails['file_2.txt'] = count2 
        
with open('file_3.txt', 'r', encoding='utf-8') as f3:
    count3 = len(f3.readlines())
    dict_fails['file_3.txt'] = count3 

# сортировка файлов по количеству строк
sorted_tuple = sorted(dict_fails.items(), key=lambda x: x[1])
sort_dict.update(dict(sorted_tuple))

with open ('result_file.txt', 'w', encoding='utf-8') as f:
    counter = 0
    for i in sorted_tuple:
        counter += 1
        f.write(f'{i[0]}\n')
        f.write(f'{i[1]}\n')
        for j in range(1, i[1]+1):         
            f.write(f'Строка номер {j} файла номер {counter}\n')