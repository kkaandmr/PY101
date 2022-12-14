# Loops
"""tek_sayi = 1
 if(int(tek_sayi))%2==0:
while tek_sayi<=10:
    print(tek_sayi)
    tek_sayi=tek_sayi+2
print("Bitti")"""
"""x = 1
while x==1:
    print("Sonsuza Kadar Giderim")
    break"""
"""print("Hoşgeldiniz")
devam = "E"
sayac = 1
x=input("Girdi :")
if x=="E":
 while x == "E":
     print("%d.kez merhaba dunyali" %sayac)
else:
    print("\nTekrar dene ")"""
"""for i in range(1,5):
    print(i)"""
"""universite="Fennaver"
for harf in universite:
    print(harf)
for x in range(1,10):
    if x % 2 == 0:
        print(x)
print("Yukarıdaki Sayılar Çift Sayılardır")

for x in range(1,10):
    if x % 2 == 1:
        print(x)
print("Yukarıdaki Sayılar Tek Sayılardır")"""
"""for i in range(1,10,2):
    print(i)
for i in range(10,1,-2):
    print(i)"""
"""isim = input("Sadece isminizi giriniz:")
for karakter in isim:
    if karakter == " ":
        continue
    print(karakter)
for x in range(2,3):
    print(1.0/x)"""
"""liste1=[0,2,3,4,5]
liste2=["a","b","c","d"]
liste3=["fizik","kimya","biyoloji"]
print(liste2[2])
print(liste3[1])
print(liste1[1]+liste1[2])
#append() = listeye eleman ekleme
#del() = Listeden eleman silmek için
#liste3[-1] son elemanı belirtir
liste3.append("matematik")
del (liste3[1])
print(liste3)"""
liste3=["fizik","kimya","biyoloji","matematik","geometri","edebiyat"]
for ders in liste3:
    print(ders)

print(liste3[::-1])
print(liste3[2:4])
print(liste3[0][1])# 0'ıncı indeksteki elemana gidip 2.belirtilen harf yazdırır.


