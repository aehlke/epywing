
# -*- coding: utf-8 -*-

from epywing.bookfilter import BookFilter
from epywing.titles import KenkyushaReadersPlus


class KenkyushaReadersPlusFilter(BookFilter):
    applies_to = [KenkyushaReadersPlus]

    def filter_heading(self, entry, heading):
        if heading is not None:
            replacements = {
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)

        return heading.strip()

    narrow_gaiji = {}

    wide_gaiji = {}
