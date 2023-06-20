# ⛔️ UnicodeDecodeError: 'ascii' codec can't decode byte 0xf0 in position 0: ordinal not in range(128)
with open('example.txt', 'r', encoding='ascii') as f:
    lines = f.readlines()

    print(lines)
