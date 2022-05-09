import random
import string
import os
import platform as pl
import gui
import pyfiglet



def get_words():
    words = []
    with open('data.txt','r', encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip('\n'))
    return words

def get_ramdom_word(words:list):
    word = words[random.randint(0, len(words)-1)].upper()
    return word

def clean_screen():
    if pl.system() =='Windows':
        os.system('cls')
    else:
        os.system('clear')

def game(): 

    word                =  list(get_ramdom_word(get_words()))
    word_to_discover    = word
    word_map            = ['_ ' for x in list(word)] 
    letters_left        = word.copy()
    _ATTEMPS            = 9
    attemps             = 0
    win_points          = 0
    letter              = str()
    letters_used        = list()
    
    clean_screen()
    print(gui.gui_in_game(points=win_points,attemps=_ATTEMPS,attemp=attemps,word_map=''.join(word_map),letters_used=letters_used))        
    while True:              

        if attemps > _ATTEMPS:
             
            input(gui.loose_screen(win_points,''.join(word)))                
            break  

        if len(letters_left) == 0: 
            clean_screen()
            input(gui.win_screen(win_points,''.join(word)))                
            break  
        
        clean_screen()
        print(gui.gui_in_game(points=win_points,attemps=_ATTEMPS,attemp=attemps,word_map=''.join(word_map),letters_used=letters_used))
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

def normalizeString(word:str):
    pass





def start_game():
    _START_GAME = 1
    _EXIT_GAME  = 2
    
    while True:
        clean_screen()
        option = input(gui.gui_game()) 
        try: 
            assert option.isnumeric()
            if int(option) == _EXIT_GAME:
                break
            elif int(option) == _START_GAME:
                game()
        except TypeError as e:
            print(e)