# Thimbleberry API v1

FastAPI gateway for Thimbleberry products.

Endpoints:
- GET /v1/health
- POST /v1/ai/chat
- GET /v1/ai/models
- GET /v1/users/me
- GET /v1/docs

Authentication:
Authorization: Bearer <THIMBLEBERRY_API_KEY>

The AI provider key must remain server-side and must never be committed to GitHub.
