f = open("C:/Users/proma/Documents/AdventOfCode/J1/input.txt","r")
lines = f.readlines()
tot=0
substringsletters=["one","two","three","four","five","six","seven","eight","nine"]
substringsnumbers=["o1e","t2o","t3ee","f4ur","f5ve","s6x","s7ven","e8ght","n9ne"]
for line in lines:
    nb = ""
    nbs=[]
    print(line)
    for i in range(len(substringsnumbers)):
        line=line.replace(substringsletters[i],substringsnumbers[i])
    print(line)
    for letter in line:
        if letter in "123456789":
            nb+=letter
    tot+=int(nb[0]+nb[-1])
    print(nb[0]+nb[-1])

print(tot)