f = open("C:/Users/proma/Documents/AdventOfCode/D2/input.txt","r")

colors =["red", "green" , "blue"]

games = f.readlines()

tot_games_power =0
for game in games:
    min_rgb =[0,0,0]
    game_inf = game.split(":")
    game_id = game_inf[0][5:]
    sets = game_inf[1].split(";")
    for set in sets :
        cubes = set.split(",")
        for cube_type in cubes:
            res = cube_type.split()
            for i,color in enumerate(colors):
                if res[1]==color:
                    if min_rgb[i]<int(res[0]):
                        min_rgb[i] = int(res[0])

    print(int(min_rgb[0])*int(min_rgb[1])*int(min_rgb[2]))
    tot_games_power+=(int(min_rgb[0])*int(min_rgb[1])*int(min_rgb[2]))
print(tot_games_power)
