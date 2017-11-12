import sys
from firstdate import FirstDate, IncorrectInputString

with open(sys.argv[1], "r") as ins:
    for line in ins:
        try:
            print(FirstDate(line.strip()))
        except IncorrectInputString as e:
            print("is illegal")
