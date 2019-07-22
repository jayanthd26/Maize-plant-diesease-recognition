from flask import *  
from sklearn.externals import joblib
import pandas as pd
import YieldPredictor as yp

app = Flask(__name__)  
  
@app.route('/',methods = ['POST'])  
def login():  
      crop=request.form['crop']
      place=request.form['place']
      mounth=request.form['mounth']
      area=request.form['landsize']
      year='2019'
      #uname=request.form['uname']  
      print(crop)
      print(place)
      print(mounth)
      print(area)

      yeild=str(round(float((yp.predict(year,"",area)))))

      #return render_template('output.html',name=uname)  
      budget1=int(area)/22*16875;
      budget1=str(round(budget1))
      return render_template('output.html',op=yeild,budget=(budget1))
       
       
   
if __name__ == '__main__':  
   app.run(debug = True,port=3001)  