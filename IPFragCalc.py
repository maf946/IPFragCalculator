import math

dataSize        = 4000
MTU             = 1500
fragIdentifier  = "x"
headerSize      = 20

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
