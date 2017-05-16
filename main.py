# -*- coding: utf-8 -*-
# file: main.py
# author: JinTian
# time: 13/04/2017 10:01 AM
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
weibo_terminator_workflow

run main.py will do:
1. first run will scrap distribute ids, every id finished all task will mark as done.
2. after all distribute ids were done, will scrap all fans id.

"""
import argparse

from core.dispatch_center import Dispatcher
from settings.config import *
from utils.string import is_valid_id
from core.scrap import scrap
import sys
import pickle


def mission(distribute_uuid=None):
    """
    mission for workflow.
    this method is very simple.
    for the first run, it will scrap distribute ids. you just get distribute_uuid from wechat
    `jintianiloveu` who is administrator of this project. get your uuid and paste it into mission param


    this will get 2-5 ids from distribute_ids.pkl, every uuid got ids are different.
    After mission complete scrap, continue scrap fans_ids.pkl which contains many many ids. as possiable as you
    can to scrap those fans ids.
    :return:
    """
    #scrap('3879293449')
    if os.path.exists(DISTRIBUTE_IDS):
        print('find distribute ids from {}'.format(DISTRIBUTE_IDS))
        with open(DISTRIBUTE_IDS, 'rb') as f:
            distribute_dict = pickle.load(f)
        if os.path.exists(SCRAPED_MARK):
            finished_ids = pickle.load(open(SCRAPED_MARK, 'rb'))
        else:
            finished_ids = []
        try:
            mission_ids = distribute_dict[distribute_uuid]

            if len([i for i in mission_ids if i in finished_ids]) == len(mission_ids):
                print('Good Done!!! Mission Complete!!')
                print('now will continue scrap fans_ids.pkl file.')

                fans_id_file = os.path.join(CORPUS_SAVE_DIR, 'weibo_fans.pkl')
                if os.path.exists(fans_id_file):
                    fans_id = pickle.load(open(fans_id_file, 'rb'))
                    for fd in fans_id:
                        scrap(fd)
            else:
                for md in mission_ids:
                    scrap(md)
        except Exception as e:
            print(e)
            print('distribute uuid invalid.')


def scrap_single(sid):
    """
    this method scrap single id.
    For you want scrap you own ids. just send it here
    :param sid:
    :return:
    """
    scrap(sid)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('run as python3 main.py your-uuid, you can get uuid via wechat `jintianiloveu`.')
    else:
        mission(sys.argv[1])
