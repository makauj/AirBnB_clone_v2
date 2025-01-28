#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
  sudo apt update && sudo apt install nginx -y
fi
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOL
server {
    listen 80;
    server_name makau.tech;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}

sudo nginx -t
sudo service nginx restart
