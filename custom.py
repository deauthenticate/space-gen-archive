import os, httpx, websocket, base64, json, random, time, threading, ctypes, string, requests, sys, certifi, requests, hfuck
from concurrent.futures import ThreadPoolExecutor; from datetime import datetime; from colorama import Fore, Style
from base64 import b64encode; from random import randint;
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

with open('config.json') as config_file:config = json.load(config_file)
solved = 0; genned = 0; errors = 0; genStartTime = time.time(); f = open('input/proxies.txt', "r"); x = open('input/xsup.txt', "r")
ORIGIN_CIPHERS = ('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:' 'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')

def TitleWorkerr():
    global genned, solved, errors, verified
    if sys.platform != "linux" or sys.platform != "darwin":
        pass #ctypes.windll.kernel32.SetConsoleTitleW(f'[Space Generator v2 | {config["discord"]["invite_code"]}] | Generated : {genned} | Errors : {errors} | Solved : {solved} | Speed : {round(genned / ((time.time() - genStartTime) / 60))}/m')

class SSLContext(object):
    def GetContext():
        ciphers_top = "ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM"
        ciphers_mid = 'DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
        cl = ciphers_mid.split(":")
        cl_len = len(cl)
        els = []
        
        for i in range(cl_len):
            idx = randint(0, cl_len-1)
            els.append(cl[idx])
            del cl[idx]
            cl_len-=1
        
        ciphers2 = ciphers_top+":".join(els)
        context = httpx.create_ssl_context()
        context.load_verify_locations(cafile=certifi.where())
        context.set_alpn_protocols(["h2"])
        context.minimum_version.MAXIMUM_SUPPORTED
        CIPHERS = ciphers2
        context.set_ciphers(CIPHERS)
        
        ciphers2
    
    def GetTransport():
        return httpx.HTTPTransport(retries=3)

class DESAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        """
        A TransportAdapter that re-enables 3DES support in Requests.
        """
        CIPHERS = ORIGIN_CIPHERS.split(':')
        random.shuffle(CIPHERS)
        CIPHERS = ':'.join(CIPHERS)
        self.CIPHERS = CIPHERS + ':!aNULL:!eNULL:!MD5'
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)

class Logger:
    def CenterText(var:str, space:int=None): # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.LIGHTGREEN_EX}+{Fore.WHITE}) {text}')
        lock.release()
    
    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.RED}-{Fore.WHITE}) {text}')
        lock.release()
    
    def Question(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.YELLOW}?{Fore.WHITE}) {text}')
        lock.release()
    
    def Debug(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] [DEBUG] ({Fore.LIGHTBLUE_EX}*{Fore.WHITE}) {text}')
        lock.release()
    
    def Console():
        os.system('cls')
        text = """
        ╔═╗┌─┐┌─┐┌─┐┌─┐  ╔═╗┌─┐┌┐┌
        ╚═╗├─┘├─┤│  ├┤   ║ ╦├┤ │││
        ╚═╝┴  ┴ ┴└─┘└─┘  ╚═╝└─┘┘└┘
        """        
        faded = ''
        red = 40
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(Logger.CenterText(faded))

class Utils(object):
    @staticmethod
    def GenerateBornDate():
        year=str(random.randint(1997,2001));month=str(random.randint(1,12));day=str(random.randint(1,28))
        if len(month)==1:month='0'+month
        if len(day)==1:day='0'+day
        return year+'-'+month+'-'+day
    
    @staticmethod
    def RandomCharacter(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
    
    @staticmethod
    def GetUsername():
        type = config['discord']['username']
        
        if type == "real":
            usernames = open("input/usernames.txt", encoding="cp437").read().splitlines()
            return random.choice(usernames)
        elif type == "emojis":
            chars = ['🙂 ','🙃','🌹','🥀','🧛🏾','🧤','👕','🔫','💊','🅾','😺','😻','😾','😿','😹','😽','👾','😀','😃','😄','😁','😆','😅','😂','🤣','🥲','☺️','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🥸','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹️','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳','🥵','🥶','😱','😨','😰','😥','😓','🤗','🤔','🤭','🤫','🤥','😶','😐','😑','😬','🙄','😯','😦','😧','😮','😲','🥱','😴','🤤','😪','😵','🤐','🥴','🤢','🤮','🤧','😷','🤒','🤕','🤑','🤠','🔕','📣','📢','👁‍🗨','💬','💭','🗯','♠️','♣️','♥️','♦️','🃏','🎴','🀄️','🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛','🕜','🕝','🕞','🕟','🕠','🕡','🕢','🕣','🕤','🕥','🕦','🕧','⌛️','⏳','📡','🔋','🔌','💡','🔦','🕯','🪔','🧯','🛢','💸','💵','💴','💶','💷','🪙','💰','💳','💎','⚖️','🪜','🧰','🪛','🔧','🔨','⚒','🛠','⛏','🪚','🔩','⚙️','🪤','🧱','⛓','🧲','🔫','💣','🧨','🪓','🔪','🗡','⚔️','🛡','🚬','⚰️','🪦','⚱️','🏺','🔮','📿','🧿','💈','⚗️','🔭','🔬','🕳','🩹','🩺','💊','💉','🩸','🧬','🦠','🧫','🧪','🌡','🧹','🪠','🧺','🧻','🚽','🚰','🚿','🛁','🛀','🧼','🪥','🪒','🧽','🪣','🧴','🛎','🔑','🗝','🚪','🪑','🛋','🛏','🛌','🧸','🪆','🖼','🪞','🪟','🛍','🛒','🎁','🎈','🎏','🎀','🪄','🪅','🎊','🎉','🎎','🏮','🎐','🧧','✉️','📩','📨','📧','💌','📥','📤','📦','🏷','🪧','📪','📫','📬','📭','📮','📯','📜','📃','📄','📑','🧾','📊','📈','📉','🗒','🗓','📆','📅','🗑','📇','🗃','🗳','🗄','📋','📁','📂','🗂','🗞','📰','🐭','🐹','🐰','🦊','🐻','🐼','🐻‍❄️','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐔','🐧','🐦','🐤','🐣','🐥','🦆','🦅','🦉','🦇','🐺','🐗','🐴','🦄','🐝','🪱','🐛','🦋','🐌','🐞','🐜','🪰','🪲','🪳','🦟','🦗','🕷','🕸','🦂','🐢','🐍','🦎','🦖','🦕','🐙','🦑','🦐','🦞','🦀','🐡','🐠','🐟','🐬','🐳','🐋','🦈','🐊','🐅','🐆','🦓','🦍','🦧','🦣','🐘','🦛','🦏','🐪','🐫','🦒','🦘','🦬','🐃','🐂','🐄','🐎','🐖','🐏','🐑','🦙','🐐','🦌','🐕','🐩','🦮','🐕‍🦺','🐈','🐈‍⬛','🪶','🐓','🦃','🦤','🦚','🦜','🦢','🦩','🕊','🐇','🦝','🦨','🦡','🦫','🦦','🦥','🐁','🐀','🐿','🦔','🐾','🐉','🐲','🌵','🎄','🌲','🌳','🌴','🪵','🌱','🌿','☘️','🍀','🎍','🪴','🎋','🍃','🍂','🍁','🍄','🐚','🪨','🌾','💐','🌷','🌹','🥀','🌺','🌸','🌼','🌻','🌞','🌝','🌛','🌜','🌚','🌕','🌖','🌗','🌘','🌑','🌒','🌓','🌔','🌙','🌎','🌍','🌏','🪐','💫','⭐️','🌟','✨','⚡️','☄️','💥','🔥','🌪','🌈','☀️','🌤','⛅️','🌥','☁️','🌦','🌧','⛈','🌩','🌨','❄️','☃️','⛄️','🌬','💨','💧','💦','☔️','☂️','🌊','🌫','🍡','🍧','🍨','🍦','🥧','🧁','🍰','🎂','🍮','🍭','🍬','🍫','🍿','🍩','🍪','🌰','🥜','🍯','🥛','🍼','🫖','☕️','🍵','🧃','🥤','🧋','🍶','🍺','🍻','🥂','🍷','🥃','🍸','🍹','🧉','🍾','🧊','🥄','🍴','🍽','🥣','🥡','🥢','🧂','⚽️','🏀','🏈','⚾️','🥎','🎾','🏐','🏉','🥏','🎱','🪀','🏓','🏸','🏒','🏑','🥍','🏏','🪃','🥅','⛳️','🪁','🏹','🎣','🤿','🥊','🥋','🎽','🛹','🛼','🛷','⛸','🥌','🎿','⛷','🏂','🪂','🏋️‍♀️','🏋️','🏋️‍♂️','🤼‍♀️','🤼','🤼‍♂️','🤸‍♀️','🤸']
            return ''.join(random.choice(chars) for x in range (15))
        elif type == "binary":
            return ''.join(random.choice(["0", "1"]) for x in range (8)) + ' | .gg/spacex'
        elif type == "copyright":
            return Utils.RandomCharacter(5) + ' | spacex'
        elif type == "cards":
            joy =['🂡','🂢','🂣','🂤','🂦','🂧','🂨','🂩','🂪','🂫','🂬','🂭','🂮','🂱','🂲','🂳','🂴','🂵','🂶','🂷','🂸','🂺','🂻','🂼','🂽','🂾','🃁','🃂','🃃','🃄','🃅','🃆','🃇','🃈','🃉','🃊','🃋','🃌','🃍','🃎']
            return ''.join(random.choice(joy) for x in range (8)) + " | .gg/spacex"
        elif type == "arrows":
            arrow =['←','↑','→','↓','↚','↛','↜','↝','↞','↟','↠','↣','↫','↨','↧','↦','↥','↤','↬','↭','↯','↰','↱','↲','↴','↳','↵','↶','↷']
            return ''.join(random.choice(arrow) for x in range (8))+f" | .gg/spacex"
        elif type == "clown":
            clown =['°⧭°','🤡','<|-)=rr','〠','☛🤡☚','🎈🎪🎈','🐒','⚫']
            return ''.join(random.choice(clown) for x in range (6)) + f"  | .gg/spacex "
        elif type == "funny":
            funny =['ඞ','✡','☭','ॐ','♱','卐','ꖦ','卍','ᛋᛋ','☤','✙']
            return ''.join(random.choice(funny) for x in range (5)) + f" | .gg/spacex "
        elif type == "lag":
            lag =['﷽','꧅꧅','𒈙']
            return ''.join(random.choice(lag) for x in range (10))
        elif type == "china":
            chars =['溜','琉','留','硫','紐','類','六','燐','璘','藺','隣','鱗','戮','陸','崙','淪','輪','律','慄','栗','率','隆','利','吏','履','李','梨','泥','痢','罹','裏']
            return ''.join(random.choice(chars) for x in range (8))+f" | .gg/spacex"
        elif type == "allah":
            chars =['🇵🇰', "☪️️", "🕋", "🕌", "🤲", "🧕"]
            return ''.join(random.choice(chars) for x in range (6))+f" | .gg/spacex"
        else:
            return type + " " + Utils.RandomCharacter(4)
    
    @staticmethod
    def GetProxy():
        return random.choice(f.readlines()).strip()
    
    @staticmethod
    def GetSuper():
        return random.choice(x.readlines()).strip()
    
    @staticmethod
    def GetFormattedProxy(proxy):
        if '@' in proxy:
            return proxy
        elif len(proxy.split(':')) == 2:
            return proxy
        else:
            if '.' in proxy.split(':')[0]:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])

    @staticmethod
    def GetRandomGame():
        game = random.choice(['Minecraft', 'Rust', 'VRChat', 'reeeee', 'MORDHAU', 'Fortnite', 'Apex Legends', 'Escape from Tarkov', 'Rainbow Six Siege', 'Counter-Strike: Global Offense', 'Sinner: Sacrifice for Redemption', 'Minion Masters', 'King of the Hat', 'Bad North', 'Moonlighter', 'Frostpunk', 'Starbound', 'Masters of Anima', 'Celeste', 'Dead Cells', 'CrossCode', 'Omensight', 'Into the Breach', 'Battle Chasers: Nightwar', 'Red Faction Guerrilla Re-Mars-tered Edition', 'Spellforce 3', 'This is the Police 2', 'Hollow Knight', 'Subnautica', 'The Banner Saga 3', 'Pillars of Eternity II: Deadfire', 'This War of Mine', 'Last Day of June', 'Ticket to Ride', 'RollerCoaster Tycoon 2: Triple Thrill Pack', '140', 'Shadow Tactics: Blades of the Shogun', 'Pony Island', 'Lost Horizon', 'Metro: Last Light Redux', 'Unleash', 'Guacamelee! Super Turbo Championship Edition', 'Brutal Legend', 'Psychonauts', 'The End Is Nigh', 'Seasons After Fall', 'SOMA', 'Trine 2: Complete Story', 'Trine 3: The Artifacts of Power', 'Trine Enchanted Edition', 'Slime-San', 'The Inner World', 'Bridge Constructor', 'Bridge Constructor Medieval', 'Dead Age', 'Risk of Rain', "Wasteland 2: Director's Cut", 'The Metronomicon: Slay The Dance Floor', 'TowerFall Ascension + Expansion', 'Nidhogg', 'System Shock: Enhanced Edition', 'System Shock 2', "Oddworld:New 'n' Tasty!", 'Out of the Park Baseball 18', 'Hob', 'Destiny 2', 'Torchlight', 'Torchlight 2', 'INSIDE', 'LIMBO', "Monaco: What's Yours Is Mine", 'Tooth and Tail', 'Dandara', 'GoNNER', 'Kathy Rain', 'Kingdom: Classic', 'Kingdom: New Lands', 'Tormentor X Punisher', 'Chaos Reborn', 'Ashes of the Singularity: Escalation', 'Galactic Civilizations III', 'Super Meat Boy', 'Super Hexagon', 'de Blob 2', 'Darksiders II Deathinitive Edition', 'Darksiders Warmastered Edition', 'de Blob', 'Red Faction 1', 'Dungeon Defenders'])
        return { "name": game, "type": 0 }

class CreateWebsocket(object):
    def __init__(self, token:str):
        if config["websocket"]["connect"]:
                try:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    ws.send(json.dumps({'op': 2, 'd': {'token': token, 'capabilities': 61, 'properties': {'os': 'Windows', 'browser': 'Chrome', 'device': '',  'system_locale': 'en-GB', 'browser_user_agent': config['discord']['useragent'], 'browser_version': '106', 'os_version': '10', 'referrer': '', 'referring_domain': '', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': '85108', 'client_event_source': 'null'}, 'presence': {'status': random.choice(['online', 'dnd', 'idle']), 'game': Utils.GetRandomGame(), 'since': 0, 'activities': [], 'afk': False}, 'compress': False, 'client_state': {'guild_hashes': {}, 'highest_last_message_id': '0', 'read_state_version': 0, 'user_guild_settings_version': -1}}}))

                    if config["spammer"]["vc_spammer"]:
                            ws.send(json.dumps({"op": 4,  "d": {"guild_id": config["spammer"]["guildid"], "channel_id": config["spammer"]["channelid"], "self_mute": True,"self_deaf": False, "self_stream?": config["spammer"]["stream"], "self_video": config["spammer"]["video"] }}))
                            ws.send(json.dumps({"op": 18, "d": {"type": "guild", "guild_id": config["spammer"]["guildid"], "channel_id": config["spammer"]["channelid"], "preferred_region": "singapore" }}))
                            ws.send(json.dumps({"op": 1,  "d": None }))
                except Exception as e:
                    pass

class SolveCaptcha(object):
    def init(proxy, site_url, site_key):
        global solved
        started_on = time.time()
        captcha_key = hfuck.Solver(proxy, site_key, site_url).solve_captcha()
        #captcha_key = httpx.get(f'http://95.216.45.162:6565/solve?proxy={proxy}',  headers={'user-agent': 'NowonSender 3.0.0 / Python', 'connection': 'keep-alive'}, timeout=None).json()['token']
        if "P1_" in captcha_key:
            solved += 1
            TitleWorkerr()
            Logger.Debug(f"Solved hCaptcha : {captcha_key.replace('P1_', 'F1_')[:40]}... ({round(time.time() - started_on)} secs)")
            return captcha_key.replace("P1_", "F1_")
        else:
            return False


def GenerateToken(key, proxy, thread_id):
    try:
        global genned, solved, errors, verified

        client = requests.session()
        client.mount('https://', DESAdapter())

        response = client.get("https://discord.com/api/v9/experiments", proxies={ "http": f"http://{proxy}", "https": f"http://{proxy}" })

        registerheaders  = {
                'Host': 'discord.com', 'Connection': 'keep-alive',
                'sec-ch-ua': '"Chromium";v="93", " Not A;Brand";v="99", "Google Chrome";v="93"',
                'X-Super-Properties': Utils.GetSuper(),
                'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',
                "User-Agent": config['discord']['useragent'],
                'Content-Type': 'application/json', 'Authorization': 'undefined',
                'Accept': '*/*', 'Origin': 'https://discord.com',
                'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register',
                'X-Debug-Options': 'bugReporterEnabled',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cookie': 'OptanonConsent=version=6.17.0; locale=th'
        }

        account_username = Utils.GetUsername()
        
        email = Utils.RandomCharacter(8)+"@gmail.com"

        payload = {
            'fingerprint': response.json()['fingerprint'], 
            'email': email, 
            'username': account_username, 
            'password': Utils.RandomCharacter(8), 
            'invite': config['discord']['invite_code'],
            'consent': True,
            'date_of_birth': Utils.GenerateBornDate(), 
            "gift_code_sku_id": None,
            "captcha_key": key, 
            "promotional_email_opt_in": True
        }

        response = client.post('https://discord.com/api/v10/auth/register', headers=registerheaders, json=payload, timeout=20, proxies={ "http": f"http://{proxy}", "https": f"http://{proxy}" })

        if response.status_code == 201:
            token = response.json()['token']
            Logger.Success(f"Created Token : {token}")
            genned = genned + 1
            file = open(f'output/{config["discord"]["invite_code"]}.txt', 'a')
            file.write(f'{token}\n')
            TitleWorkerr()
            
            CreateWebsocket(token)
            
        else:
            TitleWorkerr()
            if 'captcha' in response.text:
                errors = errors + 1
                Logger.Error('Invalid Captcha Response, Retrying...')
            else:
                errors = errors + 1
                Logger.Error(response.json())
    except Exception as e:
        TitleWorkerr()
        errors = errors + 1
        Logger.Error(e )
        print(e.__traceback__.tb_lineno)


def StartThread(thread_id, solver_address=None):
    while True:
        try:
            proxy =  Utils.GetProxy()
            proxy_raw = proxy
            proxy_formated = Utils.GetFormattedProxy(proxy_raw)
            key = SolveCaptcha.init(proxy_formated, "https://discord.com/register" , "4c672d35-0701-42b2-88c3-78380b0db560")

            if key != False and key != 0 and key !="0":
                threading.Thread(target=GenerateToken,args=[key,proxy_formated,thread_id] ).start()

        except Exception as e:
            Logger.Error(f'{e} | {e.__traceback__.tb_lineno} | {e.__traceback__.tb_frame} | {e.__traceback__.tb_lasti}')

def StartGenerator():
    global threads
    
    try:
        Logger.Console()
        Logger.Question("How many threads do you want ? ")
        threads = int(input(''))
    except:
        Logger.Error("Please enter a valid number")
        os._exit(1)

        
    with ThreadPoolExecutor(max_workers=threads) as exe:
        for x in range(threads):
            exe.map(StartThread,[x])

StartGenerator()