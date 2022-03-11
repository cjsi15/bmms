from flask import *

app = Flask(__name__,static_url_path='/static')
items=[
    { 
        "e12hy6":"Hammer"},
    {
        "r4st67":"Coring Machine"
    }
]
    
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

@app.route('/stocks')
def stocks():
    stock=jsonify(items)
    return stock

@app.route('/query')
def query():
    return render_template("query.html")

@app.route('/incomes', methods=['POST'])
def add_income():
  items.append(request.get_json())
  return 'backup saved!', 204


if __name__ == "__main__":
  app.run(host='localhost',port=8080,debug=True)
