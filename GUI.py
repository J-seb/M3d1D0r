import serial.tools.list_ports as lpuertos

# Búsqueda de puertos
ports = lpuertos.comports()
arport = 'None'
ncon = len(ports)

for p in range(0, ncon):
    puerto = ports[p]
    strpuerto = str(puerto)
    if 'Arduino' in strpuerto:
        p = strpuerto.split(' ')
        arport = p[0]
        print(arport)