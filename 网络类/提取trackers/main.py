# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: utf-8 -*-
'''
by 绝

所需模块：
    pip3 install -U requests --user
'''


# %%
import os
import requests
# from MyLib import path


class tracker:
    # tracker 获取源
    def __init__(self):
        self.url = "https://trackerslist.com/all.txt"
        self.代理 = {
            "http": "http://127.0.0.1:10001",
            "https": "http://127.0.0.1:10001",
        }

        @property
        def _get(self):
            data = requests.get(self.url[0], proxies=self.代理)
            print(data)
            return data.text()


class ComTrackersList(tracker):
    def __init__(self):
        self.url = "https://trackerslist.com/all.txt"

    def get(self):
        pass


class GitTrackersList(tracker):
    def __init__(self):
        self.url = "https://ngosang.github.io/trackerslist/trackers_all.txt"

    def get(self):
        pass


# %%
if __name__ == "__main__":

    print(ComTrackersList.get)


# %%
