from email.message import EmailMessage

from config import SMTP_USER


def get_email_template_dashboard(user_email: str) -> EmailMessage:
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = user_email

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email
