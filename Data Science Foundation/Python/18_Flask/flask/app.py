from flask import Flask
'''
It create an instance of the flask class,
which will be your WSGI (web Server Gateway Interface) application
'''
###WSGI Application
app=Flask(__name__)

@app.route("/index")
def index():
    return "Welcome to index page"

if __name__=="__main__":
    app.run(debug=True)