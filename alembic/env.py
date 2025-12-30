import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.database import Base
from app import models

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata
