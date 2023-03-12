import sqlite3
from datetime import datetime


###########################################################################
##########----------------- Sınıf Tanımlamaları -----------------##########
###########################################################################

# Ana sınıf olan ve pizza türlerin ile decoratör sınıflarının kalıtıldığı sınıftır.
class Pizza():
    def __init__(self, aciklama, fiyat):
        self.aciklama = aciklama
        self.fiyat = fiyat
        
    def get_description(self):
        return self.aciklama

    def get_cost(self):
        return self.fiyat

###########################################################################
##########--------------- Pizza Türlerinin Tanımı ---------------##########
###########################################################################
"""
Aşağıda bulunan sınıflar Pizza sınıfından kalıtıldılar. Bu sınıflar, içerisinde pizza fiyatları ve açıklamalarını tutarlar. 
Kurucu metotları, Pizza sınıfının kurucu metodunun override edilmesi ile oluşturuldu.
"""

class Klasik(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Klasik içerisinde bulunan malzemeler:\nÖzel Sezar Sos\nMozzarella Peyniri\nSucuk Küp\nSosis\nJambon\nYeşil Biber\nSiyah Zeytin\nParmesan", 90)

class Margarita(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Margarita içerisinde bulunan malzemeler:\nÖzel Sezar Sos\nMozzarella Peyniri", 60)

class TurkPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Turk Pizza içerisinde bulunan malzemeler:\nÖzel Sezar Sos\nMozzarella Peyniri\nPastırma\nKüp Sucuk\nYeşil Biber\nDomates", 100)

class SadePizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Sade Pizza içerisinde bulunan malzemeler:\nÖzel Sezar Sos\nMozzarella Peyniri\nKüp Sucuk\nSosis\nSiyah Zeytin", 70)

###########################################################################
##########--------------- Decorator Sınıfı Tanımı ---------------##########
###########################################################################
"""
Bu sınıf, pizzalar ve soslar arasında bağlantı kurmak için Pizza sınıfından kalıtılmıştır. "super" metodu yardımı ile Pizza sınıfının kurucusu,
Decorator sınıfı için yeniden oluşturulmuştur. Bu yapı dışarıdan gelen pizza türüne göre pizzanın bulunduğu sınıftan açıklama ve fiyat değerlerini alır.
Daha sonra kendi içerisinde bulunan metotlar yardımı ile fiyat ve açıklama değerlerini döndürür. 
"""

class Decorator(Pizza):
    def __init__(self,nesne,aciklama,fiyat):
        super().__init__(aciklama,fiyat)
        self.nesne = nesne

    def get_cost(self):
        return "{} + {} = {}".format(self.nesne.get_cost(), Pizza.get_cost(self), self.nesne.get_cost() + Pizza.get_cost(self))
 
    def get_description(self):
        return "{}\n{}".format(self.nesne.get_description(), Pizza.get_description(self))
    
    """
    !!!! Ödevin isteklerine göre yukarıdaki get_cost ve get_description metotları çalışmaktadır. Bu metotların çalışıldığı yapı kodun 295-304 satırları arasında "Orjinal Yapı"
    etiketi ile belirtilmiştir. (Kodun okunulabilirliği için yapılar arasında geçiş yaparken, belirtilen satırlar arasında kullanılmayan yapıları yorum satırı içine alınız.)

    !!!! Ödeve özellik eklemek ve kodun kulanılabilirliğini arttırmak için aşağıda bulunan metotlar oluşturulmuştur. Bu metotlar kullanıcıdan alınan her bir pizza ve sos değeri için
    açıklama ve fiyat değerini bize verir. Yapının bu şekilde oluşturulmasının nedeni kullanıcıdan bir sos yerine istediği kadar sos seçme olanağı sağlamaktır. Bu metotlar ile çalışan 
    yapı 265-289 satırları arasında  "Özelleştirilmiş Yapı" etiketi ile belirtilmiştir. (Kodun okunulabilirliği için yapılar arasında geçiş yaparken, belirtilen satırlar arasında 
    kullanılmayan yapıları yorum satırı içine alınız.)
    """

    def get_cost_ekurun(self):
        return Pizza.get_cost(self)
    
    def get_cost_pizza(self):
        return self.nesne.get_cost()

    def get_description_pizza(self):
        return self.nesne.get_description()
    
    def get_description_ekurun(self):
        return Pizza.get_description(self)

###########################################################################
###########--------------- Sos Türlerinin Tanımı ---------------###########
###########################################################################
"""
Aşağıda bulunan sınıflar Decarator sınıfından kalıtıldılar. Bu sınıflar, içerisinde sos fiyatları ve açıklamalarını tutarlar. 
Kurucu metotları, Decorator sınıfının kurucu metodunu çağırırlar. Kullanıcının seçtiği pizza değeri önce sos yapıları içerisindeki
nesne değişkenine gelirler. Daha sonra kurucu metotları nedeni ile Decorator sınıfına giderler.
"""

class Zeytin(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self,nesne,"\nZeytin", 10)

class Mantar(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self,nesne,"\nMantar", 10)

class KeciPeyniri(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self, nesne,"\nKeçi Peyniri", 15)

class Et(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self, nesne,"\nEt", 20)

class Sogan(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self, nesne,"\nSoğan", 10)

class Misir(Decorator):
    def __init__(self,nesne):
        Decorator.__init__(self, nesne,"\nMısır", 10)

###########################################################################
##########-------------- Veri Kaydı Sınıfı Tanımı ---------------##########
###########################################################################

class VeriKaydi():
    def __init__(self):
        self.baglanti_olustur()
    
    # SQL veri tabanına bağlantı sağladığımız fonksiyon

    def baglanti_olustur(self):
        self.baglan = sqlite3.connect("pizza.db")
        self.imlec = self.baglan.cursor()

        # Bu sorgu yapısı ile bağlanılan veri tabanında böyle bir tablo varsa üzerine yazma işlemi yap yoksa oluştur demiş oluyoruz.
        sorgu = "CREATE TABLE IF NOT EXISTS pizza_order (kullanici_Adi TEXT, kullanici_kimligi TEXT, kredi_karti_bilgisi TEXT, siparis_aciklamasi TEXT, siparis_zamani TEXT,kredi_karti_sifresi TEXT)"

        self.imlec.execute(sorgu)

        self.baglan.commit()
    
    def baglanti_kes(self):
        self.baglan.close()

    def verileri_ekle(self,kullanici_adi,tc_kimlik, kart_bilgileri, siparis_aciklamasi, siparis_zamani, sifre):
        self.kullanici_adi = kullanici_adi
        self.tc_kimlik = tc_kimlik
        self.kart_bilgileri = kart_bilgileri
        self.siparis_aciklamasi = siparis_aciklamasi
        self.siparis_zamani = siparis_zamani
        self.sifre = sifre

        # Kullanıcıdan gelen değerleri ekrana yazdırmak için  bu sorgu yapısını kullanıyoruz. Bu yapı yukarıda oluşturduğumuz tablo yapısı içerisine değerleri kayıt edecek.
        sorgu = "INSERT INTO pizza_order VALUES (?,?,?,?,?,?)"

        self.imlec.execute(sorgu,(kullanici_adi,tc_kimlik, kart_bilgileri, siparis_aciklamasi, siparis_zamani, sifre))

        self.baglan.commit()

###########################################################################
##########----------------- Menu Sınıfı Tanımı ------------------##########
###########################################################################

class MenuAl():
    def __init__(self):
        self.verileri_al()
    
    # Bu fonksiyon ile Menu.txt dosyasını okuyup ekrana bastırmaktayız. Kurucu metot içerisine yazarak sınıf çağırıldığında kurucu metot tetiklenerek bu fonksiyon çalışır.

    def verileri_al(self):
        with open("Menu.txt", "r", encoding = "utf-8") as file:
            for i in file:
                i = i[:-1]
                print(i)
    
    def verileri_listele(self):
        liste = []
        with open("Menu.txt", "r", encoding = "utf-8") as file:
            for i in file:
                i = i[:-1]
                i = i.split(": ")
                liste.append(i)
        return liste
        
    
    def __str__(self):
        return str(self.verileri_al())

###########################################################################
##########----------------- Sorgu Sınıfı Tanımı -----------------##########
###########################################################################
"""
Bu sınıf ile tc kimlik numarası, kart numarası ve kart şifresi için bir sorgu yapısı oluşturulur. Bu sorguda kullanıcının girdiği değerlerin karakter sayısına karşılık
gelip gelmediği ve rakamlardan oluşup oluşmadığı sorgulanır.
"""

class Sorgu():

    def tc_sorgula(deger):
        deger = str(deger)

        if(len(deger) != 11):
            return False
        
        if(deger.isdigit() == 0):
            return False
        
        if (int(deger[0]) == 0):
            return False
        
        return True

    def kart_sorgula(deger):
        deger = str(deger)

        if(len(deger) != 16):
            return False
        
        if(deger.isdigit() == 0):
            return False
        
        return True
    
    def sifre_sorgula(deger):
        deger = str(deger)

        if(len(deger) != 4):
            return False

        if(deger.isdigit() == 0):
            return False
        
        return True



def main():
    MenuAl()
    veri_kaydi = VeriKaydi()
    
    # Kullanıcının girdiği değere göre pizza yapısını elde edebilmek için, pizza sınıflarını döndüren sözlük yapısı oluşturduk.
    pizza_dickt = {1: Klasik(),
                    2: Margarita(),
                    3: TurkPizza(),
                    4: SadePizza()
                    }

    # Kullanıcının girdiği değerin, oluşturduğumuz sözlük içerisinde olup olmadığını sorgularız. 
    siparis_aciklamasi = input("Seçmek istediğiniz pizzaya karşılık gelen değeri giriniz: ")
    
    while siparis_aciklamasi not in ["1","2","3","4"]:
        siparis_aciklamasi = input("Hatalı değer girdiniz! Tekrar deneyiniz: ")
    
    # Eğer kullanıcının girdiği değer sözlükte varsa girilen değerin sözlükteki karşılığı pizza siparişi değişkenine kayıt edilir.
    pizza_siparisi = pizza_dickt[int(siparis_aciklamasi)]

    # Kullanıcının girdiği değere göre sos yapısını elde edebilmek için, Decorator sınıfını kullanan sos yapıları için sözlük oluşturduk. Bu yapı içine nesne değişkeni beklediği için yukarıda pizza değerlerini bize veren yapıyı bu değişken içerisine gönderdik.
    sos_dickt = {5: Zeytin(pizza_siparisi),
                 6: Mantar(pizza_siparisi),
                 7: KeciPeyniri(pizza_siparisi),
                 8: Et(pizza_siparisi),
                 9: Sogan(pizza_siparisi),
                 10: Misir(pizza_siparisi)
                 }

    ###########################################################################
    ##########---------------- Özelleştirilmiş Yapı -----------------##########
    ###########################################################################
    # Kullanıcıdan gelen sos değerlerini alıp bir liste içine atıyoruz. Eğer girilen değer sözlük içinde yoksa sos değeri tekrardan istenir.
    sos_listesi = []
    while True:
        sos_secimi = input("Seçmek istediğiniz sosa karşılık gelen değeri giriniz (Seçimden çıkmak için 'q' tuşunu kullanınız!): ")
        if(sos_secimi == "q"):
            break
        else:
            while sos_secimi not in ["5","6","7","8","9","10"]:
                sos_secimi = input("Hatalı değer girdiniz. Tekrardan deneyin: ")
            sos_listesi.append(sos_dickt[int(sos_secimi)])
    

    # Eklenen sosları listeye atama ve işlemleri yapma
    # Yukarıda kullanıcıdan alınan değerlerin bulunduğu sos listesi gezilerek her seferinde Decorator sınıfından, pizza ve girilen soslara karşılık gelen ücret ve açıklama değerleri alınır. 
    fiyat = pizza_siparisi.get_cost()
    aciklama = pizza_siparisi.get_description()
    for i in sos_listesi:
        fiyat += i.get_cost_ekurun()
        aciklama += i.get_description_ekurun()
    ###########################################################################
    ##########---------------- Özelleştirilmiş Yapı -----------------##########
    ###########################################################################    
    
    print("Ürün Fiyatı: ", fiyat)
    print(aciklama)


    ###########################################################################
    ##########-------------------- Orjinal Yapı ---------------------##########
    ###########################################################################
    # while sos_secimi not in ["5","6","7","8","9","10"]:
    #     sos_secimi = input("Hatalı değer girdiniz! Tekrar deneyiniz: ")
    
    # siparis = sos_dickt[int(sos_secimi)]
    ###########################################################################
    ##########-------------------- Orjinal Yapı ---------------------##########
    ###########################################################################



    ###########################################################################
    ##########----------------- Kullanıcı Bilgileri -----------------##########
    ###########################################################################
    """
    Aşağıda bulunan kod diziminde kullanıcıdan bilgileri alınır. Sorgu sınıfı kullanılarak girilen bu değerlerde hata olup olmadığı sorgulanır.
    """

    kullanici_adi = input("Kullanıcı Adı Giriniz: ")

    tc_kimlik = input("T.C. Giriniz: ")
    while True:
        if(Sorgu.tc_sorgula(tc_kimlik) != True):
            tc_kimlik = input("Eksik veya hatalı T.C kimlik numarası girdiniz. Lütfen 11 haneli T.C kimlik numaranızı giriniz: ")
        else:
            break

    kart_bilgileri = input("Kart Bilgilerini Giriniz: ")
    while True:
        if(Sorgu.kart_sorgula(kart_bilgileri) != True):
            kart_bilgileri = input("Eksik veya hatalı kart numarası girdiniz. Lütfen 16 haneli kart numaranızı giriniz: ")
        else:
            break

    siparis_zamani = datetime.now().strftime("%X")

    sifre = input("4 haneli şifrenizi giriniz: ")
    while True:
        if(Sorgu.sifre_sorgula(sifre) != True):
            sifre = input("Eksik veya hatalı şifre girdiniz. Lütfen 4 haneli şifrenizi giriniz: ")
        else:
            break

    ###########################################################################
    ##########----------------- Veri Tabanına Kayıt -----------------##########
    ###########################################################################
    """
    Yukarıda kullanıcıdan alınan değerler ekrana bastırılır ve VeriKaydi sınıfı kullanılarak alınan bu değerler veri tabanına kayıt edilir.
    """
    
    print("\n{},\nFiyat: {}".format(aciklama, fiyat))
    veri_kaydi.verileri_ekle(kullanici_adi,tc_kimlik,kart_bilgileri,aciklama,siparis_zamani,sifre)


main()
