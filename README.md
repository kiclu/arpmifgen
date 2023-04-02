# arpmifgen

mifgen is a tool used to convert compiled binaries to Intel MIF file format.
To use it, you first need to run `objdump -z --full-contents <binary> | cut -d ' ' -f 2,3,4,5,6 | grep -E '[[:digit:]]' > <objdump.od>`.
Then run mifgen: `python3 mifgen.py <objdump.od> <output.mif>`
