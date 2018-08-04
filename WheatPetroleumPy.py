import random

file = open("C:\\Users\\Hasan\\Desktop\\WheatPetroleum.txt")
content = file.readlines()
count1 = 0
count2 = len(content)
dic = {"0-1": 0, "1-1.5": 0, "1.5-2.0": 0, "2-3": 0, "3-5": 0, "5+": 0}
dic2 = {"0-2": 0, "2-5": 0, "5-10": 0, "10-15": 0, "15-25": 0, "25+": 0}
PetrolPrices = [0]

del (PetrolPrices[0])
PetrolCurrentPrice = float(content[len(content) - 1].split("  ")[0])
WheatCurrentPrice = float(content[len(content) - 1].split("  ")[1])
neg = 0
pos = 0

counter=0
prev=""
i_i=0
i_n=0
n_i=0
n_n=0
for line in content:
    PetrolPC = float(line.split("  ")[2])
    WheatPC = float(line.split("  ")[3])
    PetrolPrices.append(float(line.split("  ")[0]))
    curr="ni"


    if PetrolPC * WheatPC > 0:
        curr="i"



        count1 += 1
        temp = WheatPC / PetrolPC
        if temp > 5:
            dic["5+"] += 1
        elif temp > 3:
            dic["3-5"] += 1
        elif temp > 2:
            dic["2-3"] += 1
        elif temp > 1.5:
            dic["1.5-2.0"] += 1
        elif temp > 1:
            dic["1-1.5"] += 1
        elif temp > 0:
            dic["0-1"] += 1

        if abs(PetrolPC) > 25:
            dic2["25+"] += 1
        elif abs(PetrolPC) > 15:
            dic2["15-25"] += 1
        elif abs(PetrolPC) > 10:
            dic2["10-15"] += 1
        elif abs(PetrolPC) > 5:
            dic2["5-10"] += 1
        elif abs(PetrolPC) > 2:
            dic2["2-5"] += 1
        elif abs(PetrolPC) > 0:
            dic2["0-2"] += 1
        if PetrolPC > 0:
            pos += 1
        else:
            neg += 1

    if counter!=0:
        if prev=="i":
            if curr==prev:
                i_i+=1
            elif curr!=prev:
                i_n+=1
        elif prev == "ni":
            if curr == prev:
                n_n += 1
            elif curr != prev:
                n_i += 1
    prev = curr
    counter=1
#print(dic2)
c=i_i
i_i=i_i/(i_i+i_n)
i_n=i_n/(i_n+c)
c=n_n
n_n=n_n/(n_n+n_i)
n_i=n_i/(c+n_i)


print(i_i)
print(i_n)
print(n_n)
print(n_i)
ChangeProbability = count1 / count2
NoChangeProbability = 1 - ChangeProbability

print("Enter number of upcoming months you want to predict price")
n=int(input())

sum = 0.0
for i in dic.keys():
    sum = sum + dic[i]

for i in dic.keys():
    dic[i] /= sum
# print(dic)

sum = 0
print(dic)
for i in dic2.keys():
    sum = sum + dic2[i]
curr=""
prev=""
for i in dic2.keys():
    dic2[i] /= sum
temp = random.randint(0, 100000000) / 100000000
ans = "No Impact"
if temp <= ChangeProbability:
    ans = ""
    temp2 = random.randint(0, 100000000) / 100000000
    temp4 = random.randint(0, 100000000) / 100000000

    arr2 = [0]
    arr3 = {0.0: ""}
    del (arr2[0])

    for i in dic.values():
        arr2.append(i)
    arr2.sort()

        # print(arr2)
    for i in dic.keys():
        arr3[dic[i]] = i

    temp3 = 0
    key = ""
    for i in range(0, len(arr2)):
        temp3 += arr2[i]
        if temp2 < temp3:
            key = arr3[arr2[i]]
            break
    arr2.clear()
    arr3.clear()
    for i in dic2.values():
        arr2.append(i)
    arr2.sort()

        # print(arr2)
    for i in dic2.keys():
        arr3[dic2[i]] = i

    temp3 = 0
    key2 = ""
    for i in range(0, len(arr2)):
        temp3 += arr2[i]
        if temp2 < temp3:
            key2 = arr3[arr2[i]]
            break

    if key == "0-1":
        impactrate = random.randint(000, 100000) / 100000
    elif key == "1-1.5":
        impactrate = random.randint(100000, 150000) / 100000
    elif key == "1.5-2.0":
        impactrate = random.randint(150000, 200000) / 100000
    elif key == "2-3":
        impactrate = random.randint(200000, 300000) / 100000
    elif key == "3-5":
        impactrate = random.randint(300000, 500000) / 100000
    elif key == "5+":
        impactrate = random.randint(5000000, 10000000) / 100000
        # print(impactrate)

    if key2 == "0-2":
        changerate = random.randint(000, 200000) / 100000
    elif key2 == "2-5":
        changerate = random.randint(200000, 500000) / 100000
    elif key2 == "5-10":
        changerate = random.randint(500000, 1000000) / 100000
    elif key2 == "10-15":
        changerate = random.randint(1000000, 1500000) / 100000
    elif key2 == "15-25":
        changerate = random.randint(1500000, 2500000) / 100000
    elif key2 == "25+":
        changerate = random.randint(25000000, 10000000) / 100000
        # print(changerate)

    temp2 = random.randint(0, 100000000) / 100000000

    if temp2 <= pos / (pos + neg):
        changerate = changerate * -1

    PetrolCurrentPrice = PetrolCurrentPrice + PetrolCurrentPrice * (changerate / 100)
    print("Petrol price after  month  1 =", PetrolCurrentPrice)
    wheatchangerate = impactrate * changerate
    WheatCurrentPrice = WheatCurrentPrice + WheatCurrentPrice * (wheatchangerate / 100)
    print("Wheat price after month 1 =", WheatCurrentPrice)
    curr="i"
    prev="i"

if ans == "No Impact":
    stat=1
    prev="ni"
    print("No change in month 1")


for x in range(1,n):

    temp = random.randint(0, 100000000) / 100000000
    ans = "No Impact"

    if prev=="ni":
        if temp > n_i:
            print("No change in month ",x+1)
            continue
    elif prev=="i":
        if temp>i_i:
            print("No change in month ", x+1)
            continue
    prev="i"
    ans = ""
    temp2 = random.randint(0, 100000000) / 100000000
    temp4 = random.randint(0, 100000000) / 100000000

    arr2 = [0]
    arr3 = {0.0: ""}
    del (arr2[0])

    for i in dic.values():
        arr2.append(i)
    arr2.sort()

    # print(arr2)
    for i in dic.keys():
        arr3[dic[i]] = i

    temp3 = 0
    key = ""
    for i in range(0, len(arr2)):
        temp3 += arr2[i]
        if temp2 < temp3:
            key = arr3[arr2[i]]
            break
    arr2.clear()
    arr3.clear()
    for i in dic2.values():
        arr2.append(i)
    arr2.sort()

    # print(arr2)
    for i in dic2.keys():
        arr3[dic2[i]] = i

    temp3 = 0
    key2 = ""
    for i in range(0, len(arr2)):
        temp3 += arr2[i]
        if temp2 < temp3:
            key2 = arr3[arr2[i]]
            break

    if key == "0-1":
        impactrate = random.randint(000, 100000) / 100000
    elif key == "1-1.5":
        impactrate = random.randint(100000, 150000) / 100000
    elif key == "1.5-2.0":
        impactrate = random.randint(150000, 200000) / 100000
    elif key == "2-3":
        impactrate = random.randint(200000, 300000) / 100000
    elif key == "3-5":
        impactrate = random.randint(300000, 500000) / 100000
    elif key == "5+":
        impactrate = random.randint(5000000, 10000000) / 100000
    # print(impactrate)

    if key2 == "0-2":
        changerate = random.randint(000, 200000) / 100000
    elif key2 == "2-5":
        changerate = random.randint(200000, 500000) / 100000
    elif key2 == "5-10":
        changerate = random.randint(500000, 1000000) / 100000
    elif key2 == "10-15":
        changerate = random.randint(1000000, 1500000) / 100000
    elif key2 == "15-25":
        changerate = random.randint(1500000, 2500000) / 100000
    elif key2 == "25+":
        changerate = random.randint(2500000, 10000000) / 100000
    # print(changerate)

    temp2 = random.randint(0, 100000000) / 100000000

    if temp2 <= pos / (pos + neg):
        changerate = changerate * -1

    PetrolCurrentPrice = PetrolCurrentPrice + PetrolCurrentPrice * (changerate / 100)
    print("Petrol price after " + str(x + 1) + " month =", PetrolCurrentPrice)
    wheatchangerate = impactrate * changerate
    WheatCurrentPrice = WheatCurrentPrice + WheatCurrentPrice * (wheatchangerate / 100)
    print("Wheat price after " + str(x + 1) + " month =", WheatCurrentPrice)

    if ans == "No Impact":
         print("No change in month 1")


