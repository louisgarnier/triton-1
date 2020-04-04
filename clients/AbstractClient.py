import logging
import os
import yaml

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
