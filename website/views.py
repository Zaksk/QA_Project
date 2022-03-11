from flask import Blueprint, render_template, request, flash,redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import User, Product


from . import db

views = Blueprint('views',__name__)

@views.route('/') #whenever we go on our url and just type in slash it will run the home function
@views.route("/home")
@login_required
def home():
    products = Product.query.all()
    return render_template("home.html", user = current_user, products=products)


@views.route("/add_product", methods=['GET', 'POST'])
@login_required
def create_product():
    if request.method == "POST":
        text = request.form.get('text')
        title = request.form.get('title')
        price = request.form.get('price')
        category = request.form.get('category')



        if not text:
            flash('Description cannot be empty', category='error')
        elif len(title) < 1:
            flash('Please enter a product title')
        else:
            product = Product(text=text,title=title, price=price,category=category,author=current_user.id)
            db.session.add(product)
            db.session.commit()
            flash('Post created!', category='success')
            
        return redirect(url_for('views.home'))

    return render_template('add_product.html', user=current_user)


@views.route("/delete_product/<id>")
@login_required
def delete_item(id):
    product = Product.query.filter_by(id=id).first()

    if not product:
        flash("Item does not exist.", category='error')
    elif current_user.id != product.id:
        flash('Only the seller can delete this post', category='error')
    else:
        db.session.delete(product)
        db.session.commit()
        flash('Item deleted', category='sucess')
    
    return redirect(url_for('views.home'))


@views.route("/products/<username>")
@login_required
def products(username):
    user = User.query.filter_by(username=username).first()

    products = user.products
    return render_template('products.html', user=current_user, products=products, username=username)


@views.route("/update_product/<id>", methods=['GET', 'POST'])
@login_required
def update_item(id):
    product = Product.query.filter_by(id=id).first()
    if request.method == 'POST':
        product.text = request.form['text']
        product.title = request.form['title']
        product.price = request.form['price']
        product.category = request.form['category']
        db.session.commit()
        flash("Changes have been saved")
        return redirect(url_for('views.home'))    

    return render_template('update_product.html', user=current_user)



