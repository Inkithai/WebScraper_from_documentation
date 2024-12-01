# Web Scraper for AWS Lambda and React Documentation

This Python-based web scraper extracts and structures relevant documentation content from AWS Lambda and React websites. The scraped data is formatted in a JSON schema for use in a Retrieval-Augmented Generation (RAG) system.

## Table of Contents
1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Testing](#testing)

## Overview

The web scraper fetches data from the following documentation pages:
- **React Documentation** - Scrapes sections such as Quick Start, Installation, and Managing State from [React Docs](https://react.dev/learn).
- **AWS Lambda Documentation** - Scrapes sections like "What is AWS Lambda?", "Code Examples", and more from [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

The extracted data is saved in a structured JSON format for further use in a local knowledge base. A small subset of the data is included in the video demonstration.

## Setup Instructions

To set up and run this project, follow these steps:

### 1. Clone the Repository
```bash
git clone hhttps://github.com/Inkithai/WebScraper_from_documentation.git
cd WebScraper_from_documentation

Create a virtual environment and install the required libraries.
python3 -m venv venv

Windows
venv\Scripts\activate

pip install -r requirements.txt

To run the scraper, execute the following Python script:

python scraper/src/scraper.py

This will
Scrape both AWS Lambda and React documentation.
Save the full scraped data in scraped_data/complete.json.
Save a small subset in scraped_data/small_subset.json (for video demonstration).

##file-structure

scraper/
├── src/
│   ├── scraper.py          # Main script for scraping
│   ├── utils.py            # Helper functions
│   ├── config.py           # Configuration settings (URLs)
├── tests/                  # Unit tests for the scraper
├── requirements.txt        # Python dependencies
├── README.md               # Project instructions
├── scraped_data/
│   ├── complete.json       # Full scraped data in JSON format
│   └── small_subset.json   # A small subset of data for demo

##Testing
Testing can be done using pytest or similar frameworks. To run tests:
pytest

