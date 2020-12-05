import sys
import argparse
import string


def read_file(filename):
    filecontents = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            filecontents.append(line)
    return filecontents

def decode_fn(filecontents):
    encoded = ''.join(filecontents)
    decoded = []
    for pos in range(4, len(encoded)-4):
        before = encoded[pos-4:pos]
        current = encoded[pos]
        after = encoded[pos+1:pos+5]
        if before[1:].isupper() and current.islower() and after[:-1].isupper():
            if before[0].islower() and after[-1].islower():
                decoded.append(current)

    # Considering two bases cases
    if encoded[:3].isupper() and encoded[3].islower() and encoded[4:7].isupper():
        if encoded[7].islower():
            decoded.insert(0, encoded[3])

    return ''.join(decoded)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True);
    args = parser.parse_args()
    filecontents = read_file(args.filename)

    decoded = decode_fn(filecontents)
    print(decoded)


main()
