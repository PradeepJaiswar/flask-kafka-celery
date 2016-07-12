from local import LocalConfig
from dev import DevConfig
from stage import StagingConfig
from prod import ProdConfig

def get_config(MODE):
   SWITCH = {
      'LOCAL'     : LocalConfig,
      'DEV'       : DevConfig,
      'STAGING'   : StagingConfig,
      'PRODUCTION': ProdConfig
   }
   return SWITCH[MODE]
