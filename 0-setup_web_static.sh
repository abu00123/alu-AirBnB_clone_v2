#!/usr/bin/env bash
# This script sets up the web servers for deploying web_static

# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt update -y
    sudo apt install nginx -y
fi

# Create required directories if they don’t exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake index.html file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Remove the symbolic link if it exists and create a new one
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ directory to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
nginx_config="/etc/nginx/sites-available/default"

sudo sed -i "/server_name _;/a \\
        location /hbnb_static {\\
            alias /data/web_static/current/;\\
        }" $nginx_config

# Restart Nginx to apply the changes
sudo systemctl restart nginx

echo "Web server setup complete!"

