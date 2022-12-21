# part1
def campCleaning():
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day4_Input_2022.txt","r", encoding="utf-8-sig")
    l = 0
    count = 0
    for la in f:
        li = la.split(",")
        firstPair= li[0].split("-")
        secondPair= li[1].split("-")
        a, b = int(firstPair[0]), int(firstPair[1])
        x, y = int(secondPair[0]), int(secondPair[1])
        if b < x or y < a:
            continue
        if a<=x and y<=b:
            count+=1
            continue
        if x<=a and b<=y:
            count+=1
    print(count)
    f.close()
	
# part2 
def campCleaning():
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day4_Input_2022.txt","r", encoding="utf-8-sig")
    l = 0
    count = 0
    for la in f:
        li = la.split(",")
        firstPair= li[0].split("-")
        secondPair= li[1].split("-")
        a, b = int(firstPair[0]), int(firstPair[1])
        x, y = int(secondPair[0]), int(secondPair[1])
        if b < x or y < a:
            continue
        #if a<=x and y<=b:
         #   count+=1
         #   continue
        #if x<=a and b<=y:
         #   count+=1
        count+=1
    print(count)
    f.close()