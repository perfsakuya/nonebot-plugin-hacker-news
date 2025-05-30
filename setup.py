#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="nonebot-plugin-hacker-news",
    version="0.1.0",
    description="获取Hacker News文章并进行播报的NoneBot2插件",
    author="perfsakuya",
    author_email="blujewel350@gmail.com",
    url="https://github.com/perfsakuya/nonebot-plugin-hacker-news",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "nonebot2>=2.0.0rc3",
        "nonebot-adapter-onebot>=2.2.1",
        "httpx>=0.24.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Robot Framework",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "nonebot.plugins": [
            "nonebot_plugin_hacker_news = nonebot_plugin_hacker_news"
        ],
    },
)
