import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from nltk.stem import WordNetLemmatizer
import nltk
import random
import string 
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, "linarc-help.txt"), 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
                      "hello", "I am glad! You are talking to me"]

lemmer = WordNetLemmatizer()

sent_tokens = nltk.sent_tokenize(raw) 
word_tokens = nltk.word_tokenize(raw) 


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo_response = robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

class AnswerQuestions(APIView):
    def post(self,request):
            user_response = request.data['text']
            user_response = user_response.lower()
            if(user_response != 'bye'):
                if(user_response == 'thanks' or user_response == 'thank you'):
                    flag = False
                    return Response("You are welcome..")
                else:
                    if(greeting(user_response) != None):
                        return Response(greeting(user_response))
                    else:
                        return Response(response(user_response))
            else:
                flag = False
                return "Bye! take care.."