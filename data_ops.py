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
    dir_name_areas = ["Area_1", "Area_2", "Area_3", "Area_4", "Area_5", "Area_6"]

    @classmethod
    def __init__(cls, dir_data: str = "data"):
        """

        :param dir_data:
        """
        cls.dir_data = dir_data

    @staticmethod
    def check_dir_exists(path: str) -> bool:
        if os.path.exists(path):
            return True
        raise FileNotFoundError("The specified directory or file ({0}) does not exist.".format(str(path)) +
                                " Please confirm that the provided parameters are correct.")

    @classmethod
    def get_all_areas_list(cls) -> list:
        """

        :return:
        """
        return cls.dir_name_areas

    type_room = ['conferenceRoom', 'copyRoom', 'hallway', 'office', 'pantry', 'WC', 'auditorium', 'storage', 'lounge',
                 'lobby', 'openspace']

    type_object = ['beam', 'board', 'bookcase', 'ceiling', 'chair', 'clutter', 'door', 'floor', 'table', 'wall',
                   'column', 'Icon', 'sofa', 'window', 'stairs']

    @classmethod
    def get_all_rooms_list(cls, area: str = "Area_1", area_no: int = 1) -> list:
        """

        :param area:
        :param area_no:
        :return:
        """
        path = os.path.join(cls.dir_data, area if area is not None else "Area_{0}".format(area_no))
        if not os.path.isdir(path):
            raise NotADirectoryError('The path({0}) is not a valid directory.'.format(path))
        room_list = os.listdir(path)
        for room in room_list:
            if os.path.isfile(os.path.join(cls.dir_data, area, room)):
                room_list.remove(room)
        return room_list

    @classmethod
    def get_room_points(cls,
                        area: str = "Area_1", area_no: int = 1,
                        room: str = "conferenceRoom_1", room_name: str = "conferenceRoom", room_no: int = 1) \
            -> np.array:
        """

        :param area:
        :param area_no:
        :param room:
        :param room_name:
        :param room_no:
        :return:
        """
        filename = os.path.join(cls.dir_data,
                                area if area is not None else "Area_{0}".format(area_no),
                                room if room is not None else "{0}_{1}".format(room_name, room_no),
                                room + ".txt" if room is not None else "{0}_{1}.txt".format(room_name, room_no))
        cls.check_dir_exists(filename)
        points = []
        with open(filename) as f:
            while 1:
                lines = f.readlines(10000)
                if not lines:
                    break
                for line in lines:
                    points.append(np.fromstring(line, count=6, sep=' '))
        return np.array(points)

    @classmethod
    def get_all_annotations_points(cls,
                                   area: str = "Area_1", area_no: int = 1,
                                   room: str = "conferenceRoom_1", room_name: str = "conferenceRoom", room_no: int = 1)\
            -> np.array:
        """

        :param area:
        :param area_no:
        :param room:
        :param room_name:
        :param room_no:
        :return:
        """
        dir_annotations = os.path.join(cls.dir_data,
                                       area if area is not None else "Area_{0}".format(area_no),
                                       room if room is not None else "{0}_{1}".format(room_name, room_no),
                                       "Annotations")
        annotations = []
        for filename_annotation in os.listdir(dir_annotations):
            if os.path.splitext(filename_annotation)[1] != '.txt':
                print("Invalid annotation file: {0}".format(filename_annotation))
                continue
            points = cls.get_annotation_points(area=area,
                                               area_no=area_no,
                                               room=room,
                                               room_name=room_name,
                                               room_no=room_no,
                                               annotation_tag=filename_annotation)
            # print("File: {0} | Length: {1}".format(filename_annotation, len(points)))
            annotations.append(points)
        return np.array(annotations)

    @classmethod
    def get_annotation_points(cls,
                              area: str = "Area_1", area_no: int = 1,
                              room: str = "conferenceRoom", room_name: str = "conferenceRoom", room_no: int = 1,
                              annotation_tag: str = None, annotation_name: str = "beam", annotation_no: int = 1) \
            -> np.array:
        """

        :param area:
        :param area_no:
        :param room:
        :param room_name:
        :param room_no:
        :param annotation_tag:
        :param annotation_name:
        :param annotation_no:
        :return:
        """
        filename = os.path.join(cls.dir_data,
                                area if area is not None else "Area_{0}".format(area_no),
                                room if room is not None else "{0}_{1}".format(room_name, room_no),
                                "Annotations",
                                annotation_tag + ".txt" if annotation_tag is not None else
                                "{0}_{1}.txt".format(annotation_name, annotation_no))
        # print(filename)
        points = []
        cls.check_dir_exists(filename)
        with open(filename) as f:
            while 1:
                lines = f.readlines(10000)
                if not lines:
                    break
                for line in lines:
                    points.append(np.fromstring(line, count=6, sep=' '))
        return np.array(points)
