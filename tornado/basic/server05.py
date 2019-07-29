import tornado.httpserver
import config

'''
手动创建服务器
tornado 的核心循环模块，封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
'''

'''
    用来定义options选项变量的方法
    name:必须保证其唯一性，否则会错
    default:设置选项变量的默认值，默认为None
    type: 设置选项变量的类型,从命令行或配置文件导入参数的时，tornado会根据类型的值进行转换连接输入的值
    如果default没设置，则不会进行转换
    multiple:设置选项变量是否可以为多个值，默认为False
    help:选项变量的帮助提示信息，一般不用
    
    
    
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
    httpServer.bind(config.options.port)

    # start(),默认开启一个进程，如果值大于0，创建对应个数的进程
    # 值为none或小于等于0，开启对应硬件机器cpu核心的进程数
    # app.listen(),只能在单进程模式中使用
    httpServer.start(1)

    # 每个子进程都会从父进程复制一份IOLoop的实例


    # IOLoop.current()：返
    tornado.ioloop.IOLoop.current().start()
