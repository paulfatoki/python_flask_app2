from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def welcome():
   return "Welcome to the Institute of African and Diaspora Studies!"
 
@app.route('/create')
def create():
   a=100
   b=50
   c=a*b
   return "This is the result " + str(c)
 
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8009, debug =True)