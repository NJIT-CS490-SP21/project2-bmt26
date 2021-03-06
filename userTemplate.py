from app import db

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    rank = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Template %r>' % self.username