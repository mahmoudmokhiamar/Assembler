from assembler import Assembler

INPUT_FILE = 'testcode.asm'
OUT_FILE = 'testcode.mc'
MRI_FILE = 'mri.txt'
RRI_FILE = 'rri.txt'
IOI_FILE = 'ioi.txt'
if __name__ == "__main__":
    bin_text = ''
    asm = Assembler(asmpath=INPUT_FILE, \
                    mripath=MRI_FILE, \
                    rripath=RRI_FILE, \
                    ioipath=IOI_FILE)
binaries = asm.assemble()
bin_text = ''
for lc in binaries:
        bin_text += lc + ' ' + binaries[lc] + '\n'


# print(bin_text)
# with open(OUT_FILE, 'r') as file:
#         print(file.read())

outF = open('out.txt','r')
print(outF.read())
