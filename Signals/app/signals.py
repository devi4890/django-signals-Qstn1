#app/signals.py

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal received at: {now()}")
    # Simulate a delay to prove synchronous behavior
    time.sleep(5)
    print(f"Finished processing signal at: {now()}")
