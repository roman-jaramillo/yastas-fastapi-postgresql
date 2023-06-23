from dependency_injector import containers, providers
from app.core.config import settings
from app.api.deps import get_db

class Container(containers.DeclarativeContainer):
    # Line to provide configuration config = providers.Configuration(config)

    #Add the dependencies here
    get_db = providers.Factory(get_db)
