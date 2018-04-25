from selenium import webdriver

# 中途夭折，驱动不对应
def baidutest():
    browser = webdriver.Chrome(r"C:\Users\Administrator\Desktop\chromedriver_win32\chromedriver.exe")
    browser.get("https://www.baidu.com/")


if __name__ == "__main__":
    baidutest()