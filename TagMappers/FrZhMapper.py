from .TagMapper import TagMapper


class FrZhMapper(TagMapper):
    def __init__(self):
        super().__init__()

    @property
    def _tagLibrary(self):
        return {
            # PRONOUN
            "je": "我(主格)",
            # me DO/IO
            "moi": "我(重读人称代词)",
            # mon vocal change M/F
            "ma": "我的(阴性.单数)",
            "mes": "我的(复数)",
            "tu": "你(主格)",
            # te DO/IO
            "toi": "你(重读人称代词)",
            # ton same M/F
            "ta": "你的(阴性)",
            "tes": "你的(复数)",
            "il": "他(主格)",
            # lui IO/STRESSED
            # elle SBJ/STRESSED
            # son idem M/F
            # sa <= his/her
            # ses <= his/her
            "soi": "自己(反身式.重读人称代词)",
            "ils": "他们(主格)",
            "elles": "她们(主格)",
            # elles also STRESSED, ignored.
            # leur POSS/IO
            "leurs": "他们的(复数)",
            "on": "人们.代词.不定指",
            # CONNECTIOn
            # qui who/RELR
            # que CONJ/RELR
            # quand when/RELR
            # où where/RELR
            "quel": "如何",
            "quelle": "如何-阴性",
            "quels": "如何-复数",
            "quelles": "如何-阴性-复数",
            "tel": "如此(阳性)",
            "telle": "如此(阴性)",
            "tels": "如此(阳性)-复数",
            "telles": "如此-阴性(复数)",
            "ne": "不.否定1",
            "pas": "不.否定2",
            # pas also being N.M, however the freq a lot less, possibility omitted
            "rien": "什么也没有.否定",
            "même": "甚至/副词",
            "aussi": "也/副词",
            "encore": "仍然/副词",
            "déjà": "已经/副词",
            "toujours": "总是/副词",
            "jamais": "从不/副词",
            "et": "和/连词",
            "mais": "但是/连词",
            "ou": "或者/连词",
            "ce": "这个",
            "cette": "阴性\\这个(阴性)",
            "cela": "这个=那个",
            "ceci": "这个=这个",
            # un, une, number/ART
            # si CONJ/so
            # Adpositions
            # de INFMARK/from/of.GENMARK
            # à INFMARK/at/in
            "dans": "在/介词",
            "sur": "在……上/介词",
            "avec": "伴随/介词",
            "sans": "缺少/介词",
            # en ADVPRON/PREP
            "sous": "在……下/介词",
            "devant": "在……前/介词",
            "après": "在……后/介词",
            # après can also be ADV. possibility ignored.
            "jusqu\'à": "直到/副词=在/介词",
            "jusqu‘à": "直到/副词=在/介词",
            "par": "从/介词",
            # OPEN CLASS
            # VERBS
            # avoir AUX/not aux
            "être": "系词.不定式",
            "suis": "系词.第一人称单数.直陈式.现在时",
            "es": "系词.第二人称单数.直陈式.现在时",
            "est": "系词.第三人称单数.直陈式.现在时",
            # sommes not sure if somme-s
            "êtes": "系词.第二人称复数.直陈式.现在时",
            "sont": "系词.第三人称复数.直陈式.现在时",
            "étais": "系词.第一人称单数.直陈式.未完成时",
            # étais also 第二人称单数
            "était": "系词.第三人称单数.直陈式.未完成时",
            "étions": "系词.第一人称复数.直陈式.未完成时",
            "étiez": "系词.第二人称复数.直陈式.未完成时",
            "étaient": "系词.第三人称复数.直陈式.未完成时",
            "serai": "系词.第一人称单数.直陈式.将来时",
            "seras": "系词.第二人称单数.直陈式.将来时",
            "sera": "系词.第三人称单数.直陈式.将来时",
            "serons": "系词.第一人称复数.直陈式.将来时",
            "serez": "系词.第二人称复数.直陈式.将来时",
            "seront": "系词.第三人称复数.直陈式.将来时",
            "serais": "系词.第一人称单数.条件式.现在时",
            # serais also 第二人称单数
            "serait": "系词.第三人称单数.条件式.现在时",
            "serions": "系词.第一人称复数.条件式.现在时",
            "seriez": "系词.第二人称复数.条件式.现在时",
            "seraient": "系词.第三人称复数.条件式.现在时",
            # sois 第一人称单数/第二人称单数/IMP
            "soit": "系词.第三人称单数.虚拟式.现在时",
            "soyons": "系词.第一人称复数.虚拟式.现在时",
            # soyez 第二人称复数/IMP
            "soient": "系词.第三人称复数.虚拟式.现在时",
            # PUNKT
            "“": "“",
            "”": "”",
            ".": "。",
            ",": "，",
            ";": "；",
            ":": "：",
            "!": "！",
            "?": "？",
            "…": "……",
            "«": "“",
            "»": "”",
            "c\'est": "这个=系词.第三人称单数.直陈式.现在时",
            "c‘est": "这个=系词.第三人称单数.直陈式.现在时",
            "c\'était": "这个=系词.第三人称单数.直陈式.未完成时",
            "c‘était": "这个=系词.第三人称单数.直陈式.未完成时",
            "n\'est": "不.否定1=系词.第三人称单数.直陈式.现在时",
            "n\'était": "不.否定1=系词.第三人称单数.直陈式.未完成时",
            "n‘est": "不.否定1=系词.第三人称单数.直陈式.现在时",
            "n‘était": "不.否定1=系词.第三人称单数.直陈式.未完成时",
            "j\'ai": "我(主格)=有/助动词.第一人称单数.直陈式.现在时",
            "j\'avais": "我(主格)=有/助动词.第一人称单数.直陈式.未完成时",
            "j\'aurai": "我(主格)=有/助动词.第一人称单数.直陈式.将来时",
            "j\'aurais": "我(主格)=有/助动词.第一人称单数.条件式.现在时",
            "j‘ai": "我(主格)=有/助动词.第一人称单数.直陈式.现在时",
            "j‘avais": "我(主格)=有/助动词.第一人称单数.直陈式.未完成时",
            "j‘aurai": "我(主格)=有/助动词.第一人称单数.直陈式.将来时",
            "j‘aurais": "我(主格)=有/助动词.第一人称单数.条件式.现在时",
            "j\'étais": "我(主格)=系词.第一人称单数.直陈式.未完成时",
            "j‘étais": "我(主格)=系词.第一人称单数.直陈式.未完成时",
            "est-ce": "系词.第三人称单数.直陈式.现在时=这个",
            "est-il": "系词.第三人称单数.直陈式.现在时=他(主格)",
            "est-elle": "系词.第三人称单数.直陈式.现在时=她(主格)",
            "au": "到/介词=定冠词(阳性.单数)",
            "aux": "到/介词=定冠词(复数)"
        }
