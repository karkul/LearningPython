command = ""
started = False

while True:
    command = input(">").lower()

    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""\
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        print("Bye!")
        break
    else:
        print("I don't understand that...")


