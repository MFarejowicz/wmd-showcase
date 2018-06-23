#!/usr/bin/env python3
# coding: utf-8
## Down the Staircase by Matthew Farejowicz (Revision)
## Created for CMS.609 The Word Made Digital, taught by Nick Montfort
## Quotes borrowed from "House of Leaves" by Mark Z. Danielewski
import string; from random import *
flip_maps = [
  (string.ascii_lowercase, "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"),
  (string.ascii_uppercase, "ⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z"),
  (string.digits, "0ІᘔƐᔭ59Ɫ86"),
  (string.punctuation, "¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\\[ᵥ‾`}|{~")
]
topsy_turvy = {}
for chars, flipped in flip_maps: topsy_turvy.update(zip(chars, flipped))
trip_rate, blur_rate, skip_rate = 15, 25, 10

def flip(word):
    global trip_rate; trip_rate -= 1 if trip_rate > 2 else 0
    return ''.join(topsy_turvy[char] for char in word[::-1])

def walk(word):
    global blur_rate; blur_rate -= 1 if blur_rate>3 and randint(1,10)>8 else 0
    return ''.join(char if randint(1,blur_rate) > 1
        or word.find(char) == 0 or word.rfind(char) == len(word)-1
        else ' ' if randint(1, skip_rate) > skip_rate-1 else
        choice(string.ascii_lowercase) for char in word)

def descend(quote):
    words = quote.split()
    spaces = 0
    for word in words:
        step = walk(word) if randint(1, trip_rate) > 1 else walk(flip(word))
        print(' ' * spaces + step)
        spaces += len(word)

def ascend(quote):
    words = quote.split()[::-1]
    spaces = sum(len(word) for word in words)
    for word in words:
        spaces -= len(word)
        step = walk(word) if randint(1, trip_rate) > 1 else walk(flip(word))
        print(' ' * spaces + step)

quotes = (lambda x: shuffle(x) or x)([
"This great blue world of ours is but a house of \
leaves, moments before the wind.",
        "Maturity, one discovers, has everything to do with the \
        acceptance of not knowing.",
                "It may be the wrong decision, but fuck it, it's mine.",
                "We all create stories to protect ourselves.",
                    "I still get nightmares. In fact, I get them so often I \
                    should be used to them by now.",
            "Losing the possibility of something is the exact same \
            thing as losing hope.",
    "Some people reflect light, some deflect it, you by some miracle, \
    seem to collect it.",
"The greatest of love letters are always coded for the one \
and not the many.",
    "Is it possible to love something so much, you imagine it \
    wants to destroy you?",
]) + [  "I watch the sun blur into an aftermath. Soon night will \
        enfold us all."]

print('DOWN \n        THE \n              STⱯIRCⱯSE\nLed by: Matt Farejowicz')
for q in quotes: (descend if randint(1, 6) > 1 else ascend)(q)
