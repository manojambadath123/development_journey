
signal = input("enter color of signal=")

match signal:

    case "red":
        print("stop")
    case "green":
        print("go")
    case "yellow":
        print("wait")
    case _:
        print("invalid")