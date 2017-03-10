#!/usr/bin/python3
import urllib.request
import smtplib

url='http://SITE_NAME.HERE'
trustURL = ('http://www.ya.ru', 'http://www.google.com', 'http://www.mail.ru')


def send_email(url):
    """
    Send email function
    """
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    sender = 'YOUR_EMAIL@gmail.com'
    password = ''
    my_emai = 'YOUR_EMAIL@gmail.com'
    message = 'The web-site {} is DOWN!!!'.format(url)
    subj = 'The web-site {} is DOWN!!!'.format(url)
    msg = "Subject: {}\n\n{}".format(subj, message)

    mail_server.starttls()
    mail_server.login(sender, password)
    mail_server.sendmail(sender, my_emai, msg)
    mail_server.quit()


def ok_code_check(url):
    """
    Getting code from some web-site. 200 is 200_OK
    """
    response = urllib.request.urlopen(url).getcode()
    if response == 200:
        return True
    else:
        return False


def check_connect(okURLs):
    """
    Checking my internet connection by requesting code of some web-pages,
     that can't be down at the same time.
    """
    check_list = []
    for url in okURLs:
        check_list.append(ok_code_check(url))
    if True in check_list:
        return True
    else:
        return False


def test(url, trustedURLs):
    if check_connect(trustedURLs):
        site_status = ok_code_check(url)
    if site_status:
        print("OK!")
    else:
        send_email(url)

if __name__='__main__':
    test(url, trustURL)
