# 南通大学校园网一键认证

## 使用说明

NTU_In为登录脚本，需要"NTU_Account.txt"填写正确  
NTU_Out为注销脚本，与"NTU_Account.txt"无关  

关于实现原理这篇文章写的很详细[点赞👍]:
[校园网自动登录全平台解决方案 - ourongxing的文章 - 知乎](https://zhuanlan.zhihu.com/p/364016452)

### 注意：
1. 第一次使用前需要打开"NTU_Account.txt"，按照提示填入账号信息
2. 文件名保持为"NTU_Account.txt"不要修改
3. 确保"NTU_In"和"NTU_Account.txt"在同一文件夹内


### 关于开机自启，自动登录：

为登录脚本创建快捷方式，并将快捷方式移动到一下两个路径之一即可实现开机自动登录到校园网（建议路径一）  
- 路径一：  
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup  
- 路径二：  
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup  


### 声明
- 本人小白，Python仅为业余爱好
- 本脚本仅供学习交流，请勿用于商业及非法用途，因此产生法律纠纷与本人无关
