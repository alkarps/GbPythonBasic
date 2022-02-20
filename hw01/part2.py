time_in_sec = int(input("Input time in seconds: "))
hour = time_in_sec // 3600
minutes = time_in_sec % 3600 // 60
seconds = time_in_sec % 60

print(f"{hour:02}:{minutes:02}:{seconds:02}")
