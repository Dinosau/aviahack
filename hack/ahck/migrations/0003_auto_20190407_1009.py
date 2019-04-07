# Generated by Django 2.2 on 2019-04-07 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahck', '0002_auto_20190407_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('дата создания', models.DateTimeField(auto_now_add=True)),
                ('дата изменения', models.DateTimeField(auto_now=True)),
                ('delivery_officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mocks_deliveried', to='ahck.SystemUser')),
                ('inspection_officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mocks_inspected', to='ahck.SystemUser')),
                ('receiving_officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mocks_recived', to='ahck.SystemUser')),
            ],
            options={
                'verbose_name': 'доставка',
                'verbose_name_plural': 'доставки',
            },
        ),
        migrations.CreateModel(
            name='ActOfShortage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('дата создания', models.DateTimeField(auto_now_add=True)),
                ('дата изменения', models.DateTimeField(auto_now=True)),
                ('descriprion_in_json', models.TextField(default='{}', verbose_name='json act of shortage description')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ahck.Mock')),
            ],
            options={
                'verbose_name': 'акт о не достаче',
                'verbose_name_plural': 'акты о недостаче',
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='mock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fligths', to='ahck.Mock'),
        ),
    ]