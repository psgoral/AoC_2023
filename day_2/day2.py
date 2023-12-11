def load_input(filename):
    fd = open(filename,'r')
    return [line.strip() for line in fd.readlines()]

def extract_ints_from_str(txt):
    return [int(s) for s in txt.split() if s.isdigit()]

def get_cubes(game):
    reds = list()
    greens = list()
    blues = list()

    reveals = game.split(':')[1].replace(";",',')
    for reveal in reveals.split(','):
        if "red" in reveal:
            reds.append(extract_ints_from_str(reveal)[0])
        if "green" in reveal:
            greens.append(extract_ints_from_str(reveal)[0])
        if "blue" in reveal:
            blues.append(extract_ints_from_str(reveal)[0])

    if type == "max":
        return max(reds), max(greens), max(blues)
    





def main():
    games = load_input("day2_input")
    games_ok = list()
    for game in games:
        r,g,b = get_cubes(game)
        if r <=12 and g <= 13 and b <= 14:
            print(extract_ints_from_str(game))
            games_ok.append(extract_ints_from_str(game.split(':')[0])[0])
    print(games_ok)
    print(sum(games_ok))

    #part2
    games2 = list()
    for game in games:
        r,g,b = get_cubes(game)
        games2.append(r*g*b)
    print(sum(games2))






if __name__ == '__main__':
    main()