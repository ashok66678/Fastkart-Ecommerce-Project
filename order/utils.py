import random
import string
from datetime import date

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_transaction_id_generator(instance):
    Klass = instance.__class__
    try:
        transaction_id = str(date.today()).replace('-','') + str('-') + str(int(Klass.objects.all().last().id) + 1)
    except:
        transaction_id = str(date.today()).replace('-','') + str('-') + "1"
    qs_exists = Klass.objects.filter(transaction_id=transaction_id).exists()
    if qs_exists:  ## if transaction_id already exists 
        transaction_id = "{transaction_id}-{randstr}".format(
                    transaction_id=transaction_id,
                    randstr=random_string_generator(size=4)
                )
        return unique_transaction_id_generator(instance, transaction_id=transaction_id)
    return transaction_id