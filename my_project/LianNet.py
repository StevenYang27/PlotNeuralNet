
import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # Picture
    to_input('./Face.jpg', width=15, height=15),

    # Convolution
    to_ConvRelu('cr1', s_filer=48, n_filer=32, offset='(0, 0, 0)', to='(0, 0, 0)', height=64, depth=64, width=2, caption='conv1'),
    to_Pool('pool1', offset='(0, 0, 0)', to='(cr1-east)', height=32, depth=32),
    to_ConvRelu('cr2', s_filer=24, n_filer=32, offset='(1, 0, 0)', to='(pool1-east)', height=32, depth=32, width=2, caption='conv2'),
    to_connection('pool1', 'cr2'),
    to_Pool('pool2', offset='(0, 0, 0)', to='(cr2-east)', height=16, depth=16),
    to_ConvRelu('cr3', s_filer=12, n_filer=64, offset='(1,0,0)', to='(pool2-east)', height=16, depth=16, width=2, caption='conv3'),
    to_connection('pool2', 'cr3'),
    to_Pool('pool3', offset='(0, 0, 0)', to='(cr3-east)', height=8, depth=8),

    # Full Connection
    to_FullConnection('fc1', s_filer=1, n_nueron=2048, offset='(4, 0, 0)', to='(pool3-east)', caption='fc1'),
    to_connection('pool3', 'fc1'),
    to_connection_dot('fc1', 'pool3'),
    to_FullConnection('fc2', s_filer=1, n_nueron=1024, offset='(1, 0, 0)', to='(fc1-east)', depth=50, caption='fc2'),
    to_connection('fc1', 'fc2'),
    to_FullConnection('fc3', s_filer=1, n_nueron=7, offset='(1, 0, 0)', to='(fc2-east)', depth=10, caption='fc3'),
    to_connection('fc2', 'fc3'),
    to_connection_end('fc3'),

    to_end()

]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    