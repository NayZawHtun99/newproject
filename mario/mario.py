while True:
    j=input("choose from 1 to 8 how many rows?")
    print("Height= "+j)
    j=int(j)
    if 1 <= j <= 8:
        break
l="#"
p=" "
for e in range(j):
    print(p*(j-e-1)+l*(e+1)+p+l*(e+1))
    