# Redcord
### Created by Ansel Newman

## What is Redcord?

This site is a proof of concept project that scrapes reddit and discord to find information relevant to given search query. It is meant to make searching for techinical questions easier for developers by navigating a wealth of forums to find the answer to a question or to get recent public chatter on a topic. The currently supported list of searched forums are below (more will be added over time):
<ul>
    <li>Reddit/r/webdev</li>
    <li>Reddit/r/javascript</li>
    <li>Discord/JavaScript Mastery Community</li>
    <li>Discord/web dev and web design</li>
</ul>

## How do I use this site?

Simply insert a string of white-spaced seperated query words that capture the primary meaning of your question. Make sure to not include articles or other filler words because doing so can throw off the relevancy score of posts and make your results less organized or related. This scoring proces works by taking the initial string of query words, splitting it to a list, and then generating a dictionary of synonyms for each word and then parsing through all posts from the forum looking for these query words or their syonyms. Each post is then scored where scores less than 0 are discluded from the results. Higher scores are listed first and therefore manifest at the top of the web page.

## How do I deploy this site locally?

Simply clone this repository to a presignated location locally using the command within the desired directory:

<code>git clone https://github.com/ansel-newman/Redcord.git</code>

The repo should be downloaded, and a subdirectory Redcord should appear. Enter the folder (cd Redcord) and run the following commands:

<code>npm install</code>

<code>npm run dev</code>

Navigate to the localhost link that appears in the terminal within your browser.
This will effectively set up the front end but we are not complete. In a new terminal navigate to the Redcord folder, then navigate to the backend folder (cd backend)

First we will set up a virtual environment with python version 3.10.1 to be compatible with the project's dependencies and to accomplish this run the following in terminal:

<code>python3.10 -m venv venv</code>

<code>source venv/bin/activate</code>

<code>python --version</code>

Now we install the dependencies using the requirements.txt file. In the terminal run

<code>pip install -r requirements.txt</code>

Finally to begin the process of scraping the data for use and communicating with the frontend run:

<code>python3 app.py</code>

This should enable functionality, so please enjoy!


### Licensing 
This project is released under the M.I.T. open source license. Anyone is welcome to use and improve.
