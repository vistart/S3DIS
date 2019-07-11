#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  _   __ __ _____ _____ ___  ____  _____
# | | / // // ___//_  _//   ||  __||_   _|
# | |/ // /(__  )  / / / /| || |     | |
# |___//_//____/  /_/ /_/ |_||_|     |_|
# @File  : test.py
# @Author: vistart
# @Date  : 2019/7/9
# @Desc  :


import data_ops
import os
import re

s3dis = data_ops.S3DIS()
# print((len(s3dis.get_annotation_points())))
"""

if os.path.isdir(s3dis.dir_data):
    type_room = []
    category = []
    room_name_pattern = re.compile(r"[a-zA-Z]+")
    for i in os.listdir(s3dis.dir_data):
        data_dir = os.path.join(s3dis.dir_data, i)
        if os.path.isdir(data_dir):
            for j in os.listdir(data_dir):
                match = re.search(room_name_pattern, j)
                if match.group() not in type_room:
                    type_room.append(match.group())
        if os.path.isdir(data_dir):
            for j in os.listdir(data_dir):
                area_dir = os.path.join(data_dir, j, 'Annotations')
                if not os.path.exists(area_dir):
                    continue
                for k in os.listdir(area_dir):
                    match = re.search(room_name_pattern, k)
                    if match.group() not in category:
                        category.append(match.group())
    print(category)

else:
    print(s3dis.dir_data, " is not a valid directory.")
"""

print(s3dis.get_room_points())