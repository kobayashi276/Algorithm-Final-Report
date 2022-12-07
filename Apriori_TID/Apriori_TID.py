#Input: a horizontal transaction database D, a user-specified threshold minsup
#Output: the set of frequent itemsets
def Apriori_TID(D,minsup):
    L=[]
    #Counting how many TID have each item, if below than minsup => remove
    while D!=[]:
        preL = L #Store the previous result
        L = []
        for d in D:
            if len(d)>=minsup and d not in L:
                L.append(d)
        if L==[]:
            break
        #Start intersection each other in list
        D=generate_intersection(L)
    return preL

#Input: list a
#Output: a list which intersection each other
def generate_intersection(a):
    result = []
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            tmp = list(set(a[i]).intersection(set(a[j])))
            result.append(tmp)
    for r in result:
        r.sort() 
    return result

result = Apriori_TID([["T1","T4","T5","T7","T8","T9"],
                            ["T1","T2","T3","T4","T6","T8","T9"],
                            ["T3","T5","T6","T7","T8","T9"],
                            ["T2","T4"],
                            ["T1","T8"]],2)
print()
print("Final result:")
print(result)