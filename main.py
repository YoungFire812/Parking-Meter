

# Data entry with a check on
def value_input():
    while True:
        print("Enter the time only in this format: 10:00 12:45 18:30")
        time_of_arrival = input("Enter what time the car arrived: ").split(":")
        end_time = input("Enter the time when the car leaves the parking lot: ").split(":")

        if len(time_of_arrival) < 2 or len(end_time) < 2 or len(time_of_arrival) > 2 or len(end_time) > 2:
            print("Enter only in the appropriate format")
            print()
            continue
        
        try:
            time_of_arrival[0] = int(time_of_arrival[0])
            time_of_arrival[1] = int(time_of_arrival[1])
            end_time[0] = int(end_time[0])
            end_time[1] = int(end_time[1])

        except ValueError:
            print("Enter only in the appropriate format")
            print()
            continue

        if time_of_arrival[0] > 23 or time_of_arrival[0] < 0 or end_time[0] > 23 or end_time[0] < 0 or time_of_arrival[1] > 60 or time_of_arrival[1] < 0 or end_time[1] > 60 or end_time[1] < 0:
            print("Incorrect time value")
            print()
            continue

        return time_of_arrival, end_time

# Calculates and displays the cost of parking
def calculate_the_price():
        time_of_arrival, end_time = value_input()

        # Calculates the price considering the rush hour and time of arrival
        if time_of_arrival[0] >= 8 and time_of_arrival[0] <= 17:
            time_of_arrival_count = (time_of_arrival[0] * 60) + time_of_arrival[1]
            end_time_count = (end_time[0] * 60) + end_time[1]

            if end_time[0] >= 8 and end_time[0] <= 17:
                end_price = (end_time_count - time_of_arrival_count) * 0.2

            else:
                end_price = ((1080 - time_of_arrival_count) * 0.2) + ((end_time_count - 1080) * 0.1)
            
        # Calculates the price taking into account the rush hour and departure time    
        elif (end_time[0] >= 8 and end_time[0] <= 17):
            time_of_arrival_count = (time_of_arrival[0] * 60) + time_of_arrival[1]
            end_time_count = (end_time[0] * 60) + end_time[1]

            end_price = ((1920 - time_of_arrival_count) * 0.1) + ((end_time_count - 480) * 0.2)

        # Carries out the calculation if the rush hour is not obvious
        else:
            time_of_arrival_count = (time_of_arrival[0] * 60) + time_of_arrival[1]
            end_time_count = (end_time[0] * 60) + end_time[1]
            
            if end_time_count < time_of_arrival_count:
                end_price = ((480 - time_of_arrival_count) * 0.1) + 120 + (360 + end_time_count) * 0.1

            else:
                end_price = (end_time_count - time_of_arrival_count) * 0.1

        return end_price

if __name__ == '__main__':
        end_price = calculate_the_price()
        print(f"Final price: {round(end_price, 2)}$")
            