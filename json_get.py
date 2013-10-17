import json
import urllib2

def load_json(subreddit):
    req = urllib2.urlopen('http://www.reddit.com/r/' + subreddit + '.json?limit=1000')
    try:
        json_string = json.load(req)
    except ValueError:
        req = urllib2.urlopen('http://www.reddit.com/r/kittens.json?limit=1000')
        json_string = json.load(req)
        
    return json_string[u'data'][u'children']

def generate_list():
    obj = load_json(load_subreddit())
    img_urls = []
    for a in obj:
        if a[u'data'][u'domain'] == u'i.imgur.com':
            img_urls.append( a[u'data'][u'url'])
    return img_urls

def load_subreddit():
    f = open('subreddit', 'r')
    subreddit = f.readline().strip()
    f.close()
    return subreddit

