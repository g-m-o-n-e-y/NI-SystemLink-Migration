from nislmigrate.facades.facade_factory import FacadeFactory
from nislmigrate.extensibility.migrator_plugin import MigratorPlugin
from nislmigrate.facades.mongo_configuration import MongoConfiguration
from nislmigrate.facades.mongo_facade import MongoFacade

userdata_dict = {
    "arg": "userdata",
    "name": "UserData",
    "directory_migration": False,
    "singlefile_migration": False,
}


class UserDataMigrator(MigratorPlugin):

    @property
    def name(self):
        return "UserData"

    @property
    def argument(self):
        return "userdata"

    @property
    def help(self):
        return "Migrate user data"

    def capture(self, migration_directory: str, facade_factory: FacadeFactory):
        mongo_facade: MongoFacade = facade_factory.get_mongo_facade()
        mongo_configuration: MongoConfiguration = MongoConfiguration(self.config)
        mongo_facade.capture_database_to_directory(
            mongo_configuration,
            migration_directory,
            self.name)

    def restore(self, migration_directory: str, facade_factory: FacadeFactory):
        mongo_facade: MongoFacade = facade_factory.get_mongo_facade()
        mongo_configuration: MongoConfiguration = MongoConfiguration(self.config)
        mongo_facade.restore_database_from_directory(
            mongo_configuration,
            migration_directory,
            self.name)

    def pre_restore_check(self, migration_directory: str, facade_factory: FacadeFactory) -> None:
        mongo_facade: MongoFacade = facade_factory.get_mongo_facade()
        mongo_facade.validate_can_restore_database_from_directory(
            migration_directory,
            self.name)
