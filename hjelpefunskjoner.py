import re

from matplotlib.pyplot import axes
from sklearn.metrics import ConfusionMatrixDisplay

def is_garbage(text):

    text = str(text).strip().lower()
   
    cleaned = re.sub(r'[^a-z0-9\s]', '', text)
    words = cleaned.split()
    
    if len(words) == 0:
        return True

    if len(words) == 1:
        token = words[0]

        # kun symboler/tall
        if not re.search(r'[a-z]', token):
            return True

        # alfanumerisk randomstreng
        if len(token) >= 12 and re.search(r'[a-z]', token) and re.search(r'\d', token):
            return True
        
        # samme tegn gjentatt mange ganger
        if re.fullmatch(r'(.)\1{4,}', token):
            return True

    # samme ord gjentatt mange ganger
    if len(words) >= 5 and len(set(words)) == 1:
        return True

    # nesten bare repetisjon
    if len(words) >= 10 and len(set(words)) <= 2:
        return True

    return False

def map_sentiment(rating):
    if rating <= 2 :
        return 0 # negativ
    elif rating == 3:
        return 1 # nøytral
    else:
        return 2 # positiv
    

