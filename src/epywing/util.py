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

