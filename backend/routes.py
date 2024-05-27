from flask import Blueprint
from services.order_management import order_blueprint
from services.customer_service import customer_blueprint
from services.chatgpt_integration import chatgpt_blueprint

def init_routes(app):
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(chatgpt_blueprint, url_prefix='/chatgpt')
