#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
# 假设内容都是英文，请统计出你认为每篇日记最重要的词。
# Reference: http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
import math
import os

def words(blob):
	f = open(blob)
	word_list = f.read().split()
	f.close()
	return word_list

def tf(word, blob):
	nwords = words(blob)
	return float(nwords.count(word)) / len(nwords)

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in words(blob))

def idf(word, bloblist):
	return math.log(float(len(bloblist)) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)


if __name__ == "__main__":
	for root, dirnames, filenames in os.walk("MyDiary"):
		bloblist = [os.path.join(root, filename) for filename in filenames]
		for blob in bloblist:
			print "Top words in document {}".format(blob)
			scores = {word: tfidf(word,blob,bloblist) for word in set(words(blob))}
			sorted_words = sorted(scores.items(), key=lambda x:x[1], reverse=True)
			for word, score in sorted_words[:3]:
				print "\tWrod: {}, TF-IDF: {}".format(word, round(score, 5))
