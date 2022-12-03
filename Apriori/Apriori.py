#Input: a horizontal transaction database D, a user-specified threshold minsup
#Output: the set of frequent itemsets
def Apriori(D,minsup):
    #Generate F1
    F=[]
    elements=[]
    for x in D:
        for y in x:
            if [y] not in F:
                F.append([y])
                elements.append(y)
                
    F.sort()
    elements.sort()
    
    #Start checking how many subset in mother set D
    L=[]
    while F != []:
        preL = L #previous L
        L = [] #current L
        #for each element in F start count how many subset in mother set D
        for x in F:
            count=0
            for y in D:
                if(set(x).issubset(set(y))):
                    count=count+1
            #checking is suitable for minsub
            if count>=minsup:
                L.append(x)
        #if no subset sastified minsub, break while loop and return the previous L
        if L==[]:
            break
        F = generate_set(L,elements)
        
    return preL

#Input: 2 list, a is matrix list and b is single list
#Output: itemset of 2 list
#Example: [[1],[1],[1]] and [1,2,3] will return
#                                   [[1,2],[1,3]]
def generate_set(a,b):
    result=[]
    for x in a:
        if x[-1] in b:
            for i in range(b.index(x[-1])+1,len(b)):
                temp = x + [b[i]]
                result.append(temp)
    return result
      
#####MAIN#####

# x = Apriori([["I1","I2","I5"],["I2","I4"],["I2","I3"],["I1","I2","I4"],["I1","I3"],["I2","I3"],["I1","I3"],["I1","I2","I3","I5"],["I1","I2","I3"]],2)
# print(x)