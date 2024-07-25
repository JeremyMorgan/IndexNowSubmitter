# IndexNow Submitter

This is an automated submitter for IndexNow sites. 

You can automatically submit your sitemap in seconds, whenever you update your site, or create a new site. 

## What is IndexNow? 

Great question. IndexNow is an easy way for websites owners to instantly inform search engines about latest content changes on their website. In its simplest form, IndexNow is a simple ping so that search engines know that a URL and its content has been added, updated, or deleted, allowing search engines to quickly reflect this change in their search results.

You can get [more information here](https://www.indexnow.org/). 

Here's how you can use this submitter:

# Get your website URL

This should be pretty easy:

```python
url = 'www.yoursite.com'
```

Make sure your sitemap is at `www.yoursite.com/sitemap.xml` (if not you can modify this script)

# Enter your key

Then enter your IndexNow key. 

If you don't have one, [get a key here](https://www.bing.com/indexnow/getstarted#implementation) and save it as a text file on the root of your site. 

```python
key = '000000000000000000000000000'
```

# Run the Script 

There are no pre requisites to run this, it all uses standard Python libraries

So run it!

```
python3 submit.py
```

And your site will be submitted to:

[IndexNow](https://www.indexnow.com)
[Bing](https://www.bing.com)
[Yandex](https://www.yandex.com)
[Naver](https://www.naver.com)
[Yep](https://www.yep.com)
[Seznam](https://search.seznam.cz)

Automatically. Be careful not to submit too many times, submitting the same sitemap multiple times doesn't do anything. However it's helpful when you update your site map. 


