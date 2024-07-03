from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape_reddit import scrape_reddit
from scrape_discord import scrape_discord
import time
import json

reddit_file = "results_reddit.json"
discord_file = "results_discord.json"
output_file = "results.json"

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/load', methods=['GET'])
def load():
    # scrape_reddit()
    # scrape_discord()
    # time.sleep(60)
    # merge_json_files('/Users/anselnewman/Desktop/project/Redcord/backend/data/results_reddit.json','/Users/anselnewman/Desktop/project/Redcord/backend/data/results_discord.json', '/Users/anselnewman/Desktop/project/Redcord/backend/data/results.json')
    return

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    words = data.get('words', [])
    results = search_json_file('/Users/anselnewman/Desktop/project/Redcord/backend/data/results.json', words)
    # return jsonify(results)
    # return jsonify(results)
    return results

# def some_function_from_search_py(words): 
#     return [word.upper() for word in words]

def merge_json_files(file1, file2, output_file):
    with open(file1, 'r') as f:
        data1 = json.load(f)
    with open(file2, 'r') as f:
        data2 = json.load(f)
    merged_data = data1 + data2
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)
    return

def search_json_file(json_file, words):
    with open(json_file, 'r') as file:
        data = json.load(file)
    matching_elements = []
    for element in data:
        if any(word in json.dumps(element) for word in words):
            matching_elements.append(element)
    # print(matching_elements)
    return matching_elements

if __name__ == '__main__':
    scrape_reddit()
    # scrape_discord()
    app.run(debug=True)
