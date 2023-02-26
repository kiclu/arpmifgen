import sys

def read_mifdump(filename):
    return [line.strip().split(' : ') for line in open(filename).readlines()]

def insch(my_str, group=2, char=' '):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

def split_words(dump):
    cnt = 0
    for line in dump:
        line[1] = insch(line[1])
        tmp = line[1].split(' ')[::-1]
        cnt += len(tmp)
        line[1] = ' '.join(tmp)
    return cnt

def write_mifdump(dump, filename, cnt):
    with open(filename, 'w') as out:
        out.write('DEPTH = ' + str(cnt) + ';\n')
        out.write('WIDTH = 8;\n')
        out.write('ADDRESS_RADIX = HEX;\n')
        out.write('DATA_RADIX = HEX;\n')
        out.write('CONTENT\n')
        out.write('BEGIN\n')
        for (addr, data) in dump:
            out.write(addr + ' : ' + data + ';\n')
        out.write('END;\n')

print(len(sys.argv))
if len(sys.argv) != 3:
    print('Usage: python3 mifgen.py <input.mifdump> <outpud.mif>')
    exit(1)

mifdump = read_mifdump(sys.argv[1])
cnt = split_words(mifdump)
print(mifdump)
write_mifdump(mifdump, sys.argv[2], cnt)
