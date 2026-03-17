
promt = input("enter a prompt=")

match promt:

    case "start":
        print("starting")
    case "stop":
        print("stoping")
    case "restart":
        print("restarting")
    case _:
        print("invalid prompt")