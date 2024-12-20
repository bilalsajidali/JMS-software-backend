from flask import Flask
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.inventory import inventory_bp
from routes.supplier import supplier_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize mongodb with the app
init_db(app)

# Register blueprints for routing
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(inventory_bp, url_prefix='/api/inventory')
app.register_blueprint(supplier_bp, url_prefix='/api/suppliers')

# Main route 
@app.route('/', methods=['GET', 'POST'])
def home():
    return "Welcome to the Jewelry Management Backend : Health 100"

if __name__ == "__main__":
    app.run(debug=True)
