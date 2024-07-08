#! python3
# blulletPointAdder.py - adds Wikipedia bullet points to the start

import pyperclip
text = pyperclip.paste()

# odddzielic tekst i dodac gwiazdeczki
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
