import random
import string
import os
import platform as pl

from bleach import clean
import gui
import pyfiglet
import re

from life import *
from score import *



def get_words(file_name:str) ->list :
    """Reads a file text to fill a list of words    

    Returns:
        [list]: return a list with all the words in the file
    """
    words = []
    with open(file_name,'r', encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip('\n'))
    return words

def get_ramdom_word(words:list) -> str:
    """get a ramdom word from a list

    Args:
        words (list): a list of words 

    Returns:
        [str]: return a ramdom item from the list 
    """
    word = words[random.randint(0, len(words)-1)].upper()
    return word

def clean_screen():
    """
     this function clear the screen depending of OS 
    """ 
    if pl.system() =='Windows':
        os.system('cls')
    else:
        os.system('clear')


def game2(words:list):
    #initialize new game

    lifes            = Life()

    while (lifes.get_lifes() > 0):
        #get a random word
        word                =  get_ramdom_word(words)
        word_to_discover    = normalizeString(word)
        word_map            = ['_ ' for x in word]
        letters_left        = word
        game_score          = Score()  
        letters_used        = list()

        #clean_screen()
        print(gui.gui_in_game(game_score,lifes,''.join(word_map),letters_used))

        #game loop
        while True:
            #validate attemps
            if game_score.get_attemps() > game_score.get_maximun_attemps():
                input(gui.loose_screen(game_score.get_score(),word))
                break

            #validate letterrs left
            if len(letters_left) == 0:
                clean_screen()
                input(gui.win_screen(game_score.get_score(),word))
                break
            
            clean_screen()
            print(gui.gui_in_game(game_score,lifes,''.join(word_map),letters_used))
            if game_score.get_attemps() < game_score.get_maximun_attemps():
                letter = input(gui.scroll_text('Enter your gess > ')).upper()
                letters_used.append(letter)

            if letter in letters_left:
                aux_list = [x+' ' if x==letter else '_ ' for x in word_to_discover]
                for i in range(0,len(aux_list)):
                    if aux_list[i] != '_ ':
                        word_map[i] = aux_list[i]
                        try:
                            letters_left.remove(aux_list[i].strip())
                            game_score.increase_score(points())
                        except:
                            pass
            else:
                game_score.increase_attemps()

        lifes.decrease_life()


def game(): 

    word                =  list(get_ramdom_word(get_words()))
    word_to_discover    = normalizeString(''.join(word))
    word_map            = ['_ ' for x in list(word)] 
    letters_left        = word.copy()
    _ATTEMPS            = 9
    attemps             = 0
    win_points          = 0
    letter              = str()
    letters_used        = list()
    lives               = life()
    lives.set_lifes(3)
    
    clean_screen()
    print(gui.gui_in_game(win_points,_ATTEMPS,attemps,''.join(word_map),letters_used,lives))        
    while True:              

        if attemps > _ATTEMPS:
             
            input(gui.loose_screen(win_points,''.join(word)))                
            break  

        if len(letters_left) == 0: 
            clean_screen()
            input(gui.win_screen(win_points,''.join(word)))                
            break  
        
        clean_screen()
        print(gui.gui_in_game(win_points,_ATTEMPS,attemps,''.join(word_map),letters_used,lives))
        if attemps < _ATTEMPS: 
            letter = input(gui.scroll_text('Enter your gess > ')).upper()   
            letters_used.append(letter)

        if letter in letters_left:  
            aux_list = [x+' ' if x==letter else '_ ' for x in word_to_discover]
            
            for i in range(0,len(aux_list)):
                if aux_list[i] != '_ ':
                    word_map[i] = aux_list[i]
                    try:
                        letters_left.remove(aux_list[i].strip())
                        win_points += points()
                    except ValueError as a:
                        pass           
        else:
            attemps += 1
            
 


def points():
    ramdom_points = random.randrange(10,50)
    return ramdom_points

def normalizeString(word:str) -> str:
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
    _EXIT_GAME  = 2
    words = get_words('data.txt')
    
    while True:
        #clean_screen()
        option = input(gui.gui_game()) 
        try: 
            if option.isnumeric() :                 
                if int(option) == _EXIT_GAME:
                    break
                elif int(option) == _START_GAME:
                    game2(words)
        except Exception as e:
            print(e)