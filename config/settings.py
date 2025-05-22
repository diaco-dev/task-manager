from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
import sqlalchemy as sa



# class Settings(BaseSettings):
#     debug: bool = False
#     development: bool = False
#
#     echo_sql: bool = False
#     postgres_pool_size: int = 10
#
#     # PostgreSql config
#     db_host: str
#     db_port: int = 5432
#     db_user: str
#     db_password: str
#     db_name: str
#
#     # redis
#     redis_host: str
#     redis_port: int
#     fastapi_redis_db: int
#
#     # Cache
#     cache_time_highest: int = 60 * 60 * 24 * 24  # 1 Day
#     cache_time_very_high: int = 60 * 60 * 12  # 12 Hours
#     cache_time_high: int = 60 * 60 * 6  # 6 Hours
#     cache_time_medium: int = 60 * 60  # 1 Hour
#     cache_time_low: int = 60 * 30  # 30 Minutes
#     cache_time_very_low: int = 60 * 10  # 10 Minutes
#     cache_time_lowest: int = 60  # 1 Minute
#
#     # jwt config
#     jwt_algorithm: str
#     jwt_secret_key: str
#
#     api_prefix: str = '/api'
#     api_version_prefix: str = f'{api_prefix}/v2'
#
#     storage_dir: str
#     storage_url: str
#
#     # allowed_hosts: str = 'localhost,127.0.0.1,alicarpet.de,chavoshinia.de'
#     allowed_hosts: str = '*'
#
#     # validate_token_url: str
#
#     use_tz: bool = True
#     time_zone: str = 'Europe/Berlin'
#
#     api_base_url: str
#     api_image_base_url: str
#     base_url: str
#
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )
#
#     @property
#     def database_uri(self) -> str:
#         return sa.URL.create(
#             drivername="postgresql+asyncpg",
#             username=self.db_user,
#             password=self.db_password,
#             host=self.db_host,
#             port=self.db_port,
#             database=self.db_name
#         ).render_as_string(hide_password=False)
#
#     @property
#     def allowed_hosts_list(self) -> List[str]:
#         return self.allowed_hosts.split(",")
#
#     @property
#     def app_dir(self):
#         return Path(__file__).parent.parent.parent.absolute()
#
#     @property
#     def src_dir(self):
#         return Path(__file__).parent.parent.absolute()
#
#     def set_base_url(self, base_url):
#         self.base_url = base_url
