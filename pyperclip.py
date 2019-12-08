import pyperclip
data = ['Lists of animals, Lists of aquarium life, Lists of biologists by author abbreviation, Lists of cultivars']
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split(',')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)