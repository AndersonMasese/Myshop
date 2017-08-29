'''driver file for the Myshop application'''
from flask import Flask,redirect,url_for,request,render_template,session,flash
from person import Person
user=Person()
app=Flask(__name__)
app.secret_key='dfkdfjnhfubvhppnhjr'
@app.route('/add_shopping_list_item')
def add_shopping_list_item():
    pass

@app.route('/create_shopping_list')
def create_shopping_list():
    pass

@app.route('/delete_shopping_list')
def delete_shopping_list():
    pass

@app.route('/delete_shopping_list_item')
def delete_shopping_list_item():
    pass

@app.route('/homepage')
def homepage():
    flash('Registration success. Now logged in.')
    return render_template('homepage.html')
    

@app.route('/')
def sarter():
    return render_template('login.html')
    


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':

        #username=session['username']
        id=request.form
        username=id['username']
        password=id['password']
        #if username=='name':
        #if username in user.validator() and password in user.validator():
        return redirect(url_for('homepage'))
    else:

        #flash error message
        #flash('Wrong Login credentials')

        return redirect(url_for('/'))

@app.route('/usereg')
def usereg():
    return render_template('registration.html')
    

@app.route('/registration',methods=['POST','GET'])
def registration():
    if request.method=='POST':
        details=request.form
        username=details['username']
        emailaddress=details['emailaddress']
        password=details['password']
        user.register(username,emailaddress,password)
        return redirect(url_for('homepage'))
    else:
        var1=flash('Registration failed due to Internal server error')
    return redirect(url_for('usereg'))

@app.route('/shared_shopping_lists')
def shared_shopping_lists():
    pass

@app.route('/update_shopping_list')
def update_shopping_list():
    pass

@app.route('/update_shopping_list_item')
def update_shopping_list_item():
    pass

@app.route('/view_shopping_list_items')
def view_shopping_list_items():
    pass

@app.route('/view_shopping_lists')
def view_shopping_lists():
    pass


if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)