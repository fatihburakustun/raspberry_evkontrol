from EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time
import traceback
import sqlite3

con =sqlite3.connect("gomulu.db");

cursor = con.cursor();

def Kasakapaliguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=0 WHERE isim='Kasa'")
    cursor.execute("UPDATE Anahtarlar SET durum='Kapalı' WHERE isim='Kasa'")
    con.commit()
def Kasaacikguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=1 WHERE isim='Kasa'")
    cursor.execute("UPDATE Anahtarlar SET durum='Açık' WHERE isim='Kasa'")
    con.commit()



def Evkapaliguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=0 WHERE isim='Ev'")
    cursor.execute("UPDATE Anahtarlar SET Durum='Kapalı' WHERE isim='Ev'")
    con.commit()
def Evacikguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=1 WHERE isim='Ev'")
    cursor.execute("UPDATE Anahtarlar SET Durum='Açık' WHERE isim='Ev'")
    con.commit()


def Arabakapaliguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=0 WHERE isim='Araba'")
    cursor.execute("UPDATE Anahtarlar SET Durum='Kapalı' WHERE isim='Araba'")
    con.commit()
    
def Arabaacikguncelle():
    
    cursor.execute("SELECT * FROM Anahtarlar ")
    data=cursor.fetchall()
    cursor.execute("UPDATE Anahtarlar SET acikmi=1 WHERE isim='Araba'")
    cursor.execute("UPDATE Anahtarlar SET Durum='Açık' WHERE isim='Araba'")
    con.commit()




def Main():
  
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

        GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Kasa Açıldı
        GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Ev Kapısı Açıldı
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Araba Açık
        
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Araba Kapısı Kapandı
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Ev Kapısı Kapandı
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Kasa Kapandı
         
        GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)  # Kasa Açık 1, Kasa Kapalı 0
        GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)  # Ev Açık 1, Ev Kapalı 0
        GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH) # Araba Açık 1, Araba Kapalı 0
       
        
        
        
        GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)  # Nem kontrol
        
        GPIO.output(4,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        Kasakapaliguncelle()
        Evkapaliguncelle()
        Arabakapaliguncelle()
    
        while(True):
            
           
            if (GPIO.input(14) == True):
              GPIO.output(4,GPIO.HIGH)
              Kasaacikguncelle()
                                        

            if (GPIO.input(8) == True):
              GPIO.output(4,GPIO.LOW)
              Kasakapaliguncelle()
            
            
            
            
            if (GPIO.input(15) == True):
              GPIO.output(9,GPIO.HIGH)
              Evacikguncelle()
                                        

            if (GPIO.input(16) == True):
              GPIO.output(9,GPIO.LOW)
              Evkapaliguncelle()
              
              
            if (GPIO.input(18) == True):
              GPIO.output(17,GPIO.HIGH)
              Arabaacikguncelle()
                                        

            if (GPIO.input(25) == True):
              GPIO.output(17,GPIO.LOW)
              Arabakapaliguncelle()
              
      
      
             
              
        con.close()
    except Exception as ex:
        traceback.print_exc()
    finally:
        GPIO.cleanup()
Main()

