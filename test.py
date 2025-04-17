l=[2, 3, 4, 1]
empt=[]
def list_add_last(l,empt):
    a =0
    last=[]
    first =[]
    for i in range(len(l)+1):
        print (i)
        a+=1
        if a == len(l):
            last.append(l[i])
        if a < len(l):
            first.append(l[i])
    for i in range(len(last)):
        empt.append(last[i])
    for i in range(len(first)):
        empt.append(first[i])
    print(empt)

list_add_last(l,empt)
# first task