# Poke Data
This repository contains a personal data engineering project using data from the game Pokemon. 
## First Step - Crawling the data
- **poke_spider.py** is responsible for getting all the data from the game pokemon using scrapy lib.   
  - To get the output of the spider, you just need to run the command `scrapy crawl pokemon -o file_name.json` and access the json containing all relevant data of the pokemons.
