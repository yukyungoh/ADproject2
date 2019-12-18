import unittest

from crowling import Crowling
from WordData import WordData
import buttons

class TestWordData(unittest.TestCase):

    def setUp(self):
        self.actors = Crowling.get_actors(Crowling, 'https://movie.naver.com/movie/bi/mi/point.nhn?code=145162#tab')
        self.scores = Crowling.get_score(Crowling, 'https://movie.naver.com/movie/bi/mi/point.nhn?code=145162#tab')

        self.data1 = WordData.getWord(WordData, 'master.info')
        self.biggestWords, self.reivew = WordData.getReview(WordData, 'master.p')

        self.maxWords, self.reivews = buttons.setReviewData('master')
        self.maxWords = self.maxWords.split('\n')[0].split(':')[0].strip()
        self.reivews = self.reivews.split('\n')[0]


    def testCrowling(self):
        self.assertEquals(self.actors, '이병헌 강동원 김우빈 ')
        self.assertEquals(self.scores, '8.65')

    def testWordData(self):
        self.assertEquals(self.data1, ['이병헌 강동원 김우빈 ', '8.65'])

        #최다 빈도수를 가진 단어가 포함된 리뷰가 저장되었는지 확인
        self.biggestWords = max(self.biggestWords, key=lambda x: self.biggestWords[x])
        self.assertIn(self.biggestWords, self.reivew[0])

        #최다 빈도수를 가진 단어가 포함된 리뷰가 저장되었는지 확인
        self.assertIn(self.maxWords, self.reivews)


if __name__ == '__main__':
    unittest.main()