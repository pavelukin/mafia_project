from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mafia.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base=declarative_base()
Base.query = db_session.query_property()

class Game(Base):
    __tablename__ = 'Game'
    id = Column(Integer,primary_key=True)

class Role(Base):

    __tablename__ = 'Role'
    id_role = Column(Integer,primary_key=True)
    name = Column(String(140))
    description = Column(String(50))
    actions = Column(Text)

    def __init__(self, name = None, description = None, action = None):
        self.name = name
        self.decription = description
        self.action = action

    def __repr__(self):
        return '<Role {}, Description {}, Action {}>'.format(self.name,self.description,self.action)

class User(Base):
    __tablename__ = 'User'
    id_user = Column(Integer,primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    social_network = Column(Text)
    email = Column(Text)

    def __init__(self, name = None, surname = None, social_network = None, email = None):
        self.name = name
        self.surname = surname
        self.social_network = social_network
        self.email = email

    def __repr__(self):
        return '<Name {} {},Social Network {}, Email {}>'.format(self.name,self.surname,self.social_network,self.email)


class GameUser(Base):
    __tablename__ = 'GameUser'
    id_gameuser = Column(Integer,primary_key=True)
    id_game = Column(Integer, ForeignKey('Game.id'))
    id_user = Column(Integer, ForeignKey('User.id_user'))
    id_role = Column(Integer, ForeignKey('Role.id_role'))
    status = Column(Integer)

    def __init__(self, id_game = None, id_user = None, id_role = None, status = None):
        self.id_game = id_game
        self.id_user = id_user
        self.id_role = id_role
        self.status = status

    def __repr__(self):
        return '<Status {}>'.format(self.status)

class Night(Base):

    __tablename__ = 'Night'
    id_night = Column(Integer,primary_key=True)
    id_game = Column(Integer,ForeignKey('Game.id'))
    id_night_during_game = Column(Integer)

    def __init__(self, id_game = None, id_night_during_game = None):
        self.id_game = id_game
        self.id_night_during_game = id_night_during_game

    def __repr__(self):
        return '<Night during game {}>'.format(self.id_night_during_game)

class Election(Base):
    __tablename__ = 'Election'
    id_election = Column(Integer,primary_key=True)
    id_game = Column(Integer,ForeignKey('Game.id'))

    def __init__(self, id_game = None):
        self.id_game = id_game

class Action(Base):
    __tablename__ = 'Action'
    id_action = Column(Integer,primary_key=True)
    id_actor = Column(Integer,ForeignKey('GameUser.id_gameuser'))
    id_subject_of_action = Column(Integer,ForeignKey('GameUser.id_gameuser'))
    id_night = Column(Integer,ForeignKey('Night.id_night'))
    action = Column(String(140))
    status_before = Column(Integer)
    status_after = Column(Integer)

    def __init__(self, id_actor = None, id_subject_of_action = None, id_night = None, action = None, status_before = None, status_after = None):
        self.id_actor = id_actor
        self.id_subject_of_action = id_subject_of_action
        self.id_night = id_night
        self.action = action
        self.status_before = status_before
        self.status_after = status_after

class Vote(Base):
    __tablename__ = 'Vote'
    id_vote = Column(Integer,primary_key=True)
    id_election = Column(Integer, ForeignKey('Election.id_election'))
    id_voter = Column(Integer, ForeignKey('GameUser.id_gameuser'))
    id_pretender = Column(Integer, ForeignKey('GameUser.id_gameuser'))
    status_before = Column(Integer)
    status_after = Column(Integer)

    def __init__(self, id_election = None, id_voter = None, id_pretender = None, status_before = None, status_afetr = None):
        self.id_election = id_election
        self.id_voter = id_voter
        self.id_pretender = id_pretender
        self.status_after = status_afetr
        self.status_before = status_before






if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)



