

cd /opt/cloudcomputing
docker compose -f docker-compose.prod.yml exec -T \
  -e DJANGO_SUPERUSER_USERNAME=admin \
  -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
  -e DJANGO_SUPERUSER_PASSWORD=admin123 \
  web python manage.py createsuperuser --noinput

echo "Done! Admin user created: admin / admin123"
echo "Log in at: http://20.251.154.94/admin"
