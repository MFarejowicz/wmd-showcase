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

s = "\n         "
direction = None
conv_length = 0
limit = 4
log = {"E": [], "Y": []}

def generate_positive_response(conv_length, log):
    if conv_length == 1:
        return choice(["Great! Tell me what's got you glad.",
                       "Awesome! What good thing is going on?",
                       "Nice! Want to share some details?"])
    elif 2 <= conv_length <= 3:
        return choice(["I see! Can you tell me more?",
                       "Got more details?",
                       "That's cool! Anything else?",
                       "More on the subject?",
                       "Ooh. I want to know more specifics."])
    elif 4 <= conv_length <= 5:
        return choice(["And why does that make you happy?",
                       "Why's that make you glad?",
                       "Isn't that a great thing?",
                       "Wouldn't it be cool if that happened more often?",
                       "Do you wish that was the case more often?"])
    else:
        return choice(["What more do you have to say?",
                       "More good things going on?",
                       "Can you make things stay this good?",
                       "What can you do to keep the happiness going?",
                       "Any other joyful things to say?"])

def generate_negative_response(conv_length, log):
    if conv_length == 1:
        return choice(["I see. What's on your mind?",
                       "Let's talk about it then. What's up?",
                       "What exactly has you down?"])
    elif 2 <= conv_length <= 3:
        return choice(["I see. Can you tell me more?",
                       "What else about it?",
                       "And then what happened?",
                       "Tell me more, if you'd like.",
                       "How about after that?"])
    elif 4 <= conv_length <= 5:
        return choice(["And why is that a bad thing?",
                       "What would you have preferred?",
                       "Can you do anything about it?",
                       "That's pretty rough. You doing alright?",
                       "How does that make you feel?"])
    else:
        return choice(["What would make for a better situation?",
                       "And are you doing alright?",
                       "Can you avoid this in the future?",
                       "What would like to say about that?",
                       "Do you have to deal with this going forward?"])

def generate_concluding_response(direction, log):
    if direction == "positive":
        return "I'm glad things are going well. Hope things stay that way!"
    elif direction == "negative":
        return "Thanks for sharing. I hope the talking helped."
    else: return "Goodbye. Hope we can talk soon."

null_responses = [
"Nothing to say? That's okay. Take some time to think.",
"Could I get a little bit more on that?",
"No pressure to respond. Think it over.",
"No worries. Respond at your leisure."]

prompt = "Hello there, my name is Emerson.\n\
         I'd love to hear about you. Would you like to share\n\
         something positive, or perhaps something negative?"

print("Emerson: " + prompt)
source = input("You: ").lower()

while source != "!quit":

    print()
    if conv_length > limit:
        prompt = "I see. Hope talking about this has helped." if direction == \
        "negative" else "I see! Do you have more to say?" + \
        " Would you like to" + s + "continue talking (yes/no)?"
        print("Emerson: " + prompt)
        source = input("You: ").lower()

        while source != "yes" and source != "no" and source != "!quit":
            print("Emerson: " + prompt)
            source = input("You: ").lower()

        if source == "yes":
            limit += 3
            print()
        else:
            break

    if len(source) == 0:
        if not direction:
            prompt = "I'd love to hear about you. Would you like to share" \
            + s + "something positive, or perhaps something negative?"
        print("Emerson: " + choice(null_responses) + s + prompt)
    else:
        if not direction:
            if "positive" in source:
                direction = "positive"
                conv_length += 1
                log["Y"].append(source)
                prompt = generate_positive_response(conv_length, log)
            elif "negative" in source:
                direction = "negative"
                conv_length += 1
                log["Y"].append(source)
                prompt = generate_negative_response(conv_length, log)
            else:
                prompt = "Can you make that a little clearer? Would you" \
                + s + "like to share something positive or something negative?"
        else:
            if direction == "positive":
                conv_length += 1
                log["Y"].append(source)
                prompt = generate_positive_response(conv_length, log)
            elif direction == "negative":
                conv_length += 1
                log["Y"].append(source)
                prompt = generate_negative_response(conv_length, log)

        print("Emerson: " + prompt)

    source = input("You: ").lower()

print()
print("Emerson: " + generate_concluding_response(direction, log))
