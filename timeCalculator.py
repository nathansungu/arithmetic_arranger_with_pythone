def add_time(start, duration, starting_day=""):
    start_time = start[:-2]
    meridian = start[-2:]
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    sum_min = int(duration[-2:]) + int(start_time[-3:])
    sum_hours = int(duration[:-3]) + int(start_time[:-4])

    # Capitalize starting day if given
    starting_day_cap = starting_day.capitalize() if starting_day else ""
    week_day = f", {starting_day_cap}" if starting_day else ""
    day = ""

    if sum_min >= 60:
        sum_min -= 60
        sum_hours += 1
    sum_min = f"{sum_min:02d}"  

    number_of_days = 0
    if sum_hours >= 12:
        cycles = sum_hours // 12
        for _ in range(cycles):
            meridian = "PM" if meridian == "AM" else "AM"
            if meridian == "AM":
                number_of_days += 1
        sum_hours %= 12
        if sum_hours == 0:
            sum_hours = 12

    if number_of_days == 1:
        day = " (next day)"
    elif number_of_days > 1:
        day = f" ({number_of_days} days later)"

    if starting_day:
        start_index = [d.lower() for d in days_of_week].index(starting_day.lower())
        new_index = (start_index + number_of_days) % 7
        week_day = f", {days_of_week[new_index]}"

    new_time = f"{sum_hours}:{sum_min} {meridian}{week_day}{day}"
    return new_time


print(add_time('3:30 PM', '2:12'))


