from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import json

bbx_options = Options()
bbx_options.add_argument('--headless')
bbx_options.add_argument('--disable-gpu')

#直接启动浏览器
driver = webdriver.Chrome(chrome_options=bbx_options)
driver.get("https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp2%2Fsys%2FlwReportEpidemicSeu%2Findex.do%3Ft_s%3D1583654871073%23%2FdailyReport")
sleep(10)

#打开账户信息文件并键入后点击登入
try:
    with open("C:/Users/xiang/Desktop/auto_clockin/config.json",encoding='utf-8') as account:
        config=json.load(account)
except:
    print("账户文件错误！请检查是否与.py文件放置于同一目录下或账户文件是否填写出错！")
else:
    elem_num = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[4]/div/form/p[1]/input")
    elem_num.send_keys(config["number"])
    elem_pwd = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[4]/div/form/p[2]/input[1]")
    elem_pwd.send_keys(config["password"])
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[4]/div/form/p[5]/button").click()
sleep(10)

#点击新增                     
driver.find_element_by_xpath("/html/body/main/article/section/div[2]/div[1]").click()
sleep(10)

#输入体温
elem_tem = driver.find_element_by_name("DZ_JSDTCJTW")
elem_tem.send_keys(config["temperature"])

#点击保存
driver.find_element_by_id("save").click()
sleep(10)

#点击确认
driver.find_element_by_xpath("/html/body/div[59]/div[1]/div[1]/div[2]/div[2]/a[1]").click()
print("打卡成功")
sleep(5)
driver.quit()
