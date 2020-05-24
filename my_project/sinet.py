
import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    #Input
    to_input('./Number.png'),

    #Conv
    to_ConvRelu('conv1', s_filer=28, n_filer=32, offset='(0, 0, 0)', to='(0, 0, 0)', height=64, depth=64, width=2),
    


    to_end()

]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    