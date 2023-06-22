from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["./api/api_v1/endpoints"])
    #Provide configuration using "config = providers.Configuration()"

    #Add the dependencies here
