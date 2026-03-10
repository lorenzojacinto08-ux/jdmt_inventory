from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/inventory-transactions")
def inventory_transactions():
    return render_template("inventory_transactions.html")

@app.route("/inventory-management")
def inventory_management():
    return render_template("inventory_management.html")

@app.route("/config")
def config():
    return render_template("config.html")

@app.route("/other")
def other():
    return render_template("other.html")

@app.route("/system-options")
def system_options():
    return render_template("system_options.html")

@app.route("/management/1")
def management_1():
    return render_template("management/management_1.html")

@app.route("/management/2")
def management_2():
    return render_template("management/management_2.html")

@app.route("/management/3")
def management_3():
    return render_template("management/management_3.html")

@app.route("/management/4")
def management_4():
    return render_template("management/management_4.html")

@app.route("/management/5")
def management_5():
    return render_template("management/management_5.html")

@app.route("/management/6")
def management_6():
    return render_template("management/management_6.html")

@app.route("/management/7")
def management_7():
    return render_template("management/management_7.html")

@app.route("/management/8")
def management_8():
    return render_template("management/management_8.html")

@app.route("/product")
def product():
    return "<h1>Add Product Page</h1>"

@app.route("/transaction/1")
def transaction_1():
    return render_template("transactions/transaction_1.html")

@app.route("/transaction/2")
def transaction_2():
    return render_template("transactions/transaction_2.html")

@app.route("/transaction/3")
def transaction_3():
    return render_template("transactions/transaction_3.html")

@app.route("/transaction/4")
def transaction_4():
    return render_template("transactions/transaction_4.html")

@app.route("/transaction/5")
def transaction_5():
    return render_template("transactions/transaction_5.html")

@app.route("/transaction/6")
def transaction_6():
    return render_template("transactions/transaction_6.html")

@app.route("/transaction/7")
def transaction_7():
    return render_template("transactions/transaction_7.html")

@app.route("/transaction/8")
def transaction_8():
    return render_template("transactions/transaction_8.html")

@app.route("/transaction/9")
def transaction_9():
    return render_template("transactions/transaction_9.html")

@app.route("/transaction/10")
def transaction_10():
    return render_template("transactions/transaction_10.html")

@app.route("/transaction/11")
def transaction_11():
    return render_template("transactions/transaction_11.html")

@app.route("/transaction/12")
def transaction_12():
    return render_template("transactions/transaction_12.html")

@app.route("/transaction/13")
def transaction_13():
    return render_template("transactions/transaction_13.html")

@app.route("/transaction/14")
def transaction_14():
    return render_template("transactions/transaction_14.html")

@app.route("/transaction/15")
def transaction_15():
    return render_template("transactions/transaction_15.html")

@app.route("/transaction/16")
def transaction_16():
    return render_template("transactions/transaction_16.html")

@app.route("/transaction/17")
def transaction_17():
    return render_template("transactions/transaction_17.html")

@app.route("/<path:any_path>")
def placeholder(any_path):
    return f"<h1>Page: /{any_path}</h1><p>This is a placeholder route.</p>"

if __name__ == "__main__":
    app.run(debug=True)