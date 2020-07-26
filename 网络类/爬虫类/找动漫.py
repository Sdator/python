# -*- coding: utf-8 -*-
'''
by 绝 2019.4.28

# 2019.6.1
    文件保存命名方式采用“时间+关键字+字幕组”的方式
    解析动漫花园【已完成】

# 2019.4.28
    解析动漫花园【待写】
        需要填写服务器信息（梯子）
    解析nyaa【已完成】

'''
from MyLib.file import 写出文件
from MyLib.net import 爬取
import xml.dom.minidom  # xml处理模块
import re
from enum import Enum, unique

# import os
# import sys
# sys.path.append(os.getcwd())


# from bs4 import BeautifulSoup
# import MyLib.ipc.tipc as tipc


# 枚举类型


@unique
class 分类(Enum):
    全部 = 0
    動畫 = 2
    季度全集 = 31
    漫畫 = 3
    港台原版 = 41
    日文原版 = 42
    音樂 = 4
    動漫音樂 = 43
    同人音樂 = 44
    流行音樂 = 15
    日劇 = 6
    ＲＡＷ = 7
    遊戲 = 9
    電腦遊戲 = 17
    電視遊戲 = 18
    掌機遊戲 = 19
    網絡遊戲 = 20
    遊戲周邊 = 21
    特攝 = 12
    其他 = 1


@unique
class 字幕组(Enum):
    全部 = 0
    動漫花園 = 117
    动漫国字幕组 = 303
    极影字幕社 = 185
    咪梦动漫组 = 710
    悠哈C9字幕社 = 151
    喵萌奶茶屋 = 669
    天使动漫论坛 = 390
    LoliHouse = 657
    喵萌茶会字幕组 = 468
    雪飄工作室 = 37
    DHR動研字幕組 = 407
    cc动漫 = 604
    caRaws = 695
    漫貓字幕組 = 423
    风之圣殿 = 434
    幻樱字幕组 = 241
    八重樱字幕组 = 663
    千夏字幕组 = 283
    诸神kamigami字幕组 = 288
    桜都字幕组 = 619
    漫游字幕组 = 134
    ANKRaws = 375
    LoveEcho = 504
    天行搬运 = 602
    時雨初空 = 570
    YMDR发布组 = 720
    西农YUI汉化组 = 525
    青森小镇 = 708
    风车字幕组 = 454
    ZERO字幕组 = 391
    动音漫影 = 88
    TUcaptions = 492
    白恋字幕组 = 438
    豌豆字幕组 = 520
    波洛咖啡厅 = 627
    飞龙骑脸字幕组 = 709
    澄空学园 = 58
    届恋字幕组 = 703
    爱恋字幕社 = 47
    轻之国度 = 321
    未央阁联盟 = 592
    枫叶字幕组 = 630
    楓雪連載製作 = 34
    幻之字幕组 = 430
    银色子弹字幕组 = 576
    东京不够热 = 526
    新番字幕组 = 672
    天空树双语字幕组 = 485
    追新番字幕组 = 651
    VRAINSTORM = 673
    银光字幕组 = 506
    梦星字幕组 = 552
    WOLF字幕组 = 141
    聖域字幕組 = 403
    小愿8压制组 = 705
    魯邦聯會 = 721
    动漫先锋 = 104
    NEO·QSW = 537
    AikatsuFans = 675
    VCBStudio = 581
    BBA字幕组 = 436
    KRL字幕组 = 228
    小花花同盟戰線 = 699
    AQUA工作室 = 217
    梦蓝字幕组 = 574
    鈴風字幕組 = 225
    萝莉社活动室 = 550
    A80v08 = 719
    LittleBakas = 638
    脸肿字幕组 = 568
    花園壓制組 = 563
    旋风字幕组 = 370
    漫藤字幕组 = 559
    省电Raws = 631
    华盟字幕社 = 49
    柯南事务所 = 75
    天香字幕社 = 110
    虐心发布组 = 690
    冷番补完字幕组 = 641
    雪梦字幕组 = 567
    Little字幕组 = 680
    乐园字幕组 = 723
    CentaureaRaws = 573
    自由字幕组 = 432
    AstralUnion字幕组 = 716
    魔星字幕团 = 648
    Vmoe字幕組 = 536
    NAZOrip = 697
    狐狸小宮 = 701
    囧夏发布组 = 507
    虚数学区研究协会 = 664
    AZT字幕组 = 717
    CureSub = 332
    钉铛字幕组 = 561
    SFEORaws = 652
    EggPainRaws = 541
    天空字幕组 = 453
    天の翼字幕汉化社 = 606
    紫音動漫發佈組 = 459
    星火字幕组 = 558
    驯兽师联盟 = 626
    BlueRabbit = 687
    夜莺工作室 = 394
    矢车菊影音工作室 = 505
    TenYun = 702
    猪猪字幕组 = 380
    月光恋曲字幕组 = 57


@unique
class 时序(Enum):
    發佈時間從後往前 = "date-desc"
    發佈時間從前往後 = "date-asc"
    相關度 = "rel"


@unique
class 动画(Enum):
    多罗罗 = 1
    多羅羅 = 2
    博人传 = 3
    博人傳 = 4


async def 动漫花园走起(关键字="多羅羅", 那个字幕组=字幕组.全部, 那个分类=分类.動畫):
    url = "https://share.dmhy.org/topics/rss/rss.xml"

    请求数据 = {
        "keyword": 关键字,      # 搜索用关键字
        "sort_id": 那个分类.value,
        "team_id": 那个字幕组.value,
        "order": 时序.發佈時間從前往後.value  # 时间排列?
    }

    返回数据 = await 爬取(url, 请求数据, "str", 1)

    写出名字 = "%s_%s" % (关键字, 那个字幕组.name)
    路径 = 写出文件(写出名字, 返回数据, "w", "xml")

    # 解析返回的xml
    document_tree = xml.dom.minidom.parse(路径)
    collection = document_tree.documentElement  # 获取所有元素
    # 在集合中获取所有电影
    items = collection.getElementsByTagName("item")
    # 生成数组对象 后续转化为json
    arr = []
    地址 = "找不到url"
    # 解析xml
    for item in items:
        # 获取标题
        title = item.getElementsByTagName('title')[0]
        标题 = title.childNodes[0].data
        # 获取下载地址
        url = item.getElementsByTagName('enclosure')[0]
        # 是否存在属性
        if url.hasAttribute("url"):
            地址 = url.getAttribute("url")  # 获取属性值
            # tipc.下载(地址)  # 使用ipc发送下载
        # 构建新的数据用作写出
        arr.append({"标题": 标题, "磁链": 地址})

    写出文件(写出名字, arr, "w")


@unique
class 用户名(Enum):
    默认 = ""
    YMDR = "Fox-06_18"
    U3 = "U3-Web"
    咪梦动漫组 = "xiaomeng"


@unique
class 资源类型(Enum):
    动漫 = "1_0"
    动漫_动漫音乐视频 = "1_1"
    动漫_英文翻译 = "1_2"
    动漫_非英语翻译 = "1_3"
    动漫_生的 = "1_4"

    音频 = "2_0"
    无损 = "2_1"
    有损 = "2_2"

    小说 = "3_0"
    小说_英文翻译 = "3_1"
    小说_非英语翻译 = "3_2"
    小说_生的 = "3_3"

    现场剧集 = "4_0"
    英文翻译 = "4_1"
    偶像宣传视频 = "4_2"
    非英语翻译 = "4_3"
    剧集_生的 = "4_4"

    图片 = "5_0"
    图像 = "5_1"
    相片 = "5_2"

    软件 = "6_0"
    应用 = "6_1"
    游戏 = "6_2"


def nyaa走起(关键字="多羅羅", 用户名=用户名.默认, 资源类型=资源类型.动漫_非英语翻译):
    '''
        参数一  搜索关键字
        参数二  字幕组 相关名称到nyaa查找
    '''

    url = "https://nyaa.si"
    请求数据 = {
        "page": "rss",
        "u": 用户名.value,
        "q": 关键字,  # 搜索用关键字
        "c": 资源类型.value
    }

    返回数据 = 爬取(url, 请求数据)

    # 正则匹配
    集数 = re.findall(r'<title>(.*)</title>', 返回数据)[1:]
    种子 = re.findall(r'<link>(.*)</link>', 返回数据)[1:]
    磁链 = re.findall(r'<nyaa:infoHash>(.*)</nyaa:infoHash>', 返回数据)

    服务器 = r"&dn=%5BU3-Web%5D%20Dororo%20%2F%20%E3%81%A9%E3%82%8D%E3%82%8D%20%2F%20%E5%A4%9A%E7%BE%85%E7%BE%85%202019%20%5BEP15%5D%20%5BMulti-Subs%5D%20%5BAMZN%20WEB-DL%201080p%20AVC%20E-AC-3%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce"

    # 生成数组对象 后续转化为json
    arr = []
    for i in range(len(集数)):
        strTmp = "magnet:?xt=urn:btih:%s%s" % (磁链[i], 服务器)
        arr.append(
            {"集数": 集数[i], "种子": 种子[i], "磁链": strTmp}
        )
        写出名字 = "%s_%s" % (关键字, 用户名.name)
        写出文件(写出名字, arr, "w")


class 爬光头强():

    def __init__(self):
        pass

    @property
    def 返回数据(): pass
    @property
    def 请求数据(): pass

    @property
    def 获取加速服务器():
        url = "https://ngosang.github.io/trackerslist/trackers_all_ip.txt"

    def nyaa走起(关键字="多羅羅", 用户名=用户名.默认, 资源类型=资源类型.动漫_非英语翻译):
        '''
            参数一  搜索关键字
            参数二  字幕组 相关名称到nyaa查找
        '''

        url = "https://nyaa.si"
        请求数据 = {
            "page": "rss",
            "u": 用户名.value,
            "q": 关键字,  # 搜索用关键字
            "c": 资源类型.value
        }

        返回数据 = 爬取(url, 请求数据)

        # 正则匹配
        集数 = re.findall(r'<title>(.*)</title>', 返回数据)[1:]
        种子 = re.findall(r'<link>(.*)</link>', 返回数据)[1:]
        磁链 = re.findall(r'<nyaa:infoHash>(.*)</nyaa:infoHash>', 返回数据)

        服务器 = r"&dn=%5BU3-Web%5D%20Dororo%20%2F%20%E3%81%A9%E3%82%8D%E3%82%8D%20%2F%20%E5%A4%9A%E7%BE%85%E7%BE%85%202019%20%5BEP15%5D%20%5BMulti-Subs%5D%20%5BAMZN%20WEB-DL%201080p%20AVC%20E-AC-3%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce"

        # 生成数组对象 后续转化为json
        arr = []
        for i in range(len(集数)):
            strTmp = "magnet:?xt=urn:btih:%s%s" % (磁链[i], 服务器)
            arr.append(
                {"集数": 集数[i], "种子": 种子[i], "磁链": strTmp}
            )
            写出名字 = "%s_%s" % (关键字, 用户名.name)
            写出文件(写出名字, arr, "w")


if __name__ == '__main__':
    # nyaa走起("多 web")
    #    动漫花园走起("多罗罗 web", 字幕组.全部, 分类.動畫)
    #    动漫花园走起("盾", 字幕组.LoliHouse, 分类.動畫)
    #    动漫花园走起("盾", 字幕组.自由字幕组, 分类.動畫)
    #    动漫花园走起("贤者 简 web", 字幕组.全部, 分类.動畫)
    #    动漫花园走起("火影 新時代", 字幕组.cc动漫, 分类.動畫)
    # 动漫花园走起("刀剑神域 WEB-DL", 字幕组.全部, 分类.動畫)
    动漫花园走起("火影 WEB-DL", 字幕组.全部, 分类.動畫)


'''
js 遍历数据

$("#navFilter-category [data-original-index]").each(function(){

})

'''
