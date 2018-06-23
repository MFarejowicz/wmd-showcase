#!/usr/bin/python
import random

model = {}

with open('confessions.txt') as f:
    data = [x.strip() for x in f.readlines()]
    for line in data:
        line = line.lower().split()
        for i, word in enumerate(line):
            if i == len(line) - 1:
                model['END'] = model.get('END', []) + [word]
            else:
                if i == 0:
                    model['START'] = model.get('START', []) + [word]
                model[word] = model.get(word, []) + [line[i+1]]

def get_confession(model):
    output = []
    while True:
        if not output:
            options = model['START']
        elif output[-1] in model['END']:
            if len(output) < 6:
                options = model['START']
            else:
                break
        else:
            options = model[output[-1]]
        output.append(random.choice(options))
    return ' '.join(output).capitalize()

c1, c2 = get_confession(model), get_confession(model)
print(model)
print(c1 + "\n" + c2)
