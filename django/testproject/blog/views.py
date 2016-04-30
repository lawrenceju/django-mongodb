# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse  
from models import searchCompany   #className
from django.shortcuts import render_to_response
	


def index (request):
    return render(request,'index.html')	
	
	
def getExten(request,search):
	search_list = request.GET['name']  #一定要加['name']因為是要取GET物件的name屬性

	num,result,sentence= searchCompany().search_com(search_list)
	
	#weight, features,grp1_news,grp2_news= searchNews().tfIdf_cluster(content,title,date)
	
	
	
	return render_to_response('post_list.html',locals())