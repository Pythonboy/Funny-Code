import itchat
import time
itchat.auto_login(hotReload = True);
boom_remark_name = input("请输入想要轰炸的人的微信备注");
message = input("请输入轰炸内容")
boom_obj = itchat.search_friends(remarkName = boom_remark_name)[0]['UserName'];
while True:
	time.sleep(1);
	itchat.send_msg(msg = message,toUserName = boom_obj);