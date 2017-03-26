import itchat
from itchat.content import *
import getWeather
import saveMsg
import getTuring
import getPowerRate

@itchat.msg_register(FRIENDS) # 收到好友邀请自动添加
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('小傻豹很高兴认识你哦~', msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    getMsg=msg['Text']
    fr=msg['FromUserName']
    friend=itchat.search_friends(userName=fr)
    filename=(friend['NickName']+'-'+fr) #以昵称+id进行记录文件命名
    saveMsg.saveMsg(filename,'user',getMsg)

    try:
    	if getMsg=="天气": #天气请求判断
    		sendMsg=getWeather.getWeather(0)
    	elif getPowerRate.judge(getMsg)!=0: #电费请求判断
    		sendMsg=getPowerRate.judge(getMsg)
    	else:
    		sendMsg=getTuring.getTuring(getMsg) #图灵机器人
    	saveMsg.saveMsg(filename,'meme',sendMsg)
    except:
    	sendMsg='小傻豹傻掉了'
    	saveMsg.saveMsg(filename,'meme',sendMsg)
    return sendMsg
	
# 启动
itchat.auto_login(True)
itchat.run()