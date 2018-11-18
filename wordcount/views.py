from django.http import *
from django.shortcuts import render
import operator
def homepage(request):
	# name='ahsish'

    return render(request,'home.html')


def count(request):
	data = request.GET['fulltextarea']
	list1= data.split(' ')
	
	j=len(list1)


	word_dict={}


	for word in list1:
		if word in word_dict:
			word_dict[word]+=1

		else :
			word_dict[word]=1




  
	word_dict = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
	# print (word_dict)

	return render(request,'count.html',{'textarea':data,'number':j,'word_dict':word_dict})

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')