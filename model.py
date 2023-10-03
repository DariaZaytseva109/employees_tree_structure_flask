from sqlalchemy.orm import relationship, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Base(DeclarativeBase):
  pass


class Employee(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    fullname = db.Column(db.String)
    position = db.Column(db.String)
    day = db.Column(db.Date)
    salary = db.Column(db.Integer)
    boss_id = db.Column(db.Integer, db.ForeignKey('employee.id', ondelete='SET NULL'))
    level = db.Column(db.Integer)
    subordinates = db.relationship('Employee')
    boss_name = db.Column(db.String)

