from flask import *

app = Flask(__name__,static_url_path='/static')
items=[
]
stos=[]   
@app.route('/',methods=(['POST','GET']))
def index():
    user=['admin']
    pasw=['@dmin']
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
    with open('masterdata.json','r') as g:
        d=json.load(g)
        items.append(d)
        info=jsonify(items)
        print(type(info))
        return info

@app.route('/query')
def query():
    return render_template("query.html")

@app.route('/incomes', methods=['POST'])
def add_income():
  items.append(request.get_json())
  return 'backup saved!', 204
  
@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/view')
def view():
    with open('masterdata.json','r') as g:
        d=json.load(g)
        stos.append(d)
        info=jsonify(stos)
        print(type(info))
        return info

if __name__ == "__main__":
  app.run(host='localhost',port=8080,debug=True)
