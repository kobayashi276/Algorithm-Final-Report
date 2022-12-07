def Apriori_TID(R, minsup):
  D = {}
  for item in R:
    for tid in R[item]:
      if tid in D:
        D[tid].append(item)
      else:
        D[tid] = []
        D[tid].append(item)
  C1 = {}
  for tid in D:
    for item in D[tid]:
      if item in C1:
        C1[str(item)] += 1
      else:
        C1[str(item)] = 1
  F = [[]]
  for item in C1:
    if C1[item] >= minsup:
      F[0].append(set(item))
  k = 1
  while len(F[k-1]) != 0:
    C = CandidateGeneration(F[k-1], k+1)    
    for can in C:
      count = 0
      for itemset in F[k-1]:
        if itemset.issubset(set(can)):
          count += 1
      if count != (k+1):
        C.remove(can)
    sup = [0]*len(C)
    for tid in D:
      for i in range(len(C)):
        if set(C[i]).issubset(set(D[tid])):
          sup[i] += 1
    F.append([])
  
    for i in range(len(sup)):
      if sup[i] >= minsup:
        F[-1].append(set(C[i]))
    k += 1  
  result = []
  for i in F:
    for itemset in i:
      result.append(itemset)
  return result

def CandidateGeneration(F, k):
  items = set()
  for itemset in F:
    for item in itemset:
      items.add(item)
  comb = combinations(items, k)
  return list(comb)