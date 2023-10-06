# Generated by Django 4.2.3 on 2023-10-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Содержимое")),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="slug"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="article_previews/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "view_count",
                    models.PositiveBigIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]
