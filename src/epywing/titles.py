from epywing.categories import JapaneseEnglish, EnglishJapanese


class AllTitles(BookTitle):

    def matches(self, book):
        return True


class GeniusEiwaDaijiten(BookTitle):
    #label = 'Genius EiWa Daijiten'
    categories = [JapaneseEnglish]

    def matches(self, book):
        return u'ジーニアス英和大辞典' in book.name


