import os

env = os.getenv("FLASK_ENV", "development")

if env == "production":
    from config.production import DEBUG, PORT
elif env == "development":
    from config.development import DEBUG, PORT
else:
    # Default to development if unknown environment
    from config.development import DEBUG, PORT

__all__ = ["DEBUG", "PORT", "env"]
