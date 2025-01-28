#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
  sudo apt update && sudo apt install nginx -y
fi
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}'  /etc/nginx/sites-available/default

sudo nginx -t
sudo service nginx restart
