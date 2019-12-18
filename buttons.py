from crowling import Crowling
from WordData import WordData

c = Crowling
w = WordData

buttons = ['Search', 'Update', 'Clear']

title = ['영화 제목', '주연 배우', '총 평점', '리뷰 단어 \n 빈도수', '최다빈도\n단어 포함\n리뷰']

urls = {'master' : ['https://movie.naver.com/movie/bi/mi/point.nhn?code=145162#tab', 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=145162&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false']
        , '국가 부도의 날' : ['https://movie.naver.com/movie/bi/mi/point.nhn?code=164192#tab', 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=164192&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false']
        , '가장 보통의 연애' : ['https://movie.naver.com/movie/bi/mi/basic.nhn?code=182205', 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=182205&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false']
        , '검은 사제들' : ['https://movie.naver.com/movie/bi/mi/basic.nhn?code=120157', 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=120157&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false']}


def updateData(text):

    actors = c.get_actors(c, urls[text][0])
    score = c.get_score(c, urls[text][0])
    w.writeInfo(w, text + '.info', actors, score)

    reviews = c.get_urlData(c, urls[text][1])
    w.writeReviews(w, text + '.p', reviews)

def setReviewData(text):
    words = ''
    reviewData = WordData.getReview(WordData, text + '.p')
    reviewWords = sorted(reviewData[0].items(), key=lambda x: x[1], reverse=True)

    for word, nums in reviewWords:
        if word != 'actors' and word != 'score':
            words += word + ' : ' + str(nums) + '\n'

    sentences = ''
    for i in reviewData[1]:
        sentences += str(i) + '.' + '\n'

    return words, sentences