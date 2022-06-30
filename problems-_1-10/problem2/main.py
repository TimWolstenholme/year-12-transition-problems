#speed camera problem - find numberplate, then speed
import re
pattern="^[A-Z]{2}[0-9]{2} [A-Z]{3}$"
check_valid= lambda numberplate: re.match(pattern,numberplate)
with open('problem2data.txt','r') as f:
    for line in f:
        numberplate,time=line.split('-')


    valid=check_valid(numberplate)
    if not valid:
        print("Numberplate invalid")
    else:
        print("Numberplate valid")
    time_in_hours=time/3600
    speed=1/time_in_hours
    speeding="speeding" if speed>70 else "not speeding"
    print(f"{numberplate} had a speed of {speed} and was {speeding}")
