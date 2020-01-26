import os.path
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from django_sftpbrowser.sftp import get_sftp_connection

srv = get_sftp_connection()


def download_sftp_file(current_sftp_path):
    """
    It sends the bytes from the file to the user as a Django HttpResponse.
    The user just experiment a normal file download.

    :param current_sftp_path: the path to the sftp file
    :return: the HttpResponse download object for the file
    """
    in_memory_file = BytesIO()
    srv.getfo(current_sftp_path, in_memory_file)
    in_memory_file.seek(0)
    # print(in_memory_file.tell())
    response = HttpResponse(in_memory_file.read(), content_type="application/force-download")
    response['Content-Disposition'] = f'attachment;filename={os.path.basename(current_sftp_path)}'
    return response


def paramiko_is_folder(paramiko):
    """
    Checks if the SFTP entry for this paramiko object is a folder or a regular file

    :param paramiko: the paramiko object from pysftp with info from the directory entry
    :return: True if the entry corresponds to a folder, False otherwise
    """
    return paramiko.longname.startswith('d')


class Entry():
    """
    This class represents a single line or entry inside a directory shown on the web
    """
    def __init__(self, fname, is_folder, abs_path):
        self.name = fname
        self.ftype = is_folder
        self.path = abs_path


def paramiko_to_entry(paramiko, input_path):
    """
    This takes info from paramiko objects and creates the proper Entry instance that
    represents the corresponding entry from the SFTP

    :param paramiko: from pysftp with info from the directory entry
    :param input_path: the suffix for the path after the /browse/ token
    :return: an Entry instance object to be shown on the web
    """
    is_folder = paramiko_is_folder(paramiko)
    if is_folder:
        ftype = 'folder'
    else:
        ftype = 'file'

    abs_path = '/'.join((settings.SERVER_URL, 'browse'))
    if input_path.strip():
        abs_path = '/'.join((abs_path, input_path))

    abs_path = '/'.join((abs_path, paramiko.filename))

    return Entry(paramiko.filename, ftype, abs_path)


# Create your views here.
def browse_page(request, input_path=''):
    """
    Takes as input a path suffix for both SFTP and web server
    and returns or downloads accordingly the contents of the clicked resource

    :param request: the input HttpRequest
    :param input_path: the suffix for the path after the /browse/ token
    :return: if the clicked link is a file, it downloads it, otherwise, it sends the
            response with the contents of the clicked folder
    """
    current_sftp_path = settings.SFTP_ROOT
    entries = []
    browser_current_path = '/'.join((settings.SERVER_URL, 'browse'))  # HERE. I get the SERVER_URL from settings, but...
                                                                      # maybe I could do the same from request
    browser_current_parent_folder = ''

    if len(input_path.strip()):
        current_sftp_path = '/'.join((current_sftp_path, input_path))
        browser_current_path = '/'.join((browser_current_path, input_path))
        browser_current_parent_folder = os.path.dirname(browser_current_path)

    if srv.isfile(current_sftp_path):
        return download_sftp_file(current_sftp_path)

    # We show the content of the folder
    paramiko_list = srv.listdir_attr(current_sftp_path)
    entries.extend([paramiko_to_entry(paramiko, input_path) for paramiko in paramiko_list])

    return render(request,
                  'browse.html',
                  {
                      'parent_folder': browser_current_parent_folder,
                      'input_path': input_path,
                      'entries': entries,
                  })
