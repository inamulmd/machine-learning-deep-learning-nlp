### Building Url Dynamically
###Variable rule
### Jinja 2 Template Engine

### jinja2 Tempelate engine
'''
{{  }} expression to print output in html
{%...%} condition , for loops
{#...#}
'''

from flask import Flask,render_template,request,redirect,url_for
'''
It create an instance of the flask class,
which will be your WSGI (web Server Gateway Interface) application
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


# @app.route('/submit1',methods=['GET','POST'])
# def submit1():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'hello{name}'
#     return render_template('form.html')

### variabe Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"

    return render_template('result.html',result=res) 

### variabe Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"

    exp={'score':score,"res":res}    

    return render_template('result1.html',result=exp)

### variabe Rule
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html',result=score)

@app.route('/fail/<int:score>')
def fail(score):
      
    return render_template('result.html',result=score)  

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+math+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))    


if __name__=="__main__":
    app.run(debug=True)
