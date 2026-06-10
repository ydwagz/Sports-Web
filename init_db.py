from ext import app, db
from model import Sport

sport = Sport()

with app.app_context():
    db.drop_all()
    db.create_all()
