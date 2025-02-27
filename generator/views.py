from django.shortcuts import render
import random
import string

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	alphabets = string.ascii_lowercase
	length = int(request.GET.get('length', 13))
	passcount = int(request.GET.get('passcount', 1))

	if request.GET.get('uppercase'):
		alphabets += string.ascii_uppercase

	if request.GET.get('special'):
		alphabets += string.punctuation

	if request.GET.get('number'):
		alphabets += string.digits
	
	def generate(chars,length):
		finalpass = ''

		for i in range(-(-length//2)):
			finalpass += random.choice(string.ascii_letters)

		for i in range(length - -(-length//2)):
			finalpass += random.choice(chars)
		finalpass = ''.join(random.sample(finalpass,len(finalpass)))
		return finalpass

	payload = [generate(alphabets,length) for i in range(passcount)]	
		
	return render(request, 'generator/password.html', {'passwords': payload})