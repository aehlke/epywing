# -*- coding: utf-8 -*-

from epywing.bookfilter import BookFilter
from epywing.titles import GeniusEiwaDaijiten


class GeniusFilter(BookFilter):
    '''Filter for all Genius dictionaries, since they share some formatting.
    '''
    applies_to = [GeniusEiwaDaijiten]


class GeniusEiwaDaijitenFilter(BookFilter):
    applies_to = [GeniusEiwaDaijiten]

    def filter_heading(self, heading):
        if heading is not None:
            replacements = {
                u'·': u'',
                u'・': u'',
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)
        return heading

    def filter_text(self, text):
        return text

    narrow_gaiji = {
        41249: u'',
        0xa126: u'《',
        0xa127: u'》',
        0xa128: u'〔',
        0xa129: u'〕',
        #0xa12a: u'〜', #TODO span class= for any occurences
        #41262: u'e',
    }

    wide_gaiji = {
        0xa33f: u'→',
        0xa34f: u'↔',
        0xa722: u'⇒',
        0xa34e: u'━',
        0xa321: u'[名]',
        0xa322: u'[代]',
        0xa323: u'[形]',
        0xa324: u'[動]',
        0xa325: u'[副]',
        0xa326: u'[接]',
        0xa327: u'[前]',
        0xa328: u'[冠]',
        0xa329: u'[間]',
        0xa32a: u'[助',
        0xa32b: u'動]',
        0xa32c: u'[接',
        0xa32d: u'頭]',
        0xa32e: u'尾]',
        0xa32f: u'[U]',
        0xa330: u'[C]',
        0xa331: u'(単)',
        0xa332: u'(複)',
        0xa333: u'[A]',
        0xa334: u'[P]',
        0xa335: u'(自)',
        0xa336: u'(他)',
        0xa337: u'[成',
        0xa338: u'句]',
        0xa339: u'[音]',#u'§',
        0xa33a: u'[例]',#u'§',
        0xa33b: u'[メモ]',
        0xa33c: u'[一覧]',#u'§',
        0xa34f: u'⇔',
    }

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

