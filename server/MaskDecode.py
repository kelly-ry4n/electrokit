def decode(data):
    frame = bytearray(data)

    length = frame[1] & 127

    indexFirstMask = 2
    if length == 126:
        indexFirstMask = 4
    elif length == 127:
        indexFirstMask = 10

    indexFirstDataByte = indexFirstMask + 4
    mask = frame[indexFirstMask:indexFirstDataByte]

    i = indexFirstDataByte
    j = 0
    decoded = []
    while i < len(frame):
        decoded.append(frame[i] ^ mask[j%4])
        i += 1
        j += 1

    print decoded

    return "".join(chr(byte) for byte in decoded)