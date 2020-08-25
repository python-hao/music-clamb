#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： XHao
# datetime： 2020/7/2 14:05 
# ide： PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
import time
class music_163():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
    def get_html(self):
        self.song_name = "笑看风云"

        self.url = r"https://music.163.com/search/#/m/?s={}&type=1".format(self.song_name)
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(r'D:\Google\Google\Chrome\Application\chromedriver.exe',chrome_options=option)
        time.sleep(1)
        s = requests.session()
        self.html = s.get(self.url).content

        print(self.html)

    def get_song_id(self):
        # self.driver.switch_to.frame('g_iframe')
        # 返回主界面
        # self.driver.switch_to_default_content()
        self.soup = BeautifulSoup(self.html,'html5lib')
        self.elems = self.soup.find('div',id='m-search')
        self.elem1 = self.driver.find_element_by_class_name("srchsongst")
        self.elems = self.elem1.find_elements_by_class_name("item f-cb h-flag ")
        # self.names[]
        for self.elem in self.elems:
            self.name = self.elem.find_element_by_class_name("hd").get_attribute('id')
            self.song_id = self.name.split('_', 1)[1]
            print(self.song_id)
    def run(self):
        self.get_html()
        # self.get_song_id()

if __name__ == '__main__':
    music_163 = music_163()
    music_163.run()
