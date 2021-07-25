from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import PetLog
# Create your views here.


@csrf_exempt
def home(request):
    if request.method == "POST":
        policy = request.POST['policy']
        species = request.POST['species']
        age = request.POST['age']
        amount_ = request.POST['amount']
        amount = int(amount_)
        variety = request.POST['variety']

        '''checking policy type based on user input'''
        if policy == "Annual":
            if amount <= 1000:

                ''' based on amount calculating the original and discount price for annual policy'''
                discount = 10
                original_price = int(amount) * 12
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price
                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=12,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 12,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }

                '''generate and rendering data to the front end'''
                return render(request, "petapp/result.html", context)

            elif amount > 1000 and amount <=2000 :

                discount = 5
                original_price = int(amount) * 12
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price

                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=12,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 12,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }
                return render(request, "petapp/result.html", context)

        elif policy == "Lifetime":
            if amount <= 1000:
                '''based on amount calculating the original and discount price for annual policy
                '''
                discount = 20
                original_price = int(amount) * 60
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price

                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=60,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 60,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }
                '''generate and rendering data to the front end'''
                return render(request, "petapp/result.html", context)

            elif amount > 1000 and amount <=2000 :

                discount = 15
                original_price = int(amount) * 60
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price

                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=60,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 60,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }
                return render(request, "petapp/result.html", context)

        elif policy == "Pre Existing":
            if amount <= 1000:
                '''
                    based on amount calculating the original and 
                    discount price for annual policy
                '''
                discount = 15
                original_price = int(amount) * 12
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price

                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=12,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 12,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }
                '''generate and rendering data to the front end'''
                return render(request, "petapp/result.html", context)

            elif amount > 1000 and amount <=2000 :

                discount = 15
                original_price = int(amount) * 12
                discounted_price = original_price - (original_price * discount / 100)
                discount_amount = original_price-discounted_price

                ''' writing log to the database'''
                pet_log_data = PetLog.objects.create(policy=policy,
                                                     species=species,
                                                     age=age,
                                                     variety=variety,
                                                     amount=amount,
                                                     duration=12,
                                                     discount=discount,
                                                     original_price=original_price,
                                                     discount_price=discounted_price,
                                                     discount_Amount=discount_amount)
                pet_log_data.save()
                print("log data saved")

                context = {
                    "policy": policy,
                    "species": species,
                    "Age": age,
                    "variety": variety,
                    "price": amount,
                    "duration": 12,
                    "discount": discount,
                    "original_price": original_price,
                    "Discount_price": discounted_price,
                    "Discount_Amount": discount_amount,

                }
                return render(request, "petapp/result.html", context)

    else:
        return render(request, "petapp/home.html")