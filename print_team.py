if __name__ == "__main__":
    f = open("teams.txt", 'r', encoding='utf-8')
    
    names = []
    ids = []

    for line in f:
        args = line.split(' ')
        names.append(args[1])
        ids.append(args[0])



    f.close()
