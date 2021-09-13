from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from invoice_payment.models import Invoice


class InvoiceModelValidation:
    CODE_DUPLICATE_MSG = _("Invoice code %(code)s  is not unique.")
    INVALID_UPDATE_ID_MSG = _("Invoice for id  %(id)s does not exists")

    @classmethod
    def validate_create(cls, user, **data):
        code = data.get('code', None)
        if not cls.__unique_display_name(code):
            raise ValidationError(cls.CODE_DUPLICATE_MSG % {'code': code})

    @classmethod
    def validate_update(cls, user, **data):
        id_ = data.get('id', None)

        existing = Invoice.objects.filter(id=id_).first()
        if not existing:
            raise ValidationError(cls.INVALID_UPDATE_ID_MSG % {'id': id_})

        code = data.get('code', existing.code)  # New or current
        duplicated = Invoice.objects.filter(code=code).exclude(id=id_).exists()

        if duplicated:
            raise ValidationError(cls.CODE_DUPLICATE_MSG % {'code': code})

    @classmethod
    def validate_delete(cls, user, **data):
        pass

    @classmethod
    def __unique_display_name(cls, code):
        return not Invoice.objects.filter(code=code).exists()
