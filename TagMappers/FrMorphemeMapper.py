from .TagMapper import TagMapper


class FrMorphemeMapper(TagMapper):
    def __init__(self):
        super().__init__()

    @property
    def _tagLibrary(self):
        return {
            # PRONOUN
            "je": "je",
            "me": "me",
            "moi": "moi",
            "mon": "mon",
            "ma": "ma",
            "mes": "mes",
            "tu": "tu",
            "te": "te",
            "toi": "toi",
            "ton": "ton",
            "ta": "ta",
            "tes": "tes",
            "il": "il",
            "lui": "lui",
            "elle": "elle",
            "son": "son",
            "sa": "sa",
            "ses": "ses",
            "soi": "soi",
            "ils": "ils",
            "elles": "elles",
            "leur": "leur",
            "leurs": "leur-s",
            "on": "on",
            # CONNECTIOn
            "qui": "qui",
            "que": "que",
            "quand": "quand",
            "où": "où",
            "quel": "quel",
            "quelle": "quel-le",
            "quels": "quel-s",
            "quelles": "quel-le-s",
            "tel": "tel",
            "telle": "tel-le",
            "tels": "tel-s",
            "telles": "tel-le-s",
            "ne": "ne",
            "pas": "pas",
            "rien": "rien",
            "même": "même",
            "aussi": "aussi",
            "encore": "encore",
            "déjà": "déjà",
            "toujours": "toujours",
            "jamais": "jamais",
            # pas also being N.M, however the freq a lot less, possibility omitted
            "et": "et",
            "mais": "mais",
            "ou": "ou",
            "si": "si",
            "ce": "ce",
            "cette": "cet-te",
            "cela": "ce=la",
            "ceci": "ce=ci",
            # Adpositions
            "de": "de",
            "à": "à",
            "dans": "dans",
            "sur": "sur",
            "avec": "avec",
            "sans": "sans",
            "en": "en",
            "sous": "sous",
            "devant": "devant",
            "après": "après",
            "jusqu\'à": "jusque=à",
            "jusqu‘à": "jusque=à",
            "par": "par",
            # OPEN CLASS
            # VERBS
            "avoir": "avoir",
            "es": "es",
            "est": "est",
            "êtes": "êtes",
            "sont": "sont",
            "avais": "avais",
            "avait": "avait",
            "avions": "avions",
            # also avion-s => aircraft. ignored.
            "aviez": "aviez",
            "avaient": "avaient",
            "aurai": "aurai",
            "auras": "auras",
            "aura": "aura",
            "aurons": "aurons",
            "aurez": "aurez",
            "auront": "auront",
            "aurais": "aurais",
            "aurait": "aurait",
            "aurions": "aurions",
            "auriez": "auriez",
            "auraient": "auraient",
            "être": "être",
            "es": "es",
            "est": "est",
            # sommes not sure if somme-s
            "êtes": "êtes",
            "sont": "sont",
            "étais": "étais",
            # étais also 2SG
            "était": "était",
            "étions": "étions",
            "étiez": "étiez",
            "étaient": "étaient",
            "serai": "serai",
            "seras": "seras",
            "sera": "sera",
            "serons": "serons",
            "serez": "serez",
            "seront": "seront",
            "serais": "serais",
            # serais also 2SG
            "serait": "serait",
            "serions": "serions",
            "seriez": "seriez",
            "seraient": "seraient",
            # sois 1SG/2SG/IMP
            "soit": "soit",
            "soyons": "soyons",
            # soyez 2PL/IMP
            "soient": "soient",
            # PUNKT
            "\"": "\"",
            "“": "“",
            "”": "”",
            ".": ".",
            ",": ",",
            ";": ";",
            ":": ":",
            "!": "!",
            "?": "?",
            "…": "…",
            "«": "«",
            "»": "»",
            "c\'est": "ce=est",
            "c‘est": "ce=est",
            "c\'était": "ce=était",
            "c‘était": "ce=était",
            "n\'est": "ne=est",
            "n\'était": "ne=était",
            "n‘est": "ne=est",
            "n‘était": "ne=était",
            "j\'ai": "je=ai",
            "j\'avais": "je=avais",
            "j\'aurai": "je=aurai",
            "j\'aurais": "je=aurais",
            "j‘ai": "je=ai",
            "j‘avais": "je=avais",
            "j‘aurai": "je=aurai",
            "j‘aurais": "je=aurais",
            "j‘étais": "je=étais",
            "est-ce": "est=ce",
            "est-il": "est=il",
            "est-elle": "est=elle",
            "au": "à=le",
            "aux": "à=les"
        }
