time_now = int(input("What is the current time? "))

time_to_wait = int(input("In how many hours should the alarm ring? "))

alarm_time = ((time_to_wait % 24) + time_now)

print("Alarm time is ", alarm_time, "hours")
