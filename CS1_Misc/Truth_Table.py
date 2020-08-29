'''
[3ex1.py]
This program displays the truth tables of various logical expressions.
'''
#1.a) A and B

print("       a        b       a and b")
for a in [True, False]:
    for b in [True, False]:
        print("%10s%10s%10s" % (a, b, (a and b)))

#1.b) A or B

print("       a        b       a or b")
for a in [True, False]:
    for b in [True, False]:
        print("%10s%10s%10s" % (a, b, (a or b)))
        
#1.c) A and not B

print("       a        b       a and not b")
for a in [True, False]:
    for b in [True, False]:
        print("%10s%10s%10s" % (a, b, (a and not b)))

#1.d) not A or B

print("       a        b       not a or b")
for a in [True, False]:
    for b in [True, False]:
        print("%10s%10s%10s" % (a, b, (not (a or b))))

#1.e) not A and not B

print("       a        b       not a and not b")
for a in [True, False]:
    for b in [True, False]:
        print("%10s%10s%10s" % (a, b, (not a and not b)))

