import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8002
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO
    # Variables for the database
    db_file: Path = TEMP_DIR / "db.sqlite3"
    db_echo: bool = False

    # This variable is used to define
    # multiproc_dir. It's required for [uvi|guni]corn projects.
    prometheus_dir: Path = TEMP_DIR / "prom"

    aws_access_key_id: str = "AKIAIOSFODNN7EXAMPLE"
    aws_secret_access_key: str = "wJalrXUtnFEMIK7MDENG/bPxRfiCYEXAMPLEKEY"

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        print(f"Using database file: {self.db_file}")
        # return URL.build(scheme="sqlite+aiosqlite", path=f"///{self.db_file}")
        return f"sqlite+aiosqlite:///{self.db_file}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FASTAPI_AMAZON_Q_DEV_",
        env_file_encoding="utf-8",
    )


settings = Settings()
