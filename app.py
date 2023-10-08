from flask import Flask
from flask_migrate import Migrate
from flask_mail import Mail
from app.models import db
from app.incomes import incomes_bp
from app.expenses import expenses_bp
from app.budgets import budgets_bp
from app.charts import charts_bp
from app.dashboard import dashboard_bp
from app.reports import reports_bp
from app.auth import auth_bp

app = Flask(__name__, template_folder='app/templates')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'personalincomexpensetracker@gmail.com'
app.config['MAIL_PASSWORD'] = 'cclcpaaosprdwsx'  # Replace with your Gmail account password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db.init_app(app)
migrate = Migrate(app, db)

def create_app():
    app.register_blueprint(incomes_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(budgets_bp)
    app.register_blueprint(charts_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(reports_bp)

    mail = Mail(app)

    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
