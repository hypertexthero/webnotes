from django.db import models
from django.db.models import permalink
 
class Notes(models.Model):
    """Model to save our note"""
    title   = models.CharField(max_length=255)
    content = models.TextField()
    #automatically add timestamps when object is created 
    added_at = models.DateTimeField(auto_now_add=True) 
    #automatically add timestamps when object is updated
    last_update = models.DateTimeField(auto_now=True) #

    # display correct plural name in admin
    class Meta:
        verbose_name_plural = "notes"

    # display note title in admin
    def __unicode__(self):
        return self.title
    
    # define permalink (not needed?)
    # @permalink
    # def get_absolute_url(self):
    #     # return ('collection_detail', None, {'object_id': self.id})
    #     return ("note_permalink", (), {'id': self.id})