from flask import Flask, render_template,url_for
app = Flask(__name__)

#We are going to create a dummy data
#Data it related to list of people and there post 

posts =[
   {
      'author' : 'Niraj Baral',
      'title' : 'Blog Post 1',
      'content' : 'First post content',
      'date_posted' : 'April 20,2018'
   },
   {
      'author' : 'Ozzu Bhandari',
      'title' : 'Blog Post 2',
      'content' : 'Secont post content',
      'date_posted' : 'May 12,2018'
   }

]

@app.route('/')
@app.route('/home')
def hello_world():
   return render_template('home.html',title ='Home Page' ,posts= posts)


@app.route("/about")
def about():
   return render_template('about.html', title ='About')



#if we don't want  to make that env setup run each 
#time we can do that by rumming app in python directly  



if __name__ == '__main__':  ## it is main run file 
   app.run(debug=True)    # Basically now we can run by typing python main.py 
                           # instade flask run main.py 

