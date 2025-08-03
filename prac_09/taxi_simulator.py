from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Run the taxi simulator with a menu system."""
    # Create a list of available taxis
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()
    # Main loop: keep going until user chooses to quit
    while choice != 'q':
        if choice == 'c':
            # Show available taxis with their index
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except(ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == 'd':
            if current_taxi:
                try:
                    # Ask how far to drive and calculate fare
                    distance = float(input("Drive how far?"))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Invalid distance.")
            else:
                print(f"You need to choose a taxi before you can drive")

        else:
            print("Invalid option")

        # Show current total bill and menu again
        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    # After quitting, print the final bill and the state of all taxis
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()