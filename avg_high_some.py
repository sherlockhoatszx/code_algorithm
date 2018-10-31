class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        
        hash = dict()
        for r in results:
            if r.id not in hash:
                hash[r.id] = []

            hash[r.id].append(r.score)
            if len(hash[r.id]) > 5:
                index = 0
                for i in xrange(1, 6):
                    if hash[r.id][i] < hash[r.id][index]:
                        index = i

                hash[r.id].pop(index)

        answer = dict()
        for id, scores in hash.items():
            answer[id] = sum(scores) / 5.0

        return answer
