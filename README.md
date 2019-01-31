# sc2teamparse
creating sc2 parser that works with larger teams


used repos:
s2protocol (install from source)
https://github.com/Blizzard/s2protocol

python s2protocol/s2protocol/s2_cli.py --all --json {name}.SC2Replay > {name}.json



## Database
| Game     | Player   | Team    | Player_team |
|----------|----------|---------|-------------|
| id       | id       | id      | id          |
| duration | Username | Game_id | Player_id   |
| title    |          |         | Team_id     |
| date     |          |         | Race        |
|          |          |         | APM         |
|          |          |         |             |
|          |          |         |             |
|          |          |         |             |
|          |          |         |             |
|          |          |         |             |