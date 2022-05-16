import random 
import time
print("""
*********************
sayı tahmin etme oyunu


*********************

1 ile 40 arasındaki sayıyı tahmin etme 

""")
rastgele_sayı = random.randint(1,40)

while True:
    tahmin_hakkı=7
    tahmin = int(input("Tahmininiz: "))

    if(tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(2)

        print("Daha yüksek bir sayı söyleyiniz...")
        
    elif(tahmin > rastgele_sayı):
         print("Bilgiler Sorgulanıyor...")
         time.sleep(2)

         print("Daha düşük bir sayı söyleyiniz...")

         tahmin_hakkı -= 1
    else:
        print("Bililer Sorgulanıyor...")

        time.sleep(2)
        print("Tebrikler Sayınız", rastgele_sayı)
        break


    if(tahmin_hakkı ==0):
        print("Tahmin hakkınız Bitti...")
        print("Sayınız...", rastgele_sayı)



