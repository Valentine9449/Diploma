from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from datetime import datetime, date, time
from django.utils import timezone

class Gas(models.Model):
	gas_name = models.CharField(max_length=100)
	gas_type = models.CharField(max_length=50, default='')
	gas_price = models.FloatField(validators=[
						MinValueValidator(0),
                        MaxValueValidator(50)]
    )


	class Meta:
		ordering = ("gas_price", 'gas_type')
		verbose_name = 'Паливо'
		verbose_name_plural = 'Паливо'

	def __str__(self):
		return f'{self.gas_name} - {self.gas_price}'


class Stock(models.Model):
	short_text = models.CharField(max_length=120)
	description = models.CharField(max_length=700)
	start_stock = models.DateField()
	end_stock = models.DateField()

	class Meta:
		ordering = ('short_text', 'start_stock')
		verbose_name = 'Акція'
		verbose_name_plural = 'Акції'

	def __str__(self):
		return f'{self.short_text} - {self.start_stock}'



class PastStock(models.Model):
	short_text = models.CharField(max_length=120)
	description = models.CharField(max_length=700)
	start_stock = models.DateField()
	end_stock = models.DateField()

	class Meta:
		ordering = ('short_text', 'start_stock')
		verbose_name = 'Минула акція'
		verbose_name_plural = 'Минулі акції'

	def __str__(self):
		return f'{self.short_text} - {self.start_stock}'


class Category(models.Model):
	name = models.CharField(max_length=64, verbose_name='категория', default='SOME STRING')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


	class Meta:
		ordering = ('name',)
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'


	def __str__(self):
		return self.name



class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='предмет', default='One')
	full_name = models.CharField(max_length=300, verbose_name='довга назва', default='-')
	name = models.CharField(max_length=200, verbose_name='назва')
	price = models.FloatField(default=0)
	country = models.CharField(max_length=50, default='')
	image = models.ImageField(null=True, blank=True, upload_to="profile_image")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	description = models.TextField(verbose_name='Характерстика', default='-')

	@property
	def photo_url(self):
		if self.image  and hasattr(self.image , 'url'):
			return self.image .url

	class Meta:
		ordering = ('name', 'category')
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предмети'


	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('fresult', kwargs={'post_slug': self.slug})




class Service(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=100)
	full_text = models.TextField('Повідомлення')
	number = models.CharField(max_length=30)
	service_choise = (
		('Ремонт лічильників рідини', 'Ремонт лічильників рідини'),
		('Ремонт паливних колонок', 'Ремонт паливних колонок'),
		('Обслуговування паливних резервуарів', 'Обслуговування паливних резервуарів')
		)
	services = models.CharField(max_length=100, blank=True, null=True, choices=service_choise)
	created = models.DateTimeField("Додано", default=datetime.now())


	def __str__(self):
		return f' {self.first_name} - {self.full_text}'


	class Meta:
		ordering = ('first_name', 'created')
		verbose_name = 'Повідомлення'
		verbose_name_plural = 'Повідомлення'



class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	comment_text = models.TextField('', max_length=500)
	created = models.DateTimeField("Добавлен",blank=True, null=True, default=datetime.now())

	class Meta:
		ordering = ('user' ,'created')
		verbose_name = 'Коментарій'
		verbose_name_plural = 'Коментарії'


	def __str__(self):
		return f'{self.user} - {self.created}'



class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=200, verbose_name='назва')
	price = models.FloatField(default=0)
	created = models.DateTimeField("Додано", default=timezone.now)


	class Meta:
		ordering = ('user' ,'created')
		verbose_name = 'Замовлення'
		verbose_name_plural = 'Замовлення'


	def __str__(self):
		return f'{self.user} - {self.created}'