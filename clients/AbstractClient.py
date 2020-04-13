import logging
import os
import requests
import yaml

class RequestErrors(Exception):
    pass

class AbstractClient(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cfg_file = None

    def load_config(self, config_name):
        self.logger.info("Importing {} config from configs file".format(config_name))
        conf_path = "configs/{}.yml".format(config_name)
        if not os.path.isfile(conf_path):
            self.logger.error("Cannot find conf path at : %s", conf_path)
            return
        with open(conf_path) as ymlfile:
            raw_cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.cfg_file = raw_cfg[config_name]

    def _get(self, url, headers=None, data=None):
        """
        Make a GET request.
        """
        return self._request(requests.get, url, headers)

    def _post(self, url, headers=None, data=None):
        """
        Make a POST request.
        """
        return self._request(requests.post, headers=headers)

    def _request(self, func, url, headers, return_json=True):
        """
        Make a generic request, adding in any proxy defined by the instance.
        Raises a ``requests.HTTPError`` if the response status isn't 200, and
        raises a :class:`RequestErrors` if the response contains a json encoded
        error message.
        """
        self.logger.debug("Request URL: " + url)

        response = func(url, headers=headers)
        self.logger.debug("Response Code {} and Reason {}".format(response.status_code, response.reason))
        self.logger.debug("Response Text {}".format(response.text))

        # Check for error, raising an exception if appropriate.
        response.raise_for_status()

        try:
            json_response = response.json()
        except ValueError:
            json_response = None
        if isinstance(json_response, dict):
            error = json_response.get('error')
            if error:
                raise RequestErrors(error)
            elif json_response.get('status') == "error":
                raise RequestErrors(json_response.get('reason'))

        if return_json:
            if json_response is None:
                raise RequestErrors(
                    "Could not decode json for: " + response.text)
            return json_response

        return response
