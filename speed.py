import sys

def calculate_speed(distance, time):
    return distance / time

def main():
    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    else:
        # Local use only
        distance = float(input("Enter distance traveled (in km): "))
        time = float(input("Enter time taken (in hours): "))

    print("Speed =", calculate_speed(distance, time))

if __name__ == "__main__":
    main()