#Input: a horizontal transaction database D, a user-specified threshold minsup
#Output: the set of frequent itemsets
def Apriori_TID(D,minsup):
    L=[]
    print(D)
    #Counting how many TID have each item, if below than minsup => remove
    while D!={}:
        preL = L #Store the previous result
        L = {}
        for key,val in D.items():
            if len(val)>=minsup and key not in L.keys():
                L[key]=val
        if L=={}:
            break
        #Start intersection each other in dict
        D=generate_intersection(L)
        print(L)
    return preL

#Input: dict a
#Output: a dict which intersection each other
def generate_intersection(a):
    result = {}
    for key,val in a.items():
        for keyi,vali in a.items():
            if key!=keyi and val!=vali:
                        key_splited = key.split(",")
                        keyi_splited = keyi.split(",")
                        key_intersect = ",".join(sorted(list(set(key_splited) | set(keyi_splited))))
                        value_intersect = sorted(list(set(val) & set(vali)))
                        result[key_intersect] = value_intersect
    return result

result = Apriori_TID({"I1":["T1","T4","T5","T7","T8","T9"],
                            "I2":["T1","T2","T3","T4","T6","T8","T9"],
                            "I3":["T3","T5","T6","T7","T8","T9"],
                            "I4":["T2","T4"],
                            "I5":["T1","T8"]},2)
print()
print("Final result:")
print(result)

####RUNNINGTIME####
import time
import pylab
import random 
N = []
for i in range(6,100):
  D = {}
  for j in range(i):
    D[j] = [str((random.randint(0, 50))) for k in range (i)]
  N.append(D)
fuct = []
for n in N:
  start = time.time()
  minsup = int(0.2*len(n))
  f = Apriori_TID(n,minsup)
  stop = time.time()
  fuct.append(stop-start)
pylab.xlabel('data points')
pylab.ylabel('time')
pylab.plot(list(range(94)), fuct)
pylab.legend(['Apriori_TID'])