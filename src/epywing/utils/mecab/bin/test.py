# -*- coding: utf-8 -*-
import subprocess
import os
a = subprocess.Popen(['mecab', '-Owakati', '--dicdir=../dic/ipadic'], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)
a.stdin.write(u'何～これですか what is that   HUH  OK I SEE ?\n\n'.encode('utf8'))
a.stdin.flush()
b = unicode(a.stdout.readline().decode('utf8'))
print 'test'
print b.strip()#.split()
print 'test'
