text = "hello universe"
dic = {}
voules = "aieou"
for i in text:
    if i in voules:
        if i in dic:
            dic[i] +=1 
        else:
            dic[i] = 1

for k , v in dic.items():
    print(f"the vowel are {k} /t the reapted {v}")
            

       