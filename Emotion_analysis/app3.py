import streamlit as st
import string
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

st.title("Emotion in the Text")
text = st.text_area("Write your text",placeholder="Copy-Paste the text you want to analyse.")

lower_text = text.lower()
cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))
tokenized_text = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "also"]

final_words = []
for word in tokenized_text:
    if word not in stop_words:
        final_words.append(word)

emotion_list = []
with open(r'Emotion_analysis/emotion.txt') as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'","").strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
    
result = st.button("Get Graph")

if result:
    count = Counter(emotion_list)
    keys = list(count.keys())
    values = list(count.values())
    sorted_value_index = np.argsort(values)
    count= {keys[i]: values[i] for i in sorted_value_index}
    fig, ax = plt.subplots()
    ax.bar(count.keys(),count.values())
    fig.autofmt_xdate()
    #plt.xticks(rotation = 90)
    st.pyplot(fig)
