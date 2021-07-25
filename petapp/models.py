from django.db import models

# Create your models here.


class PetLog(models.Model):
    policy = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    amount = models.IntegerField()
    duration = models.IntegerField()
    discount = models.IntegerField()
    original_price= models.IntegerField()
    discount_price = models.IntegerField()
    discount_Amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pet_log"

    def __unicode__(self):
        return self.policy
