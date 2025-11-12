şehirler = []
        


while True:
         şehir_al = input("Lütfen Şehir Giriniz, Çıkmak için 'q' Tuşuna Basın:\n ")
         if şehir_al == "q": 
             break
         şehirler.append(şehir_al)
şehirler.append("Kastamonu")  
şehirler_kopya = şehirler.copy()
uzun = 0
kısa = 0
for şehir in şehirler:
       if len(şehir) >6:
              uzun+= 1
       else:
          kısa+= 1
tp = uzun + kısa    
isim_al = input("Lütfen İsminizi Giriniz:\n")
print("-"*25)  
isim_al2 = isim_al.upper()
print("şehirler:",şehirler)
print("kopya:",şehirler_kopya)
print("isim1:",isim_al)
print("isimal2:",isim_al2)
print(f"uzun şehir sayısı:{uzun},kısa şehir sayısı:{kısa},toplam şehihir sayısı:{tp}")
print("-"*25)
input("Çıkmak için Enter’a basın...")
