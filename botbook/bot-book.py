#!/usr/bin/python
print "Content-type: text/html\n"

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

print "<HTML>"
print "<head>"
print  "<link href='http://fonts.googleapis.com/css?family=Lobster+Two' rel='stylesheet' type='text/css'>"
print  "<link href='styles.css' rel='stylesheet' type='text/css'>"
print "</head>"
print "<body>"
print  "<div id='main'>"
print    "<div id='container'>"
print      "<h1 id='title'>SoulBook</h1>"
print      "<div id='content'>"
print        "<div id='top'>"
print          "<img src='git.jpg'>"
print          "<div id='nametime'>"
print            "<p id='name'>G.I.T. Confessions</p>"
print            "<p id='time'>12 Hours Ago</p>"
print          "</div>"
print        "</div>"
print        "<div id='confession'>"
print          "<p>"
print c1
print          "</p>"
print          "<br/>"
print          "<p>"
print c2
print          "</p>"
print        "</div>"
print        "<div id='responses'>"
print          "<span>#Same</span>"
print          "<span>Discuss</span>"
print          "<span>Spread</span>"
print        "</div>"
print      "</div>"
print      "<p id='info'>Find the source code <a href='http://mfarejow.scripts.mit.edu/cms/confessr/Confessr.zip'>here</a>.</p>"
print      "<p id='ref'><a href='javascript:window.location.reload()'>Refresh</a> for a new post.</p>"
print    "</div>"
print  "</div>"
print "</body>"
print "</HTML>"
