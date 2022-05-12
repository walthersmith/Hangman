import random
from time import sleep
import gui
import re
import platform as pl
import os

from life import *
from score import *
from level import *


def get_words(file_name: str) -> list:
    """Reads a file text to fill a list with words

    Returns:
        [list]: return a list with all the words in the file
    """
    words = []
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip('\n'))
    return words


def get_random_word(words: list) -> str:
    """get a random word from a list

    Args:
        words (list): a list of words 

    Returns:
        [str]: return a random item from the list
    """
    word = words[random.randint(0, len(words) - 1)].upper()
    return word


def clean_screen():
    """
     this function clear the screen depending on if OS is windows or other like linux
    """
    if pl.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def detect_special_character(pass_string: str):
    """uses regex to find special characters 
    Args:
        pass_string (string): string to analyze

    Returns:
        bool: returns True or false
    """
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(pass_string) is None:
        res = False
    else:
        res = True
    return res


def game2(words: list):
    # initialize new game

    lives = Life()
    level = Level()
    game_score = Score()
    scenes = gui.get_scenes()

    while lives.get_lifes() > 0:
        # get a random word
        word =  get_random_word(words)
        word_to_discover = normalize_string(word)
        word_map = ['_ ' for x in word]
        letters_left = list(word) 
        letters_used = list()
        game_score.set_attemps(0)
        scene = scenes['hang']

        clean_screen()
        print(gui.gui_in_game(game_score, lives, ''.join(word_map), letters_used,level,scene[game_score.get_attemps()]))

        # game loop
        continue_game = True
        while continue_game:
            # validate attempts
            if game_score.get_attemps() >= game_score.get_maximun_attemps():
                clean_screen()
                scene = scenes['loose']
                input(gui.gui_in_game(game_score, lives, ''.join(word_map), letters_used,level,scene))
                lives.loose_life()
                continue_game = False
                continue

            # validate letters left 
            if len(letters_left) == 0 and game_score.get_attemps() <= game_score.get_maximun_attemps():
                clean_screen()
                scene = scenes['win']
                input(gui.gui_in_game(game_score, lives, ''.join(word_map), letters_used,level,scene))
                print("game_score.get_level(): ",level.get_level())
                level.increase_level()
                print("game_score.get_level(): ",level.get_level())
                continue_game = False
                continue

            clean_screen()
            print(gui.gui_in_game(game_score, lives, ''.join(word_map), letters_used,level,scene[game_score.get_attemps()]))
            if game_score.get_attemps() < game_score.get_maximun_attemps():
                letter = input(gui.scroll_text('Enter your gess > ')).upper()
                # validate input
                try:
                    assert len(letter) == 1, "Please enter just one letter "
                    assert detect_special_character(letter) == False, 'No special characters allowed'
                    letters_used.append(letter)
                except AssertionError as er:
                    print(er)
                    sleep(1)

            if letter in letters_left:
                aux_list = [x + ' ' if x == letter else '_ ' for x in word_to_discover]
                for i in range(0, len(aux_list)):
                    if aux_list[i] != '_ ':
                        word_map[i] = aux_list[i]
                        try:
                            letters_left.remove(aux_list[i].strip())
                            game_score.increase_score()
                        except Exception as er:
                            print(er)
            else:
                game_score.increase_attemps()


def normalize_string(word: str) -> str:
    """Remove commons accents characters

    Args:
        word (str): word to process

    Returns:
        str: string without accents
    """

    word = re.sub(u"[àáâãäå]", 'a', word)
    word = re.sub(u"[èéêë]", 'e', word)
    word = re.sub(u"[ìíîï]", 'i', word)
    word = re.sub(u"[òóôõö]", 'o', word)
    word = re.sub(u"[ùúûü]", 'u', word)
    word = re.sub(u"[ýÿ]", 'y', word)
    word = re.sub(u"[ß]", 'ss', word)
    word = re.sub(u"[ñ]", 'n', word)
    return word


def start_game():
    _START_GAME = 1
    _EXIT_GAME = 2
    words = get_words('data.txt')

    while True:
        clean_screen()
        option = input(gui.gui_game())
        try:
            if option.isnumeric():
                if int(option) == _EXIT_GAME:
                    break
                elif int(option) == _START_GAME:
                    game2(words)
        except Exception as e:
            print(e)
