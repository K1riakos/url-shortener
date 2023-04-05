from .db import db


class Url(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.String, unique=True, nullable=False)
  short_url = db.Column(db.String, unique=True, nullable=False)

  def __repr__(self):
    return str(self.id)
