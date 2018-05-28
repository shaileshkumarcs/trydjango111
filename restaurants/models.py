from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.
from django.core.urlresolvers import reverse



from .utils import unique_slug_generator
from .validators import validation_category, validation_location

User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
    owner       = models.ForeignKey(User) #class_nstance.model_set.all() # Django Model Unleashed JOINCFE.com
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True, validators=[validation_location])
    category    = models.CharField(max_length=120, null=True, blank=True , validators=[validation_category])
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" #this is for hard code url pattern
        return reverse("restaurants:detail", kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # print('saving...')
    # print(instance.timestamp)
    instance.category = instance.category.capitalize()
    if not instance.slug:
        # instance.name = "Another new title"
        instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender, instance, *args, **kwargs):
#     print("saved")
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)

