for x in `docker image ls | grep -v REPOSITORY | awk '{print $1}'`;
do
  echo "Updating Image: $x"
  docker pull ${x}:latest
  echo
done

echo

for x in `docker ps ls -q`;
do
  echo "Stopping Container: $x"
  docker stop ${x}
  docker rm ${x}
  echo
done

echo

echo "Starting RBPI401 Containers via docker-compose"
cd /home/sysadmin/containers/docker-stuff/rbpi401
docker-compose up -d

echo 

echo "Cleaning up old images..."
docker image prune -f

echo
