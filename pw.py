def pw(*args):
    if len(args) == 0:
        print("", end=" ")
        for i in range(97,97+26):
            print(chr(i) + ":" + str(i), end="  ")
        print()
        print("heitorchang")
    else:
        out = "w"
        for c in args:
            out += chr(c)
        print(out)
        
