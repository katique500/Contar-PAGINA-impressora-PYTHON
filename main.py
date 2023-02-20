#import smb
from smb.SMBConnection import SMBConnection

# informações da impressora
ip = "192.168.1.95"  # endereço IP da impressora
printer_share = "imp_ti"  # nome do compartilhamento da impressora

# informações de autenticação
username = "Kaique"
password = "sql@123"
domain = "Administrador"

# se conectar à impressora
conn = SMBConnection(username, password, "pysmb-test", ip, domain=domain)
conn.connect(ip, 139)

# enviar comando para obter contagem de impressão
printer_name = f"\\\\{ip}\\{printer_share}"
data, _ = conn.readData(printer_name, "Printer-Get-Printer-Data", "\x06\x00\x00\x00")
count = int.from_bytes(data[8:12], byteorder="little")

# desconectar da impressora
conn.close()

print(f"Contagem de impressão: {count}")