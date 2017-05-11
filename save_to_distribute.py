# -*- coding: utf-8 -*-
# file: save_to_distribute.py
# author: JinTian
# time: 11/05/2017 8:47 AM
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
from settings.config import *
import pickle

"""
s: star 指的是明星的微博id
m: 媒体，指的是媒体的微博id
c: company，指的是公司的微博id
r：热点，指的是当前热点微博id
"""

dump_obj = {
    's00001': ['xiaopapi', 'jianglaoye', 'andyisme'],
    's00002': ['kaikai0818', '1197191492', '1730726637'],
    's00003': ['1101675253', '1895964183', 'shuchang'],
    's00004': ['2006455031', 'qiweiblog', 'chenhe09'],
    's00005': ['hereinuk', 'rishiji', '5909185172'],
    'm00001': ['2547916923', 'tangdizi', '1965681503'],
    'm00002': ['xuetucao', '2718604160', 'luvmuzik'],
    'm00003': ['shijiyinyue', '1742566624', 'sqsp',],
    'm00004': ['xiaopapi', '3217179555', 'jianglaoye', 'andyisme',],
    'm00005': ['vaaaaaa', 'kaikai0818', 'tongdaodashu'],
    'c00001': ['1197191492', '270033754', 'gaoxiaotop'],
    'c00002': ['williamchanwaiting', '2713968254', 'uktimes'],
    'c00003': ['2182038504', 'happyzhangjiang', '1927564525'],
    'c00004': ['2891529877', '2482557597', 'beckypp',],
    'c00005': ['5220839587', 'alexlovely', '1101675253',],
    'r00001': ['2547916923', '1827234850', 'xuetucao', ],
    'r00002': ['2970036311', '2155226773', '1730726637',],
    'r00003': ['zhang3250152wei', '1445962081', '2150511032',],
    'r00004': ['512789686', 'hejiong', 'fbb0916'],
    'a00001': ['5357382605', '2396658275', 'oho2012'],
    'a00002': ['meishiweidao001', 'bjshi', 'rosemary16'],
    'a00003': ['mengxian', '3986147355', '1086233511'],
    'a00004': ['137010641', '1738932247', 'lichenlichen'],
    'a00005': ['2154547207', 'changtzuyao', 'xuezhiqian'],
    'a00006': ['jjlin', 'jacksonwangG7', '3180788643'],
    'a00008': ['2807684421', '1811893237', 'jdluqi'],
    'a00009': ['zhouyangqing912', '3900215081', '2154042825'],
    'a00010': ['lubeiweida', '2111146932','hztbar'],
    'a00011': ['leijun', '2359037744', 'dushuyuluvip'],
    'a00012': ['574422122', 'ichthy', 'guimitai2'],
    'a00013': ['3622512610', '2423763501'],
    'a00014': ['2835724503', 'xiena', 'tongliyavk'],
    'a00015': ['579999138', '5222794628', 'wenwinning'],
    'a00016': ['YouTubeSP', '3641513235', '920722209'],
    'a00017': ['qingganshudong1314', '2825653895', '577335442'],
    'a00018': ['5181464632', '3974469906', 'otaku2b'],
}

with open(DISTRIBUTE_IDS, 'wb') as f:
    pickle.dump(dump_obj, f)
print('done!')

with open(DISTRIBUTE_IDS, 'rb') as f:
    d = pickle.load(f)
print('read test.')
print(d['r00004'])
