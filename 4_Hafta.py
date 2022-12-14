# Dictionary Veri Tipi: Listelere benzerler ama her değere belli bir "key" atanır.
# İlk kısım key ikinci değer value.
"""gunler={'Pazartesi':'Monday','Salı':1,'Çarşamba':2,'Perşembe':3,'Cuma':4,'Cumartesi':5,'Pazar':6}
print(gunler['Pazartesi'])"""

"""dizi={'0':'Sıfır','1':'Bir','2':'İki','3':'Üç','4':'Dört','5':'Beş','6':'Altı','7':'Yedi','8':'Sekiz','9':'Dokuz'}
x=input("Lütfen Sayı Giriniz :")
for i in x:
    print(dizi[i])"""
#Functions

"""def Silindir_Hacim(pi_sayisi,r,h):
    Hacim= pi_sayisi*r*r*h
    return Hacim
pi=float(input("Pi Sayısı : "))
r=float(input("r Sayısı : "))
h=float(input("h Sayısı : "))
print(Silindir_Hacim(pi,r,h))"""

"""def Topla(sayi1,sayi2):
    Toplam = sayi1+sayi2
    return Toplam
sayi1=int(input("Sayı 1 : "))
sayi2=int(input("Sayı 2 : "))
print(Topla(sayi1,sayi2))

def Çarpma(sayi1,sayi2):
    Çarp = sayi1*sayi2
    return Çarp
sayi1=int(input("Sayı 1 : "))
sayi2=int(input("Sayı 2 : "))
print(Çarpma(sayi1,sayi2))"""

#Dosya Okuma
#open("file_name","mod_name")#Çalışma Şekli
#"w"=> yazma "r"=> okuma
"""dosyam= open("deneme.txt","w")
dosyam.write("Hello World\n")
dosyam.write("1111111111111111\t")
dosyam.write("python")
dosyam.close()"""
dosyam= open("deneme.txt","r")
x= dosyam.read()
print(x)
dosyam.close()




