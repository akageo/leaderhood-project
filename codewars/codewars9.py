def generate_hashtag(s):
    s = "#" + s.title()
    s = s.split(" ")
    s = "".join(s)
    if len(s) in range(2,140):
        return s
    else:
        return False