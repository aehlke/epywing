# -*- coding: utf-8 -*-
import os
import sys
import subprocess
#from epywing.util import strip_tags

class Wakati(object):
    '''Wrapper class for `mecab -O wakati`, which is used to split Japanese words.
    '''
    def __init__(self):
        self._mecab = None
        
        file_path = os.path.dirname(os.path.abspath(__file__))
        if sys.platform.startswith('darwin'):
            self.mecab_path = os.path.join(file_path, 'mecab/bin/mecab')

        dic_dir = os.path.join(file_path, 'mecab/dic/ipadic')
        self._mecab_cmd = [self.mecab_path, '-Owakati', '--dicdir=' + dic_dir]
        #os.environ['PATH'] += ":" + dir + "/osx/mecab/bin"
        #os.environ['MECABRC'] = dir + "/osx/mecab/etc/mecabrc"
        #os.environ['DYLD_LIBRARY_PATH'] = dir + "/osx/mecab/bin"
        #os.chmod(dir + "/osx/mecab/bin/mecab", 0755)

    def _ensure_open(self):
        '''Opens the mecab process if it's closed.
        '''
        if not self._mecab:
            self._mecab = subprocess.Popen(self._mecab_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=-1)

    def split(self, text):
        '''Splits the text using mecab's wakati.
        '''
        if u'\n' in text:
            return [text]
        try:
            self._ensure_open()

            text = ''.join([unicode(text), u'\n']) # needs to end in a newline
            self._mecab.stdin.write(text.encode('utf8'))
            self._mecab.stdin.flush()
            return unicode(self._mecab.stdout.readline().decode('utf8')).split()
        except Exception, e:
            return [text]
            

# tests
if __name__ == '__main__':
    w = Wakati()
    print w.split(u'hello earth. did this work??')

