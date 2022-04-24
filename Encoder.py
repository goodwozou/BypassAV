# cs shellcode

buf = "input shellcode"
for b in buf:
    s = ord(b) ^ 15 ^ 16
    s = hex(s).split('0x')[1]
    if len(s) == 1:
        s = "0"+s
    print("\\x"+s,end="")
