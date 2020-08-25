#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： XHao
# datetime： 2020/7/3 20:59 
# ide： PyCharm
import requests
from lxml import etree

class Music_163():
    def __init__(self):
        self.music_name = '难念的经'
        self.url = 'https://music.163.com/#/search/m/?%23%2Fdiscover=&s={}&type=1'.format(self.music_name)
        self.get_music()

    def get_music(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
        response = requests.get(url=self.url,headers=self.headers)
        html = etree.HTML(response.text)
        self.id_list = html.xpath(r'//a[contains(@href,"/song?")]')
        print(self.id_list)

    def get_music_id(self):
        for data in self.id_list:
            href = data.xpath(r'./@href')[0]
            self.music_id = href.split('=')[1]
            self.music_name = data.xpath(r'./text()')[0]
            print(self.music_id,self.music_name)

            self.base_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(self.music_id)
            self.music_url = self.base_url + self.music_id
            self.music = requests.get(url=self.music_url,headers=self.headers)
            self.path = r'./music/{}.mp3'.format(self.music_name)
            with open(self.path,'wb') as f:
                f.write(self.music.content)
            print('<<{}>>下载完成。。。。'.format(self.music_name))


if __name__ == '__main__':
    Music_163()