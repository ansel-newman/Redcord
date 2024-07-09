from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape_reddit import scrape_reddit
from scrape_discord import scrape_discord
import time
import json
import os
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')

reddit_file = "results_reddit.json"
discord_file = "results_discord.json"
output_file = "results.json"

app = Flask(__name__)
CORS(app)
    
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    words = data.get('words', [])
    current_directory = os.getcwd()
    file_path = current_directory + "/data/results.json"
    results = search_json_file(file_path, words)
    return results

# Post rank meaning logic

def search_json_file(json_file, words):
    return process_json_file(json_file, words)

def post_rank_algorithm_1(json_file, word_list):
    return process_json_file(json_file, word_list)

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def create_synonym_dict(query_words):
    synonym_dict = {}
    for word in query_words:
        synonyms = get_synonyms(word)
        synonym_dict[word] = synonyms
    return synonym_dict

def calculate_frequency_score(post, synonym_dict):
    words_in_post = post.split()
    score = 0
    for query_word, synonyms in synonym_dict.items():
        if query_word in words_in_post:
            score += 1
        for synonym in synonyms:
            if synonym in words_in_post:
                score += 1
    return score

def process_json_file(json_file_path, query_words):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    synonym_dict = create_synonym_dict(query_words)
    scored_posts = []
    for post in data:
        score = calculate_frequency_score(post['content'], synonym_dict)
        if score > 0:
            post['score'] = score
            scored_posts.append(post)
    scored_posts.sort(key=lambda x: x['score'], reverse=True)
    return scored_posts

REDDIT_DONE = False
DISCORD_DONE = False
BOOT_DONE = False

@app.before_request
def boot():
    global REDDIT_DONE, DISCORD_DONE, BOOT_DONE
    if not BOOT_DONE:
        print("-----------------------------------------------------------------------------")
        print("R E D C O R D")
        print("=============================================================================")
        print('\n>>    Setting up Redcord Backend! This process normally takes a few minutes.\n>>    Initiating scraping sequence ...\n')
        if not DISCORD_DONE:
            scrape_discord()
            DISCORD_DONE = True
            print("[Discord data collected]")

        if not REDDIT_DONE and DISCORD_DONE:
            scrape_reddit()
            REDDIT_DONE = True
            print("[Reddit data collected]")
            print("\nRedcord Backend is up and running :)")
        BOOT_DONE = True
    return

if __name__ == '__main__':
    app.run(debug=False)
    
