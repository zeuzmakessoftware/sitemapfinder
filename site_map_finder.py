import requests
import sys

def test_existance(website):
    if "/" in website:
        website = website.strip("/")
    if "http" not in website:
        website = f"http://{website}"
    variations = ["robots.txt", "sitemap.xml", "sitemap_index.xml",
    "sitemap-index.xml", "sitemap.php", "sitemap.txt",
    "sitemap.xml.gz", "sitemap/", "sitemaps/", "sitemap/sitemap.xml",
    "sitemapindex.xml", "sitemap/index.xml", "sitemap1.xml",
    "rss/", "rss.xml", "atom.xml"]
    for vari in variations:
        check_website_exists(f"{website}/{vari}")

def check_website_exists(website):
    try:
        response = requests.get(website)
        print(f"{response.status_code} {website}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking the website: {e}")

args = sys.argv[1]
test_existance(args)
