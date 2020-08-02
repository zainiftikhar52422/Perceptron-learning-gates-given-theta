import random
def orGate():
    # Or gate Learning
    weight1=round(random.uniform(-0.5,0.5), 1)    # to round the out to 1 decimal point
    weight2=round(random.uniform(-0.5,0.5), 1)  # to round the out to 1 decimal point
    print("Weighted intialization",weight1,weight2)
    thetha=0.2
    alpha=0.1
    flage=True     # flage will be false when convergence reaches
    output=1
    orGate=((0,0,0),(0,1,1),(1,0,1),(1,1,1))
    while(flage==True):
        flage=False
        for examp in orGate:
            value=(examp[0]*weight1)+(examp[1]*weight2)
            if(value>=thetha):      #if perceptoron excited
                output=1    
            else:
                output=0
            if((output-examp[2])!=0):
                weight1=round(weight1+(alpha*(examp[2]-output)*examp[0]),1)   # to round the out to 1 decimal point
                weight2=round(weight2+(alpha*(examp[2]-output)*examp[1]),1)   # to round the out to 1 decimal point
                flage=True
    print(weight1,weight2)

for i in range(5):
    orGate()