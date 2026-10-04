from flask import Flask
from localapp.Recovered_Backend_20261004_085226.backend09_26_2026.routes.product_routes import product_bp
app = Flask(__name__)

app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)