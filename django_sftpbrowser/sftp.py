from base64 import decodebytes
import paramiko
import pysftp
from django.conf import settings

key = paramiko.RSAKey(data=decodebytes(settings.HOST_KEY))
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add(settings.CORELLI_SFTP_SERVER_URL, 'ssh-rsa', key)


def get_sftp_connection():
    return pysftp.Connection(settings.CORELLI_SFTP_SERVER_URL, username='madtyn',
                             password=settings.SFTP_PASSWORD,
                             cnopts=cnopts)
