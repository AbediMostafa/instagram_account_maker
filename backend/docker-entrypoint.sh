#!/bin/bash
php artisan migrate
php artisan db:seed --class=AdminSeeder
apache2-foreground
