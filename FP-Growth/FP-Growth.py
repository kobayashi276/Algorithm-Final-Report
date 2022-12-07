def FP_Growth(D,minsup):
    Z = {}
    
    tmp = []
    for d in D:
        #remove duplicate
        d = list(dict.fromkeys(d))
        for di in d:
            if di not in Z:
                Z[di]=1
            else:
                Z[di]=Z[di] + 1
        tmp.append(d)
    
    D = tmp
    
    #remove any set in L have frequent < minsup
    Z = {key:val for key,val in Z.items() if val>=minsup}
    #sort the set L
    Z = dict(sorted(Z.items(), key=lambda item: item[1],reverse=True))
    
    #sort the database via priority in L
    for d in D:
        i = 0
        while (i<len(d)):
            if d[i] not in Z:
                d.remove(d[i])
            else:
                i=i+1
        d = sort_via_dict(d,Z)
    
    #start generate a FP-Growth tree via dict
    Z = dict(reversed(list(Z.items())))
    
    patern_base = {}
    for z in Z:
        patern_base[z] = {}
        for d in D:
            if z in d:
                for i in range(0,d.index(z)):
                    if d[i] not in patern_base[z]:
                        patern_base[z][d[i]]=1
                    else:
                        patern_base[z][d[i]]=patern_base[z][d[i]]+1
    
    #remove set which frequency lower than minsup and add frequency value
    #for complete a COnditional Frequent Pattern Tree
    pattern_tree_value = {}
    i=0
    for p in patern_base.values():
        p = {key:val for key,val in p.items() if val>=minsup}
        pattern_tree_value[i] = p
        i=i+1
    # print(pattern_tree_value)

    #start paring each items to each pattern tree
    pattern_tree = {}
    i=0
    for z in Z:
        pattern_tree[z]={}
        val = pattern_tree_value[i]
        i=i+1
        pattern_tree[z] = val
      
    result = {}
    for key, value in pattern_tree.items():
        temp = paring(key, value)
        if temp != []:
            result[key] = temp
        # print(pattern_tree[key])
    return result

#Input: matrix a, dict b for compare priority
#Output: sorted matrix a via priority   
def sort_via_dict(a,b):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if b[a[i]] < b[a[j]]:
                a[i], a[j] = a[j], a[i]
            elif a[i] > a[j] and b[a[i]] == b[a[j]]:
                 a[i], a[j] = a[j], a[i]  
    return a

#Input: a item a, conditional frequent pattern tree b
#Output: a list of paring between a and each element in pattern tree                   
def paring(a,b):
    result = []
    itemset = []
    for key, val in b.items():
        itemset.append(key)
        
    # print(itemset)
    for i in range(1,len(itemset)+1):
        generated_itemset = (generate_subitemset(itemset,i))
        # print(generated_itemset)
        for i in generated_itemset:
            # print("Combine")
            result.append(i+[a])
    return result
   
#Input: a set s, size r:
#Output: item set of r
def generate_subitemset(s,r):
    result = []
    result.append(s[:r]) #store the min value
    #generate the list of position from 0 to r-1
    position = [i for i in range(0,len(s))]
    #current position to count
    currentPos = position[:r]
    #max value position
    maxPos = position[len(s)-r:]
    while currentPos!=maxPos:
        check = True
        i=r-1
        #check whenever the position have the max position in maxPos
        while check or i<0:
            if currentPos[i]==maxPos[i]:
                i=i-1
            else:
                check=False
        #print(i)
        #start to increase by 1
        if i!=r-1:
            currentPos[i]=currentPos[i]+1
            for j in range(i+1,r):
                currentPos[j]=currentPos[j-1]+1
        else:
            currentPos[i]=currentPos[i]+1
        #print(currentPos)
        #store the new number to result
        set=[]
        for j in range(0,r):
            set.append(s[currentPos[j]])
        result.append(set)
    return result
    # current = [i for i in range(0,k)]
    # result = []
    # max = [i for i in range(len(a)-k,len(a))]
    # # print(current)
    # # print(max)
    # result.append([a[i] for i in current])
    # while (current!=max):
    #     i=k-1
    #     while i>=0:
    #         if current[i]+1>max[i]:
    #             i=i-1
    #             print(current[i])
    #             print(max[i])
    #         else:
    #             break
    #     print(current)
    #     if i<0:
    #         print("stop while")
    #         break
    #     for j in range(i,len(current)):
    #         current[j]=current[j]+1
    #         # print(current)
    #     result.append([a[k] for k in current])
    # print(result)
                
            

# x = FP_Growth([["I1","I2","I5"],["I2","I4"],["I2","I3"],["I1","I2","I4"],["I1","I3"],["I2","I3"],["I1","I3"],["I1","I2","I3","I5"],["I1","I2","I3"]],3)           

D = [["E","K","M","N","O","Y"],
     ["D","E","K","N","O","Y"],
     ["A","E","K","M"],
     ["C","K","M","U","Y"],
     ["C","E","I","K","O","O"]]

print(FP_Growth(D,3))