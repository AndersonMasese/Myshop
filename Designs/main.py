'''Main flask app file for the Shopping list application challenge'''
from flask import Flask, redirect, url_for, request, render_template, session, flash
from person import Person
from shopping_list import ShoppingList

user=Person()
app=Flask(__name__)
app.secret_key='dfkdfjnhfubvhppnhjr'

@app.route('/add_shopping_list_item', methods=['POST','GET'])
def add_shopping_list_item():
    

    

    '''renders the html file of adding an item to a shopping list'''
    try:
        with open('shoplogger.txt','r') as f:
            records = []
            for lines in f:
                records.append(lines)
                
        return render_template('add_shopping_list_item.html',records=records)

    except FileNotFoundError as fe:
        return render_template('add_shopping_list_item.html')

    finally:
        if request.method == 'POST':
            result=request.form
            in_list=result['list']
            in_item=result['item']
            #now try to open a file with same name and populate our view function with the items in it
            try:
                with open(in_list+'.txt','a') as f:
                    f.write(in_item)
                    f.write('\n')
                flash('Item added successfully')    
                return render_template('add_shopping_list_item.html',records=records)

            except FileNotFoundError as fe:
                flash('requested shopping list not found')
                return render_template('add_shopping_list_item.html')
        

        else:
            return render_template('add_shopping_list_item.html')
    
    

@app.route('/create_shopping_list')
def create_shopping_list():
    '''Renders the html file for renderring the html file for creating shopping list'''
    return render_template('create_shopping_list.html')

@app.route('/create_shop_list', methods=['POST','GET'])
def create_sl():
    '''creates a shopping list which is a file object container'''
    if request.method=='POST':
        my_sl=ShoppingList()
        result=request.form
        sl=result['sl']
        desc=result['desc']
        my_sl.create(sl,desc)
        flash('Shopping list created successfully')
        return render_template('create_shopping_list.html')
    else:
        flash('Your shopping list failed to create')
        return render_template('create_shopping_list.html')

@app.route('/delete_shopping_list',methods=['POST','GET'])
def delete_shopping_list():
    '''receives name of a shopping list which is a file object and opens it for writing
    hence effectively deleting the items in the whole list'''
    if request.method == 'POST':
        current_file=request.form['delitem']
        try:
            with open(current_file+'.txt','w') as f:
                pass
            flash("successfully deleted all items in Shopping List")
                
            return render_template('delete_shopping_list.html')
        except FileNotFoundError as fne:
            flash('The shopping list name entered was not found')
            return render_template('delete_shopping_list.html')
    else:
        flash('Error while processing your request')
        return render_template('delete_shopping_list.html')

@app.route('/delete_shopping_list_item')
def delete_shopping_list_item():
    '''renders the html file for deleting and item from a shopping list'''
    return render_template('delete_shopping_list_item.html')
    
@app.route('/homepage')
def homepage():
    '''renderer'''
    flash('Registration success. Now logged in.')
    return render_template('homepage.html')
    

@app.route('/')
def sarter():
    '''renderer'''
    return render_template('login.html')
    
@app.route('/login',methods=['POST','GET'])
def login():
    '''renderer'''
    if request.method=='POST':
        #objects posted as keyword argument combinations
        
        details=request.form
        username=details['username']
        session['username']=details['username']
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
    '''renderer file'''
    return render_template('registration.html')
    

@app.route('/registration',methods=['POST','GET'])
def registration():
    '''function gets entries from registration.html file and processes them
    to determine if regisrations is successful or not'''
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

@app.route('/shared_shopping_lists',methods=['POST','GET'])
def shared_shopping_lists():
    '''try to read an already available shared_lists.txt file
    for a list of shared files'''
    
    
    try:
        with open('shared_lists.txt','r') as f:
            records = []
            for lines in f:
                records.append(lines)
                
        return render_template('shared_shopping_lists.html',records=records)

    except FileNotFoundError as fe:
        return render_template('shared_shopping_lists.html')
    finally:


        if request.method == 'POST':
            result=request.form
            in_list=result['item']
            #now try to open a file with same name and populate our view function with the items in it
            try:
                with open(in_list+'.txt','r') as f:
                    entries=[]
                    for lines in f:
                        entries.append(lines)
                return render_template('shared_shopping_lists.html', entries=entries,records=records)

            except FileNotFoundError as fe:
                flash('requested file not found')
                return render_template('shared_shopping_lists.html')
        else:
            return render_template('shared_shopping_lists.html')

@app.route('/share_my_list',methods=['POST','GET'])
def share_my_list():
    '''share my list by putting its name in a common file'''
    if request.method == 'POST':
        result = request.form
        items_share = result['item']
        new_share_instance = ShoppingList()
        new_share_instance.share_container(items_share)
        flash('successfully shared your shopping list')
        return render_template('share_my_list.html')
    else:
        flash('Failed to share your shopping list')
        return render_template('share_my_list.html')
    

@app.route('/update_shopping_list')
def update_shopping_list():
    '''renderer'''
    return render_template('update_shopping_list.html')
    

@app.route('/update_shopping_list_item')
def update_shopping_list_item():
    '''renderer'''
    return render_template('update_shopping_list_item.html')
    

@app.route('/view_shopping_list_items',methods=['POST','GET'])
def view_shopping_list_items():
    '''try to read an already available shared_lists.txt file
    for a list of shared files'''
    
    
    try:
        with open('shoplogger.txt','r') as f:
            records = []
            for lines in f:
                records.append(lines)
                
        return render_template('view_shopping_list_items.html',records=records)

    except FileNotFoundError as fe:
        return render_template('view_shopping_list_items.html')

    finally:

        if request.method == 'POST':
            result=request.form
            in_list=result['list']
            #now try to open a file with same name and populate our view function with the items in it
            try:
                with open(in_list+'.txt','r') as f:
                    entries=[]
                    for lines in f:
                        entries.append(lines)
                return render_template('view_shopping_list_items.html', entries=entries,records=records)

            except FileNotFoundError as fe:
                flash('requested file not found')
                return render_template('view_shopping_list_items.html')
        else:
            return render_template('view_shopping_list_items.html')


    
    
    
    

@app.route('/view_shopping_lists',methods=['POST','GET'])
def view_shopping_lists():
    '''try to read an already available shared_lists.txt file
    for a list of shared files'''
    
    
    try:
        with open('shoplogger.txt','r') as f:
            records = []
            for lines in f:
                records.append(lines)
                
        return render_template('view_shopping_lists.html',records=records)

    except FileNotFoundError as fe:
        return render_template('view_shopping_lists.html')

    finally:

        if request.method == 'POST':
            result=request.form
            in_list=result['sl']
            #now try to open a file with same name and populate our view function with the items in it
            try:
                with open(in_list+'.txt','r') as f:
                    entries=[]
                    for lines in f:
                        entries.append(lines)
                return render_template('view_shopping_lists.html', entries=entries,records=records)

            except FileNotFoundError as fe:
                flash('requested file not found')
                return render_template('view_shopping_lists.html')
        else:
            return render_template('view_shopping_lists.html')



    

@app.route('/logout')
def logout():
    '''function for destroying session and login out'''
    session.pop('username',None)
    return render_template('login.html')

if __name__=='__main__':
    app.debug=True
    
    app.run()
    app.run(debug=True)
    