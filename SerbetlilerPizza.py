import csv
import datetime



class Pizza:
    def __init__(self, tanim, cost):
        self.tanim = tanim
        self.cost = cost

    def get_tanim(self):
        return self.tanim

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__('domates sosu, mozarella peyniri, sucuk, mantar, biber ve mısır.', 45.0)


class Margarita(Pizza):
    def __init__(self):
        super().__init__('domates sosu ve mozarella peyniri.', 70.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('domates sosu, mozarella peyniri, domates sosu, pastırma, zeytin, köz biber ve sucuk.', 75.0)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__('domates sosu, mozarella peyniri, sosis, zeytin ve mısır.', 40.0)


class Sos(Pizza):
    def __init__(self, pizza=None, sos=None):
        super().__init__(None, None)
        self.pizza = pizza
        self.sos = sos

    def get_tanim(self):
        return self.sos.get_tanim() + " soslu " + self.pizza.get_tanim()

    def get_cost(self):
        return self.sos.get_cost() + self.pizza.get_cost()


class ZeytinSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza, Pizza('zeytin', 5.0))

class MantarSos(Sos):
    def __init__(self,pizza):
        super().__init__(pizza, Pizza('mantar', 8.0))

class KeciPeyniri(Sos):
    def __init__(self,pizza):
        super().__init__(pizza, Pizza('keci peyniri', 10.0))     
        
class Et(Sos):
    def __init__(self,pizza):
        super().__init__(pizza, Pizza('et', 15.0))
    
class Sogan(Sos):
    def __init__(self,pizza):
        super().__init__(pizza, Pizza('sogan', 8.0))
        
class Misir(Sos):
    def __init__(self,pizza):
        super().__init__(pizza, Pizza('misir', 5.0))

def pizza_sec():
    while True:
        print("Pizzanizi seciniz.")
        print("1: Klasik\n2: Margarita\n3: Turk Pizza\n4: Sade Pizza\n")
        choice = int(input("Secim: "))
        if choice == 1:
            return KlasikPizza()
        elif choice == 2:
            return Margarita()
        elif choice == 3:
            return TurkPizza()
        elif choice == 4:
            return SadePizza()
        else:
            print("Hata!")


def siparis_yazdir(Siparis):
    with open("Orders.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(Siparis)
        
       


while True:
    print("Siparise devam etmek icin 1'i, bitirmek icin 0'i tuslayiniz.")
    choice = int(input("Secim:"))
    if choice == 0:
        break
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    pizza = pizza_sec()

    while True:
        print("Sosunuzu seciniz.")
        print("11: Zeytin Sosu\n12: Mantar Sosu\n13: Keci Peyniri Sosu\n14: Et Sosu\n15: Sogan Sosu\n16: Misir Sosu\n")
        choice = int(input("Secim: "))
        if choice == 11:
            pizza = ZeytinSos(pizza)
            break
        if choice == 12:
            pizza = MantarSos(pizza)
            break
        if choice == 13:
            pizza = KeciPeyniri(pizza)
            break
        if choice == 14:
            pizza = Et(pizza)
            break
        if choice == 15:
            pizza = Sogan(pizza)
            break
        if choice == 16:
            pizza = Misir(pizza)
            break
        else:
           print("Hata!")
           break
       
        


kullanici_adi = input("Kullanıcı adınızı giriniz: ")
kullanici_kimligi = input("Kullanici kimliginizi giriniz: ")
kredi_karti_bilgileri = input("Kredi karti bilgilerinizi giriniz:")
kredi_karti_şifresi= input("Kredi karti sifresini giriniz: ")


        

Siparis = [time, pizza.get_tanim(), pizza.get_cost(),kullanici_adi,kullanici_kimligi,kredi_karti_bilgileri,kredi_karti_şifresi]

siparis_yazdir(Siparis)

print("Serbetli Pizzayı tercih ettiginiz icin tesekkurler!\nTarih: {}\nPizza: {}\nUcret: {:.2f}\n".format(time, pizza.get_tanim(), pizza.get_cost()))



