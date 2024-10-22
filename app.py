from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/submit_products', methods=["POST"])
def submit_products():
    name = request.form.get("product_name")
    products.append(name)
    return redirect(url_for('index'))

@app.route('/products')
def get_products():
    return render_template('products.html', products_=products)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_data = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
            "phone": request.form.get("phone"),
            "gender": request.form.get("gender"),
            "color": request.form.get("color"),
            "profile-pic": request.form.get("profile-pic"),
            "Born-date": request.form.get("Born-date"),
            "Actual-date": request.form.get("Actual-date"),
            "interests": request.form.get("interests")
        }
        user.append(user_data)
        return redirect(url_for('index'))
    return render_template('signup_form.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)