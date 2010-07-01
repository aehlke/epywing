
class BookCategory(object):
    #__metaclass__ = PluginMount
    '''
    Must implement the following attributes:
        label
    '''

class JapaneseEnglish(BookCategory):
    label = 'Japanese-English'

class EnglishJapanese(BookCategory):
    label = 'English-Japanese'

class Japanese(BookCategory):
    label = 'Japanese'


