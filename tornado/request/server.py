import  tornado.web
import  tornado.ioloop
'''
tornado 的核心循环模块，封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
'''

# 视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello ,tornado")


def method():
    pass



if __name__ == "__main__":
    # 实例化一个app应用对象,tornado 默认启动的中一个进程，如何开启多个进程
    # application 是tornado web框架的核心应用类，是与服务器对应的接口
    # 里面保存了路由映射表，有一个listen 方法，用来创建一个http服务器的实例
    # 并绑定了端口
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    # 绑定监听端口，此时服务器并没有开启监听
    app.listen(9000)
    # IOLoop.current()：返回当前IOLoop的实例
    # start()：启动IOLoop实例的I/O循环，同时开启监听
    tornado.ioloop.IOLoop.current().start()
