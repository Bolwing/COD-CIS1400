#NAME : KENNETH SEGOVIA
#DATE : 05/01/2021
#Assignment 14

#global vars
name = 'Kenneth Segovia '
data = '05/01/2021'
cla = 'CIS1400-NET '
asn = 'Assignment 14 '
smr = 'Menu Driven, Array, Input Output, Error, Loop'
emg = 'END OF FILE MESSAGE '
cm = ','
nl = '\n \n '


#extra vars

letter1 = ("A","B","C","D","F",)
letter2 = (90,80,70,60)

missq = 0
questq = 0
somequiz = None

error = "\nINVALID AMOUNT\n"
titles = ("enter the following information: ", '\tAmount of Questions: \t', '\tNum Questions Missed: \t', 'Each Question is worth', 'pts', '\tScore: \t', '\tGrade: \t')
assign = ('Assignment 1','Assignment 2','Assignment 3','Assignment 4','Assignment 5','Assignment 6','Assignment 7','Assignment 8','Assignment 9','Assignment 10','Assignment 11','Assignment 12','Assignment 13','Assignment 14','Assignment 15')
quizT = ('Quiz 1','Quiz 2','Quiz 3','Quiz 4','Quiz 5','Quiz 6','Quiz 7','Quiz 8','Quiz 9','Quiz 10','Quiz 11','Quiz 12','Quiz 13','Quiz 14','Quiz 15')
examT = ('Midterm','Final')


title14 = 'QUIZ 14'
title14 = 'QUIZ 15'

class Assignment:

    def set_score(self,s):
        self._score = s

    def get_score(self):
        return self._score

    def get_grade(self):
        if self._score >= letter2[0]:
            grade = gradeL[0]
        elif self._score >= letter2[1]:
            grade = gradeL[1]
        elif self._score >= letter2[2]:
            grade = gradeL[2]
        elif self._score >= letter2[3]:
            grade = gradeL[3]
        else:
            grade = gradeL[4]

        return grade

class Quiz(Assignment):

    def _init_(self,qs,miss):

        self._quests = qs
        self._missed = miss

        self._ptseach = 100.0/self._quests

        numscore = 100.0 - (self._missed * self._ptseach)

        self.set_score(numscore)

    def get_ptseach(self):
        return self._ptseach

    def get_missed(self):
        return self._missed

def getinfo():
    global missq
    global questq

    print(titles[0])
    questq = int(input(titles[1]))

    valid = False
    while not valid:
        missq = int(input(titles[2]))
        if missq > questq:
            print(error)
        else:
            vaild = True

    print()

def disp():
    global somequiz

    somequiz = Quiz(questq,missq)

    print(titles[3], somequiz.get_ptseach(), titles[4])
    print(titles[5], somequiz.get_score())
    print(titles[6], somequiz.get_grade())

def quiz14():
    print(title14)

    getinfo()
    disp()

def main():
    quiz14()

main()
