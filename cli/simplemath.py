userinput = ""

while True:
    userinput = input("> ")

    inputlist = userinput.split(" ")
    command = inputlist[0]

    if command == "d":
        print("double values")
        for i in range(1, len(inputlist)):
            print(2 * int(inputlist[i]))
    elif command == "t":
        print("triple values")
    elif command == "q":
        print("Goodbye")
        break
    else:
        print("unknown command", command)
        
