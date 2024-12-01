import json
from bs4 import BeautifulSoup
from utils import fetch_html, save_to_json
from config import BASE_URLS, OUTPUT_FILE, SMALL_SAMPLE_FILE, HEADERS


def clean_text(text):
    """Clean up the extracted text."""
    return text.replace('\n', ' ').strip()


def parse_react_docs(html):
    """Parse React documentation."""
    soup = BeautifulSoup(html, "html.parser")
    sections = []
    nav_links = soup.select("nav a")  # Select all links in the navigation bar
    for link in nav_links:
        section_title = link.text.strip()
        relative_url = link['href']

        # Check if the URL is already absolute, otherwise prepend the base URL
        if not relative_url.startswith('http'):
            section_url = f"https://react.dev{relative_url}"
        else:
            section_url = relative_url

        # Fetch the content of the section (article or other content)
        section_html = fetch_html(section_url, HEADERS)
        if not section_html:
            continue

        section_soup = BeautifulSoup(section_html, "html.parser")
        article = section_soup.find('article')
        content = clean_text(
            article.get_text()) if article else "No content available"

        # Append the section with title, source, URL, and content
        sections.append({
            "title": section_title,
            "source": "react",
            "url": section_url,
            "sections": [content]
        })

    return sections

def parse_aws_docs(html):
    """Parse AWS Lambda documentation."""
    soup = BeautifulSoup(html, "html.parser")
    sections = []
    content_links = soup.select("li.nav-link a")
    for link in content_links:
        section_title = link.text.strip()
        section_url = f"https://docs.aws.amazon.com{link['href']}"
        section_html = fetch_html(section_url, HEADERS)
        if not section_html:
            continue
        section_soup = BeautifulSoup(section_html, "html.parser")
        content_div = section_soup.find('div', {'class': 'awsdocs-container'})
        content = clean_text(content_div.get_text()
                             ) if content_div else "No content available"

        sections.append({
            "title": section_title,
            "source": "aws_lambda",
            "url": section_url,
            "sections": [content]
        })
    return sections


def scrape_docs():
    """Scrape React and AWS Lambda documentation."""
    scraped_data = []
    for source, url in BASE_URLS.items():
        print(f"Scraping {source}...")
        html = fetch_html(url, HEADERS)
        if not html:
            continue
        if source == "react":
            scraped_data.extend(parse_react_docs(html))
        elif source == "aws_lambda":
            scraped_data.extend(parse_aws_docs(html))
    return scraped_data


if __name__ == "__main__":
    data = scrape_docs()
    # Save all scraped data to the output file
    save_to_json(data, OUTPUT_FILE)
    # Save a small subset of the scraped data for testing purposes
    save_to_json(data[:1], SMALL_SAMPLE_FILE)
    print("Scraping completed successfully.")
