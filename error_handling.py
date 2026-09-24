while True:
    try:
        panels = int(input("Enter number of panels: "))
        print(f"Panels entered:{panels}")
        break
    except ValueError:
        print("Invalid! Enter numbers, not text.")
