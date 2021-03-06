import ConfigParser

class MetaManager(object):
    def __init__(self):
        self._experimenter = ""
        self._fish_id = ""

    def import_cfg_values(self, cfg):
        self.experimenter = cfg.get("meta", "experimenter")
        self.fish_id = cfg.get("meta", "fish_id")

    @property
    def experimenter(self):
        return self._experimenter
    @experimenter.setter
    def experimenter(self, name):
        self._experimenter = name

    @property
    def fish_id(self):
        return self._fish_id
    @fish_id.setter
    def fish_id(self, object_id):
        self._fish_id = object_id
