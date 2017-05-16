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


def init_accounts_cookies():
    if os.path.exists(COOKIES_SAVE_PATH):
        with open(COOKIES_SAVE_PATH, 'rb') as f:
            cookies_dict = pickle.load(f)
        return list(cookies_dict.keys())
    else:
        for account in accounts:
            print('preparing cookies for account {}'.format(account))
            get_cookie_from_network(account['id'], account['password'])
        print('checking account validation...')
        valid_accounts = get_valid_accounts()

        if len(valid_accounts) == len(accounts):
            print('all accounts checked valid... start scrap')
            return valid_accounts
        elif len(valid_accounts) < 1:
            print('error, not find valid accounts, please check accounts.')
            exit(0)
        elif len(valid_accounts) > 1:
            print('find valid accounts: ', valid_accounts)
            print('starting scrap..')
            return valid_accounts


def get_valid_accounts():
    with open(COOKIES_SAVE_PATH, 'rb') as f:
        cookies_dict = pickle.load(f)
    return list(cookies_dict.keys())


def get_cookies_by_account(account_id):
    with open(COOKIES_SAVE_PATH, 'rb') as f:
        cookies_dict = pickle.load(f)
    return cookies_dict[account_id]


def scrap(scrap_id):
    """
    scrap a single id
    :return:
    """
    valid_accounts = init_accounts_cookies()
    print('valid accounts: ', valid_accounts)

    # TODO currently only using single account, multi accounts using multi thread maybe quicker but seems like a mess
    # TODO maybe will adding multi thread feature when our code comes steady
    # so that maybe need to manually change accounts when one account being baned
    account_id = valid_accounts[0]
    print('using accounts: ', account_id)

    cookies = get_cookies_by_account(account_id)

    # alternative this scraper can changed into WeiBoScraperM in the future which scrap from http://m.weibo.cn
    scraper = WeiBoScraper(account_id, scrap_id, cookies)
    scraper.crawl()


def main(args):
    scrap_id = args
    scrap(scrap_id)
