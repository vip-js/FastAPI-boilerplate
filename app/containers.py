from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.api"]
    )

    db_session = providers.Dependency()
