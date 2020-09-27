# NLP-in-Bangla
A simple web project in DJango Framwork to analys any Bangla Corpus. Uses Python 3.6.2

# Installation
  - Install Django: ![Django Installation Guide](https://github.com/Yunus0or1/Guidelines-How_TO/blob/master/How%20to%20use%20Django%20Framework.txt)
  - Install mySQL client for Django.
  - This project needs **Python 3.6.2** as this is the last version (upto this text file creation) that supports mysqlclient.
  - Install Xampp.
  - Clone or download the project.
  - Load nlp.sql in Database.
  - Open the cmd.
  - Set the path to the project.
  - Run the project in localhost.
  
# pip commands
  - pip install Django
  - pip install nltk
  - pip install googletrans
  - pip install "mysqlclient==1.3.2"
  
# Update on googletrans library
>When the project was developed google translator could be used without any API key.  But this project was being uploaded googletrans stopped working. So I would suggest everyone to check if googletrans working in that time. Check stackoverflow or Github discussion to fix this. You can use first features like finding compound word and finding total number of bangla word easily. But you can not use those features which use googletrans to translate Bangla meaning to English.

# Features

  - Counts unique Bangla word
  - Extracts compund Bangla words
  - POS tagging of Bangla words by transalting them into English.
  - Search specific word frequencies.
