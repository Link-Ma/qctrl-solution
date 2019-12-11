# qctrl-solution
Please test the functionalities according to the following order.

1. Bulk upload controls in CSV format

  curl -X POST "http://localhost:8000/api/control/upload/" -F 'file=@control.csv'

2. Download controls in CSV format

  curl http://localhost:8000/api/control/download/
and open http://localhost:8000/api/control/download/ in the browser.

3. Create a new control

  curl -X Post -H "Content-Type: application/json" -d  '{"name":"create", "type": "Primitive", "maximum_rabi_rate": 63.16731, "polar_angle": 0.05671}' "http://localhost:8000/api/control/"

4. List all controls (five per page)

  curl http://localhost:8000/api/control/

5. Get a specific control

  curl http://localhost:8000/api/control/1/

6. Update a specific control

  curl -X PUT -H "Content-Type: application/json" -d  '{"name":"myname"}' "http://localhost:8000/api/control/5/"

7. Delete a specific control

  curl -X Delete -H "Content-Type: application/json" "http://localhost:8000/api/control/5/"   

<br/><br/>

PosgresQL install steps:

(install)1. brew install postgresql -v

(config) 2. initdb /usr/local/var/postgres -E utf8

(start) 3. pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

(close) 4. pg_ctl -D /usr/local/var/postgres stop -s -m fast

(create user) 5. createuser liqian -P

(create db) 6. createdb ctrldb -O liqian -E UTF8 -e

(connect db) 7. psql -U liqian -d ctrldb -h 127.0.0.1
