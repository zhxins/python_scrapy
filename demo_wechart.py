import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': 'fcf04cb99fa1402683a45d61b8fa02c4',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)


def print_content(msg):
    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)


def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()
