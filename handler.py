from datetime import datetime


MARKETING_EMAIL = 'marketing@acme.test'
SUPPORT_EMAIL = 'support@acme.test'


def send_handler_status(successfully_count, failed_count):
    """
    Function send orders count info
    :param successfully_count: Successfully processed orders count
    :param failed_count: Failed to process orders count
    """


    if failed_count:
        # incident
        message = 'Just {0} orders was handled during today successfully.\n{1} orders had problem with handle'.format(
            str(successfully_count),
            str(failed_count))
        send_message(MARKETING_EMAIL, message)
        send_message(SUPPORT_EMAIL, message)
        status = 'incident'
    else:
        if successfully_count:
            # success
            message = '{0} orders was handled during today successfully.'.format(str(successfully_count))
            send_message(MARKETING_EMAIL, message)
            status = 'success'

        else:
            # idle
            message = "No one order wasn't handled during today."
            send_message(SUPPORT_EMAIL, message)
            status = 'idle'

    log_event('{0}: failed {1} orders, success {2} orders'.format(status, str(failed_count), str(successfully_count)))


def send_message(u, m):
    print('"""\nTO: {}\n{}\n"""'.format(u, m))


def log_event(message):
    print('{}: {}'.format(datetime.utcnow().isoformat(), message))
