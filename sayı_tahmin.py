import random

print('''
      Sayi Tahmin Oyununa Hoşgeldiniz
      Bu oyunda 5 caniniz var ve doğru sayiyi bulmaniz lazim
      Sayi 1 ile 100 arasinda
                Başarilar
      ''')


seçilen_sayi=random.randint(1,101)

change=5
while change>0:
    try:
        girdi=int(input('Bir sayi giriniz: '))
        
        
    except ValueError:
        print('Kardeşim Sayi Gircen sayi')
        continue
        
    
    if change>0:
        
        if girdi==seçilen_sayi:
            print('Tebrikler doğru sayi')
            break
            
        elif girdi < seçilen_sayi:
            print('Daha büyük bir sayi giriniz')
            
        
        else:
            print('Daha küçük bir sayi giriniz')
        
        change-=1
            
        print('Kalan hak',change)
            
    if change<1:
        print('Hakkiniz bitti oyunu kaybettiniz')
        print('Seçilen Sayı',seçilen_sayi)
        break
    