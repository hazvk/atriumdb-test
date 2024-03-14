## Data source
Sourced from [https://physionet.org/content/mitdb/1.0.0/](https://physionet.org/content/mitdb/1.0.0/)

## Setup

### Environment setup
```
# make sure Docker installed

pip install virtualenv
sudo apt-get install -y libmariadb-dev
```

### Python setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
docker run --detach --name atriumdb-mariadb -p 3306:3306 -v ./_data/mariadb-serve:/var/lib/mariadb -e MARIADB_USER='atrium_tester' -e MARIADB_PASSWORD='password' -e MARIADB_ROOT_PASSWORD='root_password' -e MARIADB_DATABASE='atriumdb-test' mariadb:latest

python src/write_data.py
python src/read_data.py
```

### Read underlying data source
```
# With container running

mysql -h 172.17.0.2 -u [root | atrium_tester] -p
```