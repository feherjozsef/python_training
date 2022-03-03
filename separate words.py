# Írj egy olyan fv-t, amely paraméterül kap szavak listáját és összefűzi őket vesszővel elválasztva és ezzel tér vissza
# De az utolsó elem után NE legyen vessző

def concat_words(words):
    result = ""
    counter = 1
    for word in words:
        if counter < len(words):
            result += word + ","
            counter += 1
        else:
            result += word
    return result


print(concat_words(["a", "b", "c"]))


def concat_words(words):
    result = ""
    is_first = True
    for word in words:
        if not is_first:
            result += ","
        result+= word
        is_first = False
    return result

print(concat_words(["a", "b", "c"]))
