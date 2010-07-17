from HTMLParser import HTMLParser, HTMLParseError

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    '''Returns the string minus any HTML.
    '''
    s = MLStripper()
    try:
        s.feed(html)
    except HTMLParseError:
        # some parse error
        return html
    return s.get_data()


class ComparableMixin:
    def __eq__(self, other):
        return not self < other and not other < self
    def __ne__(self, other):
        return self < other or other < self
    def __gt__(self, other):
        return other < self
    def __ge__(self, other):
        return not self < other
    def __le__(self, other):
        return not other < self

