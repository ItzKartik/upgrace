from django.shortcuts import render
import requests
from django.http import HttpResponse
import random
import json 


class generator(View):
    def post(self, *args, **kwargs):
        hashtag = self.request.POST['keyword']
        min_posts = None
        max_posts = None
        search_url = 'https://www.instagram.com/web/search/topsearch/'
        explore_headers = {'Host': 'www.instagram.com',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                                'Accept': '*/*',
                                'Accept-Language': 'en-US;q=0.7,en;q=0.3',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'X-Requested-With': 'XMLHttpRequest',
                                'Referer': 'https://www.instagram.com/',
                                'Connection': 'keep-alive'}
        if hashtag[0] != '#':
            hashtag = '#' + hashtag
        params = {'context': 'blended',
                  'query': hashtag,
                  'rank_token': random.uniform(0, 1)}
        response = self.get_request(search_url, params=params, headers=explore_headers)
        tag_list = response.json()['hashtags']
        tags = []
        for tag in tag_list:
            if min_posts:
                if tag['hashtag']['media_count'] < min_posts:
                    continue
            if max_posts:
                if tag['hashtag']['media_count'] > max_posts:
                    continue
            tags.append(tag['hashtag']['name'])
        return HttpResponse(json.dumps(tags))

    def get_request(self, url, params=None, **kwargs):
        """Make a GET request"""
        self.s = requests.Session()
        request = self.s.get(url, params=params, **kwargs)
        return self.analyze_request(request)

    def analyze_request(self, request):
        """Check if the request was successful"""
        if request.status_code == 200:
            return request
        else:
            raise requests.HTTPError(str(request.status_code))