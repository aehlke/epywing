# -*- coding: utf-8 -*-

from epywing.bookfilter import BookFilter
from epywing.titles import SanseidoSuperDaijirin


class Daijirin(BookFilter):
    applies_to = [SanseidoSuperDaijirin]

    def filter_heading(self, heading):
        if heading is not None:
            replacements = {
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)
        return heading

    def filter_text(self, text):
        return text

    narrow_gaiji = {
        0xc121: (u'á', u'a'), # a
        0xc122: (u'à', u'a'), # a
        0xc123: (u'â', u'a'), # a
        0xc124: (u'ä', u'a'), # a
        0xc125: (u'ã', u'a'), # a
        0xc126: (u'ā', u'a'), #
        0xc127: (u'é', u'e'), # e
        0xc128: (u'è', u'e'), # e
        0xc129: (u'ê', u'e'), # e
        0xc12a: (u'ë', u'e'), # e
        0xc12b: (u'ē', u'e'), #
        0xc12c: (u'í', u'i'), # i
        0xc12d: (u'î', u'i'), # i
        0xc12e: (u'ï', u'i'), # i
        0xc12f: (u'ñ', u'n'), # n
        0xc130: (u'ó', u'o'), # o
        0xc131: (u'ò', u'o'), # o
        0xc132: (u'ô', u'o'), # o
        0xc133: (u'ö', u'o'), # o
        0xc134: (u'ř', u'r'), #
        0xc135: (u'ú', u'u'), # u
        0xc136: (u'ü', u'u'), # u
        0xc137: u'~', # ~
        0xc138: (u'ç', u'c'), # c
        0xc139: u'ˇ', #
        0xc13a: u'ɡ', #
        0xc13b: u'ŋ', #
        0xc13c: u'ʒ', #
        0xc13d: u'ʃ', #
        0xc13e: u'ɔ', #
        0xc13f: u'ð', # d
        0xc140: (u'Á', u'A'), # A
        0xc141: (u'Í', u'I'), # I
        0xc142: (u'Ú', u'U'), # U
        0xc143: (u'É', u'E'), # E
        0xc144: (u'Ó', u'O'), # O
        0xc145: (u'À', u'A'), # A
        0xc146: (u'È', u'E'), # E
        0xc147: (u'Ò', u'O'), # O
        0xc148: (u'ì', u'i'), # i
        0xc149: (u'ù', u'u'), # u
        0xc14a: (u'ý', u'y'), # y
        0xc14b: (u'y', u'y'), # y`
        0xc14c: u'ɑ', #
        0xc14d: u'ə', #
        0xc14e: None, # イタリック
        0xc14f: u'ɛ', #
        0xc150: u'θ', # θ
        0xc151: u'ʌ', #
        0xc152: u'ɑ', # ´
        0xc153: u'ə', # ´
        0xc154: u'ɔ', # ´
        0xc155: u'ɛ', # ´
        0xc156: u'ʌ', # ´
        0xc157: u'ɑ', # `
        0xc158: u'ə', # `
        0xc159: u'ɔ', # `
        0xc15a: u'ɛ', # `
        0xc15b: u'ʌ', # `
        0xc15c: (u'æ', u'ae'), # a
        0xc15d: (u'ǽ', u'ae'), #
        0xc15e: (u'æ', u'ae'), # a`
        0xc15f: (u'Æ', u'AE'), # A
        0xc160: u'ɑ', # ~
        0xc161: (u'å', u'a'), # a
        0xc162: u'˘', #
        0xc163: (u'ă', u'a'), #
        0xc164: (u'ŏ', u'o'), #
        0xc165: (u'ĭ', u'i'), #
        0xc166: (u'V́', u'V'), # V´
        0xc167: (u'T́', u'T'), # T´
        0xc168: None, # イタリック
        0xc169: u'ɔ̃', # ~
        0xc16b: None, # イタリック
        0xc16c: (None, u'-'), # -´
        0xc16d: (None, u'-'), # -`
        0xc16e: (None, u'a'), # a~´
        0xc16f: None, # イタリック
        0xc170: (None, u'm'), # m。
        0xc171: (None, u'm'), # m´。
        0xc172: None, #
        0xc173: None, # ~´
        0xc174: None, # ~´
        0xc175: (None, u'ae'), # ae~´
        0xc176: None, # ~´
        0xc177: u'ć', #
        0xc178: None, # ~`
        0xc179: None, # ~`
        0xc17a: (None, u'ae'), # ae~`
        0xc17b: (u'û', u'u'), # u^
        0xc17c: (u'Ý', u'Y'), # Y
        0xc17d: None, # ~`
        0xc17e: (u'Ḿ', u'M'), # M´
        0xc221: None, # ~
        0xc222: (None, u'+'), #
        0xc223: (None, u'X'), #
        0xc224: (u'ō', u'o'), #
        0xc225: (u'ğ', u'g'), # g
        0xc226: (None, u'A'), # イタリック
        0xc227: (None, u'B'), # イタリック
        0xc228: (None, u'D'), # イタリック
        0xc229: (u'Ḍ', u'D'), # D.
        0xc22a: (None, u'E'), # イタリック
        0xc22b: (None, u'F'), # イタリック
        0xc22c: (None, u'G'), # イタリック
        0xc22d: (None, u'H'), # イタリック
        0xc22e: (u'Ḥ', u'H'), # H.
        0xc22f: (None, u'L'), # イタリック
        0xc230: (None, u'M'), # イタリック
        0xc231: (None, u'N'), # イタリック
        0xc232: (None, u'P'), # イタリック
        0xc233: (None, u'Q'), # イタリック
        0xc234: (None, u'R'), # イタリック
        0xc235: (u'Ṛ', u'R'), # R.
        0xc236: (None, u'S'), # イタリック
        0xc237: (u'Ṣ', u'S'), # S.
        0xc238: (None, u'T'), # イタリック
        0xc239: (None, u'V'), # イタリック
        0xc23a: (u'Ẓ', u'Z'), # Z.
        0xc23b: (None, u'a'), # イタリック
        0xc23c: (u'ą', u'a'), # a
        0xc23d: (None, u'b'), # イタリック
        0xc23e: (None, u'c'), # イタリック
        0xc23f: (None, u'd'), # イタリック
        0xc240: (u'ḍ', u'd'), # d.
        0xc241: (None, u'e'), # イタリック
        0xc242: (u'ę', u'e'), # e
        0xc243: (None, u'f'), # イタリック
        0xc244: (None, u'g'), # イタリック
        0xc245: (None, u'h'), # イタリック
        0xc246: (u'ḥ', u'h'), # h.
        0xc247: (None, u'i'), # イタリック
        0xc248: (u'ị', u'i'), # i.
        0xc249: (None, u'k'), # イタリック
        0xc24a: (None, u'l'), # イタリック
        0xc24b: (None, u'm'), #
        0xc24c: (u'ṃ', u'm'), # m.
        0xc24d: (None, u'n'), # イタリック
        0xc24e: (u'ṇ', u'n'), # n.
        0xc24f: (None, u'o'), # イタリック
        0xc250: (None, u'p'), # イタリック
        0xc251: (None, u'q'), # イタリック
        0xc252: (None, u'r'), # イタリック
        0xc253: (u'ṛ', u'r'), # r.
        0xc254: (None, u's'), # イタリック
        0xc255: (u'ş', u's'), # s，
        0xc256: (u'ṣ', u's'), # s.
        0xc257: (None, u't'), # イタリック
        0xc258: (u'ṭ', u't'), # t.
        0xc259: (None, u'v'), # イタリック
        0xc25a: (None, u'x'), # イタリック
        0xc25b: (None, u'y'), # イタリック
        0xc25c: (None, u'z'), # イタリック
        0xc25d: (u'ẓ', u'z'), # z.
        0xc25e: (u'İ', u'I'), #
        0xc25f: (u'ṁ', u'm'), # m
        0xc260: (u'ṅ', u'n'), # n
        0xc261: (u'ż', u'z'), #
        0xc262: (u'Ś', u'S'), #
        0xc263: (u'ć', u'c'), #
        0xc264: (u'ń', u'n'), #
        0xc265: (u'ś', u's'), #
        0xc266: (u'ý', u'y'), # y
        0xc267: (u'ź', u'z'), #
        0xc268: (u'ì', u'i'), # i
        0xc269: (u'Ä', u'A'), # A
        0xc26a: (u'Ö', u'O'), # O
        0xc26b: (u'Ü', u'U'), # U
        0xc26c: (u'ÿ', u'y'), # y
        0xc26d: (u'Â', u'A'), # A
        0xc26e: (None, u'o'), # o^.
        0xc26f: (u'û', u'u'), # u
        0xc270: (u'Ā', u'A'), #
        0xc271: (u'Ē', u'E'), #
        0xc272: (u'Ī', u'I'), #
        0xc273: (u'Ō', u'O'), #
        0xc274: (u'Ū', u'U'), #
        0xc275: (u'ī', u'i'), #
        0xc276: (u'n̄', u'n'), # n
        0xc277: (u'p̄', u'p'), # p
        0xc278: (u'ū', u'u'), #
        0xc279: (u'ȳ', u'y'), # y
        0xc27a: (u'Ł', u'L'), #
        0xc27b: (u'ł', u'l'), #
        0xc27c: (u'ø', u'o'), # o
        0xc27d: (u'ĩ', u'i'), #
        0xc27e: (u'õ', u'o'), # o
        0xc322: (None, u'R'), # R°
        0xc323: (u'º', u'0'), # o
        0xc324: (u'½', u'1/2'), #
        0xc325: (None, u'1/3'), #
        0xc326: (u'¹', u'1'), # 1
        0xc327: (u'²', u'2'), # 2
        0xc328: (u'¾', u'3/4'), #
        0xc329: (u'³', u'3'), # 3
        0xc32a: (None, u'4'), # 上付
        0xc32b: (None, u'5'), # 上付
        0xc32c: (None, u'6'), # 上付
        0xc32d: (None, u'7'), # 上付
        0xc32e: (None, u'8'), # 上付
        0xc32f: (None, u'9'), # 上付
        0xc330: (None, u'M'), # 上付
        0xc331: (None, u'a/b'), #
        0xc332: (None, u'b'), # 上付
        0xc333: None, #
        0xc334: u'ɟ', #
        0xc335: (None, u'i'), # 上付
        0xc336: (None, u'm'), # 上付
        0xc337: (None, u'n'), # 上付
        0xc338: (None, u'r'), # 上付
        0xc339: (None, u't'), # 上付
        0xc33a: (None, u'x'), # 上付
        0xc33b: None, #
        0xc33c: (None, u'y'), # 上付
        0xc33d: (None, u'+'), # 上付
        0xc33e: (None, u'-'), # 上付
        0xc33f: (None, u'+-'), # ±
        0xc340: None, #
        0xc341: (None, u'0'), # 下付
        0xc342: (None, u'1'), # 下付
        0xc343: (None, u'2'), # 下付
        0xc344: (None, u'3'), # 下付
        0xc345: (None, u'4'), # 下付
        0xc346: (None, u'5'), # 下付
        0xc347: (None, u'6'), # 下付
        0xc348: (None, u'7'), # 下付
        0xc349: (None, u'8'), # 下付
        0xc34a: (None, u'9'), # 下付
        0xc34b: (None, u'A'), # 下付
        0xc34c: (None, u'a'), # 下付(α )
        0xc34d: (None, u'b'), # 下付
        0xc34e: (None, u'i'), # 下付
        0xc34f: (None, u'k'), # 下付
        0xc350: (None, u'm'), # 下付
        0xc351: (None, u'n'), # 下付
        0xc352: (None, u'r'), # 下付
        0xc353: (None, u'x'), # 下付
        0xc354: (None, u'一レ'), #
        0xc355: (None, u'+'), #
        0xc356: (None, u'-'), #
        0xc357: (None, u'I'), #
        0xc358: (None, u'W'), #
        0xc359: (None, u'Z'), #
        0xc35a: (u'g̀', u'g'), # g`
        0xc35c: (None, u'$'), #
        0xc35d: (None, u'C'), #
        0xc360: (None, u'レ'), #
        0xc364: (None, u'一'), #
        0xc365: (None, u'下'), #
        0xc366: (None, u'三'), #
        0xc367: (None, u'上'), #
        0xc368: (None, u'上レ'), #
        0xc369: (None, u'中'), #
        0xc36a: (None, u'ニ'), #
        0xc36b: (u'ĕ', u'e'), #
        0xc36c: (u'Č', u'C'), #
        0xc36d: (u'Š', u'S'), #
        0xc36e: (u'ǎ', u'a'), #
        0xc36f: (u'č', u'c'), #
        0xc370: (u'ě', u'e'), #
        0xc371: (u'ň', u'n'), #
        0xc372: (u'ř', u'r'), #
        0xc373: (u'š', u's'), #
        0xc374: (u'ž', u'z'), #
        0xc375: u'ヰ', # ヰ
        0xc376: u'ヱ', # ヱ
        0xc377: u'ɯ̈', # ¨
        0xc378: u'ɰ', #
        0xc379: (None, u'u'), # u~'
        0xc37a: u'ʔ', #
        0xc37b: u'ɦ', #
        0xc37c: (u'ß', u'ss'), # s
        0xc37d: (None, u'I'), #
        0xc37e: (None, u'N'), #
        0xc421: u'ɲ', #
        0xc422: u'ː', #
        0xc423: None, #

    }

    wide_gaiji = {

        0xa121: u'仿', #
        0xa122: u'佉', #
        0xa123: u'侗', #
        0xa124: u'倘', #
        0xa125: u'偓', #
        0xa126: u'傔', # 傔
        0xa127: u'傖', #
        0xa128: u'僄', #
        0xa129: u'僦', #
        0xa12a: u'兕', #
        0xa12b: u'凴', #
        0xa12c: u'刁', #
        0xa12d: u'剉', #
        0xa12e: u'剗', #
        0xa12f: u'劂', #
        0xa130: u'劓', #
        0xa131: u'勖', #
        0xa132: u'卬', #
        0xa133: u'厓', # 厓
        0xa134: u'厲', # 厲
        0xa135: u'呍', #
        0xa136: u'吧', #
        0xa137: u'咜', # 咜
        0xa138: u'呫', #
        0xa139: u'呦', #
        0xa13a: u'咿', #
        0xa13b: u'咩', # 咩
        0xa13c: u'哿', # 哿
        0xa13d: u'唫', #
        0xa13e: u'嘈', #
        0xa13f: u'嘻', #
        0xa140: u'噯', #
        0xa141: u'噲', #
        0xa142: u'嚚', #
        0xa143: u'嚬', #
        0xa144: u'圊', #
        0xa145: u'圯', #
        0xa146: u'坌', #
        0xa147: u'埸', #
        0xa148: u'埶', #
        0xa149: u'埤', #
        0xa14a: u'壔', #
        0xa14b: u'壠', #
        0xa14c: u'壚', #
        0xa14d: u'虁', #
        0xa14e: u'奝', # 奝
        0xa14f: u'奭', #
        0xa150: u'姒', #
        0xa151: u'婥', #
        0xa152: u'婕', #
        0xa153: u'孼', #
        0xa154: u'尫', #
        0xa155: u'屩', #
        0xa156: u'崧', # 崧
        0xa157: u'嵆', #
        0xa158: u'嶠', #
        0xa159: u'嶸', # 嶸
        0xa15a: u'幘', #
        0xa15b: u'庾', #
        0xa15c: u'龐', #
        0xa15d: u'弇', #
        0xa15e: u'彀', #
        0xa15f: u'彐', #
        0xa160: u'彤', #
        0xa161: u'徉', #
        0xa162: u'徜', #
        0xa163: u'徧', #
        0xa164: u'忉', #
        0xa165: u'忼', #
        0xa166: u'忡', #
        0xa167: u'怵', #
        0xa168: u'悝', #
        0xa169: u'惛', #
        0xa16a: u'惕', # 惕
        0xa16b: u'惙', #
        0xa16c: u'惲', # 惲
        0xa16d: u'愷', # 愷
        0xa16e: u'戕', #
        0xa16f: u'扃', #
        0xa170: u'扑', #
        0xa171: u'拖', #
        0xa172: u'拄', #
        0xa173: u'捃', #
        0xa174: u'挹', #
        0xa175: u'摹', #
        0xa176: u'撝', # 撝
        0xa177: u'撿', #
        0xa178: u'昱', # 昱
        0xa179: u'晡', #
        0xa17a: u'皙', # 皙
        0xa17b: u'腊', #
        0xa17c: u'臏', #
        0xa17d: u'杇', #
        0xa17e: u'枘', #
        0xa221: u'杻', #
        0xa222: u'棰', #
        0xa223: u'棖', #
        0xa224: u'楨', # 楨
        0xa225: u'楣', #
        0xa226: u'橛', #
        0xa227: u'櫬', #
        0xa228: u'欛', #
        0xa229: u'歆', #
        0xa22a: u'殂', #
        0xa22b: u'殭', #
        0xa22c: u'毱', #
        0xa22d: u'氅', #
        0xa22e: u'氐', #
        0xa22f: u'氳', #
        0xa230: u'淼', # 淼
        0xa231: u'沅', #
        0xa232: u'沆', # 沆
        0xa233: u'汴', #
        0xa234: u'沔', #
        0xa235: u'泫', #
        0xa236: u'泮', #
        0xa237: u'洄', # 洄
        0xa238: u'洎', #
        0xa239: u'洮', #
        0xa23a: u'浥', #
        0xa23b: u'淄', #
        0xa23c: u'涿', #
        0xa23d: u'淝', #
        0xa23e: u'湜', # 湜
        0xa23f: u'渧', # 渧
        0xa240: u'滃', #
        0xa241: u'漪', #
        0xa242: u'漚', #
        0xa243: u'漳', #
        0xa244: u'澌', #
        0xa245: u'瀆', #
        0xa246: u'灝', #
        0xa247: u'灤', #
        0xa248: u'灎', #
        0xa249: u'炫', # 炫
        0xa24a: u'炷', #
        0xa24b: u'焮', #
        0xa24c: u'焠', #
        0xa24d: u'煜', # 煜
        0xa24e: u'煇', # 煇
        0xa24f: u'煆', # 煆
        0xa250: u'煨', #
        0xa251: u'熅', #
        0xa252: u'熒', #
        0xa253: u'熇', #
        0xa254: u'熳', #
        0xa255: u'燋', #
        0xa256: u'燁', # 燁
        0xa257: u'燾', # 燾
        0xa258: u'凞', #
        0xa259: u'牓', #
        0xa25a: u'牕', #
        0xa25b: u'牖', #
        0xa25c: u'犍', #
        0xa25d: u'犛', #
        0xa25e: u'猨', #
        0xa25f: u'獐', #
        0xa260: u'獷', # 獷
        0xa261: u'獼', #
        0xa262: u'玕', #
        0xa263: u'珉', # 珉
        0xa264: u'琦', # 琦
        0xa265: u'琚', #
        0xa266: u'琨', #
        0xa267: u'璆', #
        0xa268: u'璉', # 璉
        0xa269: u'璟', # 璟
        0xa26a: u'璣', #
        0xa26b: u'璘', #
        0xa26c: u'璨', #
        0xa26d: u'璿', #
        0xa26e: u'瓚', #
        0xa26f: u'畎', #
        0xa270: u'痀', #
        0xa271: u'痤', #
        0xa272: u'瘖', #
        0xa273: u'瘭', #
        0xa274: u'皞', # 皞
        0xa275: u'盎', #
        0xa276: u'盌', #
        0xa277: u'盬', #
        0xa278: u'盼', #
        0xa279: u'眚', #
        0xa27a: u'眙', #
        0xa27b: u'睢', #
        0xa27c: u'睟', #
        0xa27d: u'睜', #
        0xa27e: u'睽', #
        0xa321: u'矰', #
        0xa322: u'矻', #
        0xa323: u'砭', #
        0xa324: u'确', #
        0xa325: u'磈', #
        0xa326: u'磷', #
        0xa327: u'禘', #
        0xa328: u'秔', #
        0xa329: u'窅', #
        0xa32a: u'窠', #
        0xa32b: u'窬', #
        0xa32c: u'窳', #
        0xa32d: u'竽', #
        0xa32e: u'筠', #
        0xa32f: u'簋', #
        0xa330: u'簠', #
        0xa331: u'籮', #
        0xa332: u'糗', #
        0xa333: u'糕', #
        0xa334: u'糝', #
        0xa335: u'紈', #
        0xa336: u'紓', #
        0xa337: u'絇', #
        0xa338: u'絓', #
        0xa339: u'絜', # 絜
        0xa33a: u'絺', #
        0xa33b: u'綈', #
        0xa33c: u'緂', #
        0xa33d: u'縈', #
        0xa33e: u'縕', #
        0xa33f: u'縑', #
        0xa340: u'縠', #
        0xa341: u'縝', #
        0xa342: u'繇', #
        0xa343: u'繒', # 繒
        0xa344: u'繳', #
        0xa345: u'罽', #
        0xa346: u'罾', #
        0xa347: u'翟', #
        0xa348: u'翬', #
        0xa349: u'耦', #
        0xa34a: u'聱', #
        0xa34b: u'艴', #
        0xa34c: u'芎', #
        0xa34d: u'芷', #
        0xa34e: u'芮', #
        0xa34f: u'苾', #
        0xa350: u'茀', #
        0xa351: u'荇', #
        0xa352: u'荃', #
        0xa353: u'莘', #
        0xa354: u'蒯', #
        0xa355: u'蓰', #
        0xa356: u'蕓', # 蕓
        0xa357: u'蕙', # 蕙
        0xa358: u'蕞', #
        0xa359: u'蕤', #
        0xa35a: u'薏', #
        0xa35b: u'藿', #
        0xa35c: u'蘐', #
        0xa35d: u'虗', #
        0xa35e: u'虢', #
        0xa35f: u'虬', #
        0xa360: u'虯', #
        0xa361: u'虺', #
        0xa362: u'蚑', #
        0xa363: u'蚱', #
        0xa364: u'蜋', #
        0xa365: u'蝘', #
        0xa366: u'蝥', #
        0xa367: u'螈', #
        0xa368: u'螭', #
        0xa369: u'蠲', #
        0xa36a: u'裊', #
        0xa36b: u'裛', #
        0xa36c: u'褰', #
        0xa36d: u'袪', #
        0xa36e: u'裎', #
        0xa36f: u'裱', #
        0xa370: u'褚', #
        0xa371: u'觔', #
        0xa372: u'觖', #
        0xa373: u'觳', #
        0xa374: u'訕', #
        0xa375: u'訢', #
        0xa376: u'詘', #
        0xa377: u'詡', #
        0xa378: u'詹', # 詹
        0xa379: u'誾', # 誾
        0xa37a: u'豨', #
        0xa37b: u'豳', #
        0xa37c: u'貒', #
        0xa37d: u'賙', #
        0xa37e: u'贛', #
        0xa421: u'跎', #
        0xa422: u'跗', #
        0xa423: u'踠', #
        0xa424: u'踔', #
        0xa425: u'踽', #
        0xa426: u'蹢', #
        0xa427: u'輞', #
        0xa428: u'輭', #
        0xa429: u'輶', #
        0xa42a: u'轔', #
        0xa42b: u'辧', # 辧
        0xa42c: u'辵', #
        0xa42d: u'辶', # 一点しんにょう
        0xa42e: u'辶', # 二点しんにょう
        0xa42f: u'迤', #
        0xa430: u'邅', #
        0xa431: u'邈', #
        0xa432: u'邛', #
        0xa433: u'邢', #
        0xa434: u'邳', #
        0xa435: u'郅', #
        0xa436: u'鄧', # 鄧
        0xa437: u'鄱', #
        0xa438: u'鄴', #
        0xa439: u'酈', #
        0xa43a: u'酛', #
        0xa43b: u'酤', #
        0xa43c: u'酴', #
        0xa43d: u'醃', #
        0xa43e: u'醞', #
        0xa43f: u'醮', #
        0xa440: u'釃', #
        0xa441: u'釗', # 釗
        0xa442: u'鈐', # 鈐
        0xa443: u'鈇', #
        0xa444: u'鉏', #
        0xa445: u'鉸', # 鉸
        0xa446: u'銈', # 銈
        0xa447: u'鍈', # 鍈
        0xa448: u'鏜', #
        0xa449: u'鐲', #
        0xa44a: u'鑊', #
        0xa44b: u'鑣', #
        0xa44c: u'閒', # 閒
        0xa44d: u'閟', #
        0xa44e: u'閩', #
        0xa44f: u'閽', #
        0xa450: u'闓', #
        0xa451: u'闐', #
        0xa452: u'闚', #
        0xa453: u'闞', #
        0xa454: u'阼', #
        0xa455: u'陘', #
        0xa456: u'隄', #
        0xa457: u'雒', #
        0xa458: u'雞', #
        0xa459: u'雩', #
        0xa45a: u'靛', #
        0xa45b: u'靳', #
        0xa45c: u'鞺', #
        0xa45d: u'韞', #
        0xa45e: u'韛', #
        0xa45f: u'韡', #
        0xa460: u'頫', #
        0xa461: u'顒', #
        0xa462: u'顓', #
        0xa463: u'顗', # 顗
        0xa464: u'顥', # 顥
        0xa465: u'颺', #
        0xa466: u'飥', #
        0xa467: u'餖', #
        0xa468: u'餼', #
        0xa469: u'餻', #
        0xa46a: u'饘', #
        0xa46b: u'駔', #
        0xa46c: u'駙', #
        0xa46d: u'騃', #
        0xa46e: u'騶', #
        0xa46f: u'騸', #
        0xa470: u'魞', #
        0xa471: u'鮏', # 鮏
        0xa472: u'鯁', #
        0xa473: u'鰶', #
        0xa474: u'鴞', #
        0xa475: u'鵷', #
        0xa476: u'鵰', # 鵰
        0xa477: u'鷃', #
        0xa478: u'麨', #
        0xa479: u'麼', # 麼
        0xa47a: u'黧', #
        0xa47b: u'鼂', #
        0xa47c: u'鼯', #
        0xa47d: u'齁', #
        0xa47e: u'齗', #
        0xa521: u'龔', #
        0xa522: u'捥', #
        0xa523: u'楤', #
        0xa524: u'丰', # 異体字
        0xa525: None, # (未使用)
        0xa526: u'挊', #
        0xa527: u'艜', #
        0xa528: u'桒', # 桒
        0xa529: None, # 草書
        0xa52a: None, # 草書
        0xa52b: u'亍', #
        0xa52c: u'亹', #
        0xa52d: u'儞', #
        0xa52e: u'偁', #
        0xa52f: u'儃', #
        0xa530: u'佪', #
        0xa531: u'儋', #
        0xa532: u'儈', #
        0xa533: u'侒', # 侒
        0xa534: u'佷', #
        0xa535: u'伋', #
        0xa536: u'傜', #
        0xa537: u'淸', # 淸
        0xa538: u'卺', #
        0xa539: u'划', #
        0xa53a: u'勑', #
        0xa53b: u'匇', # 匇
        0xa53c: u'匃', #
        0xa53d: u'匜', #
        0xa53e: None, # 「世」の異体字
        0xa53f: u'嗢', #
        0xa540: u'囉', #
        0xa541: u'唽', #
        0xa542: u'嚕', #
        0xa543: u'噱', #
        0xa544: u'嘽', #
        0xa545: u'嚞', #
        0xa546: u'喁', #
        0xa547: u'噞', #
        0xa549: u'哯', #
        0xa54a: u'嚩', #
        0xa54b: u'喈', #
        0xa54d: u'晷', #
        0xa54e: u'叵', #
        0xa54f: u'嗩', #
        0xa550: u'妋', #
        0xa551: u'娭', #
        0xa552: u'嫚', #
        0xa553: u'嬗', #
        0xa555: u'娓', #
        0xa556: u'姞', #
        0xa558: u'孁', #
        0xa559: u'堄', #
        0xa55a: u'埿', #
        0xa55c: u'坍', #
        0xa55d: u'垸', #
        0xa55e: u'坅', #
        0xa55f: u'坷', #
        0xa560: u'壎', #
        0xa561: u'塤', #
        0xa562: u'堠', #
        0xa563: u'墪', #
        0xa564: u'埏', #
        0xa565: u'媳', #
        0xa566: u'墉', #
        0xa567: u'坨', #
        0xa568: u'圩', #
        0xa569: u'尰', #
        0xa56a: u'屟', #
        0xa56b: u'屣', #
        0xa56d: u'异', # 異体字 已/廾
        0xa56f: u'岺', # 岺
        0xa570: u'岏', #
        0xa571: u'巋', #
        0xa572: u'巑', #
        0xa573: u'帔', #
        0xa574: u'幉', #
        0xa575: u'帒', #
        0xa576: u'幞', #
        0xa578: u'彇', #
        0xa579: u'弣', #
        0xa57a: u'弶', #
        0xa57b: u'弽', #
        0xa57c: u'庪', #
        0xa57d: u'擌', #
        0xa621: u'擎', # 擎
        0xa622: u'挗', #
        0xa623: u'擐', #
        0xa624: u'挍', #
        0xa625: u'搯', #
        0xa626: u'擷', #
        0xa627: u'掙', #
        0xa628: u'抳', #
        0xa629: u'攞', #
        0xa62a: u'挃', #
        0xa62b: u'撾', #
        0xa62c: u'摭', #
        0xa62d: u'熮', #
        0xa62f: u'烑', #
        0xa630: u'灵', #
        0xa631: u'煑', #
        0xa632: u'爕', #
        0xa633: u'焄', # 焄
        0xa634: u'獦', #
        0xa635: u'猧', #
        0xa636: u'猽', #
        0xa637: u'獒', #
        0xa638: u'獯', #
        0xa639: u'獫', #
        0xa63a: u'玁', #
        0xa63b: u'狁', #
        0xa63c: u'狻', #
        0xa63d: u'瀼', #
        0xa63e: u'瀣', #
        0xa63f: u'洿', #
        0xa640: u'濊', #
        0xa641: u'澠', #
        0xa642: u'潢', #
        0xa643: u'灊', #
        0xa644: u'淛', #
        0xa645: u'涘', #
        0xa646: u'湌', #
        0xa647: u'灔', #
        0xa649: u'涔', #
        0xa64a: u'涬', # 涬
        0xa64b: u'邾', #
        0xa64c: u'鄘', #
        0xa64d: u'邶', #
        0xa64e: u'鄀', #
        0xa64f: u'鄽', #
        0xa650: u'菇', # 菇
        0xa651: u'菆', #
        0xa652: u'蓀', #
        0xa653: u'藊', #
        0xa654: u'蘅', #
        0xa655: u'芺', #
        0xa656: u'蒺', #
        0xa657: u'蔾', #
        0xa658: u'蘼', #
        0xa659: u'薁', #
        0xa65a: u'葒', #
        0xa65b: u'蓯', #
        0xa65c: u'蒾', #
        0xa65d: u'蘩', #
        0xa65e: u'蔌', #
        0xa65f: u'蔞', #
        0xa660: u'菝', #
        0xa661: u'蕽', #
        0xa662: u'蘡', #
        0xa663: u'茛', #
        0xa664: u'荽', #
        0xa665: u'孽', #
        0xa666: u'葜', #
        0xa667: u'菀', #
        0xa668: u'薟', #
        0xa669: u'芾', #
        0xa66a: u'蘘', #
        0xa66b: u'蔲', #
        0xa66c: u'蔯', #
        0xa66d: u'荗', #
        0xa66e: u'莔', #
        0xa66f: u'噶', #
        0xa670: u'藋', #
        0xa671: u'莧', #
        0xa672: u'苆', #
        0xa673: u'蓪', #
        0xa674: u'萁', #
        0xa675: u'藦', #
        0xa676: u'薷', #
        0xa677: u'蘞', #
        0xa678: u'莕', #
        0xa679: u'蒅', #
        0xa67b: u'芿', #
        0xa67c: u'悆', #
        0xa67d: u'忞', # 忞
        0xa67e: u'惸', #
        0xa721: u'惝', #
        0xa722: u'怳', #
        0xa723: u'惔', #
        0xa724: u'怍', #
        0xa725: u'惋', #
        0xa726: u'扆', #
        0xa727: u'曛', #
        0xa728: u'昀', # 昀
        0xa729: u'昪', #
        0xa72a: u'暍', #
        0xa72b: u'臗', #
        0xa72c: u'臛', #
        0xa72d: u'膘', #
        0xa72e: u'榺', #
        0xa72f: u'樾', #
        0xa730: u'櫆', #
        0xa731: u'柀', # 柀
        0xa732: u'棱', #
        0xa733: u'橒', #
        0xa734: u'檞', #
        0xa735: u'檨', #
        0xa736: u'杮', #
        0xa737: u'楉', #
        0xa738: u'樻', #
        0xa73a: u'桕', #
        0xa73b: u'棼', #
        0xa73c: u'槾', #
        0xa73d: u'楗', #
        0xa73e: u'棙', #
        0xa740: u'桄', # 桄
        0xa741: u'杴', #
        0xa742: u'枒', #
        0xa743: u'檫', #
        0xa744: u'杈', #
        0xa745: u'欋', #
        0xa746: u'棅', #
        0xa747: u'榀', #
        0xa748: u'棻', #
        0xa749: u'栭', #
        0xa74a: u'榭', #
        0xa74b: u'棌', #
        0xa74c: u'欵', #
        0xa74d: u'殩', #
        0xa74e: u'殮', #
        0xa74f: u'槩', #
        0xa750: u'櫲', #
        0xa753: u'穀', # 穀
        0xa754: u'蒁', #
        0xa755: u'迱', #
        0xa757: u'适', #
        0xa758: u'逈', #
        0xa759: u'迍', #
        0xa75a: u'逭', #
        0xa75b: u'迮', #
        0xa75c: u'璈', #
        0xa75d: u'瑄', #
        0xa75e: u'璱', #
        0xa75f: u'玦', #
        0xa760: u'琯', #
        0xa761: u'璙', #
        0xa762: u'珅', #
        0xa763: u'珣', # 珣
        0xa764: u'玠', #
        0xa765: u'瓈', #
        0xa766: u'璫', #
        0xa767: u'琫', #
        0xa768: u'瑍', #
        0xa769: u'琊', #
        0xa76a: u'疿', #
        0xa76b: u'癕', #
        0xa76c: u'皥', #
        0xa76d: u'皪', #
        0xa76e: u'盦', #
        0xa76f: u'盔', #
        0xa770: u'瞔', #
        0xa771: u'睠', #
        0xa773: u'瞟', #
        0xa774: u'瞍', #
        0xa775: u'眶', #
        0xa777: u'畾', #
        0xa778: u'矪', #
        0xa779: u'矬', #
        0xa77a: u'穭', #
        0xa77c: u'袽', #
        0xa77d: u'襅', #
        0xa77e: u'筯', #
        0xa821: u'帘', #
        0xa822: u'笇', #
        0xa823: u'篗', #
        0xa824: u'籡', #
        0xa825: u'籗', #
        0xa826: u'褲', #
        0xa827: u'褙', #
        0xa828: u'粿', #
        0xa82b: u'縬', #
        0xa82c: u'罇', # 罇
        0xa82d: u'纆', #
        0xa82e: u'耖', #
        0xa82f: u'耟', #
        0xa830: u'艉', #
        0xa831: u'賾', #
        0xa832: u'蟫', #
        0xa833: u'蜺', #
        0xa834: u'蚨', #
        0xa835: u'蟭', #
        0xa836: u'蠐', #
        0xa837: u'螬', #
        0xa838: u'蜟', #
        0xa839: u'蠼', #
        0xa83a: u'螋', #
        0xa83b: u'蚍', #
        0xa83c: u'蟟', #
        0xa83d: u'蛁', #
        0xa83e: u'蜞', #
        0xa841: u'蝯', #
        0xa843: u'鵒', #
        0xa844: u'鴝', #
        0xa845: u'鸜', #
        0xa846: u'鸇', #
        0xa847: u'鶖', #
        0xa849: u'鸍', #
        0xa84a: u'鵩', #
        0xa84b: u'鶡', #
        0xa84c: u'鷴', #
        0xa84e: u'鷧', #
        0xa84f: u'鏌', #
        0xa850: u'鎁', #
        0xa851: u'鍱', #
        0xa852: u'銙', #
        0xa853: u'釭', # 釭
        0xa854: u'鉧', # 鉧
        0xa855: u'鍑', #
        0xa856: u'鏽', #
        0xa857: u'錕', #
        0xa858: u'鋂', #
        0xa859: u'鋧', # 鋧
        0xa85a: u'鐴', #
        0xa85c: u'鋐', # 鋐
        0xa85d: u'蹔', #
        0xa85f: u'踶', #
        0xa860: u'詵', #
        0xa861: u'諐', #
        0xa862: u'誮', #
        0xa863: u'謭', #
        0xa864: u'誷', #
        0xa865: u'觶', #
        0xa866: u'釄', #
        0xa867: u'醼', #
        0xa868: u'醨', #
        0xa869: u'釱', #
        0xa86a: u'釻', #
        0xa86b: u'鎛', #
        0xa86c: u'鐧', #
        0xa86e: u'鉃', #
        0xa86f: u'纇', #
        0xa870: u'熲', #
        0xa871: u'頞', #
        0xa872: u'顖', #
        0xa873: u'蒴', # 蒴
        0xa874: u'蕺', #
        0xa875: u'芩', #
        0xa876: u'佺', #
        0xa877: u'佾', #
        0xa878: u'俏', #
        0xa879: u'倻', #
        0xa87a: u'儵', #
        0xa87b: u'噦', #
        0xa87c: u'嗉', #
        0xa87d: u'嘰', #
        0xa87e: u'吒', #
        0xa921: u'唵', #
        0xa922: u'唼', #
        0xa923: u'埦', #
        0xa924: u'墝', #
        0xa925: u'埵', #
        0xa926: u'垜', #
        0xa927: u'墩', #
        0xa928: u'圳', #
        0xa929: u'壒', #
        0xa92a: u'羗', #
        0xa92b: u'搢', #
        0xa92c: u'搩', #
        0xa92d: u'攩', #
        0xa92e: u'擤', #
        0xa92f: u'挵', #
        0xa930: u'拼', #
        0xa931: u'擻', #
        0xa932: u'掽', #
        0xa933: u'湑', #
        0xa934: u'濹', #
        0xa935: u'泔', #
        0xa936: u'犎', #
        0xa937: u'桛', #
        0xa938: u'梣', #
        0xa939: u'樏', #
        0xa93a: u'梻', #
        0xa93b: u'橐', #
        0xa93c: u'梘', #
        0xa93d: u'梲', #
        0xa93e: u'橅', #
        0xa93f: u'檉', #
        0xa941: u'櫧', #
        0xa942: u'枻', # 枻
        0xa943: u'柃', #
        0xa944: u'栱', #
        0xa945: u'栬', #
        0xa946: u'樝', #
        0xa947: u'橖', #
        0xa948: u'朳', #
        0xa949: u'棭', #
        0xa94a: u'梂', #
        0xa94c: u'榰', #
        0xa94d: u'柷', #
        0xa94e: u'槵', #
        0xa94f: u'檔', #
        0xa950: u'桫', #
        0xa951: u'欏', #
        0xa952: u'枓', #
        0xa953: u'楲', #
        0xa954: u'腭', #
        0xa955: u'胳', #
        0xa956: u'腨', #
        0xa957: u'朓', #
        0xa958: u'鰧', #
        0xa959: u'蓏', #
        0xa95a: u'玫', #
        0xa95b: u'琰', #
        0xa95c: u'瑇', #
        0xa95d: u'璩', #
        0xa95e: u'珧', #
        0xa95f: u'瑀', #
        0xa960: u'瑒', #
        0xa961: u'瑭', #
        0xa962: u'玔', #
        0xa963: u'珖', # 珖
        0xa964: u'玢', #
        0xa965: u'皶', #
        0xa966: u'麬', #
        0xa967: u'硨', #
        0xa968: u'磠', #
        0xa969: u'磤', #
        0xa96a: u'磲', #
        0xa96b: u'砍', #
        0xa96c: u'硾', #
        0xa96d: u'碰', #
        0xa96e: u'硇', #
        0xa96f: u'礀', #
        0xa970: u'畺', #
        0xa971: u'裰', #
        0xa972: u'裑', #
        0xa973: u'袘', #
        0xa974: u'襀', #
        0xa975: u'裓', #
        0xa977: u'褘', #
        0xa978: u'褹', #
        0xa979: u'襢', #
        0xa97a: u'褨', #
        0xa97b: u'篊', #
        0xa97c: u'笧', #
        0xa97d: u'簁', #
        0xa97e: u'簎', #
        0xaa21: u'簶', #
        0xaa22: u'籰', #
        0xaa23: u'籙', #
        0xaa24: u'籭', #
        0xaa25: u'箯', #
        0xaa26: u'籑', #
        0xaa27: u'荇', #
        0xaa28: u'蓎', #
        0xaa29: u'笯', #
        0xaa2b: u'篅', #
        0xaa2c: u'簳', #
        0xaa2d: u'簹', #
        0xaa2e: u'篔', #
        0xaa31: u'筲', #
        0xaa32: u'笭', #
        0xaa33: u'筎', #
        0xaa34: u'羖', #
        0xaa35: u'籹', #
        0xaa36: u'粏', #
        0xaa37: u'糈', #
        0xaa38: u'糫', #
        0xaa39: u'粼', #
        0xaa3a: u'粔', #
        0xaa3b: u'粶', #
        0xaa3c: u'糙', #
        0xaa3d: u'糄', #
        0xaa3e: u'粬', #
        0xaa3f: u'糵', #
        0xaa40: u'紽', #
        0xaa41: u'緌', #
        0xaa42: u'絁', #
        0xaa43: u'紇', #
        0xaa44: u'纑', #
        0xaa45: u'緦', #
        0xaa46: u'紞', #
        0xaa47: u'纍', #
        0xaa49: u'羿', #
        0xaa4a: u'翺', #
        0xaa4b: u'翥', #
        0xaa4c: u'羕', #
        0xaa4d: u'蝲', #
        0xaa4e: u'蟖', #
        0xaa4f: u'蚸', #
        0xaa50: u'蜓', #
        0xaa51: u'蜾', #
        0xaa52: u'螇', #
        0xaa53: u'蠁', #
        0xaa54: u'蜱', #
        0xaa56: u'蛺', #
        0xaa57: u'虵', #
        0xaa58: u'蝱', #
        0xaa59: u'蠔', #
        0xaa5a: u'蝤', #
        0xaa5b: u'蛑', #
        0xaa5c: u'蠊', #
        0xaa5d: u'蠆', #
        0xaa5e: u'螠', #
        0xaa5f: u'鈸', #
        0xaa60: u'錑', #
        0xaa61: u'鎺', #
        0xaa62: u'鍰', # 鍰
        0xaa63: u'鏁', #
        0xaa64: u'銲', #
        0xaa65: u'鈹', # 鈹
        0xaa66: u'鏟', #
        0xaa67: u'鐖', #
        0xaa68: u'鑯', #
        0xaa69: u'闋', #
        0xaa6b: u'鏱', #
        0xaa6c: u'鈼', # 鈼
        0xaa6e: u'鬌', #
        0xaa6f: u'鞖', #
        0xaa70: u'靪', #
        0xaa71: u'鞚', #
        0xaa72: u'靮', #
        0xaa73: u'鬠', #
        0xaa74: u'鱘', #
        0xaa75: u'鮬', #
        0xaa76: u'鱰', #
        0xaa77: u'鱪', #
        0xaa78: u'鯳', #
        0xaa79: u'鱵', #
        0xaa7a: u'鯯', #
        0xaa7b: u'鯧', #
        0xaa7c: u'魳', #
        0xaa7d: u'鯎', #
        0xaa7e: u'鯥', #
        0xab21: u'鮄', #
        0xab22: u'鱩', #
        0xab23: u'鱮', #
        0xab24: u'鯇', #
        0xab25: u'鮞', #
        0xab26: u'鰖', #
        0xab27: u'鮸', #
        0xab28: u'鯷', #
        0xab29: u'魬', #
        0xab2a: u'鯘', #
        0xab2b: u'鱫', #
        0xab2c: u'鱝', #
        0xab2d: u'鱏', #
        0xab2e: u'鱓', #
        0xab2f: u'鰱', #
        0xab30: u'鮊', #
        0xab31: u'鱛', #
        0xab32: u'鮾', #
        0xab33: u'鱁', #
        0xab34: u'鮧', #
        0xab35: u'魦', #
        0xab36: u'鱭', #
        0xab37: u'孒', #
        0xab38: u'甪', #
        0xab39: u'厴', #
        0xab3a: u'尩', #
        0xab3b: u'车', # 車の簡体字
        0xab3c: u'电', # 電の簡体字
        0xab3d: u'邌', #
        0xab3e: u'仐', #
        0xab3f: u'么', #
        0xab40: u'蠃', #
        0xab41: u'兗', #
        0xab42: u'矠', #
        0xab43: u'矟', #
        0xab44: u'劻', #
        0xab45: u'勰', #
        0xab46: u'斲', #
        0xab47: u'姧', #
        0xab48: u'嬥', #
        0xab49: u'妤', # 妤
        0xab4a: u'媞', #
        0xab4c: u'廋', #
        0xab4d: u'庿', #
        0xab4e: u'愒', #
        0xab4f: u'憍', #
        0xab50: u'愐', #
        0xab51: u'豇', #
        0xab52: u'豉', #
        0xab53: u'雘', #
        0xab54: u'彔', #
        0xab55: u'邕', #
        0xab56: u'隺', #
        0xab57: u'幫', #
        0xab58: u'帮', #
        0xab59: u'毈', #
        0xab5b: u'彽', #
        0xab5c: u'徸', #
        0xab5d: u'鄯', #
        0xab5e: u'郄', #
        0xab5f: u'邙', #
        0xab60: u'隩', #
        0xab61: u'犰', #
        0xab62: u'狳', #
        0xab63: u'獱', #
        0xab64: u'貛', #
        0xab65: u'攲', #
        0xab66: u'爗', #
        0xab67: u'滎', #
        0xab68: u'煠', #
        0xab69: u'燄', #
        0xab6a: u'炻', # 炻
        0xab6b: u'烤', #
        0xab6c: u'炗', #
        0xab6d: u'剡', #
        0xab6e: u'昉', # 昉
        0xab6f: u'昰', #
        0xab70: u'甗', #
        0xab72: u'瓫', #
        0xab74: u'敔', #
        0xab75: u'忩', #
        0xab76: u'毿', #
        0xab77: u'瘵', #
        0xab78: u'痎', #
        0xab79: u'癋', #
        0xab7a: u'疒', #
        0xab7b: u'癤', #
        0xab7c: u'癭', #
        0xab7d: u'瘙', #
        0xab7e: u'痟', #
        0xac21: u'痏', #
        0xac22: u'眴', #
        0xac23: u'睺', #
        0xac24: u'毗', #
        0xac25: u'翮', #
        0xac27: u'稭', #
        0xac28: u'稹', #
        0xac29: u'祆', #
        0xac2a: u'禖', #
        0xac2b: u'皁', #
        0xac2c: u'皝', #
        0xac2d: u'翃', #
        0xac2e: u'舢', #
        0xac2f: u'艠', #
        0xac32: u'趯', #
        0xac33: u'醶', #
        0xac34: u'跑', #
        0xac35: u'蹰', #
        0xac36: u'躃', #
        0xac37: u'跆', #
        0xac38: u'韉', #
        0xac39: u'饠', #
        0xac3a: u'躻', #
        0xac3b: u'髹', #
        0xac3c: u'髁', #
        0xac3d: u'餛', #
        0xac3e: u'餺', #
        0xac3f: u'飣', #
        0xac40: u'飰', #
        0xac41: u'饆', #
        0xac42: u'靏', # 靏
        0xac43: u'閦', #
        0xac44: u'闈', #
        0xac45: u'顬', #
        0xac46: u'頊', #
        0xac47: u'骶', #
        0xac48: u'髐', #
        0xac4a: u'鶍', #
        0xac4b: u'鴲', #
        0xac4c: u'鸕', #
        0xac4d: u'鵼', #
        0xac4e: u'鷀', #
        0xac50: u'鼹', #
        0xac51: u'鼷', #
        0xac52: u'髖', #
        0xac54: u'鸊', #
        0xac55: u'鷉', #
        0xac56: u'鵟', #
        0xac57: u'鷟', #
        0xac58: u'鵂', #
        0xac59: u'鶹', #
        0xac5a: u'鴗', #
        0xac5b: u'鷚', #
        0xac5c: u'鵇', #
        0xac5d: u'鶊', #
        0xac5e: u'鶼', #
        0xac5f: u'觫', #
        0xac60: u'觘', #
        0xac61: u'觿', #
        0xac62: u'剕', #
        0xac63: u'颸', #
        0xac64: u'飇', #
        0xac65: u'飈', #
        0xac66: u'贉', #
        0xac67: u'賖', #
        0xac68: u'赬', #
        0xac69: u'鼗', #
        0xac6a: u'鼐', #
        0xac6b: u'鼺', #
        0xac6c: u'齝', #
        0xac6d: u'齭', #
        0xac6e: u'齵', #
        0xac6f: u'龗', #
        0xac70: u'蓂', #
        0xac71: u'藎', #
        0xac72: u'葼', #
        0xac73: u'茼', #
        0xac74: u'藭', #
        0xac75: u'薼', #
        0xac76: u'菪', #
        0xac77: u'莩', #
        0xac78: u'蓽', #
        0xac79: u'苕', #
        0xac7a: u'芡', #
        0xac7b: u'茺', #
        0xac7d: u'蔤', #
        0xad21: u'葈', # 葈
        0xad22: u'你', #
        0xad23: u'儛', #
        0xad25: u'塼', #
        0xad26: u'坼', #
        0xad27: u'塌', #
        0xad28: u'垿', #
        0xad29: u'姮', #
        0xad2a: u'媧', #
        0xad2b: u'嬙', #
        0xad2c: u'渲', #
        0xad2d: u'洦', #
        0xad2e: u'滇', #
        0xad2f: u'潙', #
        0xad30: u'澶', #
        0xad31: u'涮', #
        0xad32: u'涪', #
        0xad33: u'啐', #
        0xad34: u'嚈', #
        0xad35: u'噠', #
        0xad36: u'弴', # 弴
        0xad37: u'哆', #
        0xad38: u'嚳', #
        0xad39: u'洱', #
        0xad3a: u'灃', #
        0xad3b: u'濞', #
        0xad3c: u'湉', #
        0xad3d: u'泆', #
        0xad3e: u'洹', #
        0xad3f: u'昫', #
        0xad40: u'暠', # 暠
        0xad41: u'昕', # 昕
        0xad42: u'昺', #
        0xad43: u'桲', #
        0xad44: u'橉', #
        0xad45: u'窼', #
        0xad46: u'穇', #
        0xad47: u'秫', #
        0xad48: u'秭', #
        0xad49: u'禛', # 禛
        0xad4a: u'祜', #
        0xad4b: u'祹', #
        0xad4c: u'蜇', #
        0xad4d: u'蛼', #
        0xad4e: u'蚜', #
        0xad4f: u'蚉', #
        0xad50: u'蛽', #
        0xad52: u'螵', #
        0xad53: u'蚇', #
        0xad54: u'螓', #
        0xad55: u'蜐', #
        0xad56: u'瘀', #
        0xad58: u'瘼', #
        0xad5a: u'痱', #
        0xad5b: u'癯', #
        0xad5c: u'癁', #
        0xad5d: u'礴', #
        0xad5e: u'礜', #
        0xad5f: u'砉', #
        0xad60: u'耷', #
        0xad61: u'耼', #
        0xad63: u'軑', #
        0xad64: u'轘', #
        0xad65: u'輀', #
        0xad66: u'魹', #
        0xad67: u'韴', #
        0xad68: u'鞲', #
        0xad6b: u'鮲', #
        0xad6d: u'鰘', #
        0xad6f: u'鰙', #
        0xad70: u'鯝', #
        0xad71: u'鰣', #
        0xad72: u'鯽', #
        0xad74: u'魶', #
        0xad75: u'鰚', #
        0xad76: u'鱲', #
        0xad77: u'鱜', #
        0xad79: u'鱊', #
        0xad7a: u'鱐', #
        0xad7b: u'鱟', #
        0xad7c: u'魣', #
        0xad7d: u'魫', #
        0xad7e: u'驎', # 驎
        0xae21: u'麯', #
        0xae22: u'驌', #
        0xae23: u'騮', #
        0xae24: u'驊', # 異体字
        0xae25: u'駃', #
        0xae26: u'騠', #
        0xae27: u'駰', #
        0xae28: u'騭', #
        0xae29: u'麅', #
        0xae2a: u'麞', #
        0xae2c: None, # にんべん
        0xae2d: u'乚', #
        0xae2e: None, # u2E8B( )
        0xae2f: u'氵', #
        0xae30: u'艹', #
        0xae31: u'艹', #
        0xae32: u'扌', #
        0xae33: u'阝', #
        0xae34: u'犭', #
        0xae35: u'阝', #
        0xae36: u'刂', #
        0xae37: None, # やね
        0xae38: u'忄', #
        0xae39: None, # u2EB3( )
        0xae3a: u'耂', #
        0xae3b: u'爫', #
        0xae3c: None, # のつ
        0xae3d: u'灬', #
        0xae3e: None, # u38FA( )
        0xae3f: u'氺', #
        0xae40: None, # 王偏 &M020824;
        0xae41: u'罒', #
        0xae42: u'礻', #
        0xae43: u'衤', #
        0xae44: u'飠', # 食
        0xae45: None, # 食
        0xae46: None, # 「末」の初二画
        0xae47: None, # すてふで
        0xae48: None, # 合字（トキ）
        0xae49: None, # 合字（こと）
        0xae4a: None, # かりがねてん
        0xae4b: None, # 「玄」の欠画
        0xae4c: None, # 「統」の欠画
        0xae4d: None, # たまへんの偏
        0xae4e: None, # の部分
        0xae4f: None, # 一字金輪仏頂尊
        0xae51: None, # 異体文字「こ」
        0xae52: None, # 異体文字「は」
        0xae53: None, # 変体仮名「い」
        0xae54: None, # 変体仮名「た」
        0xae55: None, # 変体仮名「か」
        0xae56: (None, u'*'), #
        0xae57: (None, u'**'), #
        0xae58: u'©', # c
        0xae59: u'♮', #
        0xae5a: None, # 《楽》延長記号
        0xae5b: None, # 《楽》延長記号
        0xae5c: None, # 16分音符
        0xae5d: (None, u'***'), #
        0xae5e: (None, u'*'), # 上付*
        0xae5f: (u'㊙', u'(秘)'), #
        0xae60: u'☞', #
        0xae61: None, # 《楽》スラー
        0xae62: None, # 《楽》スラー
        0xae63: None, # フランス王家のイチハツ紋
        0xae64: None, # ハーケンクロイツ(45度傾く)
        0xae65: None, # 右まんじ(卍の逆)
        0xae66: None, # tick 照合〔チェック〕の印
        0xae67: None, # 古英語のp(近代のth)
        0xae68: (None, u'c/o'), # care of
        0xae69: (u'®', u'(R)'), # R
        0xae6a: (None, u'3√a'), #
        0xae6b: (u'Æ', u'AE'), # A
        0xae6c: (u'æ', u'ae'), # a
        0xae6d: (None, u'ffi'), # uFB03
        0xae6e: (u'ﬂ', u'fl'), #
        0xae6f: (None, u'n√'), #
        0xae70: (u'œ', u'oe'), #
        0xae71: (u'∘', u'○'), #
        0xae72: (None, u'+-'), # +と-を合わせた記号
        0xae73: None, # やまがた
        0xae74: u'℧', #
        0xae75: (None, u'√2'), #
        0xae76: (None, u'√a'), #
        0xae77: u'©', # c
        0xae78: (None, u'(公)'), #
        0xae79: (u'㊜', u'(適)'), # 丸適マーク
        0xae7a: (u'〖', u'【'), #
        0xae7b: (u'〗', u'】'), #
        0xae7c: None, # (未使用)
        0xae7d: None, # (未使用)
        0xae7e: None, # (未使用)
        0xaf21: None, # (未使用)
        0xaf22: None, # (未使用)
        0xaf23: None, # (未使用)
        0xaf24: None, # (未使用)
        0xaf25: None, # (未使用)
        0xaf26: None, # (未使用)
        0xaf27: None, # (未使用)
        0xaf28: None, # (未使用)
        0xaf29: None, # (未使用)
        0xaf2a: None, # (未使用)
        0xaf2b: None, # (未使用)
        0xaf2c: None, # (未使用)
        0xaf2d: None, # (未使用)
        0xaf2e: None, # (未使用)
        0xaf2f: None, # (未使用)
        0xaf30: None, # (未使用)
        0xaf31: None, # (未使用)
        0xaf32: None, # (未使用)
        0xaf33: None, # (未使用)
        0xaf34: None, # (未使用)
        0xaf35: None, # (未使用)
        0xaf36: None, # (未使用)
        0xaf37: None, # (未使用)
        0xaf38: None, # (未使用)
        0xaf39: None, # (未使用)
        0xaf3a: None, # (未使用)
        0xaf3b: None, # (未使用)
        0xaf3c: None, # (未使用)
        0xaf3d: None, # (未使用)
        0xaf3e: None, # (未使用)
        0xaf3f: None, # (未使用)
        0xaf40: None, # (未使用)
        0xaf41: None, # (未使用)
        0xaf42: None, # (未使用)
        0xaf43: None, # (未使用)
        0xaf44: None, # (未使用)
        0xaf45: None, # (未使用)
        0xaf46: None, # (未使用)
        0xaf47: None, # (未使用)
        0xaf48: None, # (未使用)
        0xaf49: None, # (未使用)
        0xaf4a: None, # (未使用)
        0xaf4b: None, # (未使用)
        0xaf4c: None, # (未使用)
        0xaf4d: None, # (未使用)
        0xaf4e: None, # (未使用)
        0xaf4f: None, # (未使用)
        0xaf50: None, # (未使用)
        0xaf51: None, # (未使用)
        0xaf52: None, # (未使用)
        0xaf53: None, # (未使用)
        0xaf54: None, # (未使用)
        0xaf55: None, # (未使用)
        0xaf56: None, # (未使用)
        0xaf57: None, # (未使用)
        0xaf58: None, # (未使用)
        0xaf59: None, # (未使用)
        0xaf5a: None, # (未使用)
        0xaf5b: None, # (未使用)
        0xaf5c: None, # (未使用)
        0xaf5d: None, # (未使用)
        0xaf5e: None, # (未使用)
        0xaf5f: None, # (未使用)
        0xaf60: None, # (未使用)
        0xaf61: None, # (未使用)
        0xaf62: None, # (未使用)
        0xaf63: None, # (未使用)
        0xaf64: None, # (未使用)
        0xaf65: None, # (未使用)
        0xaf66: None, # (未使用)
        0xaf67: None, # (未使用)
        0xaf68: None, # (未使用)
        0xaf69: None, # (未使用)
        0xaf6a: None, # (未使用)
        0xaf6b: None, # (未使用)
        0xaf6c: None, # (未使用)
        0xaf6d: None, # (未使用)
        0xaf6e: None, # (未使用)
        0xaf6f: None, # (未使用)
        0xaf70: None, # (未使用)
        0xaf71: None, # (未使用)
        0xaf72: None, # (未使用)
        0xaf73: None, # (未使用)
        0xaf74: None, # (未使用)
        0xaf75: None, # (未使用)
        0xaf76: None, # (未使用)
        0xaf77: None, # (未使用)
        0xaf78: None, # (未使用)
        0xaf79: None, # (未使用)
        0xaf7a: None, # (未使用)
        0xaf7b: None, # (未使用)
        0xaf7c: None, # (未使用)
        0xaf7d: None, # (未使用)
        0xaf7e: None, # (未使用)
        0xb021: None, # (未使用)
        0xb022: None, # (未使用)
        0xb023: None, # (未使用)
        0xb024: None, # (未使用)
        0xb025: None, # (未使用)
        0xb026: None, # (未使用)
        0xb027: None, # (未使用)
        0xb028: None, # (未使用)
        0xb029: None, # (未使用)
        0xb02a: None, # (未使用)
        0xb02b: None, # (未使用)
        0xb02c: None, # (未使用)
        0xb02d: None, # (未使用)
        0xb02e: None, # (未使用)
        0xb02f: None, # (未使用)
        0xb030: None, # (未使用)
        0xb031: None, # (未使用)
        0xb032: None, # 卦を表す横段。（陰）
        0xb033: None, # 卦を表す横段。（陽）
        0xb034: u'☰', #
        0xb035: u'☷', #
        0xb036: u'☱', #
        0xb037: u'☲', #
        0xb038: u'☴', #
        0xb039: u'☵', #
        0xb03a: u'☶', #
        0xb03b: None, # u3033
        0xb03c: None, # u3034
        0xb03d: None, # u3035
        0xb03e: None, # u303B 二の字点
        0xb03f: None, # 複十字
        0xb040: u'℉', #
        0xb041: u'〽', # いおりてん
        0xb042: u'卍', # 卍
        0xb043: u'♨', # 温泉マーク
        0xb044: u'♠', #
        0xb045: u'♥', #
        0xb046: None, # フェルマータ
        0xb047: None, # オンス
        0xb048: None, # ホの異体文字
        0xb049: None, # いおりてん
        0xb04a: u'♩', #
        0xb04b: None, # ダルセーニョ
        0xb04c: None, # 重嬰記号
        0xb04d: (u'❶', u'(1)'), #
        0xb04e: (u'❷', u'(2)'), #
        0xb04f: (u'❸', u'(3)'), #
        0xb050: (u'❹', u'(4)'), #
        0xb051: (u'❺', u'(5)'), #
        0xb052: (u'❻', u'(6)'), #
        0xb053: (u'❼', u'(7)'), #
        0xb054: (u'❽', u'(8)'), #
        0xb055: (u'❾', u'(9)'), #
        0xb056: (u'❿', u'(10)'), #
        0xb057: (u'⓫', u'(11)'), #
        0xb058: (u'⓬', u'(12)'), #
        0xb059: (u'⓭', u'(13)'), #
        0xb05a: (u'⓮', u'(14)'), #
        0xb05b: (u'⓯', u'(15)'), #
        0xb05c: (u'⓰', u'(16)'), #
        0xb05d: (u'⓱', u'(17)'), #
        0xb05e: (u'⓲', u'(18)'), #
        0xb05f: (u'⓳', u'(19)'), #
        0xb060: None, # 小さい「ゑ」
        0xb061: (None, u'ガ'), # 小さい文字
        0xb062: None, # (未使用)
        0xb063: None, # (未使用)
        0xb064: None, # (未使用)
        0xb065: (None, u'ト'), # 小さい文字
        0xb066: (u'ノ', u'ノ'), # ノ 小さい文字
        0xb067: None, # (未使用)
        0xb068: (None, u'ミ'), #
        0xb069: None, # (未使用)
        0xb06a: (None, u'ロ'), #
        0xb06b: u'ヰ', # ヰ
        0xb06c: (None, u'ン'), #
        0xb06d: None, # (未使用)
        0xb06e: None, # (未使用)
        0xb06f: None, # (未使用)
        0xb070: None, # (未使用)
        0xb071: None, # (未使用)
        0xb072: None, # (未使用)
        0xb073: None, # (未使用)
        0xb074: None, # (未使用)
        0xb075: None, # (未使用)
        0xb076: None, # (未使用)
        0xb077: u'㏋', # HP
        0xb078: (None, u'(〒)'), # ▽〒
        0xb079: (None, u'(〒)'), # ○〒

        # CJK拡張漢字A *-JIS2004にある文字
        0xa577: u'㡜', # (Ext-A)*
        0xa62e: u'㸅', # (Ext-A)*
        0xa85e: u'䟽', # (Ext-A)*
        0xa86d: u'䥫', # (Ext-A)
        0xa940: u'㮶', # (Ext-A)*
        0xaa2f: u'䈇', # (Ext-A)*
        0xaa30: u'䇮', # (Ext-A)*
        0xac49: u'䯊', # (Ext-A)*
        0xac4f: u'䳑', # (Ext-A)*
        0xad57: u'㾮', # (Ext-A)*
        0xae50: u'㐂', # (Ext-A)*

        # CJK拡張漢字B *-JIS2004にある文字
        0xa548: u'𠵅', # (Ext-B)*
        0xa54c: u'𠺕', # (Ext-B)*
        0xa554: u'𡝂', # (Ext-B)*
        0xa55b: u'𡑮', # (Ext-B)*
        0xa56c: u'𡱖', # (Ext-B)*
        0xa57e: u'𢷡', # (Ext-B)*
        0xa648: u'𤂖', # (Ext-B)*
        0xa73f: u'𣑊', # (Ext-B)*
        0xa751: u'𣏕', # (Ext-B)*
        0xa756: u'𨗈', # (Ext-B)*
        0xa772: u'𥄢', # (Ext-B)*
        0xa776: u'𥉁', # (Ext-B)
        0xa77b: u'𧘱', # (Ext-B)*
        0xa829: u'𥻨', # (Ext-B)*
        0xa82a: u'𦀌', # (Ext-B)*
        0xa83f: u'𧏛', # (Ext-B)*
        0xa842: u'𪆐', # (Ext-B)*
        0xa848: u'𪃹', # (Ext-B)*
        0xa94b: u'𣜌', # (Ext-B)*
        0xa976: u'𧚄', # (Ext-B)*
        0xaa2a: u'𥫱', # (Ext-B)*
        0xaa48: u'𥿠', # (Ext-B)*
        0xaa55: u'𧐐', # (Ext-B)*
        0xaa6a: u'𨵦', # (Ext-B)
        0xaa6d: u'𨫤', # (Ext-B)*
        0xab5a: u'𢏳', # (Ext-B)
        0xab71: u'𤭯', # (Ext-B)*
        0xab73: u'𤚥', # (Ext-B)*
        0xac26: u'𥝱', # (Ext-B)*
        0xac30: u'𦨞', # (Ext-B)*
        0xac53: u'𪀚', # (Ext-B)*
        0xad24: u'𦬇', # (Ext-B)
        0xad51: u'𧉫', # (Ext-B)
        0xad59: u'𤸎', # (Ext-B)*
        0xad62: u'𨏍', # (Ext-B)*
        0xad69: u'𩊱', # (Ext-B)*
        0xad6a: u'𩊠', # (Ext-B)*
        0xad6e: u'𩸭', # (Ext-B)
        0xad73: u'𩸽', # (Ext-B)*
        0xad78: u'𩺊', # (Ext-B)*

        # 不明文字
        0xa557: None, #
        0xa56e: None, # ささてんぼだい
        0xa67a: u'𫈇', # &M065576;
        0xa739: None, #
        0xa752: None, #
        0xa840: None, #
        0xa84d: None, #
        0xa85b: u'𫒒', # &M065817;
        0xab4b: None, # 彖
        0xac31: u'𫇜', # &M065553;
        0xac7c: None, #
        0xac7e: None, #
        0xad6c: u'𫙧', # &M066003;
        0xae2b: (None, u'⿰鹿子'), # &M066106;

}


