import nltk
import string
from collections import Counter
nltk.download("punkt")
nltk.download("stopwords")
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# This function displays most common word
def most_common_word(text):
    filteredWords = filtered_words(text)
    count_word = Counter(filteredWords)
    most_common_words = count_word.most_common()[:5]
    print(most_common_words)


# This function gives list of words from text without any stop words and punctuation
def filtered_words(text):
    words = nltk.word_tokenize(text)
    # list of stop words and punctuation
    words_no_use = nltk.corpus.stopwords.words("english") + list(string.punctuation)
    return [word for word in words if not word in words_no_use]


# Sample text is taken from Wikipedia Link: https://en.wikipedia.org/wiki/Main_Page

sample_text = """Segnosaurus is a genus of large-bodied
therizinosaurid dinosaurs that lived during the Late Cretaceous.
Discovered in the Gobi Desert in southeastern Mongolia in the 1970s, 
incomplete but well-preserved specimens included the lower jaw, neck and tail vertebrae, 
the pelvis, the shoulder girdle, and limb bones. Parts of the specimens have since 
gone missing or become damaged. Named in 1979, Segnosaurus ('slow lizard') is 
estimated to have been about 6–7 m (20–23 ft) long and 
to have weighed about 1.3 metric tons (1.4 short tons).
It was bipedal, with the trunk of its body tilted upwards. The head was small
with a beak at the tip of the jaws, and the neck was long and slender, 
adapted to browsing. """


most_common_word(sample_text)
# Displaying most common Words in an image
word_cloud = WordCloud().generate(sample_text)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

