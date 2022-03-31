"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.cause_all_of import CauseAllOf
    from plaid.model.plaid_error import PlaidError
    globals()['CauseAllOf'] = CauseAllOf
    globals()['PlaidError'] = PlaidError


class Cause(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('error_type',): {
            'INVALID_REQUEST': "INVALID_REQUEST",
            'INVALID_RESULT': "INVALID_RESULT",
            'INVALID_INPUT': "INVALID_INPUT",
            'INSTITUTION_ERROR': "INSTITUTION_ERROR",
            'RATE_LIMIT_EXCEEDED': "RATE_LIMIT_EXCEEDED",
            'API_ERROR': "API_ERROR",
            'ITEM_ERROR': "ITEM_ERROR",
            'ASSET_REPORT_ERROR': "ASSET_REPORT_ERROR",
            'RECAPTCHA_ERROR': "RECAPTCHA_ERROR",
            'OAUTH_ERROR': "OAUTH_ERROR",
            'PAYMENT_ERROR': "PAYMENT_ERROR",
            'BANK_TRANSFER_ERROR': "BANK_TRANSFER_ERROR",
            'INCOME_VERIFICATION_ERROR': "INCOME_VERIFICATION_ERROR",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'error_type': (str,),  # noqa: E501
            'error_code': (str,),  # noqa: E501
            'error_message': (str,),  # noqa: E501
            'display_message': (str, none_type,),  # noqa: E501
            'item_id': (str,),  # noqa: E501
            'request_id': (str,),  # noqa: E501
            'causes': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'status': (float, none_type,),  # noqa: E501
            'documentation_url': (str,),  # noqa: E501
            'suggested_action': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'error_type': 'error_type',  # noqa: E501
        'error_code': 'error_code',  # noqa: E501
        'error_message': 'error_message',  # noqa: E501
        'display_message': 'display_message',  # noqa: E501
        'item_id': 'item_id',  # noqa: E501
        'request_id': 'request_id',  # noqa: E501
        'causes': 'causes',  # noqa: E501
        'status': 'status',  # noqa: E501
        'documentation_url': 'documentation_url',  # noqa: E501
        'suggested_action': 'suggested_action',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, error_type, error_code, error_message, display_message, item_id, *args, **kwargs):  # noqa: E501
        """Cause - a model defined in OpenAPI

        Args:
            error_type (str): A broad categorization of the error. Safe for programmatic use.
            error_code (str): The particular error code. Safe for programmatic use.
            error_message (str): A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.
            display_message (str, none_type): A user-friendly representation of the error code. `null` if the error is not related to user action.  This may change over time and is not safe for programmatic use.
            item_id (str): The `item_id` of the Item associated with this webhook, warning, or error

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            request_id (str): A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks.. [optional]  # noqa: E501
            causes ([bool, date, datetime, dict, float, int, list, str, none_type]): In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.  `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object.. [optional]  # noqa: E501
            status (float, none_type): The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook.. [optional]  # noqa: E501
            documentation_url (str): The URL of a Plaid documentation page with more information about the error. [optional]  # noqa: E501
            suggested_action (str): Suggested steps for resolving the error. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'error_type': error_type,
            'error_code': error_code,
            'error_message': error_message,
            'display_message': display_message,
            'item_id': item_id,
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              CauseAllOf,
              PlaidError,
          ],
          'oneOf': [
          ],
        }
