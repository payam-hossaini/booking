import logging

DEV = ['dev', 'development']
TEST = ['test', 'Test']


def get_variables(environment):
    environment = environment.strip().lower()
    if environment in DEV:
        return development()
    elif environment in TEST:
        return test()
    else:
        message = (
            'Could not match to predefined environments!'
        )
        logging.warn(message)
        return test()


def default_var():
    main_dictionary = {}
    main_dictionary['BROWSER_TYPE'] = 'gc'
    main_dictionary['HOST'] = 'http://www.booking.com'
    main_dictionary['SELENIUM_SPEED'] = '0.25s'
    return main_dictionary


def test():
    # Get default values
    main_dictionary = default_var()
    main_dictionary['USERNAME'] = 'test user'
    main_dictionary['PASSWORD'] = 'pass'
    return main_dictionary


def development():
    # Get default values
    main_dictionary = default_var()
    main_dictionary['USERNAME'] = 'another user'
    main_dictionary['PASSWORD'] = 'pass'
    return main_dictionary
