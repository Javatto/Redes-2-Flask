import paramiko, time

def configura(host,user,passw,ip1,ip2):
    conexion = paramiko.SSHClient()
    conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conexion.connect(host, username=user, password=passw, look_for_keys=False, allow_agent=False)
    nueva_conexion = conexion.invoke_shell()
    nueva_conexion.send("configure terminal\n")
    time.sleep(0.2)
    nueva_conexion.send("router rip\n")
    time.sleep(0.2)
    nueva_conexion.send("version 2\n")
    time.sleep(0.2)
    nueva_conexion.send("redistribute ospf 1 metric 1\n")
    time.sleep(0.2)
    nueva_conexion.send("network "+ip1+" \n")
    time.sleep(0.2)
    nueva_conexion.send("network "+ip2+" \n")
    time.sleep(0.2)
    nueva_conexion.send("end\n")
    time.sleep(0.2)
    salida = str(nueva_conexion.recv(3000))
    conexion.close()

    return str(salida)