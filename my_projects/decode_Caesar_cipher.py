import argparse

def decode_Caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) - n) % len(alpha)]
    print(text)


parser = argparse.ArgumentParser(description="Decode a Caesar Cipher.")
parser.add_argument("--word", type=str, required=True, help="The word to decode")
parser.add_argument("--offset", type=int, required=True, help="The offset to use for decoding.")

args = parser.parse_args()

decode_Caesar_cipher(args.word, args.offset)