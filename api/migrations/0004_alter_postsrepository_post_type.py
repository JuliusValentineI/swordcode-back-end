# Generated by Django 5.0.1 on 2024-01-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_postsrepository_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsrepository',
            name='post_type',
            field=models.CharField(choices=[('javascript', 'Javascript Vanila'), ('typescript', 'Typescript Vanila'), ('python', 'Python Vanila'), ('next_js', 'Next Js'), ('react', 'react'), ('react_movile', 'React Mobile'), ('django', 'Django'), ('flask', 'Flask'), ('ninja', 'Ninja'), (None, None), ('test', 'Pruebas de testeo')], default=None, max_length=50),
        ),
    ]
