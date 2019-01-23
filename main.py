# -*- coding:utf-8 -*-

# 版权所有 (C) 2018.6.25 金盛羽。保留所有权利。
# Copyright 2018.6.25 Shengyu Jin. All Rights Reserved.
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

"""
本程序主要用于进行MMPI测试，相关结果按照手册公式进行计算，使用时应在受过
专业训练的人员指导下进行，并由专业人士对相关内容和结果进行解读，个人慎用
This program is mainly used for Minnesota Multiphasic Per-sonality
Inventory, and the results of the test are just for reference, for
more authoritative explanation please consult professional staff
if necessary.
"""

from mmpilib import mmpi


def run():
    mmpi.start()
    mmpi.test()
    mmpi.calculate_score()
    mmpi.analyze_score()
    mmpi.data_export()


if __name__ == '__main__':
    run()
