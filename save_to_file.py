import codecs

def save(text):
    with codecs.open("upload.txt", "w", "utf-16") as stream:  # or utf-8
        stream.write(text + u"\n")