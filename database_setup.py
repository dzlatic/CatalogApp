import re
from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy import create_engine
import json
import psycopg2


import sys
sys.path.insert(0,"/var/www/CatalogApp/CatalogApp/")

Base = declarative_base()

DB_USER = json.loads(
    open('db_secrets.json', 'r').read())['database']['user']

DB_PASSWORD = json.loads(
    open('db_secrets.json', 'r').read())['database']['password']

DB_NAME = json.loads(
    open('db_secrets.json', 'r').read())['database']['name']

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    picture = Column(String(250))
    user_items = relationship("CategoryItem")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email
        }

    @validates('name')
    def validate_username(self, key, name):
        if not name:
            raise AssertionError('No username provided')
        if len(name) < 1 or len(name) > 20:
            raise AssertionError('Username must be '
                                 'between 5 and 40 characters')

        return name

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')
        if len(email) < 5 or len(email) > 254:
            raise AssertionError('Username must be '
                                 'between 5 and 254 characters')
        return email


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True, nullable=False)
    category_items = relationship("CategoryItem")
    __table_args__ = (
        CheckConstraint(
            name.expression != "JSON",
            name='category_name_cannot_be_JSON'
        ),
        {})

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if not self.category_items:
            return {
                'id': self.id,
                'name': self.name}
        else:
            return {
                'id': self.id,
                'name': self.name,
                'Item': [i.serialize for i in self.category_items]}

    @validates('name')
    def validate_category_name(self, key, name):
        if not name:
            raise AssertionError('No category name provided')
        if len(name) < 1 or len(name) > 20:
            raise AssertionError('Category name must be between'
                                 ' 5 and 40 characters')
        return name


class CategoryItem(Base):
    __tablename__ = 'category_item'

    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False)
    description = Column(String(250), nullable=False)
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates='category_items')
    back_populates = 'items'
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates='user_items')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'cat_id': self.cat_id,
            'description': self.description,
            'id': self.id,
            'title': self.title}

    @validates('title')
    def validate_item_name(self, key, title):
        if not title:
            raise AssertionError('No item title provided')
        if len(title) < 1 or len(title) > 40:
            raise AssertionError('Item title must be between'
                                 ' 5 and 40 characters')
        return title

    @validates('description')
    def validate_item_description(self, key, description):
        if not description:
            raise AssertionError('No item description provided')
        if len(description) < 1 or len(description) > 250:
            raise AssertionError('Item description must be between'
                                 ' 5 and 40 characters')
        return description


engine = create_engine(
    'postgresql://' + DB_USER + ':' + DB_PASSWORD + '@localhost:5432/' + DB_NAME)

Base.metadata.create_all(engine)
