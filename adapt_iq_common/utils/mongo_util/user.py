from adapt_iq_common.utils.mongo_util import MongoConnectionBaseClass, MongoUtilConstants


class User(MongoConnectionBaseClass):
    def __init__(self):
        super().__init__(database_name=MongoUtilConstants.configurations, collection_name=MongoUtilConstants.users)
