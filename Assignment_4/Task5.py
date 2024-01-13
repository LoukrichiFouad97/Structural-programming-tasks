def calculate_time_difference(start_time, end_time):
    start_hours = start_time // 100
    start_minutes = start_time % 100

    end_hours = end_time // 100
    end_minutes = end_time % 100

    start_total_minutes = start_hours * 60 + start_minutes
    end_total_minutes = end_hours * 60 + end_minutes

    time_difference = end_total_minutes - start_total_minutes

    # Consider the case where the end time is on the next day
    if time_difference < 0:
        time_difference += 24 * 60

    return time_difference

def main():
    start_time = int(input("Enter the start time (in military notation, e.g., 1200): "))
    end_time = int(input("Enter the end time (in military notation, e.g., 2359): "))

    difference_in_minutes = calculate_time_difference(start_time, end_time)

    print(f"The time difference is {difference_in_minutes} minutes.")

if __name__ == "__main__":
    main()
