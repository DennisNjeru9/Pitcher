from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    '''
    Role class that defines all other different roles.
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'