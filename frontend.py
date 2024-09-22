import streamlit as st


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


st.title("Recap Rephrasing")
# st.text("please input the text you want to recap ")
# st.chat_input()

user_input = st.text_area("Enter a phrase:", "")

# Button to trigger the rephrasing
if st.button("Rephrase"):
    if user_input:
        # Use the paraphrasing model to rephrase the input
        # rephrased_text = paraphrase_model(user_input, num_return_sequences=1)[0]['generated_text']
        st.subheader("Rephrased Text:")
        st.write(functions(user_input))
    else:
        st.warning("Please enter a phrase.")