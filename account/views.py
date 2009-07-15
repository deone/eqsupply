from django.shortcuts import render_to_response

import datetime

def login(request):
	now = datetime.datetime.now()

	return render_to_response('account/login.html', {'current_date': now})
