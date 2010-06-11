# -*- coding: utf-8 -*-

from eb import *

gaiji = {
    EB_HOOK_NARROW_FONT: {
        0xa120: '',
        #0xa121: '* ',
        #0xa122: '** ',
        #0xa123: '*** ',
        0xa124: 'o ',
        0xa126: '《',
        0xa127: '》',
        0xa128: '〔',
        0xa129: '〕',
        0xa12a: '〜',
        0xa167: 'a',
        0xa168: 'e',
        0xa169: 'i',
        0xa16a: 'o',
        0xa16b: 'u',
        0xa16c: 'y',
        0xa16f: 'I',
        0xa17b: 'a',
        0xa17c: 'e',
        0xa17d: 'i',
        0xa17e: 'o',
        0xa221: 'u',
        0xa233: ':',

        #remove accents
        0xa155: 'a',
        0xa12e: 'e',
        0xa158: 'e',
        0xa15a: 'i',
        0xa159: 'i',
        0xa15b: 'o',
        0xa15c: 'o',
        0xa15d: 'u',

        0xa122: 'a',
        0xa33b: 'y',
        0xa15e: 'u',
        0xa16d: 'E',

        # other ones I've found
        0xa235: '/',

    },
    EB_HOOK_WIDE_FONT: {
        0xa34e: '━',
        0xa321: '[名]',
        0xa322: '[代]',
        0xa323: '[形]',
        0xa324: '[動]',
        0xa325: '[副]',
        0xa327: '[前]',
        0xa32f: '[U]',
        0xa330: '[C]',
        0xa332: '(複)',
        0xa333: '[A]',
        0xa334: '[P]',
        0xa335: '(自)',
        0xa336: '(他)',
        0xa337: '[成',
        0xa338: '句]',
        0xa32c: '[接',
        0xa32d: '頭]',
        0xa32e: '尾]',
        0xa339: '§',
        0xa33a: '§',
        0xa33c: '§',
        0xa34f: '⇔',

        #symbols
        0xa43a: '&mdash;',
        0xa430: '<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">C</span>',
        0xa431: '<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">U</span>',
        0xa433: '<span style="border-width:1px; border-style:solid; padding:0px 2px 0px 2px">D</span>',

        #characters with accents that shouldn't have accents (???)
        0xa438: '~',
    },
}
