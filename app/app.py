from flask import Flask

import conf_ospf , conf_rip, conf_static ,json

app = Flask(__name__)

with open('dispositivos.json','r') as f:
    ID_redes = json.load(f)
    host = ID_redes["HOST"]["ip"]
    user = ID_redes["HOST"]["user"]
    passw = ID_redes["HOST"]["password"]
    red_ip = ID_redes["RED"]["ip"]
    red_wild = ID_redes["RED"]["wild"]

@app.route('/')
def index():
    return "Flask"
    

@app.route('/ospf')
def confOSPF():
    red_ip2 = ID_redes["OSPF"]["ip"]
    red_wild2 =  ID_redes["OSPF"]["wild"]
    loop = ID_redes["OSPF"]["id"]
    hola = conf_ospf.configura(host,user,passw,red_ip,red_wild,red_ip2,red_wild2,loop)
    return hola

@app.route('/rip')
def confRIP():
    red_ip2 = ID_redes["RIP"]["ip"]
    hola = conf_rip.configura(host,user,passw,red_ip,red_ip2)
    return hola

@app.route('/static')
def confSTATIC():
    red_ip = ID_redes["STATIC"]["ip"]
    netmask = ID_redes["STATIC"]["netmask"]
    inter = ID_redes["STATIC"]["inter"]
    hola = conf_static.configura(host,user,passw,red_ip,netmask,inter)
    return hola


if __name__ == '__main__':
    app.run()