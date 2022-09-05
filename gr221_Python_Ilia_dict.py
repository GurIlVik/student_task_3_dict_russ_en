
from random import randint


# функция словаря пока программа открыта она раочая с новым запуском программы обнуляется. 
def save_dict(lang = " ", key = '', value = ''):
    dict_rus_en = {
        'привет' : ['hello', 'hi', "salutation"],
        'дивный' : ['wondrous', 'wonderful', "glorious", 'marvelous'],
        'новый' : 'new',
        'мир' : ['world', 'paece'], 
        }
    dict_en_rus = {
        'hello' : ['привет', 'здрасьте', "здорово"],
        'marvelous' : 'чудесный',
        'new' : 'новинка',
        'paece' : ['мир', 'покой'], 
        }
    if lang != " ":
        blue = False
        for elem in value:
            if elem in ', ':
                blue = True    
        if blue == True:
            value = value.split(', ')
        if lang == '1':
            dict_rus_en[key] = value
        if lang == '2':
            dict_en_rus[key] = value
        respon = input('Ваши слова записаны, если Вы хотите записать эти значения в другой словарь нажмите 1')
        if respon == "1":
            if type(value) == type(['ghj']):
                print('Я не могу в словаре указать несколько слов с одним значением')  
            else:
                if lang == '2':
                    dict_rus_en[value] = key
                if lang == '1':
                    dict_en_rus[value] = key
    return True, dict_rus_en, dict_en_rus

# модуль проверки слов который берутся из словаря.
def word_verification_module():
    
    # функция подсчета и вывода на экран ошибок
    def word_verification(resp, word):
        if type(resp) != type(word) and type(word) == type(['def']):
            print(f'Не указанно одно или более значений. Правильно {word}')
        elif type(resp) != type(word) and type(word) != type(['def']):
            print(f'Слово имеет только одно значение. Правильно {word}')
        else:
            if type(word) == type(['def']) and len(resp) == len(word):
                print(f"одно или более значений указаны не правильно. Правильное {word}")
            elif type(word) == type(['def']) and len(resp) != len(word):
                print(f"одно или более значений не указаны. Правильное {word}")
            else:
                count = 0
                if len(resp) == len(word):
                    for i in range(len(resp)):
                        if resp[i] != word[i]:
                            count += 1
                elif len(resp) > len(word):
                    count += len(resp) - len(word)
                    for i in range(len(word)):
                        if resp[i] != word[i]:
                            count += 1
                else:
                    count += len(word) - len(resp)
                    for i in range(len(resp)):
                        if resp[i] != word[i]:
                            count += 1
                if count > 3:
                    print(f'Скорее всего Вы ввели не правильное слово. Правильное {word}!')
                else:
                    print(f'При введении перевода Вы допустили {count} ошибок. Правильное {word}!')
    
    # функция загадывания слов 
    def fortune_telling_by_rus(resp):
        a, dict_rus_en, dict_en_rus = save_dict()
        if resp == '1':
            dict_word = dict_rus_en
        else:
            dict_word = dict_en_rus
        num = randint(1, len(dict_word))
        count = 0
        word_fortune = ''
        for keys in dict_word:
            count += 1
            if count == num:
                word_fortune = keys
        response_user = input(f'Наипшите значение или значения слова {word_fortune} \n')    
        if response_user == dict_word[word_fortune]:
            print('Великолепно!')
        else:
            word_verification(response_user, dict_word[word_fortune])
        
        result = input('готовы продолжить нажмите 1 или 2, но можно и 1729')    
        return result
    
    # главное меню модуля проверки слов
    def main_def_verification_module():
        print('Здорово, что именно этот модуль Вы выбрали! Это правильный выбор, самый лучший модуль!')
        print('Если Вы устанете просто введите магическое число 1729')
        respons_user = input('Введите 1 если хотите проверить английские слова и 2 если русские, и 1729 сами знаете зачем \n')
        while respons_user != '1' and respons_user != '2'  and respons_user != '1729':
            respons_user = input('Ошиблись, введите 1, 2 или 1729 \n')
        if respons_user == '1' or respons_user == '2' or respons_user == '1729':
            while True:
                if respons_user == '1729':
                    return True
                else:
                    print('kjdfnej')
                    resp = fortune_telling_by_rus(respons_user)
                    respons_user = resp
        return True
        
    return main_def_verification_module()

# модуль записи слов в словарь
def module_recording_new_words():

    # фун-я проверки   слова на язык
    def check_user_response_key(resp):
        result = True
        lang = 'русский'
        if resp[0] >= 'a' and resp[0] <= 'z':
            for el in resp:
                if el >= 'a' and el <= 'z' or el == '-':
                    lang = 'english'
                    result = False
        if resp[0] >= 'а' and resp[0] <= 'я' or resp[0] == 'ё':
            for el in resp:
                if el >= 'а' and el <= 'я' or el == 'ё' or el == '-':
                    result = False
        return result, lang
        
    # функция проверки полученных слов в запросе на добавления в словарь
    def check_user_response(user_response_key, user_response_value):
        language_key = ''
        language_value = ''
        password_cycle = True
        while password_cycle:
            password, language_key = check_user_response_key(user_response_key)
            while password:
                user_response_key = input('Вы ошиблись в написаниии слова введите его снова: \n').lower()
                password, language_key = check_user_response_key(user_response_key) 
            if user_response_value not in ", ":
                password_2, language_value = check_user_response_key(user_response_value)
                while password_2:
                    user_response_value = input('Вы ошиблись в написаниии слова или синонимов (они записываются через запятую с 1 пробеллом) введите его снова: \n').lower()
                    password_2, language_value = check_user_response_key(user_response_value)
            if language_key == language_value:
                print ('не вверно введены данные на одном языке или на одной раскладке клавиатуры')
                user_response_key = input('Введите слово которое Вы хотите записать в словарь (без пробеллов): \n').lower()
                user_response_value = input('Введите его значение или значения (в этом случае слова записываются объязательно через запятую и пробел) на другом языке: \n').lower()
            else:
                password_cycle = False
        return language_key, user_response_key, user_response_value

# основной блок модуля получение и обработка запроса
    def recording_new_words():
        result = False
        print('Это самый лучший модуль! Именно его и надо было выбрать!')
        print('Если Вы устанете просто введите магическое число 1729 \n')
        password = True
        while password:
            user_response_key = input('Введите слово которое Вы хотите записать в словарь (без пробеллов): \n').lower()
            if user_response_key == '1729':
                password = False
                result = True
                continue
            # print(user_response_key)
            user_response_value = input('Введите его значение или значения (в этом случае слова записываются объязательно через запятую и пробел) на другом языке: \n').lower()
            # print(user_response_value)
            if user_response_value == '1729':
                password = False
                result = True
                continue
            lang_key, user_response_key, user_response_value = check_user_response(user_response_key, user_response_value)
            if lang_key == 'русский':
                print(user_response_key, user_response_value)
                password = save_dict(lang = "1", key = user_response_key, value = user_response_value)
            if lang_key == 'english':
                password = save_dict(lang = "2", key = user_response_key, value = user_response_value)
        return result

    return recording_new_words()

# модуль записи словаря в файл
def module_recording_dict_in_fail():
    number = randint(1, 100)
    a, dict_rus_en, dict_en_rus = save_dict()
    dict_choice = input('Введите название словаря 1 если рус-ангб 2 если анг-рус и 3 если оба ну или 1729')
    while dict_choice != '1' and dict_choice != '2'  and dict_choice != '1729' and dict_choice != '3':
            dict_choice = input('Ошиблись, введите 1, 2, 3 или 1729 \n')
    dict_save = []
    r = ''
    if dict_choice == '1729':
        return True
    if dict_choice == '1':
        r = ['русско-английский словарь']
        dict_save.append(r)
        # dict_save.append('')
        for key, value in dict_rus_en.items():
            dict_save.append(f'{key} - {value}')
    if dict_choice == '2':
        r = f'англо-русский словарь \n'
        dict_save.append(r)
        # dict_save.append('')
        for key, value in dict_en_rus.items():
            dict_save.append(f'{key} - {value}')  
    if dict_choice == '3':
        r = f'русско-английский словарь и наоборот \n'
        dict_save.append(r)
        # dict_save.append('')
        dict_save.append(f'русско-английский словарь \n') 
        # dict_save.append('')
        for key, value in dict_rus_en.items():
            dict_save.append(f'{key} - {value}')  
        dict_save.append(f'\nангло-русский словарь \n') 
        # dict_save.append('')  
        for key, value in dict_en_rus.items():
            dict_save.append(f'{key} - {value}') 
    
    with open(f'dict{r}{number}.txt', 'w', encoding='utf-8') as file:
        for line in dict_save:
            file.write(line + '\n')
        
    print(f'Словарь записан в файле: dict{r}{number}.txt')
    
    
    return True

# вечный цикл выхода
def eternal_cycle():
    list_eternal_cycle = [
        '1729 - натуральное число, следующее за 1728 и предшествующее 1730.', 
        '1729 - число Такси, и оно по-разному известно как число Рамануджана и число Рамануджана-Харди',
        '1729 - названо в честь анекдота британского математика Г. Х. Харди, когда он посетил индийского математика Сринивасу Рамануджана в больнице.',
        '1729 - наименьшее число, которое можно выразить как сумму двух кубов двумя различными способами',
        '1729 = 1^3 + 1^3 = 9^3 + 10^3',
        '1729 - иногда выражается с использованием термина "положительные кубы", поскольку разрешение отрицательных совершенных кубов (куба отрицательного целого числа) дает наименьшее решение как 91 (которое является делителем 1729; 19 × 91 = 1729).',
        '1729 имеет делитель 91х19, а 91 = 6^3 + (−5)^3 = 4^3 + 3^3',
        '1729 и другие числа являющиеся наименьшим числом, которое может быть выражено как сумма двух кубов n различными способами[5], получили название "номера такси". ',
        '1729 - первое в последовательности "промахов Ферма" , определенных со ссылкой на Последнюю теорему Ферма как числа вида 1 + z^3, которые также можно выразить как сумму двух других кубов.',
        '1729 - является третьим числом Кармайкла, первым числом Черника–Кармайкла.',
        '1729 - первым абсолютным псевдоприложением Эйлера.',
        '1729 - сфеническое число',
        '1729 - является третьим числом Цейзеля',
        '1729 - центрированное кубическое число',
        '1729 -  додекагональное число',
        '1729 -  24-угольное',
        '1729 - 84-угольное число',
        'Исследуя пары различных целочисленных квадратичных форм, которые представляют каждое целое число одинаковое количество раз, Шиман обнаружил, что такие квадратичные формы должны быть в четырех или более переменных, а наименьший возможный дискриминант пары из четырех переменных равен 1729.',
        '1729 - наименьшее число, которое может быть представлено квадратичной формой a^2 + ab + b^2 Лешиана четырьмя различными способами с целыми положительными числами a и b',
        '1729 - это размерность преобразования Фурье, на которой основан самый быстрый известный алгоритм умножения двух чисел.',
        '1729 - пример галактического алгоритма.',
        ]
    resp = list_eternal_cycle[randint(0, len(list_eternal_cycle))]
    result = input(f"А Вы знали, что {resp}. \n Для выхода из программы нажмите - 1729 \n")
    return result   

# проверка пользовательского ответа
def check_user_response(resp, n=0):
    result = True
    if resp == '1':
        result = word_verification_module()
    elif resp == '2':
        result = module_recording_new_words()
    elif resp == '3':
        result = module_recording_dict_in_fail()
    elif resp == '1729':
        print(f'''Прощайте, вряд ли Вы вернетесь Повелитель[ница], 
расскажите обо мне своим друзьям и знакомым, пусть хоть они заходят ко мне и пополняют меня новыми Знаниями.
''')
        responses = input("Ладно жмите 1729 и уходите... ")
        while True:     
            while responses != '1729':
                responses = input("ну нет же, ввести надо 1729... \n")
            if responses == '1729':
                responses = eternal_cycle()
            
    else:
        result = True
    return result

# основное пользовательское меню для работы с разными словарями
def dict_rus_en_and_en_rus():
    user_response = input(f'''Приветствую мой Повелитель[ница], я твой покорный слуга словарь.
умею я не так много, всего то:
1. запрашивать перевод слова. Для этого необходимо ввести цифру 1 и нажать ввод
2. и пополнять словарь новыми значениями. Для этого необходимо ввести цифру 2 и нажать ввод
3. а еще записывать слова с переводом в файл (который Вы можете переслать по своему желанию)
4. и прощаться для этого необходимо набрать 1729 и нажать ввод:
''')
    password = check_user_response(user_response)

    while password:
        print('Введите 1, или 2, или 3, ну или 1729(что бы уйти, но это очень не желательно):')
        user_response = input(': ')
        password = check_user_response(user_response, n=1)
    
if __name__ == '__main__':
    dict_rus_en_and_en_rus()


