'''driver file for the Myshop application'''
from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
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
    pass

@app.route('/login')
def login():
    pass

@app.route('/registration')
def registration():
    pass

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