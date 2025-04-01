#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt update -y
    sudo apt install nginx -y
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create (or recreate) the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve web_static
nginx_conf="\
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }"

# Add Nginx configuration if not already present
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sudo sed -i "/server_name _;/a\\$nginx_conf" /etc/nginx/sites-available/default
fi

# Restart Nginx to apply changes
sudo systemctl restart nginx

# Exit successfully
echo "Web static setup completed successfully."
exit 0

