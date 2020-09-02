from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
        login serializer
    """
    email = serializers.EmailField(
        allow_blank=False,
        allow_null=False,
        error_messages={'required': 'Please enter a valid e-mail id.',
                        'invalid': 'Please enter a valid e-mail id.',
                        'blank': 'Please enter a valid e-mail id.',
                        'null': 'Please enter a valid e-mail id.'}
    )
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
                attrs['user'] = user
                return attrs
            else:
                msg = _('Incorrect Email/Password.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise serializers.ValidationError(msg)
