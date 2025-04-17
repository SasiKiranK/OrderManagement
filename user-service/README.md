# User Service

Service implementation goes here.


OrderFlow/
├── docker-compose.yml             # Spins up all services
├── .env                           # Central config for DB creds, ports
├── user-service/                  # Spring Boot
├── product-catalog/               # FastAPI + MongoDB
├── search-service/                # FastAPI + Elasticsearch
├── cart-service/                  # Spring Boot
├── order-service/                 # Spring Boot + Kafka
├── inventory-service/             # FastAPI + PostgreSQL
├── notification-service/          # FastAPI + Kafka
├── admin-dashboard/               # FastAPI
├── kafka/                         # Kafka setup with Zookeeper
└── nginx/                         # Optional reverse proxy



🧱 Updated Tech Stack
✅ Spring Boot – Order, User, Cart services

✅ FastAPI – Catalog, Notification, Admin services

✅ PostgreSQL – Orders, users, cart

✅ MongoDB – Product catalog

✅ Elasticsearch – Product search

✅ Kafka – Real-time event propagation

✅ Docker Compose – Service orchestration (instead of Kubernetes)

✅ Nginx / Traefik (optional) – API Gateway & routing (optional, simple config)

