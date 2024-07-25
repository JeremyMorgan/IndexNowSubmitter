## Parse sitemap

import re

sitemap = "sitemaps/sitemap.xml"

def main():
    # Open a sitemap only extract the url elements
    with open(sitemap, 'r') as file:
        sitemap_xml = file.read()

    url_elements = re.findall(r'<loc>(.*?)</loc>', sitemap_xml)
    # write to a text file named data/urls.txt
    with open('data/urls.txt', 'w') as file:
        for url in url_elements:
            file.write(url + '\n')

if __name__ == "__main__":
    main()



