def readint (b: bytes) -> int:
    return int.from_bytes(b, byteorder="little")

file = open("decompressed/scn000a.rts", "rb")
log = open("scene.txt", "w", encoding="utf-8")

count = readint(file.read(1))
commands = {}
log.write(f"List of commands (total: 0x{count:X})\n")
for i in range(count):
    num = readint(file.read(4))
    length = readint(file.read(1))
    string = file.read(length).decode(encoding="shift-jis", errors="backslashreplace")

    #print(f"{num:08X}\t{string}")
    log.write(f"{num:08X} {string}\n")
    commands.update({num:string})

count = readint(file.read(1))
log.write(f"List of args (total: 0x{count:X})\n")
for i in range(count):

    length = readint(file.read(1))
    string = file.read(length).decode(encoding="shift-jis", errors="backslashreplace")
    #print(f"{string}")
    log.write(f"{string}\n")

count = readint(file.read(1))
log.write(f"List of indexed commands (total: 0x{count:X})\n")
for i in range(count):

    num1 = readint(file.read(4))
    num2 = readint(file.read(4))
    value = commands.get(num1)
    #print(f"{num1:08X} {num2:X} {value}")
    log.write(f"{num1:08X} {num2:X} {value}\n")

count = readint(file.read(1))
log.write(f"List of unknown commands (total: 0x{count:X})\n")
for i in range(count):
    num1 = readint(file.read(1))
    num2 = readint(file.read(4))
    value = commands.get(num2)
    #print(f"{num1:X} {num2:08X} {value}")
    log.write(f"{num1:X} {num2:08X} {value}\n")

count = readint(file.read(1))
flag = False
log.write(f"List of unknown commands (total: 0x{count:X})\n")
for i in range(count):

    current = file.tell()
    num1 = readint(file.read(4))
    num2 = readint(file.read(1))

    value = commands.get(num1)
    if value == None:
        #current = file.tell()
        print(f"{current:X} {i:X}")
    else:
        print(f"{num1:08X} {num2:X} {value}")
        log.write(f"{num1:08X} {num2:X} {value}\n")

    if num2 == 1:
        flag = True
        continue

    if (flag):
        break