from fake_useragent import UserAgent
import httpx, base64, json, random;

useragents = UserAgent()
build_number = httpx.get(f'https://discord-user-api.cf/api/v1/properties/web').json()["client_build_number"]
languages = ['pr-AF', 'sw-AX', 'sq-AL', 'ar-DZ', 'en-AS', 'ca-AD', 'po-AO', 'en-AI', 'en-AG', 'gr-AR', 'hy-AM', 'nl-AW', 'en-AU', 'ba-AT', 'az-AZ', 'en-BS', 'ar-BH', 'be-BD', 'en-BB', 'be-BY', 'de-BE', 'en-BQ', 'bj-BZ', 'fr-BJ', 'en-BM', 'dz-BT', 'ay-BO', 'bo-BA', 'en-BW', 'no-BV', 'po-BR', 'en-IO', 'ms-BN', 'bu-BG', 'fr-BF', 'fr-BI', 'kh-KH', 'en-CM', 'en-CA', 'po-CV', 'en-KY', 'fr-CF', 'ar-TD', 'sp-CL', 'zh-CN', 'en-CX', 'en-CC', 'sp-CO', 'ar-KM', 'fr-CG', 'fr-CD', 'en-CK', 'sp-CR', 'fr-CI', 'hr-HR', 'sp-CU', 'en-CW', 'el-CY', 'ce-CZ', 'da-DK', 'ar-DJ', 'en-DM', 'sp-DO', 'sp-EC', 'ar-EG', 'sp-SV', 'fr-GQ', 'ar-ER', 'es-EE', 'am-ET', 'en-FK', 'da-FO', 'en-FJ', 'fi-FI', 'fr-FR', 'fr-GF', 'fr-PF', 'fr-TF', 'fr-GA', 'en-GM', 'ka-GE', 'de-DE', 'en-GH', 'en-GI', 'el-GR', 'ka-GL', 'en-GD', 'fr-GP', 'ch-GU', 'sp-GT', 'en-GG', 'fr-GN', 'po-GW', 'en-GY', 'fr-HT', 'en-HM', 'it-VA', 'sp-HN', 'en-HK', 'hu-HU', 'is-IS', 'en-IN', 'in-ID', 'fa-IR', 'ar-IQ', 'en-IE', 'en-IM', 'ar-IL', 'it-IT', 'en-JM', 'jp-JP', 'en-JE', 'ar-JO', 'ka-KZ', 'en-KE', 'en-KI', 'ko-KP', 'ko-KR', 'ar-KW', 'ki-KG', 'la-LA', 'la-LV', 'ar-LB', 'en-LS', 'en-LR', 'ar-LY', 'de-LI', 'li-LT', 'de-LU', 'po-MO', 'mk-MK', 'fr-MG', 'en-MW', 'en-MY', 'di-MV', 'fr-ML', 'en-MT', 'en-MH', 'fr-MQ', 'ar-MR', 'en-MU', 'fr-YT', 'sp-MX', 'en-FM', 'ro-MD', 'fr-MC', 'mo-MN', 'en-MS', 'ar-MA', 'po-MZ', 'my-MM', 'af-NA', 'en-NR', 'ne-NP', 'nl-NL', 'fr-NC', 'en-NZ', 'sp-NI', 'fr-NE', 'en-NG', 'en-NU', 'en-NF', 'ca-MP', 'nn-NO', 'ar-OM', 'en-PK', 'en-PW', 'ar-PS', 'sp-PA', 'en-PG', 'gr-PY', 'ay-PE', 'en-PH', 'en-PN', 'po-PL', 'po-PT', 'en-PR', 'ar-QA', 'fr-RE', 'ro-RO', 'ru-RU', 'en-RW', 'en-SH', 'en-KN', 'en-LC', 'fr-PM', 'en-VC', 'en-WS', 'it-SM', 'po-ST', 'ar-SA', 'fr-SN', 'cr-SC', 'en-SL', 'zh-SG', 'sl-SK', 'sl-SI', 'en-SB', 'ar-SO', 'en-SS', 'en-SX', 'af-ZA', 'en-GS', 'sp-ES', 'si-LK', 'ar-SD', 'nl-SR', 'no-SJ', 'en-SZ', 'sw-SE', 'fr-CH', 'ar-SY', 'zh-TW', 'ru-TJ', 'en-TZ', 'th-TH', 'po-TL', 'fr-TG', 'en-TK', 'en-TO', 'en-TT', 'ar-TN', 'tu-TR', 'ru-TM', 'en-TC', 'en-TV', 'en-UG', 'uk-UA', 'ar-AE', 'en-GB', 'en-US', 'en-UM', 'sp-UY', 'ru-UZ', 'bi-VU', 'sp-VE', 'vi-VN', 'en-VG', 'en-VI', 'fr-WF', 'be-EH', 'ar-YE', 'en-ZM', 'bw-ZW', 'sr-RS', 'cn-ME', 'sq-XK']
browsers = ['chrome', 'brave', 'baidu', 'ecosia', 'microsoft bing', 'yahoo', 'duckduckgo', 'ask.com']
def GenerateProperty():
    useragent = useragents.google; version = useragent.split('Chrome/')[1].split(' Safari')[0]
    print(f'Generated Chrome User Agent With The Version {version}')
    data = { "os":"Windows","browser":"Chrome","device":"","system_locale": random.choice(languages),"browser_user_agent": useragent,"browser_version":version,"os_version":random.choice(['7', '8', '10', '11', 'XP']),"referrer":"","referring_domain":"","search_engine":random.choice([browsers]),"referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number": build_number,"client_event_source": None}
    sample_string_bytes = json.dumps(data).encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(f'{base64_string[:45]}... | Saved Successfully In \' xsup.txt \'')

    with open('xsup.txt', 'a') as file:
        file.write(f'{base64_string}\n')

while True:
    GenerateProperty()