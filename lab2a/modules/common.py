import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def one_three_five(aaa):
    sequence = ""
    i = 0
    while i != 101:
        if aaa == True:
            if i % 2 == 0:
                sequence += str(i) + " "

        else:
            if i % 2 == 1:
                sequence += str(i) + " "
        i += 1
    return sequence

