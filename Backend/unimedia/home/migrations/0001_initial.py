# Generated by Django 4.2.7 on 2024-10-19 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='bba',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='bscincse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='bscineee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='bscinsoftware',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=255)),
                ('arrival', models.TimeField(blank=True, null=True)),
                ('departure', models.TimeField(blank=True, null=True)),
                ('number_of_Bus', models.IntegerField()),
                ('audience', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='', upload_to='media/Event/images')),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='media/Faculty_Members/')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=300)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coursecode', models.CharField(max_length=8, unique=True)),
                ('coursetitle', models.CharField(max_length=300, unique=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='email address')),
                ('image', models.ImageField(default='media/userimage/userimage.png', upload_to='media/userimage')),
                ('name', models.CharField(max_length=255)),
                ('phone_Number', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=300)),
                ('studentID', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('Bio', models.TextField()),
                ('batch', models.CharField(default='', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('departmentName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
