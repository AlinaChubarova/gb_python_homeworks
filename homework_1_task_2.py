time = int(input("Enter time in seconds "))
hour = time // 3600
minute = (time // 60) % 60
second = time % 60
if hour < 10:
    hour = "0" + str(hour)
else:
    hour = hour
if minute < 10:
    minute = "0" + str(minute)
else:
    minute = minute
if second < 10:
    second = "0" + str(second)
else:
    second = second

print(f"{time} seconds is {hour}:{minute}:{second}")
