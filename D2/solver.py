f = open("C:/Users/proma/Documents/AdventOfCode/D2/input.txt","r")

MAX_RGB_VALUES=[12,13,14]

colors =["red", "green" , "blue"]

games = f.readlines()

tot_games_ID =0
for game in games:
    rgb =[0,0,0]
    game_inf = game.split(":")
    game_id = game_inf[0][5:]
    sets = game_inf[1].split(";")
    for set in sets :
        cubes = set.split(",")
        for cube_type in cubes:
            res = cube_type.split()
            for i,color in enumerate(colors):
                if res[1]==color:
                    if rgb[i]<int(res[0]):
                        rgb[i] = int(res[0])
    is_game_valid=True
    for i in range(3):
        if rgb[i]>MAX_RGB_VALUES[i]:
            is_game_valid=False
            break
    if is_game_valid:
        tot_games_ID += int(game_id)
    is_game_valid=True
    
print(tot_games_ID)
