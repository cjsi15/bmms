from flask import *

app = Flask(__name__,static_url_path='/static')

@app.route('/',methods=(['POST','GET']))
def index():
    user=['admin']
    pasw=['admin']
    if request.method=='POST':
        email=request.form['email']
        pas=request.form['pass']
        if email in user and pas in pasw:
            session=email
            return render_template('homepage.html')
        else:
            return render_template('index.html',info='User or pass do not match!')    
    return render_template("index.html")      
        
    

@app.route('/homepage',methods=['POST','GET'])
def homepage():
    return render_template('homepage.html')

if __name__ == "__main__":
  app.run(host='localhost',port=8080,debug=True)
