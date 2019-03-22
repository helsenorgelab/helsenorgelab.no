# Generated by Django 2.0.9 on 2019-03-22 20:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('wagtailcore', '0040_page_draft_title'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.", max_length=255)),
                ('introduction', models.TextField(blank=True)),
                ('listing_image', models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'verbose_name': 'Pages index',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='InformationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.", max_length=255)),
                ('introduction', models.TextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title', template='patterns/molecules/streamfield/blocks/heading_block.html')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(classname='title')), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('citation_link', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('document', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False))]))])),
                ('image_caption', models.CharField(blank=True, max_length=250)),
                ('biography', models.CharField(blank=True, help_text="Use this field to override the author's biography on this page.", max_length=255)),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('listing_image', models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'verbose_name': 'Standard Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='InformationPageAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('biography', models.CharField(blank=True, help_text="Use this field to override the author's biography on this information page.", max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.PersonPage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='standardpages.InformationPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InformationPageRelatedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('source_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pages', to='standardpages.InformationPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
