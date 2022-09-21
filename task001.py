# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


tetx = 'Напишите програбвмму, удаляющую из текста все словабв,\
     содержащие абвгдейка - это передача - это передача'

tetx = list(tetx.split())

def find_abv(a:list):
    for i in a:
        if 'абв' in i:
            a.remove(i)
    return a


print(find_abv(tetx))



# tetx_new = list(filter(lambda a: a.remove(x) if 'абв' in x , tetx.split())) #---не понял где ошибка
# print(tetx_new)


