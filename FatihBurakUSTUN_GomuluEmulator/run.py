from flask import Flask, render_template, request
import sqlite3 as sql
import time
import traceback
import sqlite3

app = Flask(__name__)

@app.route('/my-link/')
def my_link():
   con =sqlite3.connect("gomulu.db");
   cur = con.cursor()
   cur.execute("UPDATE Anahtarlar SET Durum='Kapalı' WHERE isim='Kasa'")
   cur.execute("UPDATE Anahtarlar SET deger='0' WHERE isim='Kasa'")
   cur.execute("UPDATE Anahtarlar SET Durum='Kapalı' WHERE isim='Ev'")
   cur.execute("UPDATE Anahtarlar SET deger='0' WHERE isim='Ev'")
   cur.execute("UPDATE Anahtarlar SET Durum='Kapalı' WHERE isim='Araba'")
   cur.execute("UPDATE Anahtarlar SET deger='0' WHERE isim='Araba'")

   con.commit()
   return "Başarılı Elektrik Kesildi !"

@app.route('/my-link2/')
def my_link2():
   con =sqlite3.connect("gomulu.db");
   
   cur = con.cursor()
   cur.execute("UPDATE Anahtarlar SET Durum='Acik' WHERE isim='Kasa'")
   cur.execute("UPDATE Anahtarlar SET Deger='1' WHERE isim='Kasa'")

   con.commit()
   return "Kasa Açık Emulatörden Görebilirsiniz !"


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('bos.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         isim = request.form['isim']
         durum = request.form['durum']
         acikmi = request.form['acikmi']
    
         with sql.connect("gomulu.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO sera (isim,durum,acikmi)  VALUES (?,?,?,?)",(isim,durum,acikmi) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("gomulu.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Anahtarlar")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

