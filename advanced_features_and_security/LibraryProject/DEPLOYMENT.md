# HTTPS Deployment Guide (advanced_features_and_security)

This guide outlines how to deploy the Django project with HTTPS, enable redirects to HTTPS, and configure secure headers.

## 1. Django settings (already configured)

See `LibraryProject/LibraryProject/settings.py`:

- `SECURE_SSL_REDIRECT=True` when `DJANGO_DEBUG=False` (forces HTTPS).
- HSTS enabled in production: `SECURE_HSTS_SECONDS=31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`, `SECURE_HSTS_PRELOAD=True`.
- Secure cookies in production: `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`.
- Headers: `X_FRAME_OPTIONS='DENY'`, `SECURE_CONTENT_TYPE_NOSNIFF=True`, `SECURE_BROWSER_XSS_FILTER=True`.
- CSP via `django-csp` middleware.

Set `DJANGO_DEBUG=False` in the environment for production.

## 2. Example Nginx + Gunicorn HTTPS setup

Install packages on Ubuntu (example):

```bash
sudo apt-get update
sudo apt-get install -y nginx python3-venv
```

Run Gunicorn (as a systemd service in production, simplified here):

```bash
cd /srv/app
source .venv/bin/activate
export DJANGO_DEBUG=False
export DJANGO_SETTINGS_MODULE=LibraryProject.settings
# Collect static files if needed
# python manage.py collectstatic --noinput
# Start gunicorn (adjust workers, bind address)
gunicorn LibraryProject.wsgi:application --bind 127.0.0.1:8001 --workers 3
```

Nginx server block (replace `example.com`):

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    # Redirect all HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    # Proxy to gunicorn
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_pass http://127.0.0.1:8001;
    }
}
```

Optionally set in Django: `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`.

## 3. HTTPS certificates (Let’s Encrypt)

Install Certbot and obtain certs:

```bash
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx -d example.com -d www.example.com
```

Certbot will configure SSL and set up automatic renewal.

## 4. Review checklist

- [ ] `DJANGO_DEBUG=False` set in production.
- [ ] `ALLOWED_HOSTS` includes your domain(s).
- [ ] Reverse proxy sets `X-Forwarded-Proto https` and `SECURE_PROXY_SSL_HEADER` configured if needed.
- [ ] Gunicorn or another WSGI server is used (not Django dev server).
- [ ] CSP rules adjusted if loading external scripts/styles.

## 5. Troubleshooting

- Redirect loops: ensure proxy sets `X-Forwarded-Proto` and Django `SECURE_PROXY_SSL_HEADER` is set accordingly.
- Mixed content: ensure all assets are loaded via `https://` and update CSP if using third-party CDNs.
