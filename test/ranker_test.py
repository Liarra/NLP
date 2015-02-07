import unittest
from English2NAO.ranker import ranker
from English2NAO.component import component

class test_ranker(unittest.TestCase):
    def test_rankLength(self):
        test_sentence_short_7="Oops, I"
        test_sentence_long_154="Oh, what a bore it is to write a sentence that contains more than a certain amount of letters. Seriously, I am a MSc, can't I find a better thing to do???"
        test_sentence_right_35="I am a good moderate-sized sentence"
        test_sentence_0=""
        test_sentence_65536="a"*65536
        
        r=ranker()
        
        self.assertTrue(    r.rankLength(test_sentence_short_7)==-5    )
        self.assertTrue(    r.rankLength(test_sentence_long_154)==-5   )
        self.assertTrue(    r.rankLength(test_sentence_right_35)==0       )
        self.assertTrue(    r.rankLength(test_sentence_0)==-5          )
        self.assertTrue(    r.rankLength(test_sentence_65536)==-5      )
        
    def test_rankPunctuation(self):
        test_sentence_0=""
        test_sentence_question="Oh, what a bore it is to write a sentence that contains more than a certain amount of letters. Seriously, I am a MSc, can't I find a better thing to do???"
        test_sentence_dot="Hello world. "
        test_sentence_comma="Hello world,"
        test_sentence_none="I wish I had an angel"
        test_sentence_punctuation_inside="Oh, how I wish to go down with this sun. Sleeping"
        
        r=ranker()
        
        self.assertTrue(    r.rankPunctuation(test_sentence_0)                  ==0   )
        self.assertTrue(    r.rankPunctuation(test_sentence_question)           ==0   )
        self.assertTrue(    r.rankPunctuation(test_sentence_dot)                ==5   )
        self.assertTrue(    r.rankPunctuation(test_sentence_comma)              ==5   )
        self.assertTrue(    r.rankPunctuation(test_sentence_none)               ==0   )
        self.assertTrue(    r.rankPunctuation(test_sentence_punctuation_inside) ==0   )
        
    def test_rankTags(self):
        test_sentences=[
            "Nope",
            "One tag tag tag tag tag",
            "Two tags here",
            "Two tags here and third",
        ]
        
        r=ranker()
        c=component("test component")
        c.tags=["tag", "here", "third"]
        
        for i in range (0,4):
            test_sentence=test_sentences[i]
            self.assertEquals(i,r.rankTags(test_sentence,c))
        
    def test_rankRegexp(self):
        test_sentence_no="Nope"
        test_sentence_match="One tag tag tag tag tag"
        test_sentence_tricky="Two tags here"
        
        r=ranker()
        c=component("test component")
        c.regexp=".*(tag )+"
        
        self.assertTrue(    r.rankRegexp(test_sentence_no,c)                  ==0   )
        self.assertTrue(    r.rankRegexp(test_sentence_tricky,c)              ==0   )
        self.assertTrue(    r.rankRegexp(test_sentence_match,c)               ==15  )

