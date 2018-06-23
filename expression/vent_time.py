#!/usr/bin/env python3
# coding: utf-8
from random import choice
import string, os
def clear(): os.system("cls" if os.name=="nt" else "clear")
def pause(): os.system("pause" if os.name=="nt" else
    "read -s -n 1 -p 'Press any key to continue...'")
table = str.maketrans({key: None for key in string.punctuation})

print("\n        Time to Vent")
print("            by: Matthew Farejowicz\n")
print("Disclaimer: This is more effective when you share more.")
print("Type 'QUIT' at anytime to exit.")
pause()
clear()

prompts = ["Tell me how you're feeling:",
           "Tell me how your day went:",
           "Tell me what's on your mind:",
           "How are you doing?",
           "Is everything alright?",
           "Is anything bothering you?",
           "What are you happy with?",
           "What's stressing you out?",
           "What's making you sad?",
           "Will it turn out alright?"]

positive_responses = ["That's really great to hear!",
                      "Glad things are looking up!",
                      "Hope things stay well.",
                      "Woah, that's awesome.",
                      "Hey, that's pretty sweet, right?",
                      "Now that's what I'm talking about.",
                      "Hope that things stay this way.",
                      "Nice. Glad things are going well.",
                      "Ooh, that's awesome. Good to hear.",
                      "Continue living your best life."]

negative_responses = ["That's actually a real bummer.",
                      "I hope things get better soon.",
                      "Wow, that actually really sucks.",
                      "Sending you strength and good feelings.",
                      "Try not to dwell on it too much.",
                      "It's not your fault.",
                      "I'm confident things will get better.",
                      "Don't worry about it too much, it's not worth it.",
                      "I'm sorry to hear that.",
                      "Don't focus on the bad parts too much."]

neutral_responses = ["Alrighty then.",
                     "Okay then.",
                     "Okay, Could be worse.",
                     "Okay, Could be better.",
                     "I see.",
                     "Carry on, then.",
                     "Interesting.",
                     "Tell me more",
                     "Seems pretty neutral."]

good = {'appreciation', 'inventive', 'key', 'satisfy', 'handsome', 'party',
'sparkling', 'everyday', 'ready', 'peace', 'calm', 'smooth', 'recognize',
'entirely', 'flourish', 'vary', 'green', 'friendship', 'intuitive', 'hug',
'beautiful', 'triumph', 'confident', 'ally', 'effortless', 'alter', 'vivacious',
'powerful', 'transform', 'courageous', 'love', 'enjoy', 'commend', 'smart',
'adjust', 'astute', 'legendary', 'protect', 'vital', 'wonderful', 'venerate',
'exquisite', 'agree', 'fortune', 'voyage', 'today', 'allow', 'animated', 'day',
'bunch', 'hearty', 'enthuse', 'affluent', 'nurture', 'connect', 'jubilation',
'honest', 'classy', 'rejoice', 'rich', 'cheer', 'benefit', 'ingenious',
'complete', 'familiar', 'gorgeous', 'energy', 'astonish', 'satisfied',
'brave', 'nutritious', 'sunny', 'synchronized', 'companionship', 'prosperous',
'thankful', 'gather', 'accomplishment', 'enthusiastic', 'abundant', 'marvelous',
'charitable', 'explore', 'support', 'harmony', 'simple', 'see', 'grow',
'principle', 'clean', 'wonder', 'resound', 'moving', 'delight', 'replenish',
'amity', 'each', 'change', 'hold', 'value', 'zeal', 'unusual', 'shine', 'make',
'happy', 'quick', 'plethora', 'lucidity', 'soul', 'gratitude', 'learn', 'kind',
'joined', 'honor', 'healing', 'show', 'highest', 'popular', 'cultivate',
'intelligence', 'wondrous', 'activist', 'ecstasy', 'elegance', 'absolutely',
'rely', 'faith', 'closeness', 'nature', 'full', 'mission', 'constant', 'open',
'sensation', 'dazzling', 'effervescent', 'essence', 'without', 'thrilled',
'encourage', 'bounty', 'comradeship', 'grin', 'clarity', 'glow', 'character',
'serenity', 'plenty', 'luminous', 'truth', 'bright', 'yippee', 'loveliness',
'cherish', 'relax', 'well', 'energized', 'paradise', 'xanadu', 'basic',
'healthful', 'keen', 'nourish', 'refresh', 'care', 'cure', 'light', 'healthy',
'phenomenon', 'everyone', 'respect', 'prepared', 'meaningful', 'spirit',
'reliance', 'youthful', 'silence', 'celebrate', 'zest', 'authentic', 'innate',
'mind-blowing', 'wholesome', 'safe', 'genius', 'expand', 'give', 'clever',
'idea', 'donate', 'prominent', 'great', 'sustain', 'benefactor', 'exultant',
'approve', 'metamorphosis', 'spirited', 'certain', 'discover', 'together',
'earnest', 'adventure', 'therapeutic', 'healed', 'polish', 'shift', 'euphoria',
'bighearted', 'surprise', 'core', 'holy', 'accept', 'visualize', 'team',
'style', 'bloom', 'heart', 'kiss', 'lively', 'thorough', 'create', 'take',
'quest', 'copious', 'remarkable', 'feat', 'now', 'conviction', 'master',
'affirm', 'modify', 'enormous', 'natural', 'quiet', 'very', 'laugh', 'eager',
'purpose', 'helpful', 'grace', 'divine', 'strong', 'astounding', 'admire',
'venture', 'welcome', 'fortunate', 'famous', 'bubbly', 'express', 'believe',
'creative', 'established', 'embrace', 'leader', 'project', 'exhilarating',
'fit', 'meditate', 'mend', 'rousing', 'beaming', 'joy', 'group', 'knowledge',
'restore', 'good', 'realize', 'inspire', 'resources', 'revolutionize', 'sure',
'exciting', 'glad', 'unwavering', 'blessed', 'direct', 'curious', 'motivate',
'active', 'excited', 'spiritual', 'smile', 'vision', 'endorse', 'splendid',
'plenteous', 'refinement', 'airy', 'victory', 'can', 'attractive', 'acclaimed',
'sincerity', 'cuddle', 'content', 'innovate', 'instinct', 'bliss',
'ideal', 'increase', 'secure', 'action', 'funny', 'adored', 'independent',
'adopt', 'still', 'affirmation', 'aptitude', 'perfect', 'know',
'generous', 'vibrant', 'pleasure', 'brilliant', 'rewarding', 'thrive', 'hope',
'efficient', 'will', 'trust', 'renew', 'answer', 'spontaneous', 'family',
'incredible', 'fresh', 'doubt', 'willing', 'adorable', 'go', 'heavenly',
'tranquil', 'youth', 'young', 'miracle', 'resolution', 'one', 'openhanded',
'let', 'zip', 'distinguished', 'artistic', 'assertive', 'cute', 'imaginative',
'novel', 'revere', 'stir', 'follow', 'graceful', 'easy', 'intellectual',
'solution', 'alive', 'success', 'burgeon', 'connected', 'achievement',
'maintain', 'know,', 'lucrative', 'electrifying', 'alliance', 'upbeat',
'freedom', 'genuine', 'unity', 'encompassing', 'interest', 'rejuvenate',
'renowned', 'cheerful', 'positive', 'affirmative', 'robust', 'choose',
'optimistic', 'charming', 'productive', 'whole', 'vigorous', 'esteem',
'nourished', 'proud', 'poise', 'amaze', 'plentiful', 'wealthy', 'here'}

bad = {'not', 'angry', 'deplorable', 'junky', "dont", 'injure', 'hideous',
'beneath', 'awful', 'adverse', 'disheveled', 'haggard', 'hostile', 'menacing',
'dead', 'damage', 'evil', 'atrocious', 'scary', "cant", 'quirky', 'slimy',
'rocky', 'unfair', 'coarse', 'lose', 'yucky', 'hard', 'mean', 'wound', 'scare',
'hate', 'callous', 'rotten', 'upset', 'plain', 'unsatisfactory', 'faulty',
'severe', 'poisonous', 'sinister', 'quit', 'smelly', 'anxious', 'boring',
'monstrous', 'sticky', 'hurt', 'inane', 'sick', 'banal', 'undermine', 'stinky',
'broken', 'deprived', 'collapse', 'contradictory', 'unpleasant', 'dreary',
'dishonest', 'unhappy', 'deny', 'dirty', 'distress', 'prejudice', 'stressful',
'offensive', 'despicable', 'wicked', 'nobody', 'oppressive', 'bemoan', 'cruel',
'crazy', 'terrifying', 'no', 'revolting', 'contrary', 'sad', 'lousy', 'zero',
'vindictive', 'grim', 'ruthless', 'depressed', 'horrendous', 'apathy',
'damaging', 'missing', 'icky', 'noxious', 'stuck', 'filthy', 'nothing',
'shocking', 'inelegant', 'terrible', 'dismal', 'greed', 'sickening', 'hurtful',
'ignore', 'corrosive', 'suspect', 'vile', 'wary', 'alarming', 'villainous',
'rude', 'grotesque', 'renege', 'moldy', 'disease', 'fail', 'old', 'tense',
'moan', 'insipid', 'decaying', 'barbed', 'unwieldy', 'unhealthy', 'lumpy',
'poor', 'unsightly', 'naughty', 'insane', 'fear', 'imperfect', 'gawky',
'unfavorable', 'messy', 'unwholesome', 'yell', 'stupid', 'reject', 'repulsive',
'unwanted', 'pain', 'annoy', 'jealous', 'unwelcome', 'insidious', 'guilty',
'gruesome', 'frightful', 'pessimistic', 'sorry', 'petty', 'homely', 'worst',
'impossible', 'never', 'hard-hearted', 'negate', 'repugnant', 'untoward',
'perturb', 'cry', 'fight', 'foul', 'dastardly', 'questionable', 'ugly',
'misshapen', 'criminal', 'disgusting', 'savage', 'scream', 'unwise', 'creepy',
'negative', 'belligerent', 'weary', 'horrible', 'frighten', 'stressing',
'cutting', 'clumsy', 'eroding', 'ill', 'nasty', 'repellant', 'suspicious',
'vice', 'spiteful', 'dreadful', 'bad', 'stormy', 'enraged', 'confused',
'malicious', 'gross', 'immature', 'woeful', 'corrupt', 'nonsense', 'cold',
'feeble', 'stressed', 'unlucky', 'deformed', 'grimace', 'vicious', 'ignorant',
'threatening', 'infernal', 'harmful', 'shoddy', 'naive', 'cold-hearted',
'detrimental', 'nondescript', 'injurious', 'sobbing', 'unjust', 'dishonorable',
'misunderstood', 'grave', 'ghastly', 'odious', 'objectionable', 'revenge',
'worthless', 'abysmal', 'disrespect', 'disrespectful', 'hurts', 'suck', 'sucks',
'shit', 'shitty', 'fuck', 'fucked', 'damn', 'bitch', 'crap', 'piss', 'dick',
'darn', 'darned', 'cock', 'pussy', 'asshole', 'bastard', 'slut', 'douche', 'ass'
}

def determine_polarity(input):
    polarity = 0
    input = input.translate(table)
    words = input.lower().split()
    for word in words:
        if word in good:
            polarity += 1
        if word in bad:
            polarity -= 1
    return polarity

print("Hello! My name is Polo.")
source = input(choice(prompts) + "\n")

while source != "QUIT":

    if len(source) == 0:
        print("That doesn't tell me much...")
    else:
        phrase_polarity = determine_polarity(source)

        if phrase_polarity > 0: print(choice(positive_responses))
        elif phrase_polarity < 0: print(choice(negative_responses))
        else: print(choice(neutral_responses))

    print("\n-----------------------------------------------------------")
    source = input("\n" + choice(prompts) + "\n")

clear()
