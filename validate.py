import validators
from messages import *


def validate_int(response):
    result = True
    try:
        number = int(response)
    except ValueError:
        result = False
        print("The input is not integer!")
    return result


def validate_last_element_of_url(url):
    last_element  = url[-1]
    result = True
    if last_element == '/':
        result = False
    return result

def validate_url(url):
    url_is_valid = validators.url(url)
    if not url_is_valid:
        print("The url is not valid")
    return url_is_valid
''''
# TODO move to validate
    def _is_int(self,response):
        result = True
        try:
            number = int(response)
        except ValueError:
            result = False
            print("The input is not integer!")
        return result
    def validate_range_response(self,range_results_response):
        result = False
        if self._is_int(range_results_response):
            if (0 < int(range_results_response)) and (int(range_results_response) <= 10):
                #Save num of results
                self.range_results = int(range_results_response)
                result = True
            else:
                print_out_of_range()
        else:
            print_must_be_int()
        return  result
'''
def validate_range_response(range_results_response):
    result = False
    if validate_int(range_results_response):
        if (0 < int(range_results_response)) and (int(range_results_response) <= 10):
            result = True
        else:
            print_out_of_range()
    else:
        print_must_be_int()
    return  result