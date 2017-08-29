
from flask import Flask,redirect,url_for,request,render_template,session,flash
from person import Person
from shopping_list import ShoppingList
user=Person()
app=Flask(__name__)
app.secret_key='dfkdfjnhfubvhppnhjr'
@app.route('/add_shopping_list_item')
def add_shopping_list_item():
    return render_template('add_shopping_list_item.html')
    

@app.route('/create_shopping_list')
def create_shopping_list():
    return render_template('create_shopping_list.html')

@app.route('/create_shop_list', methods=['POST','GET'])
def create_sl():
    if request.method=='POST':
        my_sl=ShoppingList()
        result=request.form
        sl=result['sl']
        desc=result['desc']
        my_sl.create(sl,desc)
        flash('Shopping list created successfully')
        return redirect(url_for('create_shopping_list'))
    else:
        flash('Your shopping list failed to create')
        return redirect(url_for('create_shopping_list'))



@app.route('/delete_shopping_list')
def delete_shopping_list():
    return render_template('delete_shopping_list.html')
    

@app.route('/delete_shopping_list_item')
def delete_shopping_list_item():
    return render_template('delete_shopping_list_item.html')
    

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
        details=request.form
        username=details['username']
        pword=details['pword']
        if username in user.validator():
            

        
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('usereg'))
    else:
        var1=flash('Registration failed due to Internal server error')
    return redirect(url_for('usereg'))

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
    return render_template('shared_shopping_lists.hml')
    

@app.route('/update_shopping_list')
def update_shopping_list():
    return render_template('update_shopping_list.html')
    

@app.route('/update_shopping_list_item')
def update_shopping_list_item():
    return render_template('update_shopping_list_item.html')
    

@app.route('/view_shopping_list_items')
def view_shopping_list_items():
    return render_template('view_shopping_list_items.html')
    

@app.route('/view_shopping_lists')
def view_shopping_lists():
    #try to pass arguments which will make the viewer render the read objects dynamically
    my_ls=ShoppingList()
    records=my_ls.show()
    return render_template('view_shopping_lists.html',records=records)
    


if __name__=='__main__':
    app.debug=True
    
    app.run()
    app.run(debug=True)
    