# Permissions and Groups Setup (advanced_features_and_security)

This project demonstrates custom permissions and groups using the `bookshelf` app.

What’s included

- Custom user model (`bookshelf.CustomUser`).
- Model-level permissions on `bookshelf.Book`: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Views protected with `@permission_required('bookshelf.can_view')`.
- A management command to create default groups and assign permissions.
- Security hardening: CSP via `django-csp`, secure cookies and headers, CSRF in templates and forms.

Quick start

1. Install deps and run migrations

```powershell
cd C:\Users\hp\Desktop\Alx_DjangoLearnLab\.venv\Scripts
./Activate.ps1
cd C:\Users\hp\Desktop\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject
python manage.py migrate
```

2. Create groups and permissions

```powershell
python manage.py seed_roles
```

3. Create users and assign groups

- In Django admin (`/admin/`), add users to one of:
  - Viewers: `can_view`
  - Editors: `can_view`, `can_create`, `can_edit`
  - Admins: `can_view`, `can_create`, `can_edit`, `can_delete`

4. Test permissions

- Log in as a user in each group and access the list and detail pages.
- Views requiring permissions are in `bookshelf/views.py` and use `@permission_required`.

5. Security settings (production)

- Set environment variable `DJANGO_DEBUG=False` in production to enable strict cookie/security headers.
- Security-related settings toggled when `DEBUG=False` in [LibraryProject/LibraryProject/settings.py](advanced_features_and_security/LibraryProject/LibraryProject/settings.py):
  - `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS='DENY'`
  - `CSRF_COOKIE_SECURE=True`, `SESSION_COOKIE_SECURE=True`
  - Content Security Policy via `django-csp` with `CSP_DEFAULT_SRC 'self'` etc.
  6. HTTPS & Redirects
  - HTTPS is enforced in production (when `DJANGO_DEBUG=False`) via:
    - `SECURE_SSL_REDIRECT=True`
    - HSTS: `SECURE_HSTS_SECONDS=31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`, `SECURE_HSTS_PRELOAD=True`
  - See deployment steps and Nginx example in `DEPLOYMENT.md`.

Security demo

- Safe search form on Books list at `/books/` uses a Django `Form` and ORM filtering.
- CSRF protection included in templates via `{% csrf_token %}`. See `book_list.html` and `form_example.html`.

Notes

- Media uploads for user profile photos are enabled via `MEDIA_URL`/`MEDIA_ROOT`.
- To add create/edit/delete views for `Book`, apply the corresponding decorators:
  - `@permission_required('bookshelf.can_create', raise_exception=True)`
  - `@permission_required('bookshelf.can_edit', raise_exception=True)`
  - `@permission_required('bookshelf.can_delete', raise_exception=True)`
