from ext import db


class Sport(db.Model):
    __tablename__ = 'sports'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    desc_long = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=False)
