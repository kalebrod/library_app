from datetime import date,timedelta

from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db

class BookLoan(db.Model):
    __tablename__ = 'book_loan'
    loan_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'),primary_key=True)
    start = db.Column(db.DateTime,default=date.today())
    end = db.Column(db.DateTime,default=date.today() + timedelta(days=15))
    status = db.Column(db.String(10),default='ok')

    user = db.relationship('User',backref=db.backref(
        "book_loan",cascade="all, delete-orphan"
    ))

    book = db.relationship('Book',backref=db.backref(
        "book_loan",cascade="all, delete-orphan"
    ))

    def __repr__(self):
        return f"<BookLoan {self.user.name} - {self.book.name} - {self.status}>"

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(1000),nullable=False)
    quantity = db.Column(db.Integer,default=0)

    books = db.relationship(
        'Book',secondary='book_loan',viewonly=True
    )
    
    def __repr__(self):
        return f"<User {self.name} - {self.quantity}"

    @property
    def upassword(self):
        raise AttributeError('Cannot access unhashed passwords')
    
    @upassword.setter
    def upassword(self,value):
        self.password = generate_password_hash(value)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    autor = db.Column(db.String(50),nullable=False)
    datep = db.Column(db.DateTime,nullable=False)
    quantity = db.Column(db.Integer,default=0)

    users = db.relationship(
        'User',secondary='book_loan',viewonly=True
    )

    def __repr__(self):
        return f"<Book {self.name} - {self.autor}>"