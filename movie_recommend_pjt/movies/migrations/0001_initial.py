
# Generated by Django 4.2.16 on 2024-11-22 14:20


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('profile_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ott',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('logo_path', models.TextField()),
                ('site_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('name_kr', models.TextField()),
                ('profile_path', models.TextField(blank=True, null=True)),
                ('characters', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField()),
                ('title', models.TextField()),
                ('title_kr', models.TextField()),
                ('rank', models.FloatField()),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('summary', models.TextField()),
                ('production', models.TextField()),
                ('country', models.TextField()),
                ('poster_path', models.TextField()),
                ('is_adult', models.BooleanField()),
                ('difficulty', models.TextField()),
                ('directors', models.ManyToManyField(related_name='directed_movies', to='movies.director')),
                ('genres', models.ManyToManyField(related_name='included_movies', to='movies.genre')),
                ('otts', models.ManyToManyField(related_name='provide_movies', to='movies.ott')),
                ('stars', models.ManyToManyField(related_name='stared_movie', to='movies.star')),
                ('wish_users', models.ManyToManyField(related_name='wish_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('liked_users', models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(related_name='comments', to='movies.movie')),
                ('users', models.ManyToManyField(related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
