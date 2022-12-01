

# Input: dataset with many transactions, minimum support.

# output list of frequent itemset


data = {}
trans = 0
f = open('data.txt', 'r', encoding="utf8")
for row in f:
    trans += 1
    for item in row.rstrip('\n').split(','):
        #print(item)
        if item not in data:
            data[item] = set()
        data[str(item)].add(trans)

f.close()


list_of_name = list(data.keys())
list_of_number = data.values()
temp_number = []
temp =[]
for i in list_of_number:
    temp_number.append(list(i))

temp = dict()

for i in range(len(temp_number)):
    temp[list_of_name[i]] = temp_number[i]


count = 0
temp_count = count-1




print(list_of_name)
print(temp_number)
i = 0

minsups = 3
data_res = []
res_dict = {}
res_dict[list_of_name[0]] = []
name_list_v2 = []
while list_of_name:
    #print(list_of_name)
    name_v2 = []
    for item in range(len(list_of_name)):
        if list_of_name[item] == list_of_name[i]:
            continue

        data = [x for x in  temp[list_of_name[i]] if x in  temp[list_of_name[item]]]
        if len(data) < 3:
            continue
        #print(list_of_name[i], list_of_name[item])
        name_list_v2.append(str(list_of_name[i])+str(list_of_name[item]))
        if str(list_of_name[i])  in res_dict.keys():
           name_v2.append(str(list_of_name[i])+str(list_of_name[item]))
           res_dict[list_of_name[i]] = name_v2
        else:
             name_v2.append(str(list_of_name[i])+str(list_of_name[item]))
             res_dict[list_of_name[i]] = name_v2
        data_res.append(data)




    list_of_name.pop(count)






print(name_list_v2, data_res)
res_check = {}

for i in range(len(name_list_v2)):
    print(name_list_v2[i])
    res_check[str(name_list_v2[i])] = data_res[i]
res_dict_v2 = {}
data_res = []
name_list_v3 = []
# res_dict {A: [],B:[]}
# res_dict_v2 {AB: ABD, Aas,BD: []}
data_res2 = []
for key, value in res_dict.items():
    res_dict_v2[value[0]] = []
    i = 0
    print(key, "-",value)
    while value:
        name_v2 = []
        for item in range(len(value)):
            if value[item] == value[i]:
                continue

            data = [x for x in  res_check[value[i]] if x in  res_check[value[item]]]
            s = str(value[i]) + str(value[item])
            p=""
            for char in s:
                if char not in p:
                    p=p+char

            if len(data) < minsups:
                continue
            print(p)
            print(data)
            name_list_v3.append(p)
            if str(value[i])  in res_dict_v2.keys():
                 name_v2.append(p)
                 res_dict_v2[value[i]] = name_v2
            else:
                name_v2.append(p)
                res_dict_v2[value[i]] = name_v2

            data_res2.append(data)


        value.pop(count)

print(name_list_v3)
print(res_dict_v2)
print(data_res2)


res_check = {}

for i in range(len(name_list_v3)):
    res_check[str(name_list_v3[i])] = data_res2[i]

print("res_check", res_check)
res_dict_v4 = {}
for key, value in res_dict_v2.items():
    #res_dict_v4[value[0]] = []
    if len(value) == 0:
        continue
    i = 0
    # print(key, "-",value)

    while value:

    #      name_v2 = []
        for item in range(len(value)):
            if value[item] == value[i]:
                continue
            print("version: ",value[item], value[i])

            data = [x for x in  res_check[value[i]] if x in  res_check[value[item]]]
            print(data)
              #print(res_check)
            s = str(value[i]) + str(value[item])
            p=""
            for char in s:
                if char not in p:
                    p=p+char

            print("results", p)

        value.pop(count)