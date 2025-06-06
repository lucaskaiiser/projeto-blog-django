from django.db import models

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Site'
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    favicon = models.ImageField(
        upload_to='assets/',
        blank=True,
        default=''
    )

    def __str__(self):
        return self.title
        