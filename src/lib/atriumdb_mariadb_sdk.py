from atriumdb import AtriumSDK

_connection_params = {'host': "127.0.0.1",    'user': "root",    'password': "password",    'database': "atrium-test",    'port': 3306}
sdk = AtriumSDK.create_dataset(dataset_location="./mariadb-data", database_type="mysql", connection_params=_connection_params)