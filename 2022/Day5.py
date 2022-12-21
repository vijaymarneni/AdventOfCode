#Part 1
def shippingYard():
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day5_Input_2022.txt","r", encoding="utf-8-sig")
    #stacks = ["ZN", "MCD", "P"]
    stacks = ["RPCDBG","HVG","NSQDJPM", "PSLGDCNM","JBNCPFLS","QBDZVGTS","BZMHFTQ","CMDBF","FCQG"]
    finalOutput = ""
    for la in f:
        li = la.split(" ")
        loopTimes = int(li[1])
        fromStack = int(li[3])-1
        toStack = int(li[5])-1
        for each in range(loopTimes):
            stacks[toStack] = stacks[toStack] + stacks[fromStack][len(stacks[fromStack])-1]
            stacks[fromStack] = stacks[fromStack][:-1]
    for i in stacks:
        finalOutput = finalOutput+ i[len(i)-1]
    print(finalOutput)
    f.close()

#Part 2	
def shippingYard():
    f = open("D:\\User\\vmarneni\\OneDrive - Altimetrik Corp\\Desktop\\2021\\Day5_Input_2022.txt","r", encoding="utf-8-sig")
    #stacks = ["ZN", "MCD", "P"]
    stacks = ["RPCDBG","HVG","NSQDJPM", "PSLGDCNM","JBNCPFLS","QBDZVGTS","BZMHFTQ","CMDBF","FCQG"]
    finalOutput = ""
    for la in f:
        li = la.split(" ")
        loopTimes = int(li[1])
        fromStack = int(li[3])-1
        toStack = int(li[5])-1
        #for each in range(loopTimes):
        stacks[toStack] = stacks[toStack] + stacks[fromStack][-loopTimes:]
        stacks[fromStack] = stacks[fromStack][:-loopTimes]
    for i in stacks:
        finalOutput = finalOutput+ i[len(i)-1]
    print(finalOutput)
    f.close()