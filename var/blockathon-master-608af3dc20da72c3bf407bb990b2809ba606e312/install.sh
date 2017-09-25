#!/usr/bin/env bash

# Hier houden we dependencies bij, deze install file is een ruwe schets.

## Directories
mkdir /usr/share/blockathon
mkdir /usr/share/blockathon/upload
mkdir /usr/share/nginx/html/chain
mkdir /usr/share/nginx/html/chain/attribute
mkdir /usr/share/nginx/html/chain/images
mkdir /usr/share/blockathon/bin
mkdir /usr/share/nginx/upload

chmod 666 /usr/share/blockathon
chmod 666 /usr/share/nginx/html/upload
chmod 666 /usr/share/nginx/html/chain
chmod 775 /usr/share/nginx/upload

## Composer

php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php --install-dir=/usr/local/bin/composer
php -r "unlink('composer-setup.php');"

## Composer libraries
composer require khanamiryan/qrcode-detector-decoder
