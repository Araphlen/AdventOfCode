import numpy as np
import re 
f = open("D3/input1.txt","r")

import string

tot=0

lines = f.readlines()


def get_left_nb(i_line,i_c):
    i = i_c
    line = lines[i_line]
    nb_to_add = line[i]
    while i>0 and line[i-1].isdigit():
        i-=1
        nb_to_add =line[i] +nb_to_add
    
    if nb_to_add=='':
        return 0
    else: 
        return int(nb_to_add)
    
def get_right_nb(i_line,i_c):
    i = i_c
    line = lines[i_line]
    nb_to_add = line[i]
    while i<len(line)-1 and line[i+1].isdigit():
        i+=1
        nb_to_add =nb_to_add+line[i]
    
    if nb_to_add=='':
        return 0
    else: 
        return int(nb_to_add)


for i_line,line in enumerate(lines):
    for i_c,c in enumerate(line):
        if c=="*":
            adjacente_numbers = []
            #check a gauche 
            if line[i_c-1].isdigit():
                adjacente_numbers.append(get_left_nb(i_line,i_c-1))

            #check a droite 
            if line[i_c+1].isdigit():
                adjacente_numbers.append(get_right_nb(i_line,i_c+1))

            #check en haut 
            if i_line>0:
                up_line = lines[i_line-1]
                if up_line[i_c].isdigit():
                    i = i_c
                    nb_to_add = up_line[i]
                    while i<len(up_line)-1 and up_line[i+1].isdigit():
                        i+=1
                        nb_to_add =nb_to_add+up_line[i]
                    i = i_c
                    while i>0 and up_line[i-1].isdigit():
                        i-=1
                        nb_to_add =up_line[i] +nb_to_add
                    adjacente_numbers.append(int(nb_to_add))
                else:
                    if i_c>0:
                        if up_line[i_c-1].isdigit():
                            adjacente_numbers.append(get_left_nb(i_line-1,i_c-1))
                    if i_c<len(line)-1:
                        if up_line[i_c+1].isdigit():
                            adjacente_numbers.append(get_right_nb(i_line-1,i_c+1))

            #check en bas 
            if i_line<len(lines)-1:
                down_line = lines[i_line+1]
                if down_line[i_c].isdigit():
                    i = i_c
                    nb_to_add = down_line[i]
                    while i<len(down_line)-1 and down_line[i+1].isdigit():
                        i+=1
                        nb_to_add =nb_to_add+down_line[i]
                    i = i_c
                    while i>0 and down_line[i-1].isdigit():
                        i-=1
                        nb_to_add =down_line[i] +nb_to_add
                    adjacente_numbers.append(int(nb_to_add))
                else:
                    if i_c>0:
                        if down_line[i_c-1].isdigit():
                            adjacente_numbers.append(get_left_nb(i_line+1,i_c-1))
                    if i_c<len(line)-1:
                        if down_line[i_c+1].isdigit():
                            adjacente_numbers.append(get_right_nb(i_line+1,i_c+1))
            while 0 in adjacente_numbers:
                adjacente_numbers.remove(0)
            if len(adjacente_numbers)==2:
                tot+=adjacente_numbers[0]*adjacente_numbers[1]


print(tot)