import socket
import sys
import time
import requests


# 从文件读取账号信息，并关闭文件
#此处直接运行可能会提示No such file or directory，但代码没有问题，直接进文件夹运行没有问题
fo = open('NTU_Account.txt','r',encoding="utf-8")
NTU_user = {
    'account': fo.readline()[0:-1],

    'password': fo.readline()[0:-1],

    'type': fo.readline()[0:-1]
}
fo.close()

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

#获取本地IP，并打印
ip = get_local_ip()
print('local ip:', ip, '\n')

url = 'http://210.29.79.141:801/eportal/?\
c=Portal&a=login&callback=dr1003&login_method=1&\
user_account=,0,' + NTU_user['account'] + NTU_user['type'] + \
      '&user_password=' + NTU_user['password'] + '&wlan_user_ip=' + ip + \
      '&wlan_user_ipv6=&wlan_user_mac=000000000000&\
wlan_ac_ip=&wlan_ac_name=ME60&jsVersion=3.3.2&v=8267'

response = requests.get(url)

if r'\u8ba4\u8bc1\u6210\u529f' in response.text:
    print('认证成功!')
elif r'"ret_code":2' in response.text:
    print('已认证!\n')
    for i in range(5):
        sys.stdout.write('{}'.format(5-i)+'秒后自动退出'+'\r')
        sys.stdout.flush()
        time.sleep(1)
elif r'UmFkOkxpbWl0IFVzZXJzIEVycg==' in response.text:
    print('警告：运营商终端超限!')
    input("\n\n按下 Enter 键后退出。")
else:
    print('错误！response = ', response.text)
    input("\n\n按下 Enter 键后退出。")

# print("当前路径 -  %s" %os.getcwd())
