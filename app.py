from flask import Flask, render_template
from flask import send_file
from generate_po import generate_po

app = Flask(__name__)

suppliers = {
    "ABC Trading": [
        {"code": "JST-110", "name": "Hotdog", "price": 100.00},
        {"code": "JST-120", "name": "Coffee", "price": 120.00},
        {"code": "BEV-0210", "name": "Beans", "price": 150.00},
    ],
    "Metro Supply": [
        {"code": "POS-12345", "name": "Thermal Paper", "price": 85.00},
        {"code": "PRT-2425", "name": "Printer", "price": 1450.00},
        {"code": "BEV-89456", "name": "Chocolate", "price": 140.00},
    ],
    "Prime Goods": [
        {"code": "FRT-12032", "name": "POS", "price": 430.00},
        {"code": "PRT-1234", "name": "Printer", "price": 1500.00},
        {"code": "JST-110", "name": "Hotdog", "price": 95.00},
    ]
}


# LOGIN PAGE (FIRST PAGE)
@app.route("/")
def login():
    return render_template("login.html")


# MAIN DASHBOARD AFTER LOGIN
@app.route("/home")
def home():
    return render_template("home.html")


# INVENTORY TRANSACTIONS
@app.route("/inventory-transactions")
def inventory_transactions():
    return render_template("inventory_transactions.html")


# INVENTORY MANAGEMENT
@app.route("/inventory-management")
def inventory_management():
    return render_template("inventory_management.html")

@app.route("/config/stock-master")
def config_stock_master():
    return render_template("config/stock_master.html")

@app.route("/config")
def config():
    return render_template("config.html")

@app.route("/config/stock-group")
def config_stock_group():
    return render_template("config/stock_group.html")

@app.route("/config/inventory-cycle")
def config_inventory_cycle():
    return render_template("config/inventory_cycle.html")

@app.route("/config/recipe")
def config_recipe():
    return render_template("config/recipe.html")

@app.route("/config/menu-item-link")
def config_menu_item_link():
    return render_template("config/menu_item_link.html")

@app.route("/config/supplier")
def config_supplier():
    return render_template("config/supplier.html")

@app.route("/config/store-number")
def config_store_number():
    return render_template("config/store_number.html")

@app.route("/config/ingredient-replacement")
def config_ingredient_replacement():
    return render_template("config/ingredient_replacement.html")

@app.route("/config/portfolio-management")
def config_portfolio_management():
    return render_template("config/portfolio_management.html")

@app.route("/config/default-stock-period")
def config_default_stock_period():
    return render_template("config/default_stock_period.html")

@app.route("/config/recipe-group")
def config_recipe_group():
    return render_template("config/recipe_group.html")

@app.route("/config/recipe-replication")
def config_recipe_replication():
    return render_template("config/recipe_replication.html")

@app.route("/config/unit-measurement")
def config_unit_measurement():
    return render_template("config/unit_measurement.html")

@app.route("/config/substitute-inventory")
def config_substitute_inventory():
    return render_template("config/substitute_inventory.html")

@app.route("/config/main-stock-group")
def config_main_stock_group():
    return render_template("config/main_stock_group.html")

@app.route("/config/inventory-transactions")
def config_inventory_transactions():
    return render_template("config/inventory_transactions.html")

@app.route("/config/document-number")
def config_document_number():
    return render_template("config/document_number.html")

@app.route("/config/stock-level")
def config_stock_level():
    return render_template("config/stock_level.html")

@app.route("/config/reason")
def config_reason():
    return render_template("config/reason.html")

@app.route("/config/over-group")
def config_over_group():
    return render_template("config/over_group.html")

@app.route("/config/process-type")
def config_process_type():
    return render_template("config/process_type.html")

@app.route("/config/stock-markup")
def config_stock_markup():
    return render_template("config/stock_markup.html")

@app.route("/config/region")
def config_region():
    return render_template("config/region.html")

@app.route("/config/stock-markup-price")
def config_stock_markup_price():
    return render_template("config/stock_markup_price.html")

@app.route("/config/region-config")
def config_region_config():
    return render_template("config/region_config.html")

@app.route("/system-options")
def system_options():
    return render_template("system_options.html")

@app.route("/management/supplier-billing")
def management_supplier_billing():
    return render_template("management/supplier_billing.html")

@app.route("/management/manual-menu-item")
def management_manual_menu_item():
    return render_template("management/manual_menu_item.html")

@app.route("/management/import-menu-item")
def management_import_menu_item():
    return render_template("management/import_menu_item.html")

@app.route("/management/recalculate-mi-usage")
def management_recalculate_mi_usage():
    return render_template("management/recalculate_mi.html")

@app.route("/management/view-stock-onhand")
def management_view_stock_onhand():
    return render_template("management/view_stock_onhand.html")

@app.route("/management/stuck-opening-adjustment")
def management_stuck_opening_adjustment():
    return render_template("management/stuck_opening.html")

@app.route("/management/stock-requirements")
def management_stock_requirements():
    return render_template("management/stock_requirements.html")

@app.route("/management/stock-adjustment")
def management_stock_adjustment():
    return render_template("management/stock_adjustment.html")

@app.route("/product")
def product():
    return "<h1>Add Product Page</h1>"

@app.route("/transaction/order-request")
def transaction_order_request():
    return render_template("transactions/order_request.html", suppliers=suppliers)

@app.route("/transaction/request-approval")
def transaction_request_approval():
    return render_template("transactions/request_approval.html")

@app.route("/transaction/inventory-order")
def transaction_inventory_order():
    return render_template("transactions/inventory_order.html")

@app.route("/transaction/order-approval")
def transaction_order_approval():
    return render_template("transactions/order_approval.html")

@app.route("/transaction/inventory-receive")
def transaction_inventory_receive():
    return render_template("transactions/inventory_receive.html")

@app.route("/transaction/inventory-pick-list")
def transaction_inventory_pick_list():
    return render_template("transactions/inventory_pick_list.html")

@app.route("/transaction/inventory-dn-cn")
def transaction_inventory_dn_cn():
    return render_template("transactions/inventory_dn_cn.html")

@app.route("/transaction/inventory-transfer")
def transaction_inventory_transfer():
    return render_template("transactions/inventory_transfer.html")

@app.route("/transaction/transfer-management")
def transaction_transfer_management():
    return render_template("transactions/transfer_management.html")

@app.route("/transaction/create-batch-recipe")
def transaction_create_batch_recipe():
    return render_template("transactions/create_batch_recipe.html")

@app.route("/transaction/raw-waste-record")
def transaction_raw_waste_record():
    return render_template("transactions/raw_waste_record.html")

@app.route("/transaction/menu-item-finished")
def transaction_menu_item_finished():
    return render_template("transactions/menu_item_finished.html")

@app.route("/transaction/enter-stock-count")
def transaction_enter_stock_count():
    return render_template("transactions/enter_stock_count.html")

@app.route("/transaction/inventory-closing")
def transaction_inventory_closing():
    return render_template("transactions/inventory_closing.html")

@app.route("/transaction/email-fax-purchase")
def transaction_email_fax_purchase():
    return render_template("transactions/email_fax_purchase.html")

@app.route("/transaction/warehouse-order")
def transaction_warehouse_order():
    return render_template("transactions/warehouse_order.html")

@app.route("/transaction/transaction-17")
def transaction_transaction_17():
    return render_template("transactions/transaction_17.html")

@app.route("/<path:any_path>")
def placeholder(any_path):
    return f"<h1>Page: /{any_path}</h1><p>This is a placeholder route.</p>"

if __name__ == "__main__":
    app.run(debug=True)