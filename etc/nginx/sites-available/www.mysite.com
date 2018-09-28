# Virtual Host File
# Common wordpress configurations included in /etc/nginx/wordpress.conf
# All virtual hosts including this one are symlinked to /etc/nginx/sites-enabled
# Make sure you replace "mysite" with your domain name

location /media {
    alias /home/XXX/sites/www.mysite.com/media;
}