 def move(n, a, b, c):
    if n==1:
        print (a + '-->' + c)
        return
    else:
        move(n-1,a,c,b)  #首先需要把 (N-1) 个圆盘移动到 b
        move(1,a,b,c)    #将a的最后一个圆盘移动到c
        move(n-1,b,a,c)  #再将b的(N-1)个圆http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html盘移动到c


if __name__ == "__main__":
    move(5, 'A', 'B', 'C')