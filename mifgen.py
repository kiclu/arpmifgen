import sys

def read_mifdump(filename):
    return [line.strip().split(' : ') for line in open(filename).readlines()]

def insch(my_str, group=2, char=' '):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

def pack(addr):
    return hex(int(addr, 16)//4)[2:]

def split_words(dump):
    cnt = 0
    for line in dump:
        line[1] = insch(line[1])
        tmp = line[1].split(' ')
        cnt += 1
        line[1] = ''.join(tmp)
        print(pack(line[0]) + ' : ' + line[1])
    return cnt

def write_mifdump(dump, filename, cnt):
    with open(filename, 'w') as out:
        out.write('DEPTH = ' + str(cnt) + ';\n')
        out.write('WIDTH = 32;\n')
        out.write('ADDRESS_RADIX = HEX;\n')
        out.write('DATA_RADIX = HEX;\n')
        out.write('CONTENT\n')
        out.write('BEGIN\n')
        for (addr, data) in dump:
            out.write(pack(addr) + ' : ' + data + ';\n')
        out.write('END;\n')

if len(sys.argv) != 3:
    print('Usage: python3 mifgen.py <input.mifdump> <outpud.mif>')
    exit(1)

print('Input: ' + sys.argv[1])
print('Output: ' + sys.argv[2])
mifdump = read_mifdump(sys.argv[1])
cnt = split_words(mifdump)
write_mifdump(mifdump, sys.argv[2], cnt)
print('Done!')