# Deploying social_media_api to Production

## Hosting Choice

This project is configured for deployment on **Render** (Python web service), with:

- Gunicorn as the WSGI server
- WhiteNoise for static file serving
- PostgreSQL via `DATABASE_URL`

## Production Settings Implemented

In `social_media_api/settings.py`:

- `DEBUG` controlled by env var (default `False`)
- `ALLOWED_HOSTS` controlled by env var
- Security settings enabled:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `X_FRAME_OPTIONS = 'DENY'`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_SSL_REDIRECT` from env (default `True`)
- Static/media settings configured (`STATIC_ROOT`, `MEDIA_ROOT`)
- Database configured via `dj_database_url` + `DATABASE_URL`

## Deployment Files Included

- `Procfile`
- `runtime.txt`
- `render.yaml`
- `.env.example`

## Render Deployment Steps

1. Push repository to GitHub.
2. In Render dashboard, create a **Web Service** from the repository.
3. Use the included `render.yaml`, or set manually:
   - Build command:
     `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command:
     `gunicorn social_media_api.wsgi:application`
4. Set environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=<your-render-domain>`
   - `DATABASE_URL=<render-postgres-url>`
   - `SECURE_SSL_REDIRECT=True`
   - `SESSION_COOKIE_SECURE=True`
   - `CSRF_COOKIE_SECURE=True`
5. Deploy and verify `/api/` endpoints are accessible.

## Static and Media Files

- Static files are served via WhiteNoise in production.
- If you later use external object storage (e.g. AWS S3), replace media storage backend accordingly.

## Database

- Local development: SQLite.
- Production: PostgreSQL using `DATABASE_URL`.
- Run migrations during deploy (`python manage.py migrate`).

## Monitoring and Maintenance

- Check Render logs for runtime errors.
- Keep dependencies updated regularly.
- Rotate secrets and enforce HTTPS.
- Add uptime monitoring and error tracking (e.g. Sentry) for ongoing maintenance.

## Final Testing Checklist

- App starts without errors in production.
- `collectstatic` succeeds.
- Migrations apply successfully.
- Authenticated API endpoints work.
- HTTPS redirection and secure cookies are active.

## Live URL

Set this after deploying on Render:

- `https://<your-service-name>.onrender.com/`
