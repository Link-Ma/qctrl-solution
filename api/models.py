from django.db import models


# Control model.
class Control(models.Model):
    name = models.CharField('name', max_length=100, default='no_name')
    type = models.CharField('type', max_length=50, default='Primitive')  # Primitive, CORPSE, Gaussian, CinBB and CinSK
    maximum_rabi_rate = models.FloatField()
    polar_angle = models.FloatField()

    def __unicode__(self):
        return '%d: %s' % (self.name, self.type)
