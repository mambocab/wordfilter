from __future__ import print_function, unicode_literals

import json
from os import path

# get the path of badwords.json, in the same directory as the current file
bw_path = path.join(path.dirname(path.realpath(__file__)), 'badwords.json')
with open(bw_path) as bw_file:
    bw_json = json.load(bw_file)

badwords = frozenset(bw_json['badwords'])


class Wordfilter(object):

    def __init__(self):
        '''
        Initialize a Wordfilter object containing a copy of the module
        badwords set.
        '''
        self._badwords = set(badwords)

    def blacklisted(self, s):
        '''
        Return True if s contains any bad word as a substring.
        Case-insensitive.
        '''
        s = s.lower()
        # lazily convert all badwords to lowercase
        self._badwords = set(bw.lower() for bw in self._badwords)
        return any(bw in s for bw in self._badwords)

    def add_words(self, words):
        '''
        Add every string in 'words' to the set of bad words. If 'words' is a
        lone string, add the string to the set.
        '''
        # special-casing str avoids adding each letter to the set
        if isinstance(words, str):
            self._badwords.add(words)
        else:
            self._badwords.update(words)

    def clear_list(self):
        '''
        Clear the set of bad words.
        '''
        self._badwords = set()


# instantiates instance so functions are available directly on from module
_module_instance = Wordfilter()
blacklisted = _module_instance.blacklisted
add_words = _module_instance.add_words
clear_list = _module_instance.clear_list
