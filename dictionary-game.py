'''
Данное приложение позволяет пользователям записывать иностранные слова,
а также их перевод для последующего заучивания.
В приложении есть опция для сохранениям этих слов в текстовый файл.

Также в приложении есть игра, способствующая запоминанию слов.
Игра имеет два режима: пользователь может переводить
слова как с иностранного на русский, так и с русского на иностранный.
'''


import os
import random


'''
Функциональный блок приложения: приветствие пользователя, выход из приложения, правила пользования приложением.
'''

def hello():
    print("Добро пожаловать в словарь!\n")
    begin()


# Приветствие пользователя и выбор режима приложения: словарь или игра на заучивание слов.
def begin():
    while True:
        choice = input(
            "Введите слово 'игра', чтобы перейти в игровой режим.\n"
            "Или слово 'словарь', чтобы перейти в режим создания словаря.\n"
        )
        if choice == "словарь":
            save_or_exit()
            break
        elif choice == "игра":
            igra_instruction()
            break
        elif choice == "EXIT":
            bye()
            break
        else:
            print("Вы что-то не так поняли. Попробуйте ещё раз.")


# Объяснение пользователю функционала словаря.
def dict_instruction():
    print(
        "\n-- чтобы увидеть словарь целиком и сохранить его в текстовый файл, наберите в строке, "
               "предлагающей ввод иностранного слова, 'SAVE'." 
        "\n-- чтобы выйти из программы, наберите 'EXIT'\n"
        "P.S. Не забудьте сохранить слова в файл перед выходом из приложения. Иначе они будут утеряны.\n"
    )


# Объяснение пользователю функционала игры.
def igra_instruction():
    print("\nКогда захотите вернуться из игры в главное меню, наберите 'EXIT'.")
    check()


# Выбор: переход в главное меню или выход из приложения.
def bye_or_continue():
    while True:
        inp = input("Напишите 1, если хотите перейти в главное меню, и 2, если хотите выйти:\n")
        if inp == '1':
            begin()
            break
        elif inp == '2':
            bye()
            break
        else:
            print("Вы что-то не так поняли")


def bye():
    print("До скорого;)")


'''
Ниже представлена такая опция приложения, как словарь.
Пользователю предлагается ввести слово, затем перевод. И так происходит пока пользователь не захочет покинуть приложение
Когда пользователь захочет покинуть приложение, ему предлагается сохранить приложение.
Если пользователь соглашается, то происходит запись слов в текстовый файл, имя которого вводит пользователь.
Если пользователь отказывается, то осуществляется выход из программы.
'''

# Вход в режим словаря. Пользователю предлагается ввести слово на иностранном языке.
def save_or_exit():
    dict_instruction()
    while True:
        slovo = input("Введите слово на иностранном языке: ")
        if slovo == "SAVE":
            save()
            break
        elif slovo == "EXIT":
            bye_or_continue()
            break
        else:
            perevod(slovo)


# Функция принимает на вход иностранное слово.
# Пользователю предлагается ввести перевод слова. Слово и его перевод записываются в словарь.
def perevod(slovo):
    if slovo in dictionary:
        print("Данное слово уже находится в словаре.")
    else:
        perevod = input("Введите перевод слова: ")
        dictionary[slovo] = perevod
        print(slovo + " -- " + perevod)


# Выбор: сохранение данных словаря в форме текстового документа или отказ от этого действия.
def save():
    for key in dictionary.keys():
        print(key, " -- ", dictionary[key])
    while True:
        save = input("Хотите ли Вы сохранить словарь в виде текстового файла? Напишите: да/нет.\n")
        if save == "да":
            record()
            break
        elif save == "нет":
            bye_or_continue()
            break
        elif save == "EXIT":
            bye_or_continue()
            break
        else:
            print("\nВы что-то не так поняли.")


# Запись слов из приложения в текстовый файл.
def record():
    file = input(
        "Документ будет сохранён в ту же папку, где расположена данная программа.\n" 
        "Введите имя, под которым хотите сохранить словарь: "
    )
    with open(file, "a") as out:
        for word in dictionary:
            print(word, dictionary[word], file=out)
    print("\nСохранение прошло успешно")
    bye_or_continue()


'''
Ниже представлен такой режим приложения, как игра на запоминание слов.
Игра имеет 2 режима: 1) перевод с иностранного языка на русский; 2) перевод с русского на иностранный.
'''

# Выбор режима игры: перевод с иностранного на русский или наоборот.
def mode(file):
    dict = {}
    while True:
        option = input(
            "Если Вы хотите переводить слова с иностранного языка на русский, нажмите 1.\n" 
            "Если Вы хотите переводить слова с русского языка на иностранный, нажмите 2.\n"
        )
        with open(file, "r") as document:
            for line in document:
                key, value = line.split()
                dict[key] = value
        if option == "1":
            game_1(dict)
            break
        elif option == "2":
            game_2(dict)
            break
        elif option == "EXIT":
            begin()
            break
        else:
            print("Вы что-то не так поняли.")


# Проверка файла на соответствие требованиям программы.
# Файл должен присутствовать в директории, файл не должен быть пустым,
# Формат записи слов в документе должен быть верным: "слово перевод"
def check():
    while True:
        doc = input(
            "\nВведите имя файла, в котором хранятся слова для заучивания.\n"
            "Файл должен храниться в той же директории, что и данное приложение!\n"
        )
        if doc == "EXIT":
            bye_or_continue()
            break
        try:
            if os.stat(doc).st_size == 0:
                print("Данный файл пуст.")
            else:
                with open(doc, "r") as document:
                    for line in document:
                        first, second = line.split()
                    mode(doc)
                    break
        except FileNotFoundError:
            print("\nДанный файл не найден.")
        except ValueError:
            print(
                "\nФормат записи данных в файле не соответсует требованиям программы."
                "\nСоздайте словарь через приложение или запишите слова в файле следующим образом: 'слово перевод'."
            )


# Игра №1: перевод c иностранного (если это слово указано первым в файле) на русский.
def game_1(dict):
    while True:
        random_key = random.choice(list(dict.keys()))
        print(random_key)
        otvet = input("Введите перевод: ")
        if otvet == dict.get(random_key):
            print("Правильно!\n")
        elif otvet == "EXIT":
            print("Хорошая работа!\n")
            break
        else:
            print(
                "Неправильно.\n"
                f"Верный перевод слова: {dict.get(random_key)}.\n"
            )
    bye_or_continue()


# Игра №2: перевод c русского(если это слово указано первым в файле) на иностранный.
def game_2(dict):
    while True:
        random_value = random.choice(list(dict.values()))
        list_key = list(dict.keys())
        list_value = list(dict.values())
        print(random_value)
        otvet = input("Введите перевод: ")
        if otvet == "EXIT":
            print("Хорошая работа!\n")
            break
        elif otvet == list_key[list_value.index(random_value)]:
            print("Правильно!\n")
        else:
            print(
                "Неправильно.\n"
                f"Верный перевод слова: {list_key[list_value.index(random_value)]}.\n")
    bye_or_continue()


# Словарь для режима словаря
dictionary = {}


if __name__ == '__main__':
    hello()