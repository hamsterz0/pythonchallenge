import sys

def read_file(filepath):
    lines = []
    with open(filepath, 'r') as f:
        for line in f:
            lines.append(line)

    return ''.join(lines)


def main():
    filepath = sys.argv[1]
    file_contents = read_file(filepath)
    decode = list()
    for line in file_contents:
        for char in line:
            if char.isalpha():
                decode.append(char)
    print(''.join(decode))


main()
