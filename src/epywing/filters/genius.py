# -*- coding: utf-8 -*-

import re
import unicodedata
from epywing.bookfilter import BookFilter
from epywing.titles import GeniusEiwaDaijiten, GeniusEiwaWaeiJiten

def remove_accents(text):
    nfkd_form = unicodedata.normalize('NFKD', unicode(text))
    return u''.join([c for c in nfkd_form if not unicodedata.combining(c)])


class GeniusFilter(BookFilter):
    '''Filter for all Genius dictionaries, since they share some formatting.
    '''
    applies_to = [GeniusEiwaDaijiten, GeniusEiwaWaeiJiten]

    # for example: 【test 1】~ driver
    subentry_regex = re.compile(u'【(?P<parent>.+)】.?〜 (?P<postfix>.+)', re.UNICODE)

    # for example, test<sup>1</sup>
    homonym_regex = re.compile(r'(?P<heading>.+)<sup>(?P<index>.+)</sup>', re.UNICODE)

    def filter_heading(self, entry, heading):
        heading = remove_accents(heading)
        return heading

    def filter_normalized_heading(self, entry, normalized_heading):
        heading = entry.heading

        # Subentries
        m = self.subentry_regex.match(heading)
        if m:
            #print 'subentries'
            parent, postfix = m.group('parent'), m.group('postfix')
            #return entry.normalized_subentry_heading_format.format(parent=parent, postfix=postfix)
            #print parent,
            #print postfix
            return u'{parent} {postfix}'.format(parent=parent, postfix=postfix)

        # Homonyms
        m = self.homonym_regex.match(heading)
        if m:
            heading, index = m.group('heading'), m.group('index')
            entry._homonym_index = int(index)
            return u'{0}'.format(heading)#, index)

        return normalized_heading


class GeniusEiwaDaijitenFilter(BookFilter):
    applies_to = [GeniusEiwaDaijiten]

    def filter_heading(self, entry, heading):
        if heading is not None:
            replacements = {
                #u'·': u'',
                u'・': u'',
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)
        return heading

    def filter_text(self, entry, text):
        return text

    narrow_gaiji = {
        41249: (u'á', u'a'),
        41250: (u'à', u'a'),
        41251: u'ɑ',
        41252: None,
        41253: None,
        41254: None,
        41255: u'ʌ',
        41256: (u'ʌ́', u'^'),
        41257: (u'ʌ̀', u'^'),
        41258: u'ə',
        41259: None,
        41260: u'ə̀',
        41261: None,
        41262: (u'é', u'e'),
        41263: (u'è', u'e'),
        41264: None,
        41265: None,
        41266: None,
        41267: u'ɛ̃',
        41268: u'í',
        41269: u'ì',
        41270: u'ó',
        41271: u'ò',
        41272: None,
        41273: u'ö',
        41274: None,
        41275: None,
        41276: u'ɔ̀',
        41277: None,
        41278: None,
        41279: u'ù',
        41280: None,
        41281: None,
        41282: u'ɚ̀',
        41283: (u'æ', u'ae'),
        41284: (u'ǽ', u'ae'),
        41285: None,
        41286: None,
        41287: None,
        41288: None,
        41289: None,
        41290: None,
        41291: u'θ',
        41292: None,
        41293: None,
        41294: None,
        41295: None,
        41296: None,
        41297: None,
        41298: None,
        41299: None,
        41300: None,
        41301: u'á',
        41302: u'à',
        41303: u'é',
        41304: u'è',
        41305: (u'í', u'i'),
        41306: (u'ì', u'i'),
        41307: (u'ó', u'o'),
        41308: (u'ò', u'o'),
        41309: (u'ú', u'u'),
        41310: (u'ù', u'u'),
        41311: u'-́',
        41312: u'-̀',
        41313: u'ç',
        41314: u'Ç',
        41315: None,
        41316: None,
        41317: None,
        41318: None,
        41319: None,
        41320: None,
        41321: None,
        41322: u'Á',
        41323: u'À',
        41324: u'',
        41325: u'É',
        41326: u'Ó',
        41327: u'Ò',
        41328: u'ô',
        41329: u'ý',
        41330: u'ỳ',
        41331: u'Ý',
        41332: u'B́',
        41333: u'ë',
        41334: u'Í',
        41335: u'È',
        41336: u'Ù',
        41337: u'Ì',
        41338: u'ä',
        41339: u'ř',
        41340: u'ï',
        41341: u'Ú',

        41505: u'ü',
        41506: u'ā',
        41507: u'ē',
        41508: u'î',
        41509: u'â',
        41510: u'ã',
        41511: u'ñ',
        41512: u'ê',
        41513: (None, u'*'),
        41514: u'ö',
        41515: None,
        41516: None,
        41517: None,
        41518: u'˜',
        41519: None,
        41520: u'˘',
        41521: None,
        41522: None,
        41523: None,
        41524: None,
        41525: None,
        41526: None,
        41527: None,
        41528: None,
        41529: None,
        41530: None,
        41531: None,
        41532: None,
        41533: None,
        41534: None,
        41535: None,
        41536: None,
        41537: None,
        41538: (u'ḥ', u'h'),
        41539: (u'Ḥ', u'H'),
        41540: (u'ṃ', u'm'),
        41541: (u'ṇ', u'n'),
        41542: (u'ṛ', u'r'),
        41543: (u'ṣ', u's'),
        41544: None,
        41545: None,
        41546: (u'ẓ', u'z'),
        41547: (u'ṭ', u't'),
        41548: None,
        41549: None,
        
        41550: None,
        41551: None,
        41552: None,
        41553: None,
        41554: None,
        41555: None,
        41556: None,
        41557: None,
        41558: None,
        41559: (u'š', u's'),
        41560: (u'ă', u'a'),
        41561: (u'č', u'c'),
        41562: (u'Č', u'C'),
        41563: (u'ě', u'e'),
        41564: None,
        41565: None,
        41566: None,
        41567: None,
        41568: (u'Š', u'S'),
        41569: None,
        41570: None,
        41571: None,
        41572: None,
        41573: None,
        41574: None,
        41575: None,
        41576: u'ɚ̀',
        41577: u'ɚ́',
        41578: None,
        41579: None,
        41580: None,
        41581: None,
        41582: None,
        41583: None,
        41584: None,
        41585: None,
        41586: None,
        41587: None,
        41588: None,
        41589: None,

        41762: u'ɲ',
        #41249: u'',
        #0xa126: u'《',
        #0xa127: u'》',
        #0xa128: u'〔',
        #0xa129: u'〕',
        ##0xa12a: u'〜', #TODO span class= for any occurences
        ##41262: u'e',
    }

    wide_gaiji = {
        41249: (u'á', u'a'),
        41250: (u'à', u'a'),
        41251: u'ɑ',
        41252: None,
        41253: None,
        41254: None,
        41255: u'ʌ',
        41256: (u'ʌ́', u'^'),
        41257: (u'ʌ̀', u'^'),
        41258: u'ə',
        41259: None,
        41260: u'ə̀',
        41261: None,
        41262: None,
        41263: (u'è', u'e'),
        41264: None,
        41265: None,
        41266: None,
        41267: u'ɛ̃',
        41268: u'í',
        41269: u'ì',
        41270: u'ó',
        41271: u'ò',
        41272: None,
        41273: u'ö',
        41274: None,
        41275: None,
        41276: u'ɔ̀',
        41277: None,
        41278: None,
        41279: u'ù',
        41280: None,
        41281: None,
        41282: u'ɚ̀',
        41283: (u'æ', u'ae'),
        41284: (u'ǽ', u'ae'),
        41285: None,
        41286: None,
        41287: None,
        41288: None,
        41289: None,
        41290: None,
        41291: u'θ',
        41292: None,
        41293: None,
        41294: None,
        41295: None,
        41296: None,
        41297: None,
        41298: None,
        41299: None,
        41300: None,
        41301: u'á',
        41302: u'à',
        41303: u'é',
        41304: u'è',
        41305: (u'í', u'i'),
        41306: (u'ì', u'i'),
        41307: (u'ó', u'o'),
        41308: (u'ò', u'o'),
        41309: (u'ú', u'u'),
        41310: (u'ù', u'u'),
        41311: u'-́',
        41312: u'-̀',
        41313: u'ç',
        41314: u'Ç',
        41315: None,
        41316: None,
        41317: None,
        41318: None,
        41319: None,
        41320: None,
        41321: None,
        41322: u'Á',
        41323: u'À',
        41324: u'',
        41325: u'É',
        41326: u'Ó',
        41327: u'Ò',
        41328: u'ô',
        41329: u'ý',
        41330: u'ỳ',
        41331: u'Ý',
        41332: u'B́',
        41333: u'ë',
        41334: u'Í',
        41335: u'È',
        41336: u'Ù',
        41337: u'Ì',
        41338: u'ä',
        41339: u'ř',
        41340: u'ï',
        41341: u'Ú',

        41505: u'ü',
        41506: u'ā',
        41507: u'ē',
        41508: u'î',
        41509: u'â',
        41510: u'ã',
        41511: u'ñ',
        41512: u'ê',
        41513: (None, u'*'),
        41514: u'ö',
        41515: None,
        41516: None,
        41517: None,
        41518: u'˜',
        41519: None,
        41520: u'˘',
        41521: None,
        41522: None,
        41523: None,
        41524: None,
        41525: None,

        42040: (u'〜', u'〜'),
        42041: (u'〜', u'〜'),
        42042: u'━',

        42048: u'©',

        42065: u'®',

        42080: u'❶',
        42081: u'❷',
        42082: u'❸',
        42083: u'❹',
        42084: u'❺',
        42085: u'❻',
        42086: u'❼',
        42087: u'❽',
        42088: u'❾',
        42089: u'❿',
        42090: u'⓫',
        42091: u'⓬',
        42092: u'⓭',
        42093: u'⓮',
        42094: u'⓯',
        42095: u'⓰',
        42096: u'⓱',
        42097: u'⓲',
        42098: u'⓳',

        42359: u'♥',
        
        42366: u'☞',

        #0xa33f: u'→',
        #0xa34f: u'↔',
        #0xa722: u'⇒',
        #0xa34e: u'━',
        #0xa321: u'[名]',
        #0xa322: u'[代]',
        #0xa323: u'[形]',
        #0xa324: u'[動]',
        #0xa325: u'[副]',
        #0xa326: u'[接]',
        #0xa327: u'[前]',
        #0xa328: u'[冠]',
        #0xa329: u'[間]',
        #0xa32a: u'[助',
        #0xa32b: u'動]',
        #0xa32c: u'[接',
        #0xa32d: u'頭]',
        #0xa32e: u'尾]',
        #0xa32f: u'[U]',
        #0xa330: u'[C]',
        #0xa331: u'(単)',
        #0xa332: u'(複)',
        #0xa333: u'[A]',
        #0xa334: u'[P]',
        #0xa335: u'(自)',
        #0xa336: u'(他)',
        #0xa337: u'[成',
        #0xa338: u'句]',
        #0xa339: u'[音]',#u'§',
        #0xa33a: u'[例]',#u'§',
        #0xa33b: u'[メモ]',
        #0xa33c: u'[一覧]',#u'§',
        #0xa34f: u'⇔',
    }


class GeniusEiwaWaeiJitenFilter(BookFilter):
    applies_to = [GeniusEiwaWaeiJiten]

    @classmethod
    def filter_heading(cls, entry, heading):
        if heading is not None:
            replacements = {
                u'·': u'',
                u'・': u'',
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)
        return heading

    narrow_gaiji = GeniusEiwaDaijitenFilter.narrow_gaiji
    wide_gaiji = GeniusEiwaDaijitenFilter.wide_gaiji


#class AllBooks(BookIdentity):
#    @classmethod
#    def matches(cls, book):
#        return True

    





#class Medium(object):
#    __metaclass__ = PluginMount

#    def get_fingerprint():
#        raise NotImplementedError("Subclases must override this!")

#    def get_metadata():
#        raise NotImplementedError("Subclases must override this!")

#class Pic(Medium):
#    ext = ('jpeg', 'jpg')
#    ...

#class Mov(Medium):
#    ext = ('m4v', 'mp4')
#    ...

#all_backends = [(cls.ext, cls) for cls in Medium.plugins]

#for i_file in files:
#    matching_backends = [cls for exts,cls in all_backends
#            if i_file.ext in exts]

#    for backend in matching_backends:
#        obj = backend()
#        store_tags(obj.get_tags())
#        store_metadata(obj.get_metadata()) 

