from prac_09.unreliable_car import UnreliableCar

def main():

    # create a car that have 30% reliable.
    car = UnreliableCar("Old Bomb", 100, 30)

    # drive 10 times and each time drive 10km.
    for i in range(10):
        distance_driven = car.drive(10)
        print(f"Attempt {i + 1}: drove {distance_driven}km, fuel left: {car.fuel}, odometer: {car.odometer}")

if __name__ == "__main__":
    main()