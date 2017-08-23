from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Shopper

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a shopper to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        shopper = Shopper(first_name=form.first_name.data,
                          last_name=form.last_name.data,
                          email=form.email.data,
                          password=form.password.data)

        # add shopper to the database
        db.session.add(shopper)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('showlogin'))

    # load registration template
    return render_template('signup.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether shopper exists in the database and whether
        # the password entered matches the password in the database
        shopper = Shopper.query.filter_by(email=form.email.data).first()
        if shopper is not None and shopper.verify_password(
                form.password.data):
            # log employee in
            login_user(shopper)

            # redirect to the dashboard page after login
            return redirect(url_for('main'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('showlogin.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('showlogin'))