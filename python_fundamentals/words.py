#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:15:48 2020

@author: breannamarielee
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: URL of a UTF-8 text code
        
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
 
    
def print_words(story_words):               
    for word in story_words:
        print(word)           
        
def main(url):
    words = fetch_words(url)
    print_words(words)


#print(__name__)
        
if __name__ == "__main__": #this module is invoked, so excute the following immediately
    main(sys.argv[1])
