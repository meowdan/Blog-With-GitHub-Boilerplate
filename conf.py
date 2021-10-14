# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
 	"enabled": True,
 	"repo": "meowdan/maverick-blog@gh-pages"
 }

# 站点设置
site_name = "超时空蛋蛋"
site_logo = "${static_prefix}logo.ico"
site_build_date = "2021-09-03T16:51+08:00"
author = "meowdan"
email = "edwiinme@gmail.com"
author_homepage = "https://www.meowdan.com"
description = "这是一个单机版blog。"
key_words = ['Maverick', '超时空蛋蛋', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
     {
        "name": "夏小雪",
        "url": "https://sizheng.org/",
        "brief": "夏小雪的星球漫步"
     },
     {
        "name": "喔喔",
        "url": "https://makefile.so/",
        "brief": "喔喔的收藏夹"
    },
    {
        "name": "xiao.lu",
        "url": "https://xiao.lu/",
        "brief": "鹿哥的博客"
    },
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/meowdan/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/meowdan/",
        "icon": "gi gi-github"
    },
    {
        "name": "instagram",
        "url": "https://www.instagram.com/meowdan_/",
        "icon": "gi gi-instagram"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "mTAVavFyX0vXlmnLSlonf3HI-MdYXbMMI",
    "appKey": "h0tzL1xc2UwFzcyvreE0abJJ",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
