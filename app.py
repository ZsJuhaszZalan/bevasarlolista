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

if __name__ == "__main__":
    app.run(debug=True)