# -*- coding: utf-8 -*-

from eb import *
import re
from base64 import b64encode
from bookfilter import BookFilter

class GaijiHandler(object):
    '''Basic gaiji handler that returns gaiji PNG data embedded in <img> tags.
    This is generic and will work on any EPWING book.
    '''

    GAIJI_TEMPLATE = u'<gaiji c="{width}{index:04x}"/>'
    _GAIJI_REGEX = r'<gaiji\s+c\s*=\s*"(([zh])([0-9a-fA-F]{4,4}))"\s*/>'
    GAIJI_REGEX = re.compile(_GAIJI_REGEX)
    GAIJI_WIDTHS = {EB_HOOK_NARROW_FONT: 'h', EB_HOOK_WIDE_FONT: 'z'}
    GAIJI_WIDTHS_ = dict((v, k) for k, v in GAIJI_WIDTHS.items())
    GAIJI_IMG_TEMPLATE = u'<img src="data:image/gif;base64,{base64_data}" style="position:relative;top:{top_padding}px;margin-left:2px;"/>'
    

    def __init__(self, parent):
        '''`parent` should be an EpwingBook instance.
        '''
        self.parent = parent

    @BookFilter.filter_gaiji_tag
    def tag(self, width_code, index):
        '''Returns a <gaiji> tag.
        '''
        return self.GAIJI_TEMPLATE.format(width=self.GAIJI_WIDTHS[width_code], index=index)

    def _embedded_gif_tag(self, gif_data, font_size):
        base64_data = b64encode(gif_data)
        padding = font_size / 8 
        return self.GAIJI_IMG_TEMPLATE.format(base64_data=base64_data, top_padding=padding)

    def _replace_gaiji(self, match):
        width = self.GAIJI_WIDTHS_[match.group(2)]
        index = int(match.group(3), 16)
        font_size = self.font_sizes[0]
        gif_data = self.gif(width, index, font_size)
        return self._embedded_gif_tag(gif_data, font_size)


    def replace_gaiji(self, html):
        '''Replaces any <gaiji> tags in `html` with the proper <img> tags.
        '''
        return self.GAIJI_REGEX.sub(self._replace_gaiji, html)
        #for match in pat.finditer(data):
        #eb_write_text_string(book, gaiji[code].get(argv[0], \
        #        #'<span title=\"{0:x}\">?</span>'\
        #        u'[{0:x}]'
        #        .format(argv[0])).encode('euc-jp'))
        #data = pat.sub(replace_gaiji, data)

    @property
    def font_sizes(self):
        return self._font_sizes.keys()
    
    @property
    def _font_sizes(self):
        return {16: EB_FONT_16, 24: EB_FONT_24, 30: EB_FONT_30, 48: EB_FONT_48}
    
    def gif(self, width_code, index, font_size):
        '''Returns the bytes to a GIF representation of the given gaiji character.
        `width_code` is the `code` parameter of the hook that specifies font width
        `font_size` is either 'small' or 'large'
        '''
        #TODO error handling, invalid font size correction/availability property
        book = self.parent.book
        font_size2 = self._font_sizes[font_size]
        #fontsize = (size == kFontImageSizeLarge) ? _largeFontType : _smallFontType;
  
        eb_set_font(book, font_size2)
        height = eb_font_height(book)
        
        if width_code == EB_HOOK_NARROW_FONT:
            width = eb_narrow_font_width(book)
            bitmap = eb_narrow_font_character_bitmap(book, index)
        else:
            width = eb_wide_font_width(book)
            bitmap = eb_wide_font_character_bitmap(book, index)

        gif = eb_bitmap_to_gif(bitmap, width, height)
        eb_unset_font(book)
        return gif





gaiji = {
    EB_HOOK_NARROW_FONT: {
        0xa120: u'',
        0xa121: u'* ',
        0xa122: u'** ',
        0xa123: u'*** ',
        #0xa124: u'o ',
        0xa124: u'°',
        0xa125: u'˘',
        0xa126: u'《',
        0xa127: u'》',
        0xa128: u'〔',
        0xa129: u'〕',
        0xa12a: u'〜', #TODO span class= for any occurences
        0xa12b: u'-',
        0xa12c: u'-́',
        0xa12d: u'-̀',
        0xa132: u'˘',

        # start of ones obtained from support-chujiten.el
        0xa134: u'ç',
        0xa135: u'ə́',
        0xa136: u'ɚ́',
        0xa137: u'í',
        0xa138: u'ɔ́',
        0xa139: u'ʊ́',
        0xa13a: u'ɑ́',
        0xa13b: u'´',
        0xa13c: u'É',
        0xa13d: u'á',
        0xa13e: u'é',
        0xa13f: u'í',
        0xa140: u'ó',
        0xa141: u'ú',
        0xa142: u'ʌ́',
        0xa143: u'ə̀',
        0xa144: u'ɚ̀',
        0xa145: u'ì',
        0xa146: u'ɔ̀',
        0xa147: u'ʊ̀',
        0xa148: u'ɑ̀',
        0xa149: u'`',
        0xa14a: u'à',
        0xa14b: u'è',
        0xa14c: u'ì',
        0xa14d: u'ò',
        0xa14e: u'ù',
        0xa14f: u'ʌ̀',
        0xa150: u'ʌ',
        0xa151: u'Á',
        0xa152: u'B́',
        0xa153: u'Ć',
        0xa154: u'D́',
        0xa155: u'É',
        0xa156: u'F́',
        0xa157: u'Ǵ',
        0xa158: u'H́',
        0xa159: u'Í',
        0xa15a: u'Ĺ',
        0xa15b: u'Ḿ',
        0xa15c: u'Ó',
        0xa15d: u'Ṕ',
        0xa15e: u'Q́',
        0xa15f: u'Ŕ',
        0xa160: u'Ś',
        0xa161: u'T́',
        0xa162: u'Ú',
        0xa163: u'V́',
        0xa164: u'X́',
        0xa165: u'Ý',
        0xa166: u'Ź',
        0xa167: u'á',
        0xa168: u'é',
        0xa169: u'í',
        0xa16a: u'ó',
        0xa16b: u'ú',
        0xa16c: u'ý',
        0xa16d: u'À',
        0xa16e: u'È',
        0xa16f: u'Ì',
        0xa170: u'Ò',
        0xa171: u'ǽ',
        0xa172: u'', # right half of [ae']
        0xa173: u'æ̀',
        0xa174: u'',
        0xa175: u'æ',
        0xa176: u'',
        0xa177: u'S̀',
        0xa178: u'T̀',
        0xa179: u'Ù',
        #0xa17a: u'V̀',
        0xa17b: u'à',
        0xa17c: u'è',
        0xa17d: u'ì',
        0xa17e: u'ò',
        0xa221: u'ù',
        0xa222: u'ỳ',
        0xa223: u'ɛ̃',
        0xa224: u'ɔ̃',
        0xa225: u'ɑ̃',
        0xa226: u'ə',
        0xa227: u'ɚ',
        0xa228: u'ɪ',
        0xa229: u'ɔ',
        0xa22a: u'ʊ',
        0xa22b: u'θ',
        0xa22c: u'ð',
        0xa22d: u'ʃ',
        0xa22e: u'ʒ',
        0xa22f: u'ŋ',
        #("ha230")
        0xa231: u'Φ',
        #("ha232")
        0xa233: u'ː',
        0xa234: u'ɑ',
        #0xa235: u'ł', #??
        0xa236: u'',
        0xa237: u'ã',
        0xa238: u'ñ',
        0xa239: u'ø',
        0xa23a: u'Å',
        0xa23b: u'ţ',
        0xa23c: u'°',
        0xa23d: u'¨',
        0xa23e: u'Ö',
        0xa23f: u'ä',
        0xa240: u'ë',
        0xa241: u'ï',
        0xa242: u'ö',
        0xa243: u'ü',
        0xa244: u'^',
        0xa245: u'â',
        0xa246: u'ê',
        0xa247: u'î',
        0xa248: u'ô',
        0xa249: u'-',
        0xa24a: u'ā',
        0xa24b: u'ē',
        0xa24c: u'ī',
        0xa24d: u'ō',
        0xa24e: u'ū',
        0xa24f: u'ȳ',
        0xa250: u'ă',
        #0xa251: u'ĕ',
        #0xa252: u'ŏ',
        0xa253: u'Č',
        0xa255: u'č',
        #("ha256" . "e~")
        0xa257: u'ľ',
        0xa258: u'ř',
        0xa259: u'š',
        #Any gaiji of the code "haxxx" after this doesn't seem to
        #appear except "ha26b"
        0xa26a: u'˝',
        0xa26b: u'·',
        0xa26c: u'Ñ',
        0xa26d: u'È',
        # end of those obtained from chujiten-support.el

        ##remove accents
        #0xa155: u'a',
        #0xa12e: u'e',
        #0xa158: u'e',
        #0xa15a: u'i',
        #0xa159: u'i',
        #0xa15b: u'o',
        #0xa15c: u'o',
        ##0xa15d: 'u',
        #0xa167: u'a',
        #0xa168: u'e',
        #0xa169: u'i',
        #0xa16a: u'o',
        #0xa16b: u'a',
        #0xa16c: u'y',
        #0xa16f: u'I',
        #0xa17b: u'a',
        #0xa17c: u'e',
        #0xa17d: u'i',
        #0xa17e: u'o',
        #0xa221: u'u',
        #0xa233: u':',

        #0xa122: u'a',
        #0xa33b: u'y',
        #0xa15e: u'u',
        #0xa16d: u'E',

        ## other ones I've found
        0xa235: u'/',

        #0xa241: u'ê', #conflicts with above?
    },
    EB_HOOK_WIDE_FONT: {
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

        #symbols
        0xa43a: u'&mdash;',
        0xa430: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">C</span>',
        0xa431: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">U</span>',
        0xa432: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">S</span>',
        0xa433: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">D</span>',

        #found from readers+plus
        0xb122: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">P</span>',
        0xb123: u'<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">R</span>',
        #0xb121: u'-',
        0xb121: u'━', #this breaks it for some reason


        0xae7a: u'【',
        0xae7b: u'】',

        #characters with accents that shouldn't have accents (???)
        0xa438: u'~', # this one shows up in headings
    },
}
