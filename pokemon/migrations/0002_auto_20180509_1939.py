# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='game',
            field=models.ManyToManyField(to='pokemon.Game', blank=True),
        ),
        migrations.AlterField(
            model_name='evolution',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='generation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='move',
            name='accuracy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='move',
            name='etype',
            field=models.ManyToManyField(to='pokemon.Type', blank=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='power',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='move',
            name='pp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movepokemon',
            name='level',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='abilities',
            field=models.ManyToManyField(to='pokemon.Ability', blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='catch_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='descriptions',
            field=models.ManyToManyField(to='pokemon.Description', blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='egg_cycles',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='egg_group',
            field=models.ManyToManyField(to='pokemon.EggGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='exp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='happiness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='pkdx_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sp_atk',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sp_def',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites',
            field=models.ManyToManyField(to='pokemon.Sprite', blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(to='pokemon.Type', blank=True),
        ),
    ]
