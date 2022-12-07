def Apriori_TID(D,minsup):
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
    print("_C")
    print(_C) 
    print("C")
    print(C)   
    print()
    
    while L[k-1]!={}:
        C.append(generate_set(L[k-1],L[0]))
        temp_C = []
        # print(C[k])
        _C.append({})
        for c in C[k]:
            for key_c,val_c in _C[k-1].items():
                count = 0
                print()
                print(c)
                print(val_c)
                for v in val_c:
                    print(v)
                    if set(v).issubset(set(c)):
                        count=count+1
                        print(set(v).issubset(set(c)))
                print(count)
                if count>=minsup:
                    if c not in temp_C:
                        temp_C.append(c)
                    if key_c not in _C[k]:
                        _C[k][key_c] = [c]   
                    else:
                        val_temp = _C[k][key_c]
                        _C[k][key_c] = val_temp + [c]
        print(_C[k])
        print(temp_C)
        break 
  
def generate_set(L1,L2):
    result=[]
    a = []
    b = []
    for key in L1.keys():
        a.append([key])
    print(a)
    for key in L2.keys():
        b.append([key])
    print(b)
    for x in a:
        for y in b:
            if x!=y:
                # x_splited = x.split(",")
                # xi_splited = xi.split(",")
                # key_intersect = ",".join(sorted(list(set(x_splited) | set(xi_splited))))
                tmp = sorted(list(set(x) | set(y)))
                if tmp not in result:
                    result.append(tmp)
    print(result)
    return result            

# x = Apriori_TID({"T1":["I1","I2","I5"],"T2":["I2","I4"],"T3":["I2","I3"],"T4":["I1","I2","I4"],"T5":["I1","I3"],"T6":["I2","I3"],"T7":["I1","I3"],"T8":["I1","I2","I3","I5"],"T9":["I1","I2","I3"]},2)
x = Apriori_TID({"T1":[1,3,4],"T2":[2,3,5],"T3":[1,2,3,5],"T4":[2,5]},2)
print()
print("Final result:")
print(x)