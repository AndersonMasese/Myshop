'''Main flask app file for the Shopping list application challenge'''
from flask import Flask, redirect, url_for, request, render_template, session, flash
from redundant import *

# user=Person()
app = Flask(__name__)
app.secret_key = 'dfkdfjnhfubvhppnhjr'


@app.route('/add_shopping_list_item', methods=['POST', 'GET'])
def add_shopping_list_item():
    '''renders the html file of adding an item to a shopping list'''

    try:
        records = []
        for elements in shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('add_shopping_list_item.html', records=records)

    except:
        return render_template('add_shopping_list_item.html')

    finally:
        if request.method == 'POST':
            result = request.form
            in_list = result['list']
            in_item = result['item']

            my_items_dict = itemsdictionary[in_list]  # yields a list
            my_items_dict.append(in_item)
            new_items_dic = {in_list: my_items_dict}
            itemsdictionary.update(new_items_dic)

            try:

                flash('Item added successfully')

                return render_template('add_shopping_list_item.html', records=records)

            except:
                flash('requested shopping list not found')
                return render_template('add_shopping_list_item.html')
        else:
            return render_template('add_shopping_list_item.html')


@app.route('/create_shopping_list')
def create_shopping_list():
    '''Renders the html file for renderring the html file for creating shopping list'''
    return render_template('create_shopping_list.html')


@app.route('/create_shop_list', methods=['POST', 'GET'])
def create_sl():
    '''creates a shopping list which is a file object container'''
    if request.method == 'POST':
       # my_sl=ShoppingList()
        result = request.form
        sl = result['sl']
        desc = result['desc']
        # my_sl.create(sl,desc)
        create(sl)  # redundant create shopping list
        list_container = []
        slist = {sl: list_container}
        # create another copy of shopping list which is a dictionary with its name as key
        create1(slist)
        flash('Shopping list created successfully')
        return render_template('create_shopping_list.html')
    else:
        flash('Your shopping list failed to create')
        return render_template('create_shopping_list.html')


@app.route('/delete_shopping_list', methods=['POST', 'GET'])
def delete_shopping_list():
    '''receives name of a shopping list which is a file object and opens it for writing
    hence effectively deleting the items in the whole list'''
    if request.method == 'POST':
        current_list = request.form['delitem']
        try:
            del itemsdictionary[current_list]
            flash("successfully deleted all items in Shopping List")

            return render_template('delete_shopping_list.html')
        except:
            flash('The shopping list name entered was not found')
            return render_template('delete_shopping_list.html')
    else:
        flash('Error while processing your request')
        return render_template('delete_shopping_list.html')


@app.route('/delete_shopping_list_item', methods=['POST', 'GET'])
def delete_shopping_list_item():
    '''renders the html file for deleting an item from a shopping list, and deletes items in the specified dictionaries'''
    try:
        records = []
        for elements in shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('delete_shopping_list_item.html', records=records)

    except:
        return render_template('delete_shopping_list_item.html')

    finally:
        if request.method == 'POST':
            result = request.form
            in_list = result['list']
            in_item = result['item']

            my_items_dict = itemsdictionary[in_list]  # yields a list
            del my_items_dict[int(in_item) - 1]
            new_items_dic = {in_list: my_items_dict}
            itemsdictionary.update(new_items_dic)

            try:

                flash('Item deleted')

                return render_template('delete_shopping_list_item.html', records=records)

            except:
                flash('requested shopping list not found')
                return render_template('delete_shopping_list_item.html')
        else:
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''renderer'''
    if request.method == 'POST':
        # objects posted as keyword argument combinations

        details = request.form
        username = details['username']
        session['username'] = details['username']
        pword = details['pword']
        # if username in user.validator():

        if username in account and pword in account:
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('usereg'))

    else:
        flash('Registration failed due to Internal server error')
    return redirect(url_for('usereg'))


@app.route('/usereg')
def usereg():
    '''renderer file'''
    return render_template('registration.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    '''function gets entries from registration.html file and processes them
    to determine if regisrations is successful or not'''

    if request.method == 'POST':
        details = request.form
        username = details['username']
        emailaddress = details['emailaddress']
        password = details['password']
        # registration completely moved from files to lists
        register(username, emailaddress, password)
        # user.register(username,emailaddress,password)
        return redirect(url_for('homepage'))

    else:
        var1 = flash('Registration failed due to Internal server error')
        return redirect(url_for('usereg'))


@app.route('/shared_shopping_lists', methods=['POST', 'GET'])
def shared_shopping_lists():
    '''try to read an already available dictionary
    for a list of shared shopping lists which are actually list objects'''

    try:
        records = []
        for elements in shared_shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('shared_shopping_lists.html', records=records)
    except:
        return render_template('shared_shopping_lists.html')

    finally:

        if request.method == 'POST':
            result = request.form
            in_list = result['list']
            # now try to open a file with same name and populate our view function with the items in it
            try:
                # returns a list since the dictionary store the values as lists which hold the shopping items
                this_list = shareditemsdictionary[in_list]

                return render_template('shared_shopping_lists.html', entries=this_list, records=records)

            except:
                flash('requested shopping list not found')
                return render_template('shared_shopping_lists.html')
        else:
            return render_template('shared_shopping_lists.html')


@app.route('/share_index')
def share_index():
    return render_template('share_index.html')


@app.route('/add_shared_shopping_list', methods=['POST', 'GET'])
def add_list():
    '''Adds an existing shopping list into a common dictionary to share with other users'''
    try:
        records = []
        for elements in shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('share_index.html', records=records)

    except:
        return render_template('share_index.html')

    finally:
        if request.method == 'POST':
            result = request.form
            in_list = result['list']
            my_items_dict = itemsdictionary[in_list]  # yields a list
            new_items_dic = {in_list: my_items_dict}
            shareditemsdictionary.update(new_items_dic)
            create3(in_list)

            try:

                flash('Item added successfully')

                return render_template('share_index.html', records=records)

            except:
                flash('requested shopping list not found')
                return render_template('share_index.html')
        else:
            return render_template('share_index.html')


@app.route('/share_my_list', methods=['POST', 'GET'])
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


@app.route('/view_shopping_list_items', methods=['POST', 'GET'])
def view_shopping_list_items():
    '''try to read an already available shared_lists.txt file
    for a list of shared files'''

    try:
        records = []
        for elements in shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('add_shopping_list_item.html', records=records)
    except:
        return render_template('view_shopping_list_items.html')

    finally:

        if request.method == 'POST':
            result = request.form
            in_list = result['list']
            # now try to open a file with same name and populate our view function with the items in it
            try:
                # returns a list since the dictionary store the values as lists which hold the shopping items
                this_list = itemsdictionary[in_list]

                return render_template('view_shopping_list_items.html', entries=this_list, records=records)

            except:
                flash('requested file not found')
                return render_template('view_shopping_list_items.html')
        else:
            return render_template('view_shopping_list_items.html')


@app.route('/view_shopping_lists', methods=['POST', 'GET'])
def view_shopping_lists():
    '''try to read an already available shared_lists.txt file
    for a list of shared files'''

    try:
        records = []
        for elements in shopping_list_container:  # bring shopping list container into current namespace
            records.append(elements)

        return render_template('add_shopping_list_item.html', records=records)

    except:
        return render_template('view_shopping_lists.html')

    finally:

        if request.method == 'POST':
            result = request.form
            in_list = result['sl']
            # now try to open a file with same name and populate our view function with the items in it
            try:
                # returns a list since the dictionary store the values as lists which hold the shopping items
                this_list = itemsdictionary[in_list]

                return render_template('view_shopping_lists.html', entries=this_list, records=records)

            except:
                flash('requested file not found')
                return render_template('view_shopping_lists.html')
        else:
            return render_template('view_shopping_lists.html')


@app.route('/logout')
def logout():
    '''function for destroying session and login out'''
    session.pop('username', None)
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True

    app.run()
    app.run(debug=True)
