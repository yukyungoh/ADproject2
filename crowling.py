import requests
from bs4 import BeautifulSoup
import re

class Crowling:

    def get_actors(self, test_url):
        resp = requests.get(test_url)
        html = BeautifulSoup(resp.content, 'html.parser')
        info_spec = html.find('dl', {'class': 'info_spec'})
        p = info_spec.findAll('p')
        actors = p[2].findAll('a')

        totalactors = ''
        for actor in actors:
            totalactors += (actor.getText() + ' ')
        return totalactors

    def get_score(self, test_url):
        resp = requests.get(test_url)
        html = BeautifulSoup(resp.content, 'html.parser')
        star_score = html.find('div', {'class': 'star_score'})
        scores = star_score.findAll('em')

        totalscore = ''
        for i in scores:
            totalscore += i.getText()
        return totalscore

    def get_review(self, test_url):
        resp = requests.get(test_url)
        html = BeautifulSoup(resp.content, 'html.parser')
        score_result = html.find('div', {'class': 'score_result'})
        lis = score_result.findAll('li')
        reviewList = []

        for li in lis:
            review_text = li.find('p').getText()
            review_text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》관람객]', '', review_text)
            reviewList.append((review_text).strip())
        return reviewList

    def get_urlData(self, url):
        totalText = []
        for i in range(1, 101):
            reviewUrl = url + '&page=' + str(i)
            print(reviewUrl)
            totalText.append(self.get_review(self, reviewUrl))
        return totalText

if __name__ == "__main__":
    c = Crowling
    test_url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=145162&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
    print(c.get_urlData(c, test_url))
    print(c.get_score(c, 'https://movie.naver.com/movie/bi/mi/point.nhn?code=120157#tab'))
