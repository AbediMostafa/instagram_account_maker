FROM registry.docker.ir/composer:latest as build
COPY . /app/
RUN composer i

FROM registry.docker.ir/php:8.2-apache as production

RUN docker-php-ext-install pdo pdo_mysql

RUN pecl install redis && docker-php-ext-enable redis

COPY --from=build /app /var/www/html
RUN chmod 777 -R /var/www/html/storage/ && \
    chown -R www-data:www-data /var/www/ && \
    a2enmod rewrite
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf
RUN chmod +x /var/www/html/docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]
