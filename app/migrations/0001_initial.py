# Generated by Django 2.2 on 2020-12-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_name', models.CharField(max_length=100)),
                ('log_dev', models.CharField(max_length=100)),
                ('log_area', models.CharField(max_length=100)),
                ('log_srcip', models.CharField(max_length=100)),
                ('log_dstip', models.CharField(max_length=100)),
                ('log_payload', models.CharField(max_length=3000)),
                ('log_time', models.DateTimeField(auto_now=True)),
                ('log_fenxi', models.CharField(max_length=3000)),
                ('log_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AppDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=100)),
                ('dev_ip', models.CharField(max_length=100, unique=True)),
                ('dev_user', models.CharField(max_length=100)),
                ('dev_password', models.CharField(max_length=100)),
                ('dev_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='attlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_name', models.CharField(max_length=100)),
                ('log_dev', models.CharField(max_length=100)),
                ('log_area', models.CharField(max_length=100)),
                ('log_srcip', models.CharField(max_length=100)),
                ('log_dstip', models.CharField(max_length=100)),
                ('log_payload', models.CharField(max_length=3000)),
                ('log_time', models.DateTimeField(auto_now=True)),
                ('log_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Code_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='dev_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_type', models.CharField(max_length=100, unique=True)),
                ('d_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='devgroup_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devgroup_name', models.CharField(max_length=100, unique=True)),
                ('devgroup_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fdjl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_ip', models.CharField(max_length=100)),
                ('log_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mgt_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_sb', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='devgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_time', models.DateTimeField(auto_now=True)),
                ('dev_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AppDevice', to_field='dev_ip')),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.devgroup_name', to_field='devgroup_name')),
            ],
        ),
        migrations.AddField(
            model_name='appdevice',
            name='dev_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Code_name', to_field='name'),
        ),
        migrations.AddField(
            model_name='appdevice',
            name='dev_mgt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mgt_type', to_field='type_sb'),
        ),
        migrations.AddField(
            model_name='appdevice',
            name='dev_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dev_type', to_field='d_type'),
        ),
    ]
