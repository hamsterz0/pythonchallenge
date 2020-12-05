def decode(char):
    if char.isalpha():
        return chr((((ord(char) - ord('a')) + 2) % 26) + 97)
    return char


def main():
    enc = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    enc2 = "map"
    
    text = map(decode, enc2)
    print(''.join(list(text)))
main()
