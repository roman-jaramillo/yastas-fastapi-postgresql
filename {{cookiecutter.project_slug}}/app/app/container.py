from dependency_injector import containers, providers
from app.core.config import settings
from app.api.deps import get_db

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["./api/api_v1/endpoints"])
    
    # Line to provide configuration config = providers.Configuration(config)

    #Add the dependencies here
    get_db = providers.Factory(get_db)
