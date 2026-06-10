
def traffic_decision(choice, emergency=False, night=False):
    
    if emergency == True:
        return "EMERGENCY! It's an emergency please give space."

    choice = choice.lower().strip()

    if night == True and choice == "yellow":
        return "It is night - drive slow, be safe!"
    
    if choice=="red":
        print("STOP!")
    elif choice== "yellow" :
        print("GET READY!")
    elif choice == "green" :
        print("YOU MAY GO!")
    else:
        print("Invalid choice of colour for signal.")

def main():
    print("-" * 45)
    print("     TRAFFIC SIGNAL DECISION SYSTEM")
    print("-" * 45)
    print("Signals: green / yellow / red")
    print("For closing type 'q'.")
    print("-" * 45)

    while True:
        print()
        colour = input("Tell the signal colour - ")

        if colour.lower()=="q":
            print("Program closed.Safe driving!")
            break

        emg = input("Is this is an emergency vehicle ?(y/n):' ").lower()
        emergency = emg in "y"

        nig = input("Is it night? (y/n) : ").lower()
        night = nig in "y"

        result = traffic_decision(colour, emergency=emergency, night=night)
 
        # Result print karo
        print("-" * 45)
        if result is None:
            continue
        else:
            print("Decision:", result)
        print("-" * 45)
 
 
# Program yahan se shuru hota hai
if __name__ == "__main__":
    main()