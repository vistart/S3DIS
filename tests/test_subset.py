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


@pytest.mark.skip
def test_room_points_unique(s3dis):
    """
    Check that the points that appear in a single file are not duplicated at all.
    :param s3dis:
    :return:
    """
    for area in s3dis.get_all_areas_list():
        area = "Area_1"
        print("————{0}————".format(area))
        for room in s3dis.get_all_rooms_list(area):
            points = (s3dis.get_room_points(area=area, room=room))
            print("{0} | Lines {1} | PASSED.".format(room, len(points)))
            points = s3dis.get_all_annotations_points(area=area, room=room)
            count = 0
            for point in points:
                count = count + len(point)
            print("{0} | Annotations Lines {1} | PASSED.".format(room, count))
        print("————{0}————".format(area))
    return True


def test_unique(s3dis):
    sub_set = s3dis.get_annotation_points(area="Area_1", room="conferenceRoom_1", annotation_tag="beam_1")
    length = len(sub_set)
    import numpy as np
    unique, unique_indices, unique_counts = (np.unique(sub_set, return_counts=True, return_index=True, axis=0))
    for i in range(len(unique_counts)):
        if unique_counts[i] > 1:
            print(i, unique_indices[i])
    return True


@pytest.mark.skip
def test_no_intersection_between_any_two_collections(s3dis):
    complete_set = s3dis.get_room_points(area="Area_1", room="conferenceRoom_1")
    assert len(complete_set) > 0
    all_sub_sets = s3dis.get_all_annotations_points(area="Area_1", room="conferenceRoom_1")
    assert len(all_sub_sets) > 0
    import numpy as np
    diff_complete_set = len(complete_set) - len(np.unique(complete_set, axis=0))
    print(len(complete_set), len(np.unique(complete_set, axis=0)))
    diff_sub_sets = 0
    total = 0
    for i in range(len(all_sub_sets)):
        total = total + len(all_sub_sets[i])
        diff_sub_sets = diff_sub_sets + len(all_sub_sets[i]) - len(np.unique(all_sub_sets[i], axis=0))
    assert len(complete_set) == total
    assert diff_complete_set == diff_sub_sets
    return True


@pytest.mark.skip
def test_subset(s3dis):
    complete_set = s3dis.get_room_points(area="Area_1", room="conferenceRoom_1")
    sub_set = s3dis.get_annotation_points(area="Area_1", room="conferenceRoom_1", annotation_tag="beam_1")
    import numpy as np
    checked_index = []
    line = 0
    for point in sub_set:
        assert point in complete_set
        line = line + 1
        if line % 100 == 1:
            print(line)
    print(checked_index)
    return True
