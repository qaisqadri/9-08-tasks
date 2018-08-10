
if __name__ == '__main__':
    N = int(input())
    instList=list()
    data=list()
    for i in range(0,N):
        inst=input()
        #instList.append(inst)
        instl=inst.split(" ")
        if instl[0]=="insert":
            data.insert(int(instl[1]),int(instl[2]))
        elif instl[0]=="print":
            print(data)
        elif instl[0]=="remove":
            data.remove(int(instl[1]))
        elif instl[0]=="append":
            data.append(int(instl[1]))
        elif instl[0]=="sort":
            data.sort()
        elif instl[0]=="pop":
            data.pop()            
        elif instl[0]=="reverse":
            data.reverse()
            
    
