from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
	return render_template('signup.html')
@app.route("/showlogin")
def showlogin():
	return render_template('login.html')
@app.route("/showviewlist")
def showviewlist():
	return render_template('view.html')
@app.route("/showlist")
def showlist():
	return render_template('list.html')

if __name__=="__main__":
	app.run(debug = True)


