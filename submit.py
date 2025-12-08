
import http.client
import json
import os
import re

## URL (without https)

url = 'www.formularookies.com'
# get your key here https://www.bing.com/indexnow/getstarted#implementation
key = 'a2e79b4e18904bb3bf5e0efd94f89d75'

def download_and_save_sitemap(url):
    """
    This function downloads a sitemap from the specified URL and saves it to the 'sitemaps' directory.

    :param url: The URL of the sitemap to be downloaded.
    :type url: str
    :return: A string indicating the success or failure of the operation. If successful, it returns "Sitemap downloaded and saved successfully." Otherwise, it returns "Error! " followed by the exception message.
    :rtype: str
    """
    try:
        # Create HTTPS connection
        conn = http.client.HTTPSConnection(url)
        conn.request("GET", "/sitemap.xml")
        res = conn.getresponse()
        data = res.read()
        conn.close()

        # Define the path for the sitemap
        sitemap_path = 'sitemaps/sitemap.xml'

        # Check if the sitemap already exists and delete it
        if os.path.exists(sitemap_path):
            os.remove(sitemap_path)

        # Ensure the sitemaps directory exists
        if not os.path.exists('sitemaps'):
            os.makedirs('sitemaps')

        # Save the new sitemap
        with open(sitemap_path, 'wb') as file:
            file.write(data)

        return "Sitemap downloaded and saved successfully."
    except Exception as e:
        return "Error! " + str(e)

def write_urls():
    """
    This function reads the sitemap.xml file, extracts the URLs from it, and writes them to a text file named data/urls.txt.

    :param None: This function does not require any input parameters.
    :return: This function does not return any value explicitly. It writes the extracted URLs to the specified text file.
    """
    with open('sitemaps/sitemap.xml', 'r') as file:
        sitemap_xml = file.read()
        url_elements = re.findall(r'<loc>(.*?)</loc>', sitemap_xml)
        with open('data/urls.txt', 'w') as file:
            for url in url_elements:
                file.write(url + '\n')

def create_postman_file():
    """
    This function creates a postman.txt file containing the IndexNow API request format.
    It uses the URL and key from the configuration, and includes all URLs from data/urls.txt.

    :param None: This function does not require any input parameters.
    :return: A string indicating success or failure of the operation.
    """
    try:
        # Read URLs from urls.txt
        with open('data/urls.txt', 'r') as file:
            urlList = [line.strip() for line in file if line.strip()]
        
        # Format the URL list with proper indentation and quotes
        formatted_urls = ',\n      '.join([f'"{url}"' for url in urlList])
        
        # Create the postman.txt content
        postman_content = f"""POST /IndexNow HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: api.indexnow.org
{{
  "host": "{url}",
  "key": "{key}",
  "keyLocation": "https://{url}/{key}.txt",
  "urlList": [
      {formatted_urls}
      ]
}}"""
        
        # Write to postman.txt
        with open('postman.txt', 'w') as file:
            file.write(postman_content)
        
        return "postman.txt created successfully."
    except Exception as e:
        return f"Error creating postman.txt: {str(e)}"

def submit_payload(payload, headers, sitename, siteurl):

    #print("Payload: " + payload)
    #print("Headers: " + headers)
    #print("Site name: " + sitename)
    #print("URL : " + siteurl)


  conn = http.client.HTTPSConnection(siteurl)
  conn.request("POST", "/IndexNow", payload, headers)
  res = conn.getresponse()
  data = res.read()

  if res.status == 200 or res.status == 202:
    print(sitename +" submission successful.")
  else:
    print(sitename + " submission failed.")
    print(f"Status code: {res.status}")
    print(data.decode("utf-8"))
  conn.close()

# main block
def main():
    """
    This function is the main entry point for the script. It performs the following tasks:
    1. Downloads the sitemap from the specified URL and saves it to the 'sitemaps' directory.
    2. Writes the URLs extracted from the sitemap to a text file named 'data/urls.txt'.
    3. Submits the extracted URLs to various search engines using the 'submit_payload' function.

    :param None: This function does not require any input parameters.
    :return: This function does not return any value explicitly. It prints the submission status for each search engine.
    """

    try:
      # Download the sitemap
      print(download_and_save_sitemap(url))

      # Write the URLs to a text file
      write_urls()

      # Create the postman.txt file
      print(create_postman_file())

      # read from urls.txt and parse line by line
      with open('data/urls.txt', 'r') as file:
        urlList = [line.strip() for line in file]
        print("Submitting: " + url)
        payload = json.dumps({
            "host": url,
            "key": key,
            "keyLocation": "https://" + url + "/" + key + ".txt",
            "urlList": urlList
        })
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

        print("Submitting: https://" + url)
        #submit_payload(payload, headers, "seznam", "search.seznam.cz")
        #submit_payload(payload, headers, "IndexNow", "api.indexnow.org")
        #submit_payload(payload, headers, "Bing", "www.bing.com")
        #submit_payload(payload, headers, "Yandex", "yandex.com")
        #submit_payload(payload, headers, "Amazon", "indexnow.amazonbot.amazon")
        #submit_payload(payload, headers, "Naver", "searchadvisor.naver.com")
        #submit_payload(payload, headers, "Yep", "indexnow.yep.com")


        #IndexNow hub	https://api.indexnow.org/indexnow
        #Bing	https://www.bing.com/indexnow
        #Yandex	https://yandex.com/indexnow
        #Naver	https://searchadvisor.naver.com/indexnow
        ##Seznam.cz	https://search.seznam.cz/indexnow
        #Yep	https://indexnow.yep.com/indexnow


    except Exception as e:
        print("Error! " + str(e))

if __name__ == "__main__":
   main()
