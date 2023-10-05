import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6564670359:AAFM_4UJPr_OZehplXqg4FlEdG9VcRM2Jt4")
      API_ID = int(os.environ.get("APP_ID", "21513517"))
      API_HASH = os.environ.get("API_HASH", "838d3451485b95722878921877f12066")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "save_m8y_bot")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 5904348755 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
