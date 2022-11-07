import paramiko, time

def configura(host,user,passw,ip,netmask,interfaz):
    conexion = paramiko.SSHClient()
    conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conexion.connect(host, username=user, password=passw, look_for_keys=False, allow_agent=False)
    nueva_conexion = conexion.invoke_shell()
    nueva_conexion.send("configure terminal\n")
    time.sleep(0.2)
    nueva_conexion.send("ip route "+ip+" "+netmask+" "+interfaz+" \n")
    time.sleep(0.2)
    nueva_conexion.send("end\n")
    time.sleep(0.2)
    salida = str(nueva_conexion.recv(3000))
    conexion.close()

    return str(salida)