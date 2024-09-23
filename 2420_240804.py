# 2420
fam = input()
space = fam.index(" ")
fam1 = int(fam[:space])
fam2 = int(fam[space+1:])
if fam1 > fam2:
    print(fam1-fam2)
else:
    print(fam2-fam1)