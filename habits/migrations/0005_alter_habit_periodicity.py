# Generated by Django 5.1 on 2024-08-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_alter_habit_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("daily", "Ежедневно"),
                    ("in a day", "Через день"),
                    ("in a two days", "Раз в три дня"),
                    ("weekly", "Раз в неделю"),
                ],
                default="daily",
                help_text="Как часто выполнять?",
                max_length=50,
                verbose_name="Периодичность",
            ),
        ),
    ]