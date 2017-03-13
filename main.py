import itchat
from itchat.content import *
import getWeather
import saveMsg
import getTuring

@itchat.msg_register(FRIENDS) # 收到好友邀请自动添加
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('小傻豹很高兴认识你哦~', msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    getMsg=msg['Text']
    fr=msg['FromUserName']
    saveMsg.saveMsg(fr,'user',getMsg)

    if getMsg=="天气":
        sendMsg=getWeather.getWeather(0)
        saveMsg.saveMsg(fr,'meme',sendMsg)
    else:
        sendMsg=getTuring.getTuring(getMsg) #图灵机器人
        saveMsg.saveMsg(fr,'meme',sendMsg)
    return sendMsg

	
# 启动
itchat.auto_login(True)
itchat.run()