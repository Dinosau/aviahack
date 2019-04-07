from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User

from ahck.mixin import TimestampMixin

from bitfield import BitField


# class Mock(models.Model):
#     pass
class Flight(TimestampMixin):
    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"
    
    number = models.CharField(max_length=255)
    description = models.TextField()


class ServiceClass(TimestampMixin):
    description = models.CharField(max_length=255)
    fligth = models.ForeignKey(Flight, related_name='servise_classes', on_delete=models.PROTECT)


class Cargo(TimestampMixin):
    plomb_id = models.CharField(max_length=255, default='', unique=True)
    barcode = models.CharField(max_length=255, default='', unique=True)
    serviceclass = models.ForeignKey(
        ServiceClass, related_name='cargos',on_delete=models.PROTECT)


class Packet(TimestampMixin):
    class Meta:
        verbose_name = "индивидуальный комплект"
        verbose_name_plural = "индивидуальные комплекты"
    barcode = models.CharField(max_length=255, default='', unique=True)
    description_in_json = models.TextField("json packet description", default="{}")
    cargo = models.ForeignKey(Cargo, related_name='packets', on_delete=models.PROTECT)


class SystemUser(User):
    flags = BitField(flags=(
        ('board_conductor', '0'),
        ('deliveryman', '1')
    ))
