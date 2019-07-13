import sys
import struct
from pattern_create import pattern_create

stack_length = 8192
pattern = ""
query = 0

try:
    if len(sys.argv) == 1:
        print("[x] Missing argument: <query> is required")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            raise ValueError
        else:
            pattern = pattern_create(stack_length)
    elif len(sys.argv) == 4:
        pattern = pattern_create(stack_length, sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        pattern = pattern_create(stack_length, sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise ValueError
except ValueError:
    print("Usage: python {} <query> [set_a] [set_b] [set_c]".format(sys.argv[0]))
    print("Example: python {} 0x37614136\n".format(sys.argv[0]))
    print("[*] Exact match at offset 20")
    sys.exit(1)

try:
    query = int(sys.argv[1], 16)
except ValueError as e:
    print("Enter a valid number!\n", e)
    sys.exit(1)

offset = pattern.find(struct.pack('<L', query).decode('utf-8'))

if offset != -1:
    while offset != -1:
        print("[*] Exact match at offset {}".format(offset))
        offset = pattern.find(struct.pack('<L', query).decode('utf-8'), offset + 1)
else:
    print("Not found!")
