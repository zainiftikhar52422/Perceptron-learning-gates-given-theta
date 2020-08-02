def notGate():
    # Or gate Learning
    weight1=round(random.uniform(-0.5,0.5), 1)    # to round the out to 1 decimal point
    thetha=0
    alpha=0.1
    flage=True     # flage will be false when convergence reaches
    output=1
    notGate=((0,1),(1,0))
    while(flage==True):
        flage=False
        for examp in notGate:
            value=(examp[0]*weight1)
            if(value>=thetha):      #if perceptoron excited
                output=1    
            else:
                output=0
            if((output-examp[1])!=0):
                weight1=round(weight1+(alpha*(examp[1]-output)*examp[0]),1)   # to round the out to 1 decimal point
                flage=True
    print(weight1)

for i in range(5):
    notGate()