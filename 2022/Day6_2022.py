# Part 1 - not scalable solution so changed in part2
def isUnique(s):
    if s[0] == s[1] or s[0] == s[2] or s[0] == s[3] or s[1] == s[2] or s[1] == s[3] or s[2] == s[3]:
        return False
    return True

def startOfPacket():
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day6_Input_2022.txt","r", encoding="utf-8-sig")
    position = 0
    for la in f:
        for c in range(4, len(la)):
            if isUnique(la[c:c+4]):
                position = c+4
                break
    print(position)
    f.close()

# part 2 
def isUnique(s):
    # this converts string into a list and then to a set. set does not allow duplicates. returning length of set. Hope you got the logic. lenght is 14 means no duplicates otherwise continue
    return len(set(list(s)))
    
def startOfPacket(pos):
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day6_Input_2022.txt","r", encoding="utf-8-sig")
    position = 0
    for la in f:
        for c in range(len(la)-pos):
            # if you get the 14 consecutive characters without duplicate then get position and break loop.
            if isUnique(la[c:c+pos]) == pos:
                position = c+pos
                break
    print(position)
    f.close()
    
# run with number of messages you look for in the puzzle asked to find 14
# so run as startOfPacket(14)