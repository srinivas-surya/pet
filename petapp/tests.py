from django.test import TestCase
from .models import PetLog
from django.utils import timezone

# models test


class PetLogTest(TestCase):
    ''' writing test case for model '''
    def create_pet_log(self):
        policy = "Annual"
        species = "Cat"
        age = "0-5"
        variety = "cat1"
        amount = 1000
        duration = 12
        discount = 100
        original_price = 12000
        discount_price = 10800
        discount_Amount = 1200
        ''' creating model object using custom data'''
        return PetLog.objects.create(policy=policy, species=species,age=age,variety=variety,
                                     amount=amount, duration=duration, discount=discount,
                                     original_price=original_price, discount_price=discount_price,
                                     discount_Amount=discount_Amount,created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_pet_log()
        self.assertTrue(isinstance(w, PetLog))
        ''' test the model object whatever we created earlier'''
        self.assertEqual(w.__unicode__(), w.policy)

