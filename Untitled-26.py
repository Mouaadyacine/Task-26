n=int( input("entrer un nombre superieur de 0") )
if n==0 or n<0:
    print("erreur")
else:
    i=1
    s=i
for i in range(1,n):
    s=s*i
print(n,"!=",s)