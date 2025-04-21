# User Service

Service implementation goes here.

docker-compose down -v --remove-orphans
docker system prune -af --volumes
docker-compose build --no-cache
docker-compose up

Kafka event → product.created in product-catalog → search-service consumes and indexes it
help me on this

how to know how es indexing the pridyct details and  what are index's and what can be custamized and optimzation techniqyes 
when to use mutiple indexes


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



Spring Boot
PostgreSQL
MongoDB
Elasticsearch
Kafka - Not Started
Docker Compose
Nginx




🧱 Updated Tech Stack
✅ Spring Boot – Order, User, Cart services

✅ FastAPI – Catalog, Notification, Admin services

✅ PostgreSQL – Orders, users, cart

✅ MongoDB – Product catalog

✅ Elasticsearch – Product search

✅ Kafka – Real-time event propagation

✅ Docker Compose – Service orchestration (instead of Kubernetes)

✅ Nginx / Traefik (optional) – API Gateway & routing (optional, simple config)

