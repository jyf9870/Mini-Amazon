# ECE568 Final Project - Amazon

## Authors: Oliver Chen (yc557), Yifan Jiang (yj193) 

## Notes to create local postgres database
```bash
sudo service postgresql start
sudo su - postgres
psql
CREATE user yc557;
ALTER USER yc557 WITH PASSWORD 'Oliver666';
CREATE DATABASE "projectDB";
GRANT ALL PRIVILEGES ON DATABASE "projectDB" TO yc557;
```
Quit postgresql, then connect to the db as the corresponding user
```bash
psql -d projectDB -U yc557
\dt
```
To stop postgres,
```bash
sudo service postgresql stop
```

## Notes related to Docker
To create a superuser in Django within Docker, first use `docker ps` to
get the container id, then
```bash
sudo docker exec -it <container_id> python3 manage.py createsuperuser
```
To enter into a Docker container:
```bash
docker exec -it <container_id_or_name> bash
```
