from django.db import models

class VisitorLog(models.Model):
    ip_address  = models.GenericIPAddressField()
    page_visited = models.CharField(max_length=500)
    browser     = models.CharField(max_length=200, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} → {self.page_visited} at {self.timestamp}"
