# IBM Full Stack Software Developer: Retrospective Portfolio

A retrospective, independently authored full-stack project aligned to public themes from the IBM Full Stack Software Developer Professional Certificate. This was created after certification; it is not recovered Coursera coursework, a submitted assessment, or a graded project. The course version completed may differ from the current public syllabus.

## Project: LaunchOps

A small project-readiness tracker: Django REST API, React client, SQLite persistence, Docker Compose, and a GitHub Actions workflow. The app demonstrates CRUD flows and clear API boundaries; it is a learning artifact, not a production service.

## Run locally

Requires Docker Desktop:

```bash
docker compose up --build
```

Frontend: <http://localhost:8080> · API: <http://localhost:8000/api/projects/> · Django admin: <http://localhost:8000/admin/>

To run without containers, install `backend/requirements.txt`, run `python backend/manage.py migrate`, then `python backend/manage.py runserver`. Start the frontend with `cd frontend && npm install && npm run dev`.

## Design and operations

- API supports list, create, retrieve, update, and delete; title, status and due date are validated server-side.
- SQLite data is persisted in a Compose volume. The container uses a development server and is not a hardened production deployment.
- `.env.example` documents configuration; never put real secrets in source control.
- The workflow runs dependency installation and Django system checks on pushes and pull requests.

See [`CURRICULUM_MAP.md`](CURRICULUM_MAP.md) for course alignment. No external services or credentials are required.

## Sources

- [IBM Full Stack Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)
- [Full Stack Application Development Capstone Project](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone)

This independent portfolio is not affiliated with or endorsed by IBM or Coursera. It contains no course-only lab solutions.
