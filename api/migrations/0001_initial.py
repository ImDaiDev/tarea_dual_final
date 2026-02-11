from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=200)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
