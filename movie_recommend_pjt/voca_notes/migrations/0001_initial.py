from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('word_mean', models.TextField()),
                ('examples', models.TextField()),
                ('memo', models.TextField()),
                ('is_memorized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VocaNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=True)),
                ('movies', models.ManyToManyField(related_name='voca_notes', to='movies.movie')),
                ('users', models.ManyToManyField(related_name='voca_notes', to=settings.AUTH_USER_MODEL)),
                ('vocas', models.ManyToManyField(related_name='voca_notes', to='voca_notes.voca')),
            ],
        ),
    ]
