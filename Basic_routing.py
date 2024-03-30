from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
   return "<h1>Hello World To flask</h1>"


@app.route("/about")
def about():
   return "<h1>About page</h1>"



#if we don't want  to make that env setup run each 
#time we can do that by rumming app in python directly  



if __name__ == '__main__':  ## it is main run file 
   app.run(debug=True)    # Basically now we can run by typing python main.py 
                           # instade flask run main.py 

