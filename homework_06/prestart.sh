#!/usr/bin/env bash

echo "Run migrations"
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
echo "Done migrations"
