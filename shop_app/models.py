from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    art = models.CharField(max_length=50,default='', db_index=True, verbose_name='Артикуль')
    material = models.CharField(max_length=200, blank=True, db_index=True, default='', verbose_name='Материал')
    color = models.CharField(max_length=50, db_index=True, blank=True,  default='',  verbose_name='Цвет')
    maker = models.CharField(max_length=200, db_index=True, blank=True, default='',  verbose_name='Изготовитель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_app:product_detail',
                        args=[self.id, self.slug])

class Bathroom_accessories(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    size = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Размер')

    class Meta:
        verbose_name = 'Аксессуар для ванной'
        verbose_name_plural = 'Аксессуары для ванной'

    def __str__(self):
        return self.product.name

    '''def get_absolute_url(self):
        return reverse('shop_app:product_list_by_category',
                        args=[self.product.slug])'''

class Bath(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    length = models.PositiveIntegerField(verbose_name='Длина, см', blank=True)
    width = models.PositiveIntegerField(verbose_name='Ширина, см', blank=True)
    depth = models.PositiveIntegerField(verbose_name='Глубина, см', blank=True)
    thickness = models.PositiveIntegerField(verbose_name='Толщина, мм', blank=True)
    completeness = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name='Комплектность')
    coating = models.BooleanField(default=True, blank=True,  verbose_name='Антискользящее покрытие')
    hydromassage = models.BooleanField(default=True, blank=True, verbose_name='Гидромассаж')
    form = models.CharField(max_length=200, db_index=True, blank=True, verbose_name='Форма')    

    class Meta:
        verbose_name = 'Ванна или поддон'
        verbose_name_plural = 'Ванны и поддоны'

    def __str__(self):
        return self.product.name


class Plumbing(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    size = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Размер')

    class Meta:
        verbose_name = 'Инженерная сантехника'
        verbose_name_plural = 'Инженерная сантехника'

    def __str__(self):
        return self.product.name


class Sink(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    length = models.PositiveIntegerField(blank=True, verbose_name='Длина, см')
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина, см')
    depth = models.PositiveIntegerField(blank=True, verbose_name='Глубина, см')
    number_of_bowls = models.PositiveIntegerField(blank=True, verbose_name='Количество чаш')
    mounting = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Способ монтажа')
    shredder = models.BooleanField(blank=True, default=True, verbose_name='Измельчитель отходов')
    form = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Форма')

    class Meta:
        verbose_name = 'Кухонная мойка'
        verbose_name_plural = 'Кухонные мойки'

    def __str__(self):
        return self.product.name


class Furniture(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    length = models.PositiveIntegerField(blank=True, verbose_name='Длина, см')
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина, см')
    depth = models.PositiveIntegerField(blank=True, verbose_name='Глубина, см')
    shell_material = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Материал раковины')
    facade_material = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Материал фасада')
    mounting = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Способ монтажа')
    backlight = models.BooleanField(blank=True, default=True, verbose_name='Подсветка')

    class Meta:
        verbose_name = 'Мебель для ванной'
        verbose_name_plural = 'Мебель для ванной'

    def __str__(self):
        return self.product.name


class Sanfayance(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    length = models.PositiveIntegerField(blank=True, verbose_name='Длина, см')
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина, см')
    depth = models.PositiveIntegerField(blank=True, verbose_name='Глубина, см')
    drain_mode = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Режим слива воды')
    mounting = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Способ монтажа')
    form = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Форма')

    class Meta:
        verbose_name = 'Санфаянс'
        verbose_name_plural = 'Санфаянс'

    def __str__(self):
        return self.product.name


class Faucet(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    mounting = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Способ монтажа')
    management = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Управление')
    size = models.CharField(blank=True, max_length=50, db_index=True, verbose_name='Размер')
    spout = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Излив')    
    appointment = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Назначение')

    class Meta:
        verbose_name = 'Смеситель или система для душа'
        verbose_name_plural = 'Смесители и системы для душа'

    def __str__(self):
        return self.product.name


class Towel_rail(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE, primary_key = True, verbose_name='Продукт')
    length = models.PositiveIntegerField(blank=True, verbose_name='Длина, см')
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина, см')
    connection = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Вид подключения')
    type = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Тип')
    form = models.CharField(blank=True, max_length=200, db_index=True, verbose_name='Форма')

    class Meta:
        verbose_name = 'Полотенцесушитель'
        verbose_name_plural = 'Полотенцесушители'

    def __str__(self):
        return self.product.name

