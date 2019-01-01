morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

text = ['Morze code', 'Prometheus', 'SOS', '1']

def encode_morze(text):
    diagram = ''
    code = ''
    text = text.upper()
    for letter in text:
        if letter in morse_code.keys():
            code = morse_code[letter]
            for elem in code:
                if elem == '.':
                    diagram = diagram + '^_'
                elif elem == '-':
                    diagram = diagram + '^^^_'
            diagram = diagram + '__'
        elif letter == ' ':
            diagram = diagram + '____'

    code = ''
    for i in range(len(diagram)-3):
        code = code + diagram[i]
    return code

for i in range(len(text)):
    print(encode_morze(text[i]))