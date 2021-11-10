import argparse
from argparse import RawTextHelpFormatter
import math

usageInfo = "Example usage:\npython3 IPFragCalc.py --dataSize 5144 --MTU 1500 --fragIdentifier y --headerSize 20"

parser = argparse.ArgumentParser(description='A teaching tool for IP fragmentation', epilog=usageInfo, formatter_class=RawTextHelpFormatter)
parser.add_argument('--dataSize', dest='dataSize', type=int, nargs='?', default=4000,
                    help='The size of the datagram to be formatted')
parser.add_argument('--MTU', dest='MTU', type=int, nargs='?', default=1500, help='The maximum transmission unit')
parser.add_argument('--fragIdentifier', dest='fragIdentifier', nargs='?', default="x", help='The fragment identifier')
parser.add_argument('--headerSize', dest='headerSize', type=int, nargs='?', default=20,
                    help='The size of the IP header. This amount is deducted from the dataSize when calculating '
                         'fragment lengths')
args = parser.parse_args()

dataSize = args.dataSize
MTU = args.MTU
fragIdentifier = args.fragIdentifier
headerSize = args.headerSize

maxPayload = MTU - ((MTU - headerSize) % 8)
fragFlag = 1
offset = 0
remaining = dataSize

print('| {:^10} | {:^5} | {:^8} | {:^8} | {:^23} |'.format('Length', 'ID', 'fragFlag', 'Offset',
                                                           'FYI: len (excl. header)'))
i = 0

while remaining > 0:
    length = 0
    if maxPayload < remaining:
        length = MTU
    else:
        length = remaining
        fragFlag = 0
        remaining = 0
    remaining = remaining - (length - headerSize)
    print('| {:>10} | {:>5} | {:>8} | {:>8} | {:>23} |'.format(length, fragIdentifier, fragFlag, int(math.ceil(offset)), length - headerSize))
    offset = offset + ((length - headerSize) / 8)
    i += 1
