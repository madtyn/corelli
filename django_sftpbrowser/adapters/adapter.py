import logging
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from allauth.account.adapter import DefaultAccountAdapter

logger = logging.getLogger(__name__)


class DjangoSftpAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(
            request,
            emailconfirmation)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'

        logger.info('Sending confirmation mail to %s', settings.ADMIN_EMAIL_ADDRESS)
        self.send_mail(email_template,
                       settings.ADMIN_EMAIL_ADDRESS,
                       ctx)

    def confirm_email(self, request, email_address):
        """
        Marks the email address as confirmed on the db
        """
        email_address.verified = True
        email_address.set_as_primary(conditional=True)
        email_address.save()
        logger.info('Sending account created confirmation mail to %s', email_address.email)
        self.send_mail('account/email/account_activated',
                       email_address.email,
                       {'email': email_address.email})
