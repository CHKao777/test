from django.db import models

# Create your models here.
class FeedBack(models.Model):
    citing_context = models.TextField()
    cited_context = models.TextField()
    citation_text = models.TextField()
    citation_text_quality = models.IntegerField()
    citation_intent_quality = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)