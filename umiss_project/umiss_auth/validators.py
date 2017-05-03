from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from umiss_auth.models import CustomUser
import hashlib


def validate_token(token):
    patients = CustomUser.objects.filter(user_type='patient')
    patient_tokens = [user.token for user in patients]
    hash_token = hashlib.sha512(
        self.token.encode('utf-8')
    ).hexdigest()

    if hash_token not in patient_tokens:
        raise ValidationError(
            _("The monitor must have a token from a patient." +
              " The token %(token) is wrong"),
            params={'token': token},

        )
