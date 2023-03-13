#Gerekli kütüphaneleri içe aktarıyoruz.
import tkinter as tk 
from tkinter import messagebox
from datetime import datetime
import csv

# Pizza ust Sınıfı oluşturuyoruz.
class Pizza:  
    def __init__(self,cost,description):
        self.__cost = cost 
        self.__description = description
        
        
#Kapsülleme işlemi fonksiyonu
    def get_cost(self): 
        return self.__cost
    
    def get_description(self):
        return self.__description
    
    
#Pizza  sınıfları oluşturuyoruz.Pizzaların fiyatlarını ve özelliklerini tanımlıyoruz.
class Klasik(Pizza):
    def __init__(self):
        cost = 80 
        description = "Klasik Pizza"
        Pizza.__init__(self,cost,description)
        
       
    
class Margarita(Pizza):
    def __init__(self):
        cost = 95 
        description = "Margarita Pizza"
        Pizza.__init__(self,cost,description)
        
class TurkPizza(Pizza):
    def __init__(self):
        cost = 100
        description = "Turk Pizza"
        Pizza.__init__(self,cost,description)

class Sade(Pizza):
    def __init__(self):
        cost = 60 
        description = "Sade Pizza"
        Pizza.__init__(self,cost,description)
        
class Bos(Pizza):
    def __init__(self):
        cost = 0 
        description = ""
        Pizza.__init__(self, cost, description)
        
#Decorator üst sınıfını tanımlıyoruz. Kapsüllüyoruz.
class Decorator(Pizza):
    def __init__(self,component,cost,description):
        self.component = component
        self.__cost = cost 
        self.__description = description
        Pizza.__init__(self,cost,description)
        
#Pizza ve ek malzemelerin fiyatını toplama işlemi.
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
   
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)#pizza ve ek malzemelerin özelliklerinin yazilmasi
   

#Ek Malzemelerin sınıflarının tanımlanması.Ve pizzalarda olduğu gibi fiyat tanımlama.Decorator sınıfıyla bağlama.  
class Zeytin(Decorator):
    def __init__(self,component):
        cost = 5
        description = "Zeytinli"
        Decorator.__init__(self, component, cost, description)
        
class Mantar(Decorator):
    def __init__(self,component):
        cost = 12
        description = "Mantarli"
        Decorator.__init__(self, component, cost, description)

class KeciPeynir(Decorator):
    def __init__(self,component):
        cost = 19
        description = "Keci Peynirli"
        Decorator.__init__(self, component, cost, description)
        
class Et(Decorator):
    def __init__(self,component):
        cost = 20
        description = "Etli"
        Decorator.__init__(self, component, cost, description)

class Sogan(Decorator):
    def __init__(self,component):
        cost = 5
        description = "Soganli"
        Decorator.__init__(self, component, cost, description)

class Misir(Decorator):
    def __init__(self,component):
        cost = 7
        description = "Misirli "
        Decorator.__init__(self, component, cost, description)
   
#Tkinter Uygulama Aşamaları,tema renkleri vs atamaları.
class PizzaApp():
    def __init__(self):
        bgAll ='#eed2c4' 
        fgAll="#3d4448"
        
        self.root = tk.Tk() 
        self.root.geometry("700x450+80+100") 
        self.root.title("Pizza Sipariş Sistemi") 
        self.root.configure(bg=bgAll) 
        
        menuLabel = tk.Label(self.root,text=" Pizza Sipariş Sistemi ", bg ="#eed2c4", fg="black",font="Arial 24 bold")
        menuLabel.pack(pady=10) 
        
        pizzaTabanLabel = tk.Label(self.root,text="Lütfen Bir Pizza Seçiniz :",font="Arial 11 italic bold",bg = bgAll,fg=fgAll)
        pizzaTabanLabel.pack(pady= 5,anchor="w",padx=5) 

        self.tabanDegiskeni = tk.StringVar() 
        self.tabanDegiskeni.set(None) 
        
#for dongüsü için liste tanımlıyoruz.
        pizzaDegiskenleri = [("Klasik Pizza  (" + str(Klasik().get_cost()) +" ₺)","klasik"),
                             ("Margarita Pizza  (" + str(Margarita().get_cost()) + " ₺)","margarita"),
                             ("Türk Pizza  (" + str(TurkPizza().get_cost()) + " ₺)","turkpizza"),
                             ("Sade Pizza  (" + str(Sade().get_cost()) + " ₺)","sade")]

#Butonları ekrana yerleştiriyoruz.
        for text, value in pizzaDegiskenleri: 
            pizzaRadioButon = tk.Radiobutton(self.root, text= text, variable = self.tabanDegiskeni, value=value,bg = bgAll,font="Arial 10 italic")
            pizzaRadioButon.pack(anchor="w",padx=10)

        sosLabel = tk.Label(self.root,text="Lütfen İstediğiniz Ek Malzemeleri Seçin :",font="Arial 11 italic bold",bg =bgAll, fg=fgAll)
        sosLabel.pack(pady=5,anchor="w",padx=5)

#Ek malzemeler için boş liste oluşturuyoruz.
        self.sosDegerListesi = []
        
        sosDegiskenleri = [("Zeytin (+" + str(Zeytin(Bos()).get_cost()) + " ₺)","zeytin"),  
                           ("Mantar (+" + str(Mantar(Bos()).get_cost()) + " ₺)","mantar"),        
                           ("Keçi Peyniri (+" + str(KeciPeynir(Bos()).get_cost()) + " ₺)","peynir"),       
                           ("Et (+" + str(Et(Bos()).get_cost()) + " ₺)"  ,"et"),            
                           ("Soğan (+" + str(Sogan(Bos()).get_cost()) + " ₺)","sogan"),      
                           ("Mısır (+" + str(Misir(Bos()).get_cost()) + " ₺)","misir")]

#Frame oluşturup checkboxları düzenliyoruz.
        frame = tk.Frame(self.root,bg= bgAll)
        frame.pack(anchor="w")

    
        for i, (text, value) in enumerate(sosDegiskenleri): 
            self.sosDegiskeni = tk.BooleanVar() 
            sosCheckButon = tk.Checkbutton(frame, text=text, variable= self.sosDegiskeni, font="Arial 10 italic", bg=bgAll, anchor="w")
            sosCheckButon.grid(row=i//2, column=i%2, padx=10, pady=2, sticky="w") 
            self.sosDegerListesi.append((self.sosDegiskeni, value))

#Ücreti yazdırıyoruz.
        self.ucretLabel =tk.Label(self.root,text=" Toplam Ücret  = ",font=("Arial 12 italic bold"),bg= bgAll,fg= fgAll)
        self.ucretLabel.pack(pady=8,padx=8,anchor="w") 

        
        frame = tk.Frame(self.root,bg=bgAll)
        frame.pack(side="top", fill="x")
        
#Çıkış,ücret ve sipariş verme butonlarını oluşturuyoruz.  
        cıkısButon = tk.Button(frame,text="İptal Et",font="Arial 12 italic",bg="#362E41",fg = "white",command= self.root.destroy)
        cıkısButon.pack(side="left", padx=10, pady=1) 


        self.siparisButon = tk.Button(frame,text="Bilgi Girişi ve Ödeme Adımına Geç ",font="Arial 13 italic",bg="#362E41",command=self.odemeSayfasi ,fg = "white",state="disabled")
        self.siparisButon.pack(side="right", padx=25, pady=1) 


        hesapButon = tk.Button(frame, text="Tercihlerimi Onaylıyorum.\nÜcretimi Hesapla",font="Arial 10 italic",bg="#362E41",fg = "white",command=self.ucretHesapla)      
        hesapButon.pack(side="right", padx=10, pady=18) 
        
        self.root.mainloop()  
    
    def ucretHesapla(self): 
        tabanDegiskeni = self.tabanDegiskeni.get() 
        
        if tabanDegiskeni == "klasik":
            self.pizzam = Klasik()
            
        elif tabanDegiskeni == "margarita":
            self.pizzam = Margarita()
            
        elif tabanDegiskeni == "turkpizza":
            self.pizzam = TurkPizza()
            
        elif tabanDegiskeni == "sade":
            self.pizzam = Sade()
            
        for self.sosDegiskeni, value in self.sosDegerListesi:
             if self.sosDegiskeni.get():

#Herhangi bir seçim olmaması halinde kodun devam etmesini sağlıyoruz.
                 try:
                     if value == "zeytin":
                         self.pizzam = Zeytin(self.pizzam)
                         
                     elif value == "mantar":
                         self.pizzam = Mantar(self.pizzam)
                         
                     elif value == "peynir":
                         self.pizzam = KeciPeynir(self.pizzam)
                         
                     elif value == "et":
                         self.pizzam = Et(self.pizzam)
                         
                     elif value == "sogan":
                         self.pizzam = Sogan(self.pizzam)
                         
                     elif value == "misir":
                         self.pizzam = Misir(self.pizzam)
                 except:
                     pass
        try: 
#Ekrana ücreti yazdırıyoruz.
            self.ucretLabel.config(text=(" Toplam Ücret  = "+ str(self.pizzam.get_cost()) + " ₺") )
            self.siparisButon.configure(state="normal") 

        except:
            pass

#Ödeme sayfası oluşturuyoruz ve renklerini ayarlıyoruz.
    def odemeSayfasi(self):
        self.siparisButon.configure(state="disabled")
        
        
        bg = "#eed2c4" 
        fg = "black"
        self.pencere = tk.Tk()
        self.pencere.title("Ödeme Ekranı") 
        self.pencere.geometry("400x500+782+150") 
        self.pencere.configure(bg="#eed2c4") 

        menuLabel = tk.Label(self.pencere ,text=" Ödeme Ekranı ", bg = "#eed2c4", fg="black",font="Arial 15 italic bold")
        menuLabel.grid(pady=15, row =0,column=0,columnspan=2) 
       
#Entryler oluşturuyoruz.
        isimLabel = tk.Label(self.pencere,text="Ad Soyad :",font="Arial 11 bold",bg = bg,fg = fg)
        isimLabel.grid(pady= 10,row=1, column=0,padx=10)
       
        self.entry = tk.Entry(self.pencere,width=30)
        self.entry.grid(pady= 10,row=1, column=1,padx=10)
        
        TCLabel = tk.Label(self.pencere,text="TC. Kimlik Numarası :",font="Arial 11 bold",bg = bg,fg = fg)
        TCLabel.grid(pady= 10,row=2, column=0,padx=10)
       
        self.entry2 = tk.Entry(self.pencere,width=30)
        self.entry2.grid(pady= 10,row=2, column=1,padx=10)
       
        telefonLabel = tk.Label(self.pencere,text="Telefon Numarası :",font="Arial 11 bold",bg = bg,fg = fg)
        telefonLabel.grid(pady= 10,row=3, column=0,padx=10)
       
        self.entry3 = tk.Entry(self.pencere,width=30)
        self.entry3.grid(pady= 10,row=3, column=1,padx=10)
       
        adresLabel = tk.Label(self.pencere,text="Adres :",font="Arial 11 bold", bg = bg, fg = fg)
        adresLabel.grid(pady= 10,row=4, column=0,padx=10)
       
        self.entry4 = tk.Entry(self.pencere,width=30)
        self.entry4.grid(pady= 10,row=4, column=1,padx=10)
       
        kartNoLabel = tk.Label(self.pencere,text="Kredi Kartı Numarası :",font="Arial 11 bold",bg = bg,fg = fg)
        kartNoLabel.grid(pady= 10,row=5, column=0,padx=10)
       
        self.entry5 = tk.Entry(self.pencere,width=30)
        self.entry5.grid(pady= 10,row=5, column=1,padx=10)
        
        kartNosifreLabel = tk.Label(self.pencere,text="Kredi Kartı Şifresi :",font="Arial 11 bold",bg = bg,fg = fg)
        kartNosifreLabel.grid(pady= 10,row=6, column=0,padx=10)
       
        self.entry6 = tk.Entry(self.pencere,width=30)
        self.entry6.grid(pady= 10,row=6, column=1,padx=10)
        
        
        bilgiLabel = tk.Label(self.pencere,text="Sipariş İçeriği  = ",font="Arial 10 italic bold underline",fg = fg ,bg = bg)
        bilgiLabel.grid(row=7,column=0,sticky= tk.E,padx=10)
        
        bilgiLabel1 = tk.Label(self.pencere,text= self.pizzam.get_description() ,font="Arial 10 italic bold",fg = fg ,bg = bg)
        bilgiLabel1.grid(row=7,column=1,sticky=tk.W)
        
        bilgiUcretLabel = tk.Label(self.pencere,text= "Toplam Ücret  =  ",font="Arial 10 italic bold underline",fg = fg ,bg = bg)
        bilgiUcretLabel.grid(row=8,column=0,sticky= tk.E,padx=8)
        
        bilgiUcretLabel1 = tk.Label(self.pencere,text= str(self.pizzam.get_cost())+ " TL",font="Arial 10 italic bold ",fg = fg ,bg = bg)
        bilgiUcretLabel1.grid(row=8,column=1,sticky=tk.W)
            
        siparisOlusturmaButon = tk.Button(self.pencere, text="SİPARİŞİ ONAYLA", state=tk.NORMAL,command=self.bilgiKaydet,font="Arial 12 bold",bg = "#277da1",fg=fg)
        siparisOlusturmaButon.grid(padx=10,row=10, column=1)
        
        self.pencere.mainloop()
 
 #Kullancı tarafından girilen tüm bilgilerin bir databasee kaydolmasını sağlıyoruz.       
    def bilgiKaydet(self): 
        adSoyad = self.entry.get() 
        TCno = self.entry2.get()
        telNo = self.entry3.get()
        adres = self.entry4.get()
        kartNo = self.entry5.get()
        kartNosifre = self.entry6.get()

        suan = datetime.now() 
        tarih = datetime.strftime(suan, "%d-%m-%Y %B %A %H:%M:%S")

        with open('Orders_Database.csv', mode='a', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow([tarih,adSoyad,TCno,telNo,adres,kartNo,kartNosifre,self.pizzam.get_description(),self.pizzam.get_cost()])


        messagebox.showinfo(title="Sipariş Onay Ekranı",message= "SİPARİŞİNİZ ONAYLANDI .\nKartınızdan yalnız ' " + str(self.pizzam.get_cost()) 
                            + " 'TL çekilmiştir."+ "\nSiparişiniz yola çıktığında bilgilendirileceksiniz. \nBizi tercih ettiğiniz için teşekkür ederiz.")

        self.pencere.destroy()

#Main fonksiyonunu çağıryoruz.
def main():
    PizzaApp() 

if __name__ == "__main__":
    main() 