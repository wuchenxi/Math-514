s=""
for i in range(11):
    d=str(i*0.5)[:3]
    ts="1/(1+2*("+d+"-2)*("+d+"-2))"
    for j in range(11):
        if j!=i:
            e=str(j*0.5)[:3]
            ts+="*(\\x-"+e+")/("+d+"-"+e+")"
    if i==0:
        s+=ts
    else:
        s+="+"+ts
print(s)
