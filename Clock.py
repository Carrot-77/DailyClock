from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

import json, time
import logging
import os
import SendMail
import Log


mylog = Log.Log()

def get_user(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    return data

class Login:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(120)

        # 邮箱初始化
        self.mail_server = SendMail.SendMail()


    def run(self, name, passwd, email):
        try:
            self.driver.get('http://one.hrbeu.edu.cn/taskcenter/workflow/index')
            time.sleep(2)

            # 输入账号密码
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
            # 登录
            self.driver.find_element_by_xpath('//*[@id="login-submit"]').click()
            time.sleep(2)

            # 进入打卡界面
            self.driver.get('http://one.hrbeu.edu.cn/infoplus/form/JKXXSB/start')
            time.sleep(5)

            # 确认打卡
            self.driver.find_element_by_xpath('//*[@id="V1_CTRL82"]').click()
            self.driver.find_element_by_class_name('command_button_content').click()
            time.sleep(1)

            # 两次弹窗确认
            self.driver.find_element_by_xpath('//*[@class="dialog_button default fr"]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@class="dialog_button default fr"]').click()
            time.sleep(2)

            # 写入日志
            mylog.info_log('{}已打卡'.format(name))
        except:
            # 写入错误日志
            mylog.info_err('{}打卡失败'.format(name))

            # 失败则发送邮箱
            self.mail_server.sendmail(email)

    def destroy(self):
        self.driver.close()
        time.sleep(1)
        self.driver.quit()
        self.mail_server.destroy()


if __name__ == '__main__':
    filename = '/home/carrot/DailyClock/data/data.json'
    data_msg  = get_user(filename)

    for every in data_msg:
        log_user = Login()
        name = every['user']
        passwd = every['passwd']
        email = every['email']
        log_user.run(name, passwd, email)
        log_user.destroy()

