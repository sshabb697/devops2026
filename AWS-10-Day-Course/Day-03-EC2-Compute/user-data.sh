#!/bin/bash
# EC2 user-data script — runs once on first boot (Amazon Linux 2023).
# Installs Apache and publishes a simple web page.
dnf update -y
dnf install -y httpd
systemctl enable --now httpd

TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
AZ=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/placement/availability-zone)

cat > /var/www/html/index.html <<HTML
<!doctype html>
<html>
  <head><title>AWS Class</title></head>
  <body style="font-family: sans-serif; text-align:center; margin-top:4rem;">
    <h1>Hello from EC2 🎉</h1>
    <p>This page is served by Apache on an EC2 instance.</p>
    <p>Availability Zone: <b>${AZ}</b></p>
  </body>
</html>
HTML
