Steps to create a dedicated admin service (recommended)

1) Create an `admin` branch locally and push it to GitHub:

```bash
# from repo root
git checkout -b admin
# Optional: make admin-only changes (see step 2)
git add .
git commit -m "admin branch: prepare admin-only deployment"
git push origin admin
```

2) (Optional but recommended) Harden the `admin` branch so students cannot access student pages:
- Remove or hide student-facing routes (index, submit) or set an env guard like `ADMIN_ONLY=true`.
- Example: in `app.py` you can check `os.environ.get('ADMIN_ONLY')` and return 404 for `/` or registration routes.

3) In Render dashboard:
- New → Web Service → Connect your GitHub repo.
- When choosing branch, select `admin` for the admin service (name it `student-platform-admin`).
- Enable Persistent Disk if you use SQLite, and set `DB_PATH=/data/database.db` in Environment.
- Add environment variables (only set sensitive vars on the admin service):
  - `ADMIN_PASSWORD`
  - `SECRET_KEY`
  - `PROFESSOR_EMAIL`
  - `BREVO_API_KEY`
  - (Optionally) `ANTHROPIC_API_KEY`

4) Deploy: Render will build the `admin` service from the `admin` branch. Verify at the admin service URL.

Notes:
- Prefer a managed Postgres DB (Render Postgres) if you want both services to share data. I can add optional `DATABASE_URL` support to `app.py` if you want that.
- The included `render.yaml` defines both `main` and `admin` services so Render can create them when you import the repo.
