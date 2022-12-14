array1=[[10,0],[3,5],[5,8]]
array2=[[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]

binen=0
inen=0

for i in array2:
    binen += i[0]
    inen += i[1]

    toplam = binen-inen
print("Otobüste Kalanların Sayısı : ",toplam)

binen2=0
inen2=0

for i in array1:
    binen2 += i[0]
    inen2 += i[1]

    toplam2=binen2-inen2
print("Otobüste Kalanların Sayısı : ",toplam2)