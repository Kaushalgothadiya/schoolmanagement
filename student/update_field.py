# from typing import Any
# from .models import Items
# from django.core.management.base import BaseCommand


# class Command(BaseCommand):
#     help='Update price including tax for Items'

#     def handle(self, *args: Any, **options: Any) -> str | None:
#         obj=Items.objects.filter(update_price_including_tax__isnull=True)
        
#         for item in obj:
#             item.price_including_tax=item.price*item.price
#             item.save()
#         self.stdout.write(self.style.SUCCESS('price updating successfully..'))


