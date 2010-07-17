# -*- coding: utf-8 -*-

import re
import unicodedata

# punctuation (and other non-word characters) regex for unicode
#
_po_numbers = u'1234567890１２３４５６７８９０'
_po_extra = u'〈〉（）()←↓↑→⇒⇔＜＞【】《》[]［］〔〕「」『』◇◆★‖｜＝━−‘-〜…=×+＋○°θ▽'
_po_punc = u''.join(unichr(x) for x in xrange(65536) if unicodedata.category(unichr(x)) == 'Po')

_po = u''.join([_po_numbers, _po_extra, _po_punc])


def _regex_for_chars(*chars):
    chars = u''.join(chars)

    # escape \ and ]
    escaped = chars.replace(u'\\', u'\\\\').replace(u']', u'\\]')

    return re.compile(u'[' + escaped + u']')


punctuation_and_numbers_regex = _regex_for_chars(_po_numbers, _po_extra, _po_punc)

punctuation_regex = _regex_for_chars(_po_extra, _po_punc)
