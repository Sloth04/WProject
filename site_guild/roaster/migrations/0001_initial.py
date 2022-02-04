# Generated by Django 3.2.12 on 2022-02-04 00:49

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuildRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('tier', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='class_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='class_specialization_logo/')),
                ('player_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roaster.role')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('join_date', models.DateTimeField(null=True, verbose_name='join_date')),
                ('approved', models.BooleanField(default=True)),
                ('player_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roaster.role')),
                ('rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roaster.guildrank')),
                ('specs', smart_selects.db_fields.GroupedForeignKey(group_field='player_class', null=True, on_delete=django.db.models.deletion.CASCADE, to='roaster.specialization')),
            ],
        ),
    ]
