from flask import Flask,render_template,request
import app1 as a

app=Flask(__name__)

@app.route('/')

def home():
    print ("home")
    return render_template("frontend.html")

@app.route('/search',methods=['POST'])

def search():
    print("search")
    value_set_name = request.form['valueset']
    data=a.func1(value_set_name)

    for i in data:
        for j in data[i]:
            print ([j].encode('ascii', 'ignore'))
            print (data[i][j].encode('ascii', 'ignore'))
    return render_template("frontend.html")



if __name__=='__main__':
    app.run(debug=True)
