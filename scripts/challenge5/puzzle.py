import pickle

def main():
    pdata = None
    with open('banner.p', 'rb') as f:
        pdata = pickle.load(f)

    line = ''
    for data in pdata:
        for code in data:
            line = line + code[0]*code[1]
        line = line + '\n'


    print(line)


main()
