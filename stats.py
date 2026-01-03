def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    
    for ch in text:
        lch = ch.lower()
        if lch not in chars:
            chars[lch] = 1
        else:
            chars[lch] += 1

    return chars

def sort_on_num(item):
    return item["num"]

def sorted_char_list(chars):
    result = []
    for k in chars:
        result.append({"char": k, "num": chars[k]})

    result.sort(reverse=True, key=sort_on_num)

    return result

