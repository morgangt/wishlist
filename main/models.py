from django.db import models


class Product(models.Model):
    """ Таблица "Товар"

    id
    Название товара
    Ссылка на товар
    Цена товара
    Дата и время создания записи
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
