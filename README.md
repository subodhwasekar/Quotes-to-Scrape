# Quotes to Scrape Scrapy Project

This is a Scrapy project for practicing web scraping on the [Quotes to Scrape](http://quotes.toscrape.com/) website. The project is designed to extract quotes, authors, and tags from the website's pages.

## Project Overview

Web scraping is a technique used to extract data from websites. In this project, we are using Scrapy, a powerful and flexible web scraping framework for Python, to build a spider that navigates through the Quotes to Scrape website, extracts valuable information, and saves it for further analysis.

## Project Steps

### 1. Setup

- Ensure you have Python installed on your system.
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment:
  - On Windows: `venv\Scripts\activate`
  - On Unix or MacOS: `source venv/bin/activate`
- Install Scrapy: `pip install scrapy`

### 2. Project Initialization

- Create a new Scrapy project: `scrapy startproject project_name`
- Navigate to the project folder: `cd project_name`

### 3. Generic Spider Creation

- scrapy genspider <name_of_spider> <website>

### 4. Spider Development

- Open `name_of_spider.py` in the `spiders` folder.
- Implement the spider to extract quotes, authors, and tags.
- Test the spider in the Scrapy shell: `scrapy shell "http://quotes.toscrape.com"`

### 5. Spider Execution

- Run the spider and store the results in a CSV file:
  
  scrapy crawl name_of_spider -o file_name.csv


