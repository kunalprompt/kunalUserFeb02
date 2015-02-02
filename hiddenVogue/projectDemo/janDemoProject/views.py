from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from django.core.context_processors import csrf

def loginView(request):
	if request.method == "GET":
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
				# send POST to Database Server to check Cookie first and then for a valid user get the data
				# response = HttpResponse("Second time user")
				# return response
				response = HttpResponseRedirect('/dashboard')
				return response
		else:
			csrf_token = {}
			csrf_token.update(csrf(request))
			template_name = 'login.html'
			response = render_to_response(template_name, csrf_token)
			response['HTTP_CACHE_CONTROL'] = 'no-cache; private; max-age=0'
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response
	elif request.method == "POST":
		# get and set cookie
		response = HttpResponseRedirect('/dashboard')
		response.set_cookie('uid', '12345')
		response.set_cookie('token', 'mydata#123')
		return response

def dashboardView(request):
	if request.method=="GET":
		# if get
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
			data = {
				'username': 'Kunal Sharma',
				'users_count': 190,
				'items_count': 10,
				'dashboard_chart_data': [
					{ 'period': '2014-09-30', 'users': 2, 'items_sold': 0, 'items_pending': 10 },
					{ 'period': '2014-10-24', 'users': 20, 'items_sold': 3, 'items_pending': 45 }, 
					{ 'period': '2014-11-24', 'users': 40, 'items_sold': 10, 'items_pending': 67 }, 
					{ 'period': '2014-12-24', 'users': 65, 'items_sold': 56, 'items_pending': 15 }, 
					{ 'period': '2015-01-24', 'users': 190, 'items_sold': 27, 'items_pending': 10 }
				]
			}
			return render_to_response('index.html', data)
		else:
			response = HttpResponseRedirect('/')
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response

def usersView(request):
	if request.method=="GET":
		# if get
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
			data = {
				'username': 'Kunal Sharma',
				'users_count': 190,
				'new_joined': 10,
				'users_chart_data': [
					{ 'period': '2014-09-30', 'users_total': 2, 'users_active': 0},
					{ 'period': '2014-10-24', 'users_total': 20, 'users_active': 10},
					{ 'period': '2014-11-24', 'users_total': 40, 'users_active': 28},
					{ 'period': '2014-12-24', 'users_total': 65, 'users_active': 40},
					{ 'period': '2015-01-17', 'users_total': 190, 'users_active': 120},
					{ 'period': '2015-01-28', 'users_total': 205, 'users_active': 85}
				]
			}
			return render_to_response('users.html', data)
		else:
			response = HttpResponseRedirect('/')
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response

def usersListView(request):
	if request.method=="GET":
		# if get
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
			data = {
				'username': 'Kunal Sharma',
				'users_count': 190,
				'new_joined': 10,
				'users' : [					
					{'uid': 1234, 'name': 'Sachin Kumar', 'email': 'sachin.kumar@gmail.com', 'mobile': '8894405512', 'type': 'Buyer', 'date': '2015-01-19'},
					{'uid': 1235, 'name': 'Gurkirat Singh', 'email': 'gurkirat.singh@gmail.com', 'mobile': '8894905612', 'type': 'Buyer/Seller', 'date': '2015-01-19'},
					{'uid': 1236, 'name': 'Tanmoy Mahajan', 'email': 'tanmoy123@gmail.com', 'mobile': '8994905612', 'type': 'Buyer', 'date': '2015-01-20'},
					{'uid': 1236, 'name': 'Mohit Bhardwaj', 'email': 'mohit13.07@gmail.com', 'mobile': '8998605612', 'type': 'Seller', 'date': '2015-01-24'}
				]
			}
			return render_to_response('users_list.html', data)
		else:
			response = HttpResponseRedirect('/')
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response

def itemsView(request):
	if request.method=="GET":
		# if get
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
			data = {
				'username': 'Kunal Sharma',
				'items_sold_count': 190,
				'items_pending_count': 10,
				'items_in_transit_count': 27,
				'items_delivered_count': 27,
				'items_chart_data': [
					{ 'period': '2014-09-30', 'items_sold': 2, 'items_pending': 0, 'items_in_transit': 0, 'items_delivered': 0},
					{ 'period': '2014-10-24', 'items_sold': 20, 'items_pending': 10, 'items_in_transit': 3, 'items_delivered': 17},
					{ 'period': '2014-11-24', 'items_sold': 40, 'items_pending': 28, 'items_in_transit': 8, 'items_delivered': 12},
					{ 'period': '2014-12-24', 'items_sold': 65, 'items_pending': 40, 'items_in_transit': 0, 'items_delivered': 26},
					{ 'period': '2015-01-17', 'items_sold': 190, 'items_pending': 120, 'items_in_transit': 2, 'items_delivered': 19},
					{ 'period': '2015-01-28', 'items_sold': 205, 'items_pending': 85, 'items_in_transit': 100, 'items_delivered': 105},
				]
			}
			return render_to_response('items.html', data)
		else:
			response = HttpResponseRedirect('/')
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response

def itemsListView(request):
	if request.method=="GET":
		# if get
		uid = request.COOKIES.get('uid')
		token = request.COOKIES.get('token')
		if uid != None and token != None:
			data = {
				'username': 'Kunal Sharma',
				'items_sold_count': 190,
				'items_pending_count': 10,
				'items_in_transit_count': 27,
				'items_delivered_count': 27,
				'items' : [
					{'itemId': 1234, 'itemName': 'Allen Solly Shirt', 'itemBrand': 'Allen Solly', 'itemPrice': '512', 'itemLocation': 'Lower Bazar, Shimla', 'itemStatus': 'Sold'},
					{'itemId': 1235, 'itemName': 'Puma ZX Shorts', 'itemBrand': 'Puma', 'itemPrice': '5612','itemLocation': '7C, Chandigarh', 'itemStatus': 'Sold'},
					{'itemId': 1236, 'itemName': 'One Piece Dress - Eavan Womens Shift Dress', 'itemBrand': 'Eavan', 'itemPrice': '9182','itemLocation': 'Arya Bazar, New Delhi', 'itemStatus': 'Delivered'},
					{'itemId': 1237, 'itemName': 'Ishin Floral Print Cotton Sari', 'itemBrand': 'Gujrati Fabrics', 'itemPrice': '1860','itemLocation': 'Phase 3, Mohali', 'itemStatus': 'Pending'},
					{'itemId': 1238, 'itemName': 'Plosh Heels', 'itemBrand': 'Plosh', 'itemPrice': '1360','itemLocation': '19 D, Chandigarh', 'itemStatus': 'In-transit'}
				]
			}
			return render_to_response('items_list.html', data)
		else:
			response = HttpResponseRedirect('/')
			response.delete_cookie('uid')
			response.delete_cookie('token')
			return response

def logoutView(request):
	if request.method=="GET":
		response = HttpResponseRedirect('/')
		response.delete_cookie('uid')
		response.delete_cookie('token')
		return response



'''
response = render_to_response("template.html", {}, context_instance=RequestContext(request))
response['Cache-Control'] = 'no-cache'
return response
'''