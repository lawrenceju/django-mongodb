from django.db import models
from django.shortcuts import render
from pymongo import MongoClient
import sys
import pymongo


# Create your models here.

class searchCompany(object):
	def __init__(self):
		self.client= MongoClient('10.120.28.17', 27017)

	def search_TT(self,tag1,tag2):
		db=self.client.test       #databaseName
		collection=db.testjobs3      #tableName
		col = collection.find({"$and":[                   
			{"company":{"$regex":tag1}},
			{"jobname":{"$regex":tag2}}
			]},{"_id":0})

		num = col.count()
		result = []
		if num > 0:
			for post in col:
				result.append(post)
		return num,result		
		client.close()		
				
	def search_FT(self,tag2):
		db=self.client.test       #databaseName
		collection=db.testjobs3      #tableName
		num = collection.find({"jobname":{"$regex":tag2}}).count()
		result = []
		for post in collection.find({"jobname":{"$regex":tag2}}):
			result.append(post)
		return num,result
		client.close()	
			
	def search_TF(self,tag1):
		db=self.client.test       #databaseName
		collection=db.testjobs3      #tableName
		num = collection.find({"company":{"$regex":tag1}}).count()
		result = []
		for post in collection.find({"company":{"$regex":tag1}}):
			 result.append(post)
		return num,result
		client.close()	
			
			
	def search_com(self,search_list):
		db=self.client.test       #databaseName
		collection=db.testjobs3		#tableName
		tag1,tag2 = search_list.split(',')
		sentence = tag1 + tag2
		num1 = collection.find({"company":{"$regex":tag1}}).count()
		num2 = collection.find({"jobname":{"$regex":tag2}}).count()
		if num1 > 0:
			if num2 > 0:
				num,result = searchCompany.search_TT(self,tag1,tag2)
			else:
				num,result = searchCompany.search_TF(self,tag1)
		else:
			if num2 > 0:
				num,result = searchCompany.search_FT(self,tag2)
			else:
				result = " "
				num = 0
		return num,result,sentence
		client.close()
