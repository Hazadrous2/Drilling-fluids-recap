import pandas as pd 

def capitalize_after_punctuation(text):
    # Split by both period and comma, but retain punctuation marks
    punctuations = ['.',',']
    
    for punc in punctuations:
        sentences = text.split(f'{punc} ')
        sentences = [sentence.strip().capitalize() for sentence in sentences]
        text = f'{punc} '.join(sentences)
    return text

def check_punctuation(word):
    punctuations = ['.', ',']
    return any(char in punctuations for char in word)

def functions(input_text):
    df=pd.read_excel("Recap Reph.xlsx")
    a=df.set_index('Initials').to_dict()['Complete words']
    data =input_text.split()
    final=[]
    
    for i in data:
        if check_punctuation(i):
            if "," in i:
                dd=i.split(",")
                for j in dd:
                    if j.upper() in list(a.keys()):
                        final.append(a[j.upper()])
                    else:
                        final.append(j)
                    if dd.index(j) != len(dd) - 1: 
                        final.append(",")

            elif '.' in i:
                dd=i.split(".")
                for j in dd:
                    if j.upper() in list(a.keys()):
                        final.append(a[j.upper()])
                    else:
                        final.append(j)
                    if dd.index(j) != len(dd) - 1: 
                        final.append(".")
                    
        else:
            if i.upper() in list(a.keys()):
                final.append(a[i.upper()])
            else:
                final.append(i)
    final_text = ' '.join(final)
    final_text = final_text.capitalize()
    final_text=capitalize_after_punctuation(final_text)

    return final_text
