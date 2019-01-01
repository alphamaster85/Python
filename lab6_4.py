text = ['Hello,Hello, my dear!', 'to understand recursion you need first to understand recursion...', 'Mom! Mom! Are you sleeping?!!!']

def find_most_frequent(text):
    def get_words(text):
        word = text[0]
        words = []

        for l in range(1, len(text)):        
            if (text[l] >= 'a' and text[l] <= 'z') or (text[l] >= 'A' and text[l] <= 'Z'):
                word = word + text[l]
            else:
                if text[l-1] != ',' and text[l-1] != '!' and text[l-1] != '?' and text[l-1] != '.':
                    words.append(word.lower())
                    word = ''
            
        return words

    def count_words(words):
        count = {}
        for i in words:
            for j in words:
                if i == j:
                    if count.get(i, 0) == 0:
                        count[i] = 1
                    else:
                        count[i] += 1
        
        max_words = 0;
        max_words = max(count.values())
        words = []
        for e in count:
            if count[e] == max_words:
                words.append(e)

        return words

    text = get_words(text)
    text = count_words(text)
    text.sort()
    return text

for i in range(len(text)):
    print(find_most_frequent(text[i]))