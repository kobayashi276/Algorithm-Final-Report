#Input: a horizontal transaction database D, a user-specified threshold minsup
#Output: the set of frequent itemsets
def Apriori_TID(D,minsup):
    #Generate C, _C, L with k = 1
    L=[]
    elements = []
    temp = []
    for val in D.values():
        temp.append(val)
        for v in val:
            if v not in elements:
                elements.append(v)
    elements = sorted(elements)
    
    C=[]
    C.append(temp)
    temp = {}
    for e in elements:
        count = 0
        for val in D.values():
            count = count + val.count(e)
        if count>=minsup:
            temp[e] = count
    L.append(temp)
    k=1
    _C = []
    
    dict_temp = {}
    for key, val in D.items():
        temp = []
        for v in val:
            temp.append([v])
        dict_temp[key] = temp
    
    _C.append(dict_temp)
      
    while L[k-1]!={}:
        C.append(generate_set(L[k-1],L[0])) #New candidates
        temp_C = []
        _C.append({})
        L.append({})
        temp_L = {}
        for c in C[k]:
            for key_c,val_c in _C[k-1].items():
                #Determine candidate itemset in Ck contained in the transaction
                count = 0
                for v in val_c:
                    if set(v).issubset(set(c)):
                        count=count+1
                if count>=len(c):
                    key_L = ','.join(str(e) for e in c)
                    if key_L not in temp_L:
                        temp_L[key_L] = 1
                    else:
                        val_L = temp_L[key_L]
                        temp_L[key_L] =  val_L + 1
                    if c not in temp_C:
                        temp_C.append(c)
                    if key_c not in _C[k]:
                        _C[k][key_c] = [c]   
                    else:
                        val_temp = _C[k][key_c]
                        _C[k][key_c] = val_temp + [c]
        #Check all candidate itemset if sastify minsup 
        for key_l, val_l in temp_L.items():
            if val_l>=minsup:
                L[k][key_l] = val_l
        print("K = " + str(k))
        print(L[k])
        k = k + 1
    return L

#Input: 2 dict a and b
#Output: all itemset of a and b
#Example: [[1],[1],[1]] and [1,2,3] will return
#                                   [[1,2],[1,3]]
def generate_set(L1,L2):
    result=[]
    a = []
    b = []
    for key in L1.keys():
        a.append(list(key.split(",")))
    for key in L2.keys():
        b.append([key])
    for x in a:
        for y in b:
            if x!=y:
                tmp = sorted(list(set(x) | set(y)))
                if tmp not in result:
                    result.append(tmp)
    return result            

x = Apriori_TID({"T1":["1","3","4"],"T2":["2","3","5"],"T3":["1","2","3","5"],"T4":["2","5"]},2)
print()
print("Final result:")
print(x)

# import time
# import random 
# import pylab

# N = []
# for i in range(6,50):
#   D = {}
#   for j in range(i):
#     D[j] = list([str((random.randint(0, 50))) for k in range (i)])
#   N.append(D)
# # print(N)
# import time
# def measure_time(func, N):
#     runtime = []
#     for n in N:
#         start = time.time()
#         f = func(n,2)
#         stop = time.time()
#         runtime.append(stop-start)
#     return runtime

# rtime = measure_time(Apriori_TID, N)
# rtime2 = [t*1.5 for t in rtime]
# pylab.plot(N, rtime, N, rtime2)
# pylab.legend(['1','2'])