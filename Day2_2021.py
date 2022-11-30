def depthOfTravel():
    f = open("D:\\User\\vmarneni\\Downloads\\puzzle2.csv","r", encoding="utf-8-sig")
    l = 0
    d = 0
    for la in f:
        li = la.split(" ")
        x = int(li[1])
        if li[0] == "forward":
            l=l+x
        if li[0] == "down":
            d=d+x
        if li[0] == "up":
            d=d-x
    f.close()
    return l,d, l*d


def depthOfTravel():
    f = open("D:\\User\\vmarneni\\Downloads\\puzzle2.csv","r", encoding="utf-8-sig")
    l = 0
    d = 0
    depth = 0
    for la in f:
        li = la.split(" ")
        x = int(li[1])
        if li[0] == "forward":
            if d != 0:
                depth+=x*d
            l=l+x
        if li[0] == "down":
            d=d+x
        if li[0] == "up":
            d=d-x
    f.close()
    return l,d, depth,  l*depth



