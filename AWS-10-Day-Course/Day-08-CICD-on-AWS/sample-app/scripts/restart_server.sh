#!/bin/bash
# CodeDeploy AfterInstall hook - make sure the web server is running.
dnf install -y httpd
systemctl enable --now httpd
systemctl restart httpd
