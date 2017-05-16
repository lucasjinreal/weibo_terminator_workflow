# -*- coding: utf-8 -*-
# file: weibo_scraper_m.py
# author: JinTian
# time: 16/05/2017 11:32 AM
# Copyright 2017 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
"""
this is another option for WeiBo scraper, using domain:
http://m.weibo.cn

this scraper under development, welcome submit PR to add more features
"""
import os
import requests
import numpy as np
from settings.config import *
import pickle


class WeiBoScraperM(object):
    """
    this scraper under construct, contributor can follow this template to compatible WeiBoScraper API
    """

    def __init__(self, using_account, scrap_id, cookies, filter_flag=0):
        self.using_account = using_account
        self.scrap_id = scrap_id
        self.cookies = cookies
        self.filter_flag = filter_flag

    def _init_cookies(self):
        cookie = {
            "Cookie": self.cookies
        }
        self.cookie = cookie

    def _init_headers(self):
        """
        avoid span
        :return:
        """
        headers = requests.utils.default_headers()
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0'
        }
        headers.update(user_agent)
        print('headers: ', headers)
        self.headers = headers

    def jump_scraped_id(self):
        """
        check mark scrapd ids, jump scraped one.
        :return:
        """
        if os.path.exists(SCRAPED_MARK):
            with open(SCRAPED_MARK, 'rb') as f:
                scraped_ids = pickle.load(f)
            if self.scrap_id in scraped_ids:
                return True
            else:
                return False
        else:
            return False

    def crawl(self):
        if self.jump_scraped_id():
            print('scrap id {} already scraped, directly pass it.'.format(self.scrap_id))
        else:
            try:
                self._get_html()
                self._get_user_name()
                self._get_user_info()

                self._get_fans_ids()
                self._get_wb_content()
                self._get_wb_content_and_comment()
                return True
            except Exception as e:
                print('error when crawl: ', e)
                return False

    def _get_html(self):
        pass

    def _get_user_name(self):
        pass

    def _get_user_info(self):
        pass

    def _get_fans_ids(self):
        pass

    def _get_wb_content(self):
        pass

    def _save_content(self, page):
        pass

    def _get_wb_content_and_comment(self):
       pass

    def _save_content_and_comment(self, i, one_content_and_comment, weibo_detail_urls):
       pass

    def switch_account(self, new_account):
        assert new_account.isinstance(str), 'account must be string'
        self.using_account = new_account

    @staticmethod
    def mark_as_scraped(scrap_id):
        """
        this will mark an id to be scraped, next time will jump this id directly
        :return:
        """
        scraped_ids = []
        if os.path.exists(SCRAPED_MARK):
            with open(SCRAPED_MARK, 'rb') as f:
                scraped_ids = pickle.load(f)
        scraped_ids.append(scrap_id)
        with open(SCRAPED_MARK, 'wb') as f:
            pickle.dump(scraped_ids, f)
        print('scrap id {} marked as scraped, next time will jump this id directly.'.format(scrap_id))