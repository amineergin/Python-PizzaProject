import csv
import datetime
import pandas as pd
import mysql.connector

#Connect to mysql workbench
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pizzapydb"
)

# cursor = mydb.cursor()
# cursor.execute("Create database pizzapydb") #pizzapydb adında bir veritabanı oluşturduk

class Pizza():
  def __init__(self, description, cost):
    self.__description = description,
    self.__cost = cost
  #Encapsulation ile cost ve description tanımlanması.
  def get_description(self):
    return self.__description

  def set_description(self,description_):
    self.__description = description_

  def get_cost(self):
    return self.__cost
  def set_cost(self,cost_):
    self.__cost = cost_

class Classic(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)
class Margherita(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)
class TurkPizza(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)
class Dominos(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class Decorator(Pizza):
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost

    def get_cost(self):
        return self.__cost
    def set_cost(self,cost_):
        self.__cost = cost_

    def get_description(self):
        return self.__description
    def set_description(self,description_):
        self.__description = description_

# Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır
class Zeytin(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Mantar(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class KeciPeyniri(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Et(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Sogan(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Misir(Decorator):
    def __init__(self, description, cost):
        super().__init__(description, cost)

#Pizza Tabanları
pizCls = Classic("Klasik Pizza",100)
pizMar = Margherita("Margeritha Pizza", 135)
pizTurk = TurkPizza("Turk Pizza", 120)
pizDo = Dominos("Dominos Pizza", 150)

#Soslar
soszeytin = Zeytin("Siyah Zeytin",5)
sosKeciPeyniri = KeciPeyniri("Keçi Peyniri 50gr", 20)
sosMantar = Mantar("Kültür Mantarı", 7)
sosMisir = Misir("Süt Mısır 22gr", 12)
sosEt = Et("Dana Eti 15gr", 35)
sosSogan = Sogan("Karamelize Soğan", 15)

if __name__ == '__main__':
    df = pd.read_csv("C:/Users/Win10/Desktop/PythonProjects/PizzaProject/Menu.txt")
    print(df.head(12))

    casesPizza = {
        "1": pizCls,
        "2": pizMar,
        "3": pizTurk,
        "4": pizDo
    }

    casesSos = {
            "1": soszeytin,
            "2": sosMantar,
            "3": sosKeciPeyniri,
            "4": sosEt,
            "5": sosSogan,
            "6": sosMisir
    }

    for key, item in casesPizza.items():
        choice_pizza = input('Lütfen bir pizza tabanı seçiniz: ')
        chosen_pizza = casesPizza.get(choice_pizza)
        pizza_price = chosen_pizza.get_cost()
        break

    soru = int(input("Sos ister misiniz? 1(evet)/0(hayır)"))
    if soru == 1:
        for key, item in casesSos.items():
            choice_sos = input('Lütfen bir sos seçiniz: ')
            chosen_sos = casesSos.get(choice_sos)
            sos_price = chosen_sos.get_cost()
            break
    else:
        sos_price = 0

    total_price = pizza_price + sos_price
    print("Ödemeniz gereken miktar : ", total_price )
    odeme = int(input("Onaylıyor musunuz? 1(evet)/0(hayır)"))
    if odeme == 1:
        if mydb.is_connected():
            name = input("İsminizi Giriniz>> ")
            surname = input("Soyisminizi Giriniz>> ")
            tc_no = input("Tc Kimlik Numaranızı Giriniz>> ")
            kart_no = input("Kart Numaranızı Giriniz>> ")
            kart_sifre = input("Kart Şifrenizi Giriniz>> ")

            mycursor = mydb.cursor()

            sql = "INSERT INTO new_table (user_name, user_surname, tc_no, kk_no, kk_sifre) VALUES (%s, %s, %s, %s, %s)"
            val = (name, surname, tc_no, kart_no, kart_sifre)
            mycursor.execute(sql, val)
            mydb.commit()

        else:
            print("Veritabanı Bağlantısı Sağlayınız! ")

    else:
        pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
