<<<<<<< HEAD
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)
=======
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)
    
>>>>>>> 3a6380d9d934b66f4ea6210c986fe378a15c2247
