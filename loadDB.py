import subprocess
import os
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
#from sqlalchemy import CreateView
Base = declarative_base()
class Game(Base):
    __tablename__ = "game"
    
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(50))
    duration = Column('duration', Integer)
    uploadDate = Column('date', DateTime)

class Team(Base):
    __tablename__ = "team"
    
    id = Column('id', Integer, primary_key=True)
    gameId = Column('gameId', Integer, ForeignKey(Game.id))

class Player(Base):
    __tablename__ = "player"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50))
    result = Column('result', String(50))
    race = Column('race', String(50))
    discordName = Column('discordName', String(200))
    teamId = Column('teamId', Integer, ForeignKey(Team.id))

engine = create_engine('sqlite:///sc2db.db', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
#createview = CreateView('PlayerDetail', t.select().where(player.teamid == team.id AND team.gameId == game.id)
def getNewGameID():#gets most recently created game ID
    games = session.query(Game).all()
    t = 0
    for g in games:
        if g.id > t:
            t = g.id
    return t
def getNewTeamID():#get most recently created team ID
    teams = session.query(Team).all()
    t = 0
    for g in teams:
        if g.id > t:
            t = g.id
    return t

for f in os.listdir("sc2Replays"):
    f = "sc2Replays/" + f 
    j = subprocess.check_output(['python','s2protocol/s2protocol/s2_cli.py',"--all","--ndjson",f]).split("\n")
    n0 = json.loads(j[0])
    n1 = json.loads(j[1])
    players = []
    game = Game()#creates game 
    game.duration = n0['Duration']
    game.title = n0['Title']
    game.uploadDate = datetime.now()
    session.add(game)
    session.commit()
    gameid = getNewGameID()#gets the auto increment game id for use in team
    teamids = []#this stores the id's in relation to the database
    teamList = []#this stores the id's in relation to the json file
    fPlayerList = n0['Players']
    z = 0
    for player in n1['m_playerList']:
        tid = player['m_teamId']
        
        fPlayer = fPlayerList[z]#this gets player from earlier iteration of the players in JSON 
        print fPlayer
        print player
        if tid not in teamList:#check to see if there has been a team created in the database for this player
            teamList.append(tid)
            team = Team()
            team.gameId = gameid
            session.add(team)#creates team in database tied to game
            session.commit()
            teamids.append(getNewTeamID())
        nplayer = Player()
        nplayer.teamId = teamids[tid]#accesses the team id from the database
        nplayer.result = fPlayer['Result'] 
        nplayer.race = player['m_race']
        nplayer.username = list(reversed(player['m_name'].split("<sp/>")))[0]#removes clan tags
        nplayer.apm = fPlayer['APM']
        session.add(nplayer)
        session.commit()
        z = z + 1
    print(n0['Title'] + ' uploaded')
session.close()
    
