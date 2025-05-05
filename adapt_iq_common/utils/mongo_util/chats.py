from adapt_iq_common.utils.mongo_util import MongoConnectionBaseClass, MongoUtilConstants


class Chats(MongoConnectionBaseClass):
    def __init__(self):
        super().__init__(database_name=MongoUtilConstants.llm_data, collection_name=MongoUtilConstants.chats)
