from unittest import mock

from handler import *

@mock.patch('handler.log_event')
@mock.patch('handler.send_message')
def test_send_handler_status(sender_mock, logger_mock):
    """
    Tests for send_handler_status procedure
    :param sender_mock: sender patch
    :param logger_mock: logger patch
    """

    #success
    send_handler_status(11, 0)
    sender_mock.assert_called_with(MARKETING_EMAIL, '11 orders was handled during today successfully.')
    logger_mock.assert_called_with('success: failed 0 orders, success 11 orders')
    sender_mock.reset_mock()
    logger_mock.reset_mock()

    #incident test 1
    send_handler_status(11, 9)
    sender_mock.assert_any_call(SUPPORT_EMAIL,
                                'Just 11 orders was handled during today successfully.\n9 orders had problem with handle')
    sender_mock.assert_any_call(MARKETING_EMAIL,
                                'Just 11 orders was handled during today successfully.\n9 orders had problem with handle')
    logger_mock.assert_called_with('incident: failed 9 orders, success 11 orders')
    sender_mock.reset_mock()
    logger_mock.reset_mock()

    # incident test 2
    send_handler_status(0, 9)
    sender_mock.assert_any_call(SUPPORT_EMAIL,
                                'Just 0 orders was handled during today successfully.\n9 orders had problem with handle')
    sender_mock.assert_any_call(MARKETING_EMAIL,
                                'Just 0 orders was handled during today successfully.\n9 orders had problem with handle')
    logger_mock.assert_called_with('incident: failed 9 orders, success 0 orders')
    sender_mock.reset_mock()
    logger_mock.reset_mock()

    # idle
    send_handler_status(0, 0)
    sender_mock.assert_any_call(SUPPORT_EMAIL, "No one order wasn't handled during today.")
    logger_mock.assert_called_with('idle: failed 0 orders, success 0 orders')


if __name__ == '__main__':
    test_send_handler_status()