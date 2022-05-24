echo "Update plex container..."
docker pull ghcr.io/linuxserver/plex:latest
docker ps | grep plex | awk '{print "docker stop "$1" && docker rm "$1}' | sh
docker run -d --name=plex --net=host -e PUID=1000 -e PGID=119 -e VERSION=docker -v /data/plex/config:/config -v /data/plex/tvshows/:/tv -v /data/plex/movies:/movies --restart unless-stopped ghcr.io/linuxserver/plex:latest

echo "Update nginx container..."
docker pull nginx:latest
docker ps | grep nginx | awk '{print "docker stop "$1" && docker rm "$1}' | sh
docker run -d --name=nginx -p 80:80 -v /data/nginx/html:/usr/share/nginx/html -v /data/nginx/conf.d:/etc/nginx/conf.d  --restart unless-stopped --name nginx nginx:latest

echo "Cleaning up old images..."
docker image prune -f
