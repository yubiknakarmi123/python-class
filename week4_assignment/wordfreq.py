def word_frequency(text):
    text = text.lower()
 
    # remove punctuation
    for ch in ".,!?":
        text = text.replace(ch, "")
 
    words = text.split()
 
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
 
    # find top 3 manually
    top_3 = []
    counts_copy = counts.copy()
    for i in range(3):
        best_word = None
        best_count = 0
        for word in counts_copy:
            if counts_copy[word] > best_count:
                best_word = word
                best_count = counts_copy[word]
        if best_word is not None:
            top_3.append((best_word, best_count))
            del counts_copy[best_word]
 
    return top_3
 
 
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""
 
print("Word frequency counter")
top_words = word_frequency(text)
print("Top 3 words:")
for word, count in top_words:
    print(word + " - " + str(count) + " times")
