from flask import Flask,render_template,url_for


app = Flask(__name__)

@app.route('/task',methods=['post','get'])
def task():
    # return jsonify(code=0,result="hello world")
    return '<h1>hello world</h1>'

@app.route('/demo',methods=['get'])
def demo():
    return render_template("html/demo.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)