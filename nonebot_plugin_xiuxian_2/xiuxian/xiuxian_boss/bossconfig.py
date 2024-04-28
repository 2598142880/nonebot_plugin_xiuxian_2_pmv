try:
    import ujson as json
except ImportError:
    import json
import os
from pathlib import Path

configkey = ["Boss灵石", "Boss名字", "Boss倍率", "Boss个数上限", "Boss生成时间参数", 'open', "世界积分商品"]
CONFIG = {
    "open": {},
    "Boss灵石": {
        # 生成Boss给的灵石
        '搬血境': [5000, 7000, 9800],
        '搬血境中期': 7000,
        '搬血境圆满': 9800,
        '洞天境': [10000, 14000, 19600],
        '化灵境': [20000, 28000, 39200],
        '铭纹境': [30000, 42000, 58800],
        '列阵境': [60000, 84000, 117600],
        '尊者境': [120000, 168000, 235200],
        '神火境': [240000, 336000, 470400],
        '真一境': [800000, 1120000, 1568000],
        '圣祭境': [1800000, 2520000, 3528000],
        '天神境': [3400000, 4760000, 6664000],
        '虚道境': [6000000, 8400000, 11760000],
        '斩我境': [10000000, 14000000, 19600000],
        '遁一境': [30000000, 42000000, 58800000],
        '至尊境': [50000000, 82000000, 117600000],
        '真仙境': [100000000, 140000000, 196000000],
        '仙王境': [180000000, 252000000, 352800000],
        '准帝境': [300000000, 420000000, 588000000],
        '仙帝境': [500000000, 700000000, 980000000],
        '祭道境': [800000000, 900000000, 1200000000]
    },
    "Boss名字": [
        "九寒",
        "精卫",
        "少姜",
        "陵光",
        "莫女",
        "术方",
        "卫起",
        "血枫",
        "以向",
        "砂鲛",
        "鲲鹏",
        "天龙",
        "莉莉丝",
        "霍德尔",
        "历飞雨",
        "神风王",
        "衣以候",
        "金凰儿",
        "元磁道人",
        "外道贩卖鬼",
        "散发着威压的尸体"
        ],  # 生成的Boss名字，自行修改
    "Boss个数上限": 45,
    "Boss倍率": {
        # Boss属性：大境界平均修为是基础数值，气血：15倍，真元：10倍，攻击力：0.2倍
        # 作为参考：人物的属性，修为是基础数值，气血：0.5倍，真元：1倍，攻击力：0.1倍
        "气血": 450,
        "真元": 20,
        "攻击": 2
    },
    "Boss生成时间参数": {  # Boss生成的时间，每1小时5分钟生成一只，2个不可全为0
        "hours": 1,
        "minutes": 5
    },
    "世界积分商品": {
        "1": {
            "id": 1999,
            "cost": 1000,
            "desc": "渡厄丹,使下一次突破丢失的修为减少为0!"
        },
        "2": {
            "id": 4003,
            "cost": 500,
            "desc": "陨铁炉,以陨铁炼制的丹炉,耐高温,具有基础的炼丹功能"
        },
        "3": {
            "id": 4002,
            "cost": 2500,
            "desc": "雕花紫铜炉,表面刻有精美雕花的紫铜丹炉,一看便出自大师之手,可以使产出的丹药增加1枚"
        },
        "4": {
            "id": 4001,
            "cost": 10000,
            "desc": "寒铁铸心炉,由万年寒铁打造的顶尖丹炉,可以使产出的丹药增加2枚"
        },
        "5": {
            "id": 2500,
            "cost": 500,
            "desc": "一级聚灵旗,提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "6": {
            "id": 2501,
            "cost": 1000,
            "desc": "二级聚灵旗,提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "7": {
            "id": 2502,
            "cost": 2000,
            "desc": "三级聚灵旗,提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "8": {
            "id": 2503,
            "cost": 4000,
            "desc": "四级聚灵旗,提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "9": {
            "id": 2504,
            "cost": 8000,
            "desc": "仙级聚灵旗,大幅提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "10": {
            "id": 2505,
            "cost": 16000,
            "desc": "无上聚灵旗,极大提升洞天福地中的灵气汇集速度,加速修炼速度和灵田中药材生长速度"
        },
        "11": {
            "id": 7085,
            "cost": 200000,
            "desc": "冲天槊，无上仙器，不属于这个位面的武器，似乎还有种种能力未被发掘...提升100%攻击力！提升50%会心率！提升20%减伤率！提升50%会心伤害！"
        },
        "12": {
            "id": 8931,
            "cost": 200000,
            "desc": "苍寰变，无上神通，不属于这个位面的神通，连续攻击两次，造成6.5倍！7倍伤害！消耗气血0%、真元70%，发动概率100%，发动后休息一回合 "
        },
        "13": {
            "id": 9937,
            "cost": 200000,
            "desc": "一气化三清，无上仙法，比上面几个还牛逼 "
        },
        "14": {
            "id": 10402,
            "cost": 70000,
            "desc": "真神威录，天阶下品辅修功法，增加70%会心率！"
        },
        "15": {
            "id": 10403,
            "cost": 100000,
            "desc": "太乙剑诀，天阶下品辅修功法，增加100%会心伤害！"
        },
        "16": {
            "id": 10411,
            "cost": 120000,
            "desc": "真龙九变，天阶上品辅修功法，增加攻击力60%！"
        }
    }
}


def get_config():
    try:
        config = readf()
        for key in configkey:
            if key not in list(config.keys()):
                config[key] = CONFIG[key]
        savef(config)
    except:
        config = CONFIG
        savef(config)
    return config


CONFIGJSONPATH = Path(__file__).parent
FILEPATH = CONFIGJSONPATH / 'config.json'


def readf():
    with open(FILEPATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return json.loads(data)


def savef(data):
    data = json.dumps(data, ensure_ascii=False, indent=3)
    savemode = "w" if os.path.exists(FILEPATH) else "x"
    with open(FILEPATH, mode=savemode, encoding="UTF-8") as f:
        f.write(data)
        f.close()
    return True
