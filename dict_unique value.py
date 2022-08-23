Dict=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
b=[]
while i<len(Dict):
    for j in Dict[i]:
        if Dict[i][j] not in b:
            b.append(Dict[i][j])
        i+=1
print(b)


        # 

rrc                        aaaaaa