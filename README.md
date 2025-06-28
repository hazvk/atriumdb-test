# Testing AtriumDB

> Note that all commands are run from this directory - the root of the project

The purpose of this repo is to follow the [AtriumDB tutorial for Standard Data Access](https://docs.atriumdb.io/tutorial.html#standard-data-access).

It takes it one step further to play with data in three different ways:
1. [Analog-transformed signal data](./src/analog_transformed_signal_data/)
1. [Signal data](./src/signal_data/)
1. [Segmented signal data](./src/signals_by_segment/)

## Setup

### Pre-requisite installs
* Python 3
```
sudo apt install python3
```

* Docker (which will also have MariaDB/MySQL enabled, per [Usage](#usage))
```
sudo apt install docker.io -y
sudo groupadd docker # only required if group doesn't exist
sudo usermod -aG docker $USER
newgrp docker
```

### Environment setup
```
pip install virtualenv
sudo apt-get install -y libmariadb-dev
```

### Python setup
```
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Deploy and use MariaDB

All data we create and use per this image will be stored within this project folder, at `_data/mariadb-serve`

```
docker run --detach --name atriumdb-mariadb -p 3306:3306 -v ./_data/mariadb-serve:/var/lib/mariadb -e MARIADB_USER='atrium_tester' -e MARIADB_PASSWORD='password' -e MARIADB_ROOT_PASSWORD='root_password' -e MARIADB_DATABASE='atriumdb-test' mariadb:latest
```

### Write and read sample data

The scripts listed below have been written to ingest sample datasets. E.g. for [Signal data](./src/signal_data/), you can run the following:
```
python src/signal_data/write_data.py
python src/signal_data/read_data.py
```

### Read underlying data source

To see what's being stored inside the MariaDB metadata, you can use the MySQL console, as commanded below (with [MariaDB container running](#deploy-and-use-mariadb)):
```
mysql -h 172.17.0.2 -u [root | atrium_tester] -D atriumdb -p
```

## References

* [AtriumDB tutorial for Standard Data Access](https://docs.atriumdb.io/tutorial.html#standard-data-access)
* Data source: sourced from [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/)