#Input: database vertical R, int minsup
#Output: itemset of frequency
def Eclat(R,minsup):
    result = {} #final frequent itemset
    for x,y in R.items():
        if len(y)>=minsup:
            E = {} #current frequent itemset
            for xi,yi in R.items():
                if xi!=x and yi!=y:
                    #calculate the tidset of X={x:y} | Y={xi:yi}
                    if len(yi)>= minsup:
                        x_splited = x.split(",")
                        xi_splited = xi.split(",")
                        key_intersect = ",".join(sorted(list(set(x_splited) | set(xi_splited))))
                        value_intersect = sorted(list(set(y) & set(yi)))
                        if len(value_intersect)>=minsup: #If X | Y is frequent
                            #Add X | Y to frequent extension of X
                            E[key_intersect] = value_intersect 
                        print(E)
                    result = result | Eclat(E,minsup) #recursive call using current dataase E
            result = result | E
    return result


R = {"Bread":["T1","T4","T5","T7","T8","T9"],
     "Butter":["T1","T2","T3","T4","T6","T8","T9"],
     "Milk":["T3","T5","T6","T7","T8","T9"],
     "Coke":["T2","T4"],
     "Jam":["T1","T8"]}

result = Eclat(R,2)
print()
print("Final Reuslt:")
print(result)