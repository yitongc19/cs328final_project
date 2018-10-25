import os

# def clean_str(string):
#     """
#     Tokenization/string cleaning for all datasets except for SST.
#     Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
#     """
#     import re
#     string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
#     string = re.sub(r"\'s", " \'s", string)
#     string = re.sub(r"\'ve", " \'ve", string)
#     string = re.sub(r"n\'t", " n\'t", string)
#     string = re.sub(r"\'re", " \'re", string)
#     string = re.sub(r"\'d", " \'d", string)
#     string = re.sub(r"\'ll", " \'ll", string)
#     string = re.sub(r",", " , ", string)
#     string = re.sub(r"!", " ! ", string)
#     string = re.sub(r"\(", " \( ", string)
#     string = re.sub(r"\)", " \) ", string)
#     string = re.sub(r"\?", " \? ", string)
#     string = re.sub(r"\s{2,}", " ", string)
#     return string.strip().lower()

def clean(text):
    import re
    words = []
    for line in text:
        ws = line.strip().split(" ")
        ws = [re.sub(r'\W+', '', w) for w in ws]
        words.append(ws)
    return words
    
def load_data(folder):
    labels = []
    data = []
    for f in os.listdir("data/" + folder):
        first = 0 if f[0] == "d" else 1 
        second = 0 if folder[:3] == "neg" else 1
        labels.append((first, second))
        text = clean(open("data/" + folder + "/" + f))
        data.append(text)
    return labels, data