from flask import request
from flask import Flask, render_template,url_for,redirect
from models import ShoppingList, User, Item
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp", methods=['GET', 'POST'])
def showSignUp():
    
    if request.method == 'GET':
        return render_template('signup.html', form=form)

    if request.method == 'POST' :
        email = request.form['email_field']
        f_name = request.form['firstname_field']
        l_name = request.form['lastname_field']
        p_word = request.form['password_field']

        new_user = User(email, f_name, l_name, p_word)
        print(new_user.email, new_user.firstname)
           #return redirect (url_for('showlogin')
        return render_template('login.html')
    

@app.route("/showlogin")
def showlogin():
    return render_template('login.html')
@app.route("/showviewlist")
def showviewlist():
    return render_template('items.html')
@app.route("/showlist")
def showlist():
    return render_template('shoppinglist.html')

if __name__=="__main__":
    app.run(debug = True)


