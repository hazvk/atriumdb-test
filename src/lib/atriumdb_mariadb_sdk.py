import os
from pathlib import PurePath
from atriumdb import AtriumSDK

# _connection_params = {'host': "127.0.0.1",    'user': "atrium_tester",    'password': "password",    'database': "atriumdb-test",    'port': 3306}
_connection_params = {'host': "127.0.0.1",    'user': "root",    'password': "root_password",    'database': "atriumdb-test",    'port': 3306}

sdk = AtriumSDK.create_dataset(dataset_location=PurePath(os.path.dirname(os.path.abspath(__file__)), "../../_data/mariadb-data"),
                                database_type="mariadb", connection_params=_connection_params)