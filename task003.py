# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
#  написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком


def sum_ord(x:list):
    '''сумма очков слова'''
    result = []
    count = 0
    for i in x:
        for j in i:
            count += ord(j)
        result.append(count)
        count = 0
    return result

def num_ord(a:list,b:list):
    '''Проверяет есть ли делитель'''
    result = []
    count = 0
    for i in range(len(a)):
        if a[i]%b[i] == 0:
            result.append(a[i])
        else:
            result.append(b[i])
    return result


language = ['C++','Kotlin', 'PHP', 'Curry', 'Delphi', 'Erlang', 'Mathematica', 'Mozart', 'Nemerle',\
     'Python', 'Rust', 'Scala','Swift', 'Zonnon', 'Julia']

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


# Первое задание
lan_num = list(zip(map(lambda x: x.upper(), language), numbers))
print(lan_num)
print()

# Второе заданиe
lan_num_ = list(zip(map(lambda x: x.upper(), language), num_ord(sum_ord(map(lambda x: x.upper(), language)), numbers)))
print(lan_num_)
print()




        

