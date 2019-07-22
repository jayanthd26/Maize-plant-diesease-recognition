from flask import *  
from sklearn.externals import joblib
import pandas as pd
import YieldPredictor as yp

app = Flask(__name__)  
  
@app.route('/process_get',methods = ['POST'])  
def login():  
      
      filepath=request.form['path']
      print (filepath);
      #return render_template('output.html',cropselected=crop,placeselected=place,mounthselected=mounth,op=yeild,budget=budget1)
       
       
   
if __name__ == '__main__':  
   app.run(debug = True,port=3001)  