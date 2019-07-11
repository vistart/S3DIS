#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  _   __ __ _____ _____ ___  ____  _____
# | | / // // ___//_  _//   ||  __||_   _|
# | |/ // /(__  )  / / / /| || |     | |
# |___//_//____/  /_/ /_/ |_||_|     |_|
# @File  : test_subset.py
# @Author: vistart
# @Date  : 2019/7/7
# @Desc  :


import pytest
import sys
import os
sys.path.append('..')
import data_ops


@pytest.fixture
def s3dis():
    s3dis = data_ops.S3DIS(os.path.join("..", "data"))
    return s3dis


def test_get_annotation_points(s3dis):
    assert s3dis.dir_data == os.path.join("..", "data")
    assert len(s3dis.get_areas_dir(1)) > 0
