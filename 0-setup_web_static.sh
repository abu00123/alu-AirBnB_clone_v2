#!/bin/bash
# Script to set up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create required directories
sudo mkdir -p /data/web_static/releases/test /
data/web_static/shared

# Create a fake HTML file
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create (or recreate) symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ under /hbnb_static
config="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sudo sed -i "/server_name _;/a \t$config" /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo service nginx restart

exit 0

