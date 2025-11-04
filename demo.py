serial = bytes.fromhex('5B134977135E7D13')
v7 = b'\x10\x20\x30'

output = [chr(serial[i] ^ v7[i % 3]) for i in range(len(serial))]

print(''.join(output))