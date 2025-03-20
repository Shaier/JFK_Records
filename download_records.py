import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

def download_file(url, folder):
    try:
        filename = os.path.basename(url)
        filepath = os.path.join(folder, filename)
        
        if os.path.exists(filepath):
            print(f"File {filename} already exists, skipping...")
            return
            
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def get_pdf_urls(page_url):
    try:
        # Get the page content
        response = requests.get(page_url)
        response.raise_for_status()
        
        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links that point to PDFs
        links = soup.find_all('a', href=True)
        pdf_urls = [urljoin(page_url, link['href']) for link in links if link['href'].endswith('.pdf')]
        
        print(f"Found {len(pdf_urls)} PDF links on the page.")
        return pdf_urls
    except Exception as e:
        print(f"Error fetching PDF links: {e}")
        return []

def main():
    # Create the records folder
    download_folder = "records"
    os.makedirs(download_folder, exist_ok=True)

    # URL of the page to scrape
    page_url = "https://www.archives.gov/research/jfk/release-2025"
    
    # Get all the PDF URLs from the page
    pdf_urls = get_pdf_urls(page_url)
    
    # Download all PDFs using thread pool
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda url: download_file(url, download_folder), pdf_urls)

if __name__ == "__main__":
    main()
