# sc2teamparse
creating sc2 parser that works with larger teams


needed data:
[0].Title
[0].Players.APM
[0].Players.Result
[0].Players.PlayerID
[1].m_playerList.m_name(playerlist is in order of players)
[1].m_playerList.m_teamId(playerlist is in order of players)
[1].m_playerList.m_race(playerlist is in order of players)


used repos:
s2protocol (install from source)
https://github.com/Blizzard/s2protocol

python s2protocol/s2protocol/s2_cli.py --all --json {name}.SC2Replay > {name}.json

