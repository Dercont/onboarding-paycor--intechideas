import json
import os
import inspect
import re


class Formatters():
    pass


class PreFormatters():
    pass


class PostFormatters():
    pass


def __get_methods(klass):
    """
    Returns a list o
    """
    return [method[1] for method in inspect.getmembers(klass, predicate=inspect.ismethod)]


def get_pre_formatters():
    return __get_methods(PreFormatters)


def get_post_formatters():
    return __get_methods(PostFormatters)
