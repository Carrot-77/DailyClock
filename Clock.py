from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

import json, time
import logging
import os
import SendMail

def get_user(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    # name = data[0]['user']
    # passwd = data[0]['passwd']
    return data

class Login:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(120)

        self.today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        self.log_name = "./clock.log"
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(logging.DEBUG)

        log_path = os.path.dirname(os.path.abspath(__file__))
        logname = log_path + '/' + 'clock.log'  # 指定输出的日志文件名

        fh = logging.FileHandler(logname, mode='a', encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        self.mail_server = SendMail.SendMail()

    def info_log(self, msg):
        self.logger.info(msg)

    def run(self, name, passwd, email):
        self.driver.get('http://one.hrbeu.edu.cn/taskcenter/workflow/index')
        time.sleep(2)

        # 输入账号密码
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
        # 登录
        self.driver.find_element_by_xpath('//*[@id="fm1"]/li[4]/input[4]').click()
        time.sleep(2)

        # 进入打卡界面
        self.driver.get('http://one.hrbeu.edu.cn/infoplus/form/JKXXSB/start')
        time.sleep(10)

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
        self.info_log('{}已打卡'.format(name))

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

