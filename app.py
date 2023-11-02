from flask import Flask,render_template,request
app=Flask(__name__)
list1=[]
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        data=request.json
        list1.append(data)
    return render_template("home.html",datum=list1)

if __name__=="__main__":
    app.run(debug=True)