q=input("What do you want to find volume/lsa/tsa of cuboid ?.\n").lower()
if q=='volume':
    l=int(input("Enter the value of length.,\n"))
    b=int(input("Enter the value of breadth.,\n"))
    h=int(input("Enter the valur of height.,\n"))

    print("volume of cuboid =",l,"x",b,"x",h)
    print("volume of cuboid =",l*b,"x",h)
    print("volume of cuboid =",l*b*h)
elif q=='lsa':
    a=int(input("Enter the value of length.,\n"))
    c=int(input("Enter the value of breadth.,\n"))
    d=int(input("Enter the valur of height.,\n"))

    print("lsa of cuboid =2h(l+b)")
    print("lsa of cuboid =2x",d,"x",(a,'+',c))
    print("lsa of cuboid =2x",d,"x",(a+c))
    print("lsa of cuboid =",2*d*(a+c),)

elif q=='tsa':
    w=int(input("Enter the value of length.,\n"))
    e=int(input("Enter the value of breadth.,\n"))
    r=int(input("Enter the valur of height.,\n"))

    print("tsa of cuboid = 2(lb+bh+hl)")
    print("tsa of cuboid =",2*(w*e+e*r+r*w))


