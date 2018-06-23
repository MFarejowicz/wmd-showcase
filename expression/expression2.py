#!/usr/bin/env python3
# coding: utf-8

from random import choice
import string, os
def clear(): os.system("cls" if os.name=="nt" else "clear")

print("\nExpression\n")
print("This program is intended to be used to facilitate the process of \
venting,\nof expressing excitement, or of the general communication of \
emotion.\nIt is meant only to prompt you to share, so please do so as \
little \nor as much as you feel like doing so.\n")
print("Type '!quit' at anytime to exit.")
input("Press enter to start.")
clear()

node = 0
name = None
def get_tag(name): return name + ": " if name is not None else "You: "

null_responses = [
"Nothing to say? That's okay. Take some time to think.",
"Could I get a little bit more on that?",
"No pressure to respond. Think it over.",
"Respond at your leisure."]

def missed_prompt(name):
    return

def name_prompt(name):
    return "Could I get your name?\n\
         Alternately, just say 'no' if you don't wish to share your name."

def branch_prompt(name):
    return "Now, tell me, " + (name + ", " if name is not None else \
    "") + "would you like to share something positive or negative?"

def good_prompt(name):
    return "good!"

def bad_prompt(name):
    return "bad!"

tree = {0: name_prompt, 1: branch_prompt, 2: good_prompt, 3: bad_prompt}

print("Emerson: Hello there, my name is Emerson.\n\
         First, could I get your name?\n\
         Alternatively, just say 'no' if you don't wish to share your name.")
source = input("You: ").lower()

while source != "!quit":

    print()
    if len(source) == 0:
        print("Emerson: " + choice(null_responses))
        source = input("         "+tree[node](name)+"\n"+get_tag(name)).lower()
    else:
        if node == 0:
            if source != "no":
                name = source.capitalize()
            node = 1
        elif node == 1:
            if source == "positive":
                node = 2
            if source == "negative":
                node = 3
        source = input("Emerson: "+tree[node](name)+"\n"+get_tag(name)).lower()

clear()




# prompts = ["Tell me how you're feeling:",
#            "Tell me how your day went:",
#            "Tell me what's on your mind:",
#            "How are you doing?",
#            "Is everything alright?",
#            "Is anything bothering you?",
#            "What are you happy with?",
#            "What's stressing you out?",
#            "What's making you sad?",
#            "Will it turn out alright?"]
#
# positive_responses = ["That's really great to hear!",
#                       "Glad things are looking up!",
#                       "Hope things stay well.",
#                       "Woah, that's awesome.",
#                       "Hey, that's pretty sweet, right?",
#                       "Now that's what I'm talking about.",
#                       "Hope that things stay this way.",
#                       "Nice. Glad things are going well.",
#                       "Ooh, that's awesome. Good to hear.",
#                       "Continue living your best life."]
#
# negative_responses = ["That's actually a real bummer.",
#                       "I hope things get better soon.",
#                       "Wow, that actually really sucks.",
#                       "Sending you strength and good feelings.",
#                       "Try not to dwell on it too much.",
#                       "It's not your fault.",
#                       "I'm confident things will get better.",
#                       "Don't worry about it too much, it's not worth it.",
#                       "I'm sorry to hear that.",
#                       "Don't focus on the bad parts too much."]
#
# neutral_responses = ["Alrighty then.",
#                      "Okay then.",
#                      "Okay, Could be worse.",
#                      "Okay, Could be better.",
#                      "I see.",
#                      "Carry on, then.",
#                      "Interesting.",
#                      "Tell me more",
#                      "Seems pretty neutral."]
#
# good = {'appreciation', 'inventive', 'key', 'satisfy', 'handsome', 'party',
# 'sparkling', 'everyday', 'ready', 'peace', 'calm', 'smooth', 'recognize',
# 'entirely', 'flourish', 'vary', 'green', 'friendship', 'intuitive', 'hug',
# 'beautiful', 'triumph', 'confident', 'ally', 'effortless', 'alter', 'vivacious',
# 'powerful', 'transform', 'courageous', 'love', 'enjoy', 'commend', 'smart',
# 'adjust', 'astute', 'legendary', 'protect', 'vital', 'wonderful', 'venerate',
# 'exquisite', 'agree', 'fortune', 'voyage', 'today', 'allow', 'animated', 'day',
# 'bunch', 'hearty', 'enthuse', 'affluent', 'nurture', 'connect', 'jubilation',
# 'honest', 'classy', 'rejoice', 'rich', 'cheer', 'benefit', 'ingenious',
# 'complete', 'familiar', 'gorgeous', 'energy', 'astonish', 'satisfied',
# 'brave', 'nutritious', 'sunny', 'synchronized', 'companionship', 'prosperous',
# 'thankful', 'gather', 'accomplishment', 'enthusiastic', 'abundant', 'marvelous',
# 'charitable', 'explore', 'support', 'harmony', 'simple', 'see', 'grow',
# 'principle', 'clean', 'wonder', 'resound', 'moving', 'delight', 'replenish',
# 'amity', 'each', 'change', 'hold', 'value', 'zeal', 'unusual', 'shine', 'make',
# 'happy', 'quick', 'plethora', 'lucidity', 'soul', 'gratitude', 'learn', 'kind',
# 'joined', 'honor', 'healing', 'show', 'highest', 'popular', 'cultivate',
# 'intelligence', 'wondrous', 'activist', 'ecstasy', 'elegance', 'absolutely',
# 'rely', 'faith', 'closeness', 'nature', 'full', 'mission', 'constant', 'open',
# 'sensation', 'dazzling', 'effervescent', 'essence', 'without', 'thrilled',
# 'encourage', 'bounty', 'comradeship', 'grin', 'clarity', 'glow', 'character',
# 'serenity', 'plenty', 'luminous', 'truth', 'bright', 'yippee', 'loveliness',
# 'cherish', 'relax', 'well', 'energized', 'paradise', 'xanadu', 'basic',
# 'healthful', 'keen', 'nourish', 'refresh', 'care', 'cure', 'light', 'healthy',
# 'phenomenon', 'everyone', 'respect', 'prepared', 'meaningful', 'spirit',
# 'reliance', 'youthful', 'silence', 'celebrate', 'zest', 'authentic', 'innate',
# 'mind-blowing', 'wholesome', 'safe', 'genius', 'expand', 'give', 'clever',
# 'idea', 'donate', 'prominent', 'great', 'sustain', 'benefactor', 'exultant',
# 'approve', 'metamorphosis', 'spirited', 'certain', 'discover', 'together',
# 'earnest', 'adventure', 'therapeutic', 'healed', 'polish', 'shift', 'euphoria',
# 'bighearted', 'surprise', 'core', 'holy', 'accept', 'visualize', 'team',
# 'style', 'bloom', 'heart', 'kiss', 'lively', 'thorough', 'create', 'take',
# 'quest', 'copious', 'remarkable', 'feat', 'now', 'conviction', 'master',
# 'affirm', 'modify', 'enormous', 'natural', 'quiet', 'very', 'laugh', 'eager',
# 'purpose', 'helpful', 'grace', 'divine', 'strong', 'astounding', 'admire',
# 'venture', 'welcome', 'fortunate', 'famous', 'bubbly', 'express', 'believe',
# 'creative', 'established', 'embrace', 'leader', 'project', 'exhilarating',
# 'fit', 'meditate', 'mend', 'rousing', 'beaming', 'joy', 'group', 'knowledge',
# 'restore', 'good', 'realize', 'inspire', 'resources', 'revolutionize', 'sure',
# 'exciting', 'glad', 'unwavering', 'blessed', 'direct', 'curious', 'motivate',
# 'active', 'excited', 'spiritual', 'smile', 'vision', 'endorse', 'splendid',
# 'plenteous', 'refinement', 'airy', 'victory', 'can', 'attractive', 'acclaimed',
# 'sincerity', 'cuddle', 'content', 'innovate', 'instinct', 'bliss',
# 'ideal', 'increase', 'secure', 'action', 'funny', 'adored', 'independent',
# 'adopt', 'still', 'affirmation', 'aptitude', 'perfect', 'know',
# 'generous', 'vibrant', 'pleasure', 'brilliant', 'rewarding', 'thrive', 'hope',
# 'efficient', 'will', 'trust', 'renew', 'answer', 'spontaneous', 'family',
# 'incredible', 'fresh', 'doubt', 'willing', 'adorable', 'go', 'heavenly',
# 'tranquil', 'youth', 'young', 'miracle', 'resolution', 'one', 'openhanded',
# 'let', 'zip', 'distinguished', 'artistic', 'assertive', 'cute', 'imaginative',
# 'novel', 'revere', 'stir', 'follow', 'graceful', 'easy', 'intellectual',
# 'solution', 'alive', 'success', 'burgeon', 'connected', 'achievement',
# 'maintain', 'know,', 'lucrative', 'electrifying', 'alliance', 'upbeat',
# 'freedom', 'genuine', 'unity', 'encompassing', 'interest', 'rejuvenate',
# 'renowned', 'cheerful', 'positive', 'affirmative', 'robust', 'choose',
# 'optimistic', 'charming', 'productive', 'whole', 'vigorous', 'esteem',
# 'nourished', 'proud', 'poise', 'amaze', 'plentiful', 'wealthy', 'here'}
#
# bad = {'not', 'angry', 'deplorable', 'junky', "dont", 'injure', 'hideous',
# 'beneath', 'awful', 'adverse', 'disheveled', 'haggard', 'hostile', 'menacing',
# 'dead', 'damage', 'evil', 'atrocious', 'scary', "cant", 'quirky', 'slimy',
# 'rocky', 'unfair', 'coarse', 'lose', 'yucky', 'hard', 'mean', 'wound', 'scare',
# 'hate', 'callous', 'rotten', 'upset', 'plain', 'unsatisfactory', 'faulty',
# 'severe', 'poisonous', 'sinister', 'quit', 'smelly', 'anxious', 'boring',
# 'monstrous', 'sticky', 'hurt', 'inane', 'sick', 'banal', 'undermine', 'stinky',
# 'broken', 'deprived', 'collapse', 'contradictory', 'unpleasant', 'dreary',
# 'dishonest', 'unhappy', 'deny', 'dirty', 'distress', 'prejudice', 'stressful',
# 'offensive', 'despicable', 'wicked', 'nobody', 'oppressive', 'bemoan', 'cruel',
# 'crazy', 'terrifying', 'no', 'revolting', 'contrary', 'sad', 'lousy', 'zero',
# 'vindictive', 'grim', 'ruthless', 'depressed', 'horrendous', 'apathy',
# 'damaging', 'missing', 'icky', 'noxious', 'stuck', 'filthy', 'nothing',
# 'shocking', 'inelegant', 'terrible', 'dismal', 'greed', 'sickening', 'hurtful',
# 'ignore', 'corrosive', 'suspect', 'vile', 'wary', 'alarming', 'villainous',
# 'rude', 'grotesque', 'renege', 'moldy', 'disease', 'fail', 'old', 'tense',
# 'moan', 'insipid', 'decaying', 'barbed', 'unwieldy', 'unhealthy', 'lumpy',
# 'poor', 'unsightly', 'naughty', 'insane', 'fear', 'imperfect', 'gawky',
# 'unfavorable', 'messy', 'unwholesome', 'yell', 'stupid', 'reject', 'repulsive',
# 'unwanted', 'pain', 'annoy', 'jealous', 'unwelcome', 'insidious', 'guilty',
# 'gruesome', 'frightful', 'pessimistic', 'sorry', 'petty', 'homely', 'worst',
# 'impossible', 'never', 'hard-hearted', 'negate', 'repugnant', 'untoward',
# 'perturb', 'cry', 'fight', 'foul', 'dastardly', 'questionable', 'ugly',
# 'misshapen', 'criminal', 'disgusting', 'savage', 'scream', 'unwise', 'creepy',
# 'negative', 'belligerent', 'weary', 'horrible', 'frighten', 'stressing',
# 'cutting', 'clumsy', 'eroding', 'ill', 'nasty', 'repellant', 'suspicious',
# 'vice', 'spiteful', 'dreadful', 'bad', 'stormy', 'enraged', 'confused',
# 'malicious', 'gross', 'immature', 'woeful', 'corrupt', 'nonsense', 'cold',
# 'feeble', 'stressed', 'unlucky', 'deformed', 'grimace', 'vicious', 'ignorant',
# 'threatening', 'infernal', 'harmful', 'shoddy', 'naive', 'cold-hearted',
# 'detrimental', 'nondescript', 'injurious', 'sobbing', 'unjust', 'dishonorable',
# 'misunderstood', 'grave', 'ghastly', 'odious', 'objectionable', 'revenge',
# 'worthless', 'abysmal', 'disrespect', 'disrespectful', 'hurts', 'suck', 'sucks',
# 'shit', 'shitty', 'fuck', 'fucked', 'damn', 'bitch', 'crap', 'piss', 'dick',
# 'darn', 'darned', 'cock', 'pussy', 'asshole', 'bastard', 'slut', 'douche', 'ass'
# }
#
# def determine_polarity(input):
#     polarity = 0
#     input = input.translate(table)
#     words = input.lower().split()
#     for word in words:
#         if word in good:
#             polarity += 1
#         if word in bad:
#             polarity -= 1
#     return polarity
