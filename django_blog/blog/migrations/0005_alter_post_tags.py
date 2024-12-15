from django.db import migrations
import taggit.managers

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_alter_comment_post_post_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        # Remove the existing 'tags' field
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        
        # Re-add the 'tags' field using the correct TaggableManager
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'
            ),
        ),
    ]
