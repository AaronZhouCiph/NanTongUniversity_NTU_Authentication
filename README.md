# NTU_Login
南通大学校园网一键认证


# 使用说明

NTU_In.exe为登录脚本，需要"NTU_Account.txt"填写正确  
NTU_Out.exe为注销脚本，与"NTU_Account.txt"无关  


### 注意：
1. 第一次使用前需要打开"NTU_Account.txt"，按照提示填入账号信息
2. 文件名保持为"NTU_Account.txt"不要修改
3. 确保"NTU_In.exe"和"NTU_Account.txt"在同一文件夹内


### 关于开机自启，自动登录：

为登录脚本创建快捷方式，并将快捷方式移动到一下两个路径之一即可（建议路径一）  
- 路径一：  
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup  
- 路径二：  
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup  
