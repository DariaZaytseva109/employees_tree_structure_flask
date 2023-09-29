from sqlalchemy.orm import relationship, DeclarativeBase, backref
from datetime import date
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Base(DeclarativeBase):
  pass



class Employee(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    fullname = db.Column(db.String)
    position = db.Column(db.String)
    day = db.Column(db.Date, default=date.today())
    salary = db.Column(db.Integer)
    boss_id = db.Column(db.Integer, db.ForeignKey('employee.id', ondelete='SET NULL'))
    level = db.Column(db.Integer)
    subordinates = db.relationship('Employee', remote_side=[id], backref='employee')



class Employee_0(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullname = db.Column(db.String)
    position = db.Column(db.String)
    day = db.Column(db.Date, default=date.today())
    salary = db.Column(db.Integer)
    subordinates = db.relationship('Employee_1', backref='employee_0')


class Employee_1(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullname = db.Column(db.String)
    position = db.Column(db.String)
    day = db.Column(db.Date, default=date.today())
    salary = db.Column(db.Integer)
    boss_id = db.Column(db.Integer, db.ForeignKey('employee_0.id', ondelete='SET NULL'))
    subordinates = db.relationship('Employee_2', backref='employee_1')



class Employee_2(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullname = db.Column(db.String)
    position = db.Column(db.String)
    day = db.Column(db.Date, default=date.today())
    salary = db.Column(db.Integer)
    boss_id = db.Column(db.Integer, db.ForeignKey('employee_1.id', ondelete='SET NULL'))
    #subordinates = relationship('employee_3', back_populates='boss_id')


