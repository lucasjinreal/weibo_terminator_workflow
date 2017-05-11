# -*- coding: utf-8 -*-
# file: scrap.py
# author: JinTian
# time: 10/05/2017 10:38 PM
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
from scraper.weibo_scraper import WeiBoScraper
from utils.cookies import get_cookie_from_network
from settings.config import *
import pickle
from settings.accounts import accounts


def set_accounts_cookies():
    if os.path.exists(COOKIES_SAVE_PATH):
        pass
    else:
        for account in accounts:
            print('preparing cookies for account {}'.format(account))
            get_cookie_from_network(account['id'], account['password'])
        print('all accounts getting cookies finished. starting scrap..')


def get_account_cookies(account):
    """
    get account cookies
    :return:
    """
    try:
        with open(COOKIES_SAVE_PATH, 'rb') as f:
            cookies_dict = pickle.load(f)
        print('cookies dict: ', cookies_dict)
        return cookies_dict[account]
    except Exception as e:
        print(e)
        print('error, not find cookies file.')
        return None


def scrap(scrap_id):
    """
    scrap a single id
    :return:
    """
    set_accounts_cookies()
    account_id = accounts[0]['id']

    cookies = get_account_cookies(account_id)
    scraper = WeiBoScraper(account_id, scrap_id, cookies)
    scraper.crawl()


def main(args):
    scrap_id = args
    scrap(scrap_id)
