from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)  # Ensure unique usernames
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        return Profile.objects.get(user=self)  # Added return statement

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timetable_events')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.event_name} on {self.start_time.date()} by {self.user.username}" 

    def clean(self):
        """ Validate that the event does not overlap with existing events. """
        overlapping_events = Timetable.objects.filter(
            user=self.user
        ).exclude(id=self.id).filter(
            models.Q(start_time__lt=self.end_time, end_time__gt=self.start_time)
        )

        if overlapping_events.exists():
            raise ValidationError("This time slot overlaps with an existing event.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)