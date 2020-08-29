import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

fil = open("PopTimes.csv", "w")

print('%0s, %12s , %13s'%('List-Size','pop(0)','pop()'))
print("------------------------------------------")
for i in range(1000000, 20000001, 1000000):
    x = [0]*i
    pt = popend.timeit(number=1000)
    x = [0]*i
    pz = popzero.timeit(number=1000)
    print("%d, %15.5f, %15.5f" %(i,pz,pt))
    
    fil.write("\n%d, %f.3, %f"%(i, pz, pt))

fil.close()

