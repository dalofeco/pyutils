"""
    test_utils.py defines test cases for the provided utils package
"""
from utils import Safe


# noinspection PyTypeChecker
class TestSafe:

    @staticmethod
    def test_keys_in_dict():

        # Define test dict
        test_dict = {
            'unique': 2,
            'other': 4,
            'me': 'da',
            'not_checked': None,
        }

        # Define valid test keys
        valid_test_keys = ['unique', 'other', 'me']
        invalid_test_keys = ['unique', 'other', 'not_here']
        improper_type_test_keys = [dict(), 2]

        # Assertion cases
        assert Safe.keys_in_dict(test_dict, valid_test_keys) is True
        assert Safe.keys_in_dict(test_dict, invalid_test_keys) is False
        assert Safe.keys_in_dict(test_dict, improper_type_test_keys) is False
        assert Safe.keys_in_dict(None, 22) is False

    @staticmethod
    def test_which_key_in_dict():

        # Define test dict
        test_dict = {
            'train': 2,
            'test': 4,
            'dev': 'da',
            'validation': None,
        }

        # Define valid test keys
        key_options = ['unique', 'train', 'me']
        multiple_key_options = ['train', 'test', 'dev']
        no_valid_key = ['quantum', 'theory', 'of', 23]
        no_valid_bad_type = ['quantum', 'theory', 'of', 23]

        # Test proper operation with only one key
        assert Safe.which_key_in_dict(test_dict, key_options) == 'train'

        # Test multiple key options to return the first match
        assert Safe.which_key_in_dict(
            test_dict, multiple_key_options,
        ) == 'train'

        # Test no valid outcomes with proper args
        assert not Safe.which_key_in_dict(test_dict, no_valid_key)

        # Test invalid key types
        assert not Safe.which_key_in_dict(test_dict, no_valid_bad_type)

        # Test empty lists and dicts
        assert not Safe.which_key_in_dict({}, [])

        # Test improper types
        assert not Safe.which_key_in_dict([], {})

    @staticmethod
    def test_is_email():

        # Define valid emails of various formats in list
        valid_emails = [
            'hereiamagain@yahoo.com',
            'ten23_me@realtek.com',
            'wherever23@googlemail.com',
            'robertdeNIRO@gmail.org',
            'sur.prise@facebook.net',
            'this233453@legit.co.uk',
            'fearsomeguy33@me.com',
            'her.ew.ego@labanca.es',
        ]

        # Define invalid emails of various formats in list
        invalid_emails = [
            '1234583@yahoo.com',
            '2stream@gmail.org',
            '_rererealize@yahoo.net',
            'i-am-me@propane.co.uk',
            'herewego@temporary',
            'fasternotslower_@yahoo.com',
            'slower234@234.com',
            'well23-@robust.com',
            'thisi$cool@email.net',
        ]

        # Assertion cases for all emails
        for valid_email in valid_emails:
            assert Safe.is_email(valid_email) is True
        for invalid_email in invalid_emails:
            assert Safe.is_email(invalid_email) is False

        # Test for bad argument type
        assert Safe.is_email(2) is False

    @staticmethod
    def test_is_namespace_email():

        # Define valid emails of various formats in list
        valid_emails = [
            'hereiamagain@{}.com',
            'ten23_me@{}.com',
            'wher.ever.23@{}.es',
            'robertdeNIRO@{}.org',
            'surprise@{}.net',
            'this233453@{}.co.uk',
            'fearsomeguy33@{}.com',
            'slower234@{}.com',
        ]

        # Define invalid emails of various formats in list
        invalid_emails = [
            '1234583@{}.com',
            '2stream@{}.org',
            '_rererealize@{}.net',
            'i-am-me@{}.co.uk',
            'herewego@{}',
            'notvalidcausedot.@{}.es',
            'fasternotslower_@{}.com',
            'well23-@{}.com',
            'thisi$cool@{}.net',
        ]

        # Define valid namespaces
        valid_namespaces = [
            'google', 'gmail', 'realtek',
            'however', 'twenty.coordinate', '2345',
        ]

        # Define invalid namespaces
        invalid_namespaces = ['rau*d', 'h&8']

        # Assertion cases for all emails
        for valid_email in valid_emails:
            for valid_namespace in valid_namespaces:
                assert Safe.is_valid_namespace_email(
                    valid_email.format(valid_namespace), valid_namespace,
                ) is True
            for invalid_namespace in invalid_namespaces:
                assert Safe.is_valid_namespace_email(
                    valid_email.format(
                        invalid_namespace,
                    ), invalid_namespace,
                ) is False

        for invalid_email in invalid_emails:
            for valid_namespace in valid_namespaces:
                assert Safe.is_valid_namespace_email(
                    invalid_email.format(valid_namespace), valid_namespace,
                ) is False
            for invalid_namespace in invalid_namespaces:
                assert Safe.is_valid_namespace_email(
                    invalid_email.format(
                        invalid_namespace,
                    ), invalid_namespace,
                ) is False

        # Test improper types
        assert Safe.is_valid_namespace_email(2, 'da') is False
        assert Safe.is_valid_namespace_email('do', dict()) is False
