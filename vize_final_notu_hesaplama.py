
a = float(input("Vize notunu girin: "))
b = float(input("Final notunu girin: "))


ortalama1 = a * 0.40 + b * 0.60
print(ortalama1)


if ortalama1 >= 60:
    
    x = input("Bütünlemeye girmek istiyorsanız 'E' yazın, istemiyorsanız 'H' yazın: ")
    
  
    if x == "H":
        print("Geçtiniz.")
    
    elif x == "E":
        y = float(input("Bütünleme notunu girin: "))
        ortalama2 = a * 0.40 + y * 0.60  
        print(f"Yeni ortalamanız: {ortalama2}")
        
        if ortalama2 >= 60:
            print("Geçtiniz.")
        else:
            print("Kaldınız.")
    else:
        print("Geçersiz giriş.")
        

else:
    print("Vize ve Final ile geçemediniz.")
    y = float(input("Bütünleme notunu girin: "))
    ortalama2 = a * 0.40 + y * 0.60  
    print(f"Bütünleme ile yeni ortalamanız: {ortalama2}")
    
    if ortalama2 >= 60:
        print("Geçtiniz.")
    else:
        print("Kaldınız.")


     