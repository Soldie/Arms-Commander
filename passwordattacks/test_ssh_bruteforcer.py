import password_toolkits

username_list = '/root/Documents/basic_username_list'
password_list = '/root/Documents/25-worst-passwords'
ip_list = '/root/Documents/IPwordlist_ftp'
protocol = 'ftp'

password_toolkits.hydra_ip_list(username_list, password_list, ip_list, protocol)
