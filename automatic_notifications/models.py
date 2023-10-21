from django.db import models

# Create your models here.

class mail_info(models.Model):
    user_id = models.CharField(null=False,unique=True,max_length=40,verbose_name='user_id')
    subject = models.CharField(null=False,max_length=40,verbose_name='subject')
    message = models.CharField(null=False,max_length=40,verbose_name='message')

    def __str__(self):
        return self.user_id
    
    class Meta:
        db_table = 'mail_info'
        verbose_name = 'Mail_Info'
        verbose_name_plural = "mails_info"
        ordering = ['id']