import subprocess
import os
import json
for f in os.listdir("sc2Replays"):
    f = "sc2Replays/" + f 
    j = subprocess.check_output(['python','s2protocol/s2protocol/s2_cli.py',"--all","--ndjson",f]).split("\n")
    n0 = json.loads(j[0])
    n1 = json.loads(j[1])
    n2 = json.loads(j[2])
    i = 0
    players = []
    print n0['Title']
    print n0['Duration']
    for player in n0['Players']:
        print player['APM']
    for player in n1['m_playerList']:
        print player['m_result']
        print player['m_race']
        print player['m_name']
        print player['m_teamId']