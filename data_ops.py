#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  _   __ __ _____ _____ ___  ____  _____
# | | / // // ___//_  _//   ||  __||_   _|
# | |/ // /(__  )  / / / /| || |     | |
# |___//_//____/  /_/ /_/ |_||_|     |_|
# @File  : data_ops.py
# @Author: vistart
# @Date  : 2019/7/8
# @Desc  :

import os
import numpy as np


class S3DIS:
    area_nos = [1, 2, 3, 4, 5, 6]

    dir_data = "data"
    dir_areas = ["Area_1", "Area_2", "Area_3", "Area_4", "Area_5", "Area_6"]

    @classmethod
    def __init__(cls, dir_data):
        cls.dir_data = dir_data

    @staticmethod
    def check_dir_exists(path):
        if os.path.exists(path):
            return True
        raise FileNotFoundError("The directory or file specified to hold the points of room does not exist."
                                " Please confirm that the provided parameters are correct.")

    @classmethod
    def get_areas_dir(cls, area_no):
        """

        :param area_no:
        :return:
        """
        dir_area = os.path.join(cls.dir_data, 'Area_' + str(area_no))
        cls.check_dir_exists(dir_area)
        return dir_area

    type_room = ['conferenceRoom', 'copyRoom', 'hallway', 'office', 'pantry', 'WC', 'auditorium', 'storage', 'lounge',
                 'lobby', 'openspace']

    type_object = ['beam', 'board', 'bookcase', 'ceiling', 'chair', 'clutter', 'door', 'floor', 'table', 'wall',
                   'column', 'Icon', 'sofa', 'window', 'stairs']

    @classmethod
    def get_room_points(cls,
                        area_no=1,
                        room_name="conferenceRoom",
                        room_no=1):
        """

        :param area_no:
        :param room_name:
        :param room_no:
        :return:
        """
        filename = os.path.join(cls.dir_data,
                                "Area_{0}".format(area_no),
                                "{0}_{1}".format(room_name, room_no),
                                "{0}_{1}.txt".format(room_name, room_no))
        cls.check_dir_exists(filename)
        return np.loadtxt(filename)

    @classmethod
    def get_all_annotations_points(cls,
                                   area_no=1,
                                   room_name="conferenceRoom",
                                   room_no=1):
        """

        :param area_no:
        :param room_name:
        :param room_no:
        :return:
        """

    @classmethod
    def get_annotation_points(cls,
                              area_no=1,
                              room_name="conferenceRoom",
                              room_no=1,
                              annotation_name="beam",
                              annotation_no=1):
        """

        :param area_no:
        :param room_name:
        :param room_no:
        :param annotation_name:
        :param annotation_no:
        :return:
        """
        filename = os.path.join(cls.dir_data,
                                "Area_{0}".format(area_no),
                                "{0}_{1}".format(room_name, room_no),
                                "Annotations",
                                "{0}_{1}.txt".format(annotation_name, annotation_no))
        cls.check_dir_exists(filename)
        return np.loadtxt(filename)
