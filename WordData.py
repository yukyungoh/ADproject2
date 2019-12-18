import pickle

class WordData:

    def writeInfo(self, textFile, actors, scores):
        f = open(textFile, 'wb')
        infoList = [actors, scores]
        pickle.dump(infoList, f)
        f.close()

    def writeReviews(self, textFile, totalText):
        f = open(textFile, 'wb')
        reviewWordDic = dict()

        for k in totalText:
            for i in k:
                reviewWord = i.split()
                for j in reviewWord:
                    if j in reviewWordDic:
                        reviewWordDic[j] += 1
                    else:
                        reviewWordDic[j] = 1

        #최다 빈도수의 단어가 포함된 리뷰 얻어오기
        maxWords = max(reviewWordDic, key=lambda x: reviewWordDic[x])
        reviewSentence = []

        for i in totalText:
            for j in i:
                if maxWords in j:
                    reviewSentence.append(j)

        pickle.dump(reviewWordDic, f)
        pickle.dump(reviewSentence, f)
        f.close()

    def getWord(self, textFile):
        f = open(textFile, 'rb')
        data = pickle.load(f)
        return data

    def getReview(self, textFile):
        f = open(textFile, 'rb')
        words = pickle.load(f)
        sentences = pickle.load(f)
        return words, sentences


if __name__ == "__main__":
    print(WordData.getReview(WordData, 'master.p'))
    tmp = {'tmp':5, 'xd':10}
    print(max(tmp))
    lists = ['abweeefdxd', 'wergsdxd', 'wee']
    for i in lists:
        if max(tmp) in i:
            print(i)
