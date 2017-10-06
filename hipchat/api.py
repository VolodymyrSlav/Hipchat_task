import falcon
import re
import urllib2
from BeautifulSoup import BeautifulSoup

class ParserResource:
    def on_get(self,req,resp):
        response = {}
        input_string = req.get_param("input")
        if input_string:
            mentions = re.findall(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", input_string)
            emoticons = re.findall(r"\(([^\W_]{,15})\)", input_string)
            links = []
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', input_string)
            for url in urls:
                soup = BeautifulSoup(urllib2.urlopen(url))
                page_title = soup.title.string 
                links.append({"url": url, "title": page_title})

            if len(mentions):
                response['mentions'] = mentions
            if len(emoticons):
                response['emoticons'] = emoticons
            if len(links):
                response['links'] = links

        resp.media = response

api = falcon.API()
api.add_route('/', ParserResource())
