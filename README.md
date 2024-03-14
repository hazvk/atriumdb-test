## Data source
Sourced from [https://physionet.org/content/mitdb/1.0.0/](https://physionet.org/content/mitdb/1.0.0/)

## Setup

### Environment setup
```
# make sure Docker installed
docker run --name atriumdb-mariadb -d -p 127.0.0.1:3306:3306 -v ./mariadb-data:/var/lib/mysql -e MARIADB_ROOT_PASSWORD='password' mariadb:latest
pip install virtualenv
sudo apt-get install -y libmariadb-dev
```

### Python setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```