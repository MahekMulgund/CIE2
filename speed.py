import sys

def calculate_speed(distance, time):
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time

def main():
    # Case 1: If arguments are provided (for Jenkins)
    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
        speed = calculate_speed(distance, time)
        print(f"Speed: {speed} km/hr")
    else:
        # Case 2: Normal user input
        distance = float(input("Enter distance traveled (in km): "))
        time = float(input("Enter time taken (in hours): "))
        speed = calculate_speed(distance, time)
        print(f"Speed: {speed} km/hr")

if __name__ == "__main__":
    main()
