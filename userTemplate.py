from app import DB


class Template(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    rank = DB.Column(DB.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Template %r>' % self.username
