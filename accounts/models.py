from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to="profile_picture/", blank=True, verbose_name="Profile Picture (Optional) ",
            default='profile_picture/no-pic-uploaded.png')
    phone_number = models.IntegerField(default=0, blank=True, verbose_name="Phone Number (Optional) ")
    website_url = models.URLField(max_length=200, blank=True, verbose_name="Website URL (Optional) ")
    address_country = models.CharField(max_length=50, verbose_name="Country Name ")
    address_state = models.CharField(max_length=50, verbose_name="State / Province Name ")
    address_city = models.CharField(max_length=50, verbose_name="City Name ")
    address_zip = models.CharField(max_length=5, blank=True, verbose_name="ZIP Code (Optional) ")
    address_street = models.CharField(max_length=50, verbose_name="Street Name / Number (Optional) ")
    address_postal = models.CharField(max_length=5, blank=True, verbose_name="Postal Address (Optional) ")

    def __str__(self):
        return u'%s' % (self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

# upload videos
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users_videos/{0}/{1}/'.format(instance.user.username, filename)

class UploadVideo(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s' % (self.user)
