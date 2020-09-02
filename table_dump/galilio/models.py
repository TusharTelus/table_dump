from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime
class GenderType(object):
    MALE = 1
    FEMALE = 2
# Create your models here.

class RollType(object):
    Admin = 1
    User = 2

class Mapping_Record(models.Model):
    mapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    folder_name = models.IntegerField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    schema_json = models.JSONField(max_length=600)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    now = datetime.now()
    if created:
        Token.objects.create(user=instance)


class Roll(models.Model):
    role_id = models.CharField(max_length=36, blank=True, null=True)
    role_name = models.CharField(max_length=255, blank=True, null=True)

class Permission(models.Model):
    permission_id = models.CharField(max_length=36, blank=True, null=True)
    permission_name = models.CharField(max_length=255, blank=True, null=True)
    permission_type = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.ForeignKey(Roll,on_delete=models.PROTECT)


class Upload_Record(models.Model):
    file_id = models.CharField(max_length=36, blank=True, null=True)
    row_count = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.CharField(max_length=255, blank=True, null=True)
    uploaded_by = models.CharField(max_length=255, blank=True, null=True)
    mapping_id = models.ForeignKey(Mapping_Record,on_delete=models.PROTECT)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.CharField(max_length=255, blank=True, null=True)
    deleted_by = models.CharField(max_length=255, blank=True, null=True)

class users(models.Model):
    GENDER_CHOICES = (
        (None, 'Select The Gender Choices'),
        (GenderType.MALE, 'Male'),
        (GenderType.FEMALE, 'Female')
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    users_id = models.ForeignKey(Roll, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.CharField(max_length=40, default='timestamprequired')
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True
    )
    email = models.EmailField(
        _('email address'), max_length=255, unique=True, null=True
    )
    enabled = models.IntegerField()

    last_login = models.CharField(max_length=40, default='timestamprequired')
    phone = models.CharField(
        max_length=16,
        unique=True,
        help_text="The mobile number to deliver tokens to."
    )
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.CharField(max_length=40, default='timestamprequired')
    username = models.CharField(max_length=40, default='timestamprequired')

