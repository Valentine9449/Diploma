from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings

from django.views.generic import ListView

from cart.cart import Cart

from authentication.models import User
from datetime import date

from .models import Gas, Stock, PastStock, Category, Product, Comment, Order, Service
from .forms import ImageForm, ServiceForm, CommentForm


#-------------SEARCH PRODUCT-------------#


class SearchResultsView(ListView):
    model = Category
    template_name = 'app/search_results.html'
 
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
        	Q(name__iregex=query) | 
        	Q(category__name__iregex=query)
        	)
        if len(object_list) == 0:
        	raise Http404('На жаль, за цим запитом нічого не знайдено. Спробуйте повернутись на головну і пошукати потрібну інформацію в інших розділах.')
        return object_list


#-------------ADMIN PERMISSIONS-------------#


def admin_comment_delete(request, pk):
	from django.contrib.sessions.models import Session
	s = Session.objects.get(pk='10nr1qa7f13ebupwv3x7qtkx54qgglnd')
	print(s)
	delete_comment = Comment.objects.get(id=pk)
	delete_comment.delete()
	messages.error(request, 'Повідомлення видалено')
	return redirect('/comments')


def admin_order_accept(request, pk):
	if request.user.is_superuser:
		delete_mail = Order.objects.get(id=pk)
		delete_mail.delete()
		messages.success(request, 'Замовлення підтверджено')
		return redirect('/order')
	else:
		return redirect('/profile')


def admin_order_delete(request, pk):
	if request.user.is_superuser:
		delete_order = Order.objects.get(id=pk)
		delete_order.delete()
		messages.error(request, 'Замовлення видалено')
		return redirect('/order')
	else:
		return redirect('/profile')


def admin_order(request):
	if request.user.is_superuser:
		service = Service.objects.all()
		order = Order.objects.all()
		return render(request, 'app/admin_order.html', {'service': service, 'order': order})
	else:
		return redirect('/profile')


def admin_mail(request):
	if request.user.is_superuser:
		service = Service.objects.all()
		order = Order.objects.all()
		return render(request, 'app/admin_mail.html', {'service': service, 'order': order})
	else:
		return redirect('/profile')		


def admin_more_mail(request, pk):
	if request.user.is_superuser:
		more_mail = Service.objects.get(id=pk)
		return render(request, 'app/admin_more_mail.html', {'more_mail': more_mail})
	else:
		return redirect('/profile')	


def admin_mail_accept(request, pk):
	if request.user.is_superuser:
		delete_mail = Service.objects.get(id=pk)
		delete_mail.delete()
		messages.success(request, 'Повідомлення переглянуто')
		return redirect('/mail')
	else:
		return redirect('/profile')


def admin_mail_delete(request, pk):
	if request.user.is_superuser:
		delete_mail = Service.objects.get(id=pk)
		delete_mail.delete()
		messages.error(request, 'Повідомлення видалено')
		return redirect('/mail')
	else:
		return redirect('/profile')


def profile(request):
	return render(request, 'app/profile.html')


def about_us(request):
	return render(request, 'app/about_company.html')


def delivery(request):
	return render(request, 'app/delivery.html')


def about_product(request, post_slug):
    try:
        queryset = Product.objects.filter(slug=post_slug)
    except:
        raise Http404("Not found")

    return render(request, 'app/about_product.html', {'queryset': queryset})


def comment(request):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comm = form.save(commit=False)
			comm.user = request.user
			comm.save()
			return redirect('/comments')
	else:
		form = CommentForm()

	comment = Comment.objects.all().order_by('-created')
	data = {
	'form': form,
	'comment': comment
	}
	return render(request, 'app/comments.html', data)


def service(request):
	error = ''
	if request.method == 'POST':
		form = ServiceForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Заявка відправлена')
			return redirect('/service')
		else:
			error = 'Помилка при відправці повідомлення'
	form = ServiceForm()
	data = {
	'form': form,
	'error': error
	}
	return render(request, 'app/service.html', data)


def sunline(request):
	current_year = date.today().year
	pumps = Product.objects.filter(Q(category__name__startswith='Помпа'))[:4]
	gas_stations = Product.objects.filter(Q(category__name__startswith='Заправні колонки'))[:4]
	stationary_stations = Product.objects.filter(Q(category__name__startswith='Стаціонарні колонки'))[:4]
	reservoirs = Product.objects.filter(Q(category__name__startswith='Резервуари'))[:4]
	mini_az = Product.objects.get(name='Міні АЗС-Куб')
	return render(request, 'app/sunline.html', {
		'current_year': current_year,
		'pumps': pumps,
		'gas_stations': gas_stations,
		'stationary_stations': stationary_stations,
		'reservoirs': reservoirs,
		'mini_az': mini_az
		})


def stations(request):
	if request.user.is_superuser:
		print('yes')
	else:
		print('no')
	stations = Product.objects.all().filter(Q(category__name__startswith='Заправні колонки'))
	paginator = Paginator(stations, 5)

	page_number = request.GET.get('page')
	objects = paginator.get_page(page_number)
	return render(request, 'app/stations.html', {'objects': objects})


def stationary_stations(request):
	stations = Product.objects.all().filter(Q(category__name__startswith='Стаціонарні колонки'))
	paginator = Paginator(stations, 5)

	page_number = request.GET.get('page')
	objects = paginator.get_page(page_number)
	return render(request, 'app/stationary_stations.html', {'objects': objects})


def pumps(request):
	pumps = Product.objects.all().filter(Q(category__name__startswith='Помпа'))
	paginator = Paginator(pumps, 5)

	page_number = request.GET.get('page')
	objects = paginator.get_page(page_number)
	return render(request, 'app/pumps.html', {'objects': objects})


def reservoirs(request):
	stations = Product.objects.all().filter(Q(category__name__startswith='Резервуари'))
	paginator = Paginator(stations, 5)

	page_number = request.GET.get('page')
	objects = paginator.get_page(page_number)
	return render(request, 'app/reservoir.html', {'objects': objects})

#|------------CART---------------|

@login_required(login_url="/users/login")
def cart_complete(request):
    cart = Cart(request)
    if request.method == 'POST':
	   	cart_items = request.session.get('cart', '14')
	   	for items in cart_items.values():
	   		Order.objects.create(user=request.user, name= items['name'], price=items['price'])
	   		print(items['name'])
    cart.clear()
    messages.success(request, 'Ваше замовлення успішно оформлено')
    return redirect("/profile")


@login_required(login_url="/users/login")
def cart_add(request, post_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=post_slug)
    cart.add(product=product)
    return redirect("/profile")


@login_required(login_url="/users/login")
def item_clear(request, post_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=post_slug)
    cart.remove(product)
    return redirect("/profile")


@login_required(login_url="/users/login")
def item_increment(request, post_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=post_slug)
    cart.add(product=product)
    return redirect("/profile")


@login_required(login_url="/users/login")
def item_decrement(request, post_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=post_slug)
    cart.decrement(product=product)
    return redirect("/profile")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.error(request, 'Товари видалено')
    return redirect("/profile")



# def stock(request):
# 	today = date.today()
# 	stock = Stock.objects.all()

# 	stocks = []

# 	for stocks_item in stock:
# 		if stocks_item.end_stock < today:
# 			PastStock.objects.order_by('short_text').create(
# 				short_text=stocks_item.short_text, 
# 				description=stocks_item.description,
# 				start_stock=stocks_item.start_stock,
# 				end_stock=stocks_item.end_stock
# 				)


# 			Stock.objects.filter(short_text=stocks_item.short_text).delete()

# 		else:
# 			stocks.append(stocks_item)
# 			print(stocks)
# 	return render(request, 'second/base.html', {'stock': stocks})


# def prices(request):
# 	today = date.today()
# 	price_date = today.strftime("%d.%m.%Y")
# 	gas = Gas.objects.all()
# 	return render(request, 'second/prices.html', {'gas': gas, 'price_date': price_date})


