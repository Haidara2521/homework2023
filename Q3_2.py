import json
from pprint import pprint
print ("x=4","y=5","z=6")
s=0
haidara = {}
L1 = []
name_ = input("enter name :")
with open("haidara.json","r") as f:
    q=json.loads(f.read())
    for i in q :
        print(i)
        ans = input("enter the answer a/b :")
        L1.append(ans)
        if ans ==q[i]:
            print("correct answer,you got 1 point")
            s=s+1
        else:
            print("wrong answer,you lost 1 point")
            s=s-1

    haidara ={name1:L1}
    print(ali)

    print("final score is :",s)
haidara1=json.dumps(haidara)
with open("ali.json","w")as f:
    f.write(haidara1)
