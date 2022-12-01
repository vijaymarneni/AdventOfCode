# Please look at this link for more details of this program https://adventofcode.com/2022/day/1
def test():
    # open file, using encoding to get rid of the special character in file reading.
    with open("C:\\Users\\vijay\\AdventOfCode\\2022\\day1_input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        total, calories = 0 , []
        # read through each line
        for line in data:
                # Add all numbers till blank line. if the blank line comes, add total to list and reset total to 0.
                if line == "" or line == "\n":
                    calories.append(total)
                    total = 0
                else:
                    total+=int(line)
        # print the maximum number from list.
        print(max(calories))

def test2():
    with open("C:\\Users\\vijay\\AdventOfCode\\2022\\day1_input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        total, calories = 0 , []
        for line in data:
                if line == "" or line == "\n":
                    calories.append(total)
                    total = 0
                else:
                    total+=int(line)
        # sort data
        calories.sort()
        # Add last 3 numbers in the list.
        print(calories[-1]+calories[-2]+calories[-3])


test()
test2()