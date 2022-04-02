import socket
import requests


def get_local_ip():
    """ 
    函数名：get_local_ip 
    返回本地IP
    来源：https://zhuanlan.zhihu.com/p/364016452
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


ip = get_local_ip()

print('local ip:',ip,'\n')

url = 'http://210.29.79.141:801/eportal/?\
c=Portal&a=logout&callback=dr1003&\
login_method=1&user_account=drcom&\
user_password=123&ac_logout=0&register_mode=1&\
wlan_user_ip='+ip+'&wlan_user_ipv6=&\
wlan_vlan_id=0&wlan_user_mac=000000000000&\
wlan_ac_ip=&wlan_ac_name=ME60&jsVersion=3.3.2&v=3400'

# print('url=',url,'\n')

response = requests.get(url)


if r'\u6ce8\u9500\u6210\u529f' in response.text:
    print('注销成功!')
elif r'\u6ce8\u9500\u5931\u8d25' in response.text:
    print('已注销!')
    input("\n\n按下 enter 键后退出。")
else:
    print('错误！response = ',response.text)
    input("\n\n按下 enter 键后退出。")
