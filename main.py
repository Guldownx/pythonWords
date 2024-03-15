from random import choice
from colorama import Fore, Back, Style, init

init(autoreset=True)


def show_words_pool(word_s: str, word_list: list) -> None:
    for i in word_list:
        if i == word_s:
            print(Back.YELLOW + Fore.BLACK + ' '.join(i.upper().split()) + Style.BRIGHT)
        else:
            for j in range(len(i)):
                if i[j] == word_s[j]:
                    print(Back.YELLOW + Fore.BLACK + i[j].upper() + Style.BRIGHT, end='')
                elif i[j] in word_s:
                    print(Back.GREEN + Fore.BLACK + i[j].upper() + Style.BRIGHT, end='')

                else:
                    print(i[j].upper() + Style.BRIGHT, end='')
            print()


def show_russian_alphabet(word_list: list) -> None:
    russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    check = ''.join(word_list)
    for i in russian_alphabet:
        if i.lower() in check:
            print(Back.WHITE + Fore.BLACK + i + Style.BRIGHT, end='')
        else:
            print(i, end='')
    print()


def game_words(n: int = 6) -> str:
    with open('WordDict', mode='r', encoding='utf-8') as f:
        words = [word.lower().strip() for word in f.readlines() if len(word) == n + 1]
    print(words)
    word_search = choice(words)
    players_list = []
    attempts = 6
    while True:
        print(Back.BLACK + f'Введите слово из {n} букв' + Style.BRIGHT)
        word_players = input().lower()
        if word_players == word_search:
            players_list.append(word_players)
            show_words_pool(word_search, players_list)
            show_russian_alphabet(players_list)
            return Back.BLACK + 'Поздравляю, вы нашли слово!' + Style.BRIGHT
        if len(word_players) == n and (word_players in words):
            players_list.append(word_players)
            show_words_pool(word_search, players_list)
            show_russian_alphabet(players_list)
        else:
            print(Back.BLACK + 'Вашего слова нет в нашем словаре,' + Style.BRIGHT)
            print(Back.BLACK + 'либо его длина не соответствует правилам.' + Style.BRIGHT)
            show_words_pool(word_search, players_list)
            show_russian_alphabet(players_list)
        attempts -= 1
        if attempts == 0:
            print('К сожалению, вы не нашли слово :(')
            return Back.YELLOW + Fore.BLACK + word_search.upper() + Style.BRIGHT
        else:
            print(Back.BLACK + f'Попыток осталось: {attempts}' + Style.BRIGHT)


if __name__ == '__main__':
    print(Back.BLACK + 'Добро пожаловать в игру Words!' + Style.BRIGHT)
    print(Back.BLACK + 'Для начала введите длину слов' + Style.BRIGHT)
    print(Back.BLACK + 'которыми хотите играть:' + Style.BRIGHT)
    N = int(input())
    print(game_words(N))
