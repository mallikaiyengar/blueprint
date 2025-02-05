from flask import Flask
from blueprints.home import home_bp
from blueprints.m2pm import m2pm_bp
from blueprints.TaraSPRapp import TaraSPRapp_bp
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(m2pm_bp)
app.register_blueprint(TaraSPRapp_bp)

#add after app is defined
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

if __name__ == "__main__":
    app.run(debug=True)
