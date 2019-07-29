import  tornado.web
import  tornado.ioloop
import  tornado.httpserver

'''
手动创建服务器
tornado 的核心循环模块，封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
'''

# 视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello ,tornado")


def method():
    pass

# tornado 默认启动的中一个进程，如何开启多个进程

if __name__ == "__main__":


    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    # 手动实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000);

    # bind()，绑定端口
    httpServer.bind(8000)

    # start(),默认开启一个进程，如果值大于0，创建对应个数的进程
    # 值为none或小于等于0，开启对应硬件机器cpu核心的进程数
    # app.listen(),只能在单进程模式中使用
    httpServer.start(5)

    # 每个子进程都会从父进程复制一份IOLoop的实例


    # IOLoop.current()：返
    tornado.ioloop.IOLoop.current().start()
