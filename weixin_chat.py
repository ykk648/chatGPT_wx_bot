# -- coding: utf-8 --
# @Time : 2022/12/7
# @Author : ykk648

from PyOfficeRobot.api.chat import wx
import time
from revChatGPT.revChatGPT import Chatbot

config = {
    # "email": "<YOUR_EMAIL>",
    # "password": "<YOUR_PASSWORD>"#,
    "session_token": ""    
    # "proxy": "<HTTP/HTTPS_PROXY>"
}

chatbot = Chatbot(config, conversation_id=None)

#智能闲聊
def chat_with_AI(who):
    wx.GetSessionList()  # 获取会话列表
    wx.ChatWith(who)  # 打开`who`聊天窗口
    temp_msg = ''
    while True:
        try:
            time.sleep(0.5)  #释放资源

            friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
            print(friend_name, receive_msg)
            if receive_msg[:6] == '!chat ':
                if receive_msg != temp_msg:
                    temp_msg = receive_msg
                    try:
                        answer = chatbot.get_chat_response(receive_msg[6:])['message']
                    except Exception as e:
                        print(e)
                    # answer = 'test'
                    wx.SendMsg(answer)  # 向`who`发送消息
        except:
            pass

if __name__ == '__main__':
    who = "小号群"  # 你好友名字
    chat_with_AI(who)   #智能闲聊

