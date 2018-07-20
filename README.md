Udacity Log Analysis
==

> Console app to list analysis in log tables

## Prerequisites

- [vagrant](https://www.vagrantup.com/)

### Data

[Download data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
Unzip newsdata.zip then copy to udacity-log-analysis

## Install

```shell
git clone https://github.com/paulorsouza/udacity-log-analysis.git
cd udacity-log-analysis

vagrant up
vagrant ssh
```

## Dependencies

```shell
pip3 install texttable psycopg2 psycopg2-binary
pip3 install -U pytest
```

## Populate database

```shell
cd /vagrant
psql -d news -f newsdata.sql
```

### Run

```shell
cd /vagrant/app
python3 analysis.py
```

### Run tests

```shell
cd /vagrant/app
pytest
```
