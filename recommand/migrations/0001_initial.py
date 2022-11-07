# Generated by Django 4.1 on 2022-11-07 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movie_id", models.IntegerField(primary_key=True, serialize=False)),
                ("movie_name", models.CharField(max_length=200)),
                ("year", models.IntegerField()),
                ("movie_dir", models.CharField(max_length=100)),
                ("movie_act", models.CharField(max_length=200)),
                ("movie_ger", models.CharField(max_length=200)),
                ("movie_text", models.TextField(null=True)),
                ("movie_poster", models.ImageField(null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Ost",
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
                ("ost_name", models.CharField(max_length=200)),
                ("valence", models.FloatField(blank=True, null=True)),
                ("acousticness", models.FloatField(blank=True, null=True)),
                ("danceability", models.FloatField(blank=True, null=True)),
                ("energy", models.FloatField(blank=True, null=True)),
                ("loudness", models.FloatField(blank=True, null=True)),
                ("tempo", models.FloatField(blank=True, null=True)),
                ("cluster", models.IntegerField(blank=True, null=True)),
                (
                    "movie_id",
                    models.ForeignKey(
                        db_column="movie_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post",
                        to="recommand.movie",
                    ),
                ),
            ],
        ),
    ]
