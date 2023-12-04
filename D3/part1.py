import numpy as np
import re 
f = open("C:/Users/proma/Documents/AdventOfCode/D3/input1.txt","r")

special_characters = "!@#$%^&*()-+?_=,<>/"

tot=0

chiffres = {}
lines = f.readlines()
#liste des syboles autours du nombre
tour_du_chiffre=""

for l_idx,line in enumerate(lines):
    
    chiffres_line = np.array(re.findall(r'\d+', line))
    
    for i in range(len(chiffres_line)):
        chiffres[chiffres_line[i]] = line.find(chiffres_line[i])

    if l_idx==0:
        for nb, i_nb in chiffres.items():
            #reset du tour du nombre
            tour_du_chiffre=""
            if i_nb>0:
                tour_du_chiffre+=line[i_nb-1]
                tour_du_chiffre+=lines[l_idx+1][i_nb-1]

            if i_nb+len(nb)-1<len(line)-1:
                tour_du_chiffre+=line[i_nb+len(nb)]
                tour_du_chiffre+=lines[l_idx+1][i_nb+len(nb)]

            tour_du_chiffre+=lines[l_idx+1][i_nb:i_nb+len(nb)-1]
            for carac in special_characters:
                if carac in tour_du_chiffre:
                    tot += int(nb)
                    break

    elif l_idx<len(lines)-1:
        for nb, i_nb in chiffres.items():
            #reset du tour du nombre
            tour_du_chiffre=""
            if i_nb>0:
                tour_du_chiffre+=line[i_nb-1]
                tour_du_chiffre+=lines[l_idx+1][i_nb-1]

            if i_nb+len(nb)-1<len(line)-1:
                tour_du_chiffre+=line[i_nb+len(nb)]
                tour_du_chiffre+=lines[l_idx+1][i_nb+len(nb)]
            
            tour_du_chiffre+=lines[l_idx+1][i_nb:i_nb+len(nb)-1]
            tour_du_chiffre+=lines[l_idx-1][i_nb:i_nb+len(nb)-1]
            for carac in special_characters:
                if carac in tour_du_chiffre:
                    tot += int(nb)
                    break
    else:
        for nb, i_nb in chiffres.items():
            #reset du tour du nombre
            tour_du_chiffre=""
            if i_nb>0:
                tour_du_chiffre+=line[i_nb-1]
                tour_du_chiffre+=lines[l_idx-1][i_nb-1]

            if i_nb+len(nb)-1<len(line)-1:
                tour_du_chiffre+=line[i_nb+len(nb)]
                tour_du_chiffre+=lines[l_idx-1][i_nb+len(nb)]
            
            tour_du_chiffre+=lines[l_idx-1][i_nb:i_nb+len(nb)-1]
            for carac in special_characters:
                if carac in tour_du_chiffre:
                    tot += int(nb)
                    break

print(tot)