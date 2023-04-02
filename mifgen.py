import sys
import itertools

def read_objdump(filename):
    return [line.strip().split(' ') for line in open(filename).readlines()]

def write_mifdump(mif, filename):
    cnt = 0
    with open(filename, 'w') as out:
        out.write('DEPTH = 8192;\n')
        out.write('WIDTH = 32;\n')
        out.write('ADDRESS_RADIX = HEX;\n')
        out.write('DATA_RADIX = HEX;\n')
        out.write('CONTENT\n')
        out.write('BEGIN\n')
        for (addr, data) in mif:
            print(addr + ' : ' + data + ';')
            out.write(addr + ' : ' + data + ';\n')
        out.write('END;\n')

def split_lines(objdump):
    res = []
    for line in objdump:
        addr = int(line[0], 16) // 4
        for i in range(1, len(line)):
            # print(addr + i - 1, line[i])
            res.append((hex(addr + i - 1, )[2:], line[i]))
    return res
        

def reverse_words(mif):
    res = []
    for (addr, word) in mif:
        res.append((addr.rjust(4, '0'), word[6:8] + word[4:6] + word[2:4] + word[0:2]))
    return res

if len(sys.argv) != 3:
    print('Usage: python3 mifgen.py <input.od> <outpud.mif>')
    exit(1)
print('Input file: ' + sys.argv[1])
print('Output file: ' + sys.argv[2])
objdump = read_objdump(sys.argv[1])
mif = split_lines(objdump)
mif = reverse_words(mif)
write_mifdump(mif, sys.argv[2])
print('\nDone!')
