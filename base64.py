
from base64 import urlsafe_b64encode as urlsafe_b64encode2, urlsafe_b64decode as urlsafe_b64decode2

#resource id encoding
def _position_to_resource_id(positions):
    '''positions is a list of offsets, where odds are start and evens are end offsets
    '''
    return _ENTRY_ID_SPLIT.join(map(_num_encode, positions))

_ENTRY_ID_SPLIT = 'z'
_ALPHABET = string.ascii_uppercase + string.ascii_lowercase.replace(_ENTRY_ID_SPLIT,'') + \
           string.digits + '-_'
_ALPHABET_REVERSE = dict((c, i) for (i, c) in enumerate(_ALPHABET))
_BASE = len(_ALPHABET)

def _num_encode(n):
    s = []
    while True:
        n, r = divmod(n, _BASE)
        s.append(_ALPHABET[r])
        if n == 0: break
    return ''.join(reversed(s))

def _num_decode(s):
    n = 0
    for c in s:
        n = n * _BASE + _ALPHABET_REVERSE[c]
    return n

def urlsafe_b64_encode(s):
    return urlsafe_b64encode2(s).strip('=')

def urlsafe_b64_decode(s):
    return urlsafe_b64decode2(s + '=' * (lambda x: x % 4 and (4 - x % 4) or 0)(len(s)))#s + '=' * (4 - len(s) % 4))

