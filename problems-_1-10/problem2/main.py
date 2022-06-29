#speed camera problem - find numberplate, then speed
import re
pattern="^[A-Z]{2}[0-9]{2} [A-Z]{3}$"
check_valid= lambda numberplate: re.match(pattern,numberplate)

numberplate=input("Please enter the numberplate in UK format (i.e. XX77 787): ")
valid=check_valid(numberplate)
if not valid:
    print("Numberplate invalid")
else:
    print("Numberplate valid")
time=int(input("How long did the car take to travel between the two speed cameras in seconds: "))
time_in_hours=time/3600
speed=1/time_in_hours
print(f"The speed of the driver was {speed} mph")

