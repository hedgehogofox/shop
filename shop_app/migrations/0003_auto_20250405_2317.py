# Generated by Django 3.2 on 2025-04-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20250405_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bath',
            name='coating',
            field=models.BooleanField(blank=True, default=True, verbose_name='Антискользящее покрытие'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='completeness',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Комплектность'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='depth',
            field=models.PositiveIntegerField(blank=True, verbose_name='Глубина, см'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='form',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='hydromassage',
            field=models.BooleanField(blank=True, default=True, verbose_name='Гидромассаж'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина, см'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='thickness',
            field=models.PositiveIntegerField(blank=True, verbose_name='Толщина, мм'),
        ),
        migrations.AlterField(
            model_name='bath',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина, см'),
        ),
        migrations.AlterField(
            model_name='bathroom_accessories',
            name='size',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='appointment',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Назначение'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='management',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Управление'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='mounting',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Способ монтажа'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='size',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='spout',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Излив'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='backlight',
            field=models.BooleanField(blank=True, default=True, verbose_name='Подсветка'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='depth',
            field=models.PositiveIntegerField(blank=True, verbose_name='Глубина, см'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='facade_material',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Материал фасада'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина, см'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='mounting',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Способ монтажа'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='shell_material',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Материал раковины'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина, см'),
        ),
        migrations.AlterField(
            model_name='plumbing',
            name='size',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, db_index=True, default='', max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='maker',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200, verbose_name='Изготовитель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='depth',
            field=models.PositiveIntegerField(blank=True, verbose_name='Глубина, см'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='drain_mode',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Режим слива воды'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='form',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина, см'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='mounting',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Способ монтажа'),
        ),
        migrations.AlterField(
            model_name='sanfayance',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина, см'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='depth',
            field=models.PositiveIntegerField(blank=True, verbose_name='Глубина, см'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='form',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина, см'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='mounting',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Способ монтажа'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='number_of_bowls',
            field=models.PositiveIntegerField(blank=True, verbose_name='Количество чаш'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='shredder',
            field=models.BooleanField(blank=True, default=True, verbose_name='Измельчитель отходов'),
        ),
        migrations.AlterField(
            model_name='sink',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина, см'),
        ),
        migrations.AlterField(
            model_name='towel_rail',
            name='connection',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Вид подключения'),
        ),
        migrations.AlterField(
            model_name='towel_rail',
            name='form',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='towel_rail',
            name='length',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина, см'),
        ),
        migrations.AlterField(
            model_name='towel_rail',
            name='type',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='towel_rail',
            name='width',
            field=models.PositiveIntegerField(blank=True, verbose_name='Ширина, см'),
        ),
    ]
