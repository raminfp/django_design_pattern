# Django Project Template with Modular Architecture

## Overview
This project is a Django-based template designed with a modular architecture, making it scalable and maintainable. It serves as a robust starting point for building applications that require clear separation of concerns and integration with various services.

## Features
* **Modular API structure** with versioning support (`api/v1`).
* **Service-oriented design** integrating third-party services (e.g., Elasticsearch, Minio, RabbitMQ).
* **Custom management commands** for streamlined operations.
* **Reusable components** such as middleware, permissions, and caching strategies.
* **Repository pattern** for data access, promoting clean and testable code.
* **Dependency Injection** for improved testability and modularity in service integration and component management.
* **Custom validation** to ensure data integrity and enforce business rules.
* **Pydantic integration** for data validation and settings management, enhancing data integrity and configuration management.
* **Serializer management** to handle data transformation and serialization across different API components.
* **URL management** with organized routing configurations for different parts of the application.
* **Model management** for effective database schema design and migrations, supporting scalable and maintainable data structures.
* **Comprehensive test suite** with organized test modules

## Project Structure
Here's a detailed breakdown of the project structure:

```
.
├── django_design_pattern
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py
│   │   ├── extra.py
│   │   └── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── django_design_pattern_app
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── admin
│   │       │   ├── __init__.py
│   │       │   └── users.py
│   │       ├── auth
│   │       │   └── __init__.py
│   │       ├── __init__.py
│   │       └── users
│   │           ├── __init__.py
│   │           └── users.py
│   ├── apps.py
│   ├── cache
│   │   ├── cache_decorators.py
│   │   ├── __init__.py
│   │   └── redis_cache.py
│   ├── __init__.py
│   ├── injector
│   │   ├── base_injector.py
│   │   └── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   ├── create_superuser.py
│   │   │   ├── import_sql.py
│   │   │   ├── __init__.py
│   │   │   └── launch_queue_listener.py
│   │   └── __init__.py
│   ├── middleware
│   │   ├── exceptionhandler.py
│   │   ├── exceptions.py
│   │   ├── __init__.py
│   │   ├── response.py
│   │   └── validate.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models
│   │   ├── base.py
│   │   ├── __init__.py
│   │   └── users.py
│   ├── modules
│   │   ├── elastic_module.py
│   │   ├── __init__.py
│   │   ├── kavenegar_module.py
│   │   ├── minio_module.py
│   │   ├── rabbitmq_module.py
│   │   └── redis_module.py
│   ├── permissions
│   │   ├── __init__.py
│   │   └── permissions.py
│   ├── repositories
│   │   ├── base_repo.py
│   │   ├── __init__.py
│   │   └── users_repo.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── users.py
│   ├── serializers
│   │   ├── admin
│   │   │   ├── __init__.py
│   │   │   └── user_serializers.py
│   │   ├── auth
│   │   │   ├── auth_serializers.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── users
│   │       ├── __init__.py
│   │       └── users_serializers.py
│   ├── services
│   │   ├── elasticsearch
│   │   │   ├── elasticsearch.py
│   │   │   ├── indexing
│   │   │   │   ├── __init__.py
│   │   │   │   └── users_index.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── kafka
│   │   │   ├── __init__.py
│   │   │   ├── producer_user_created.py
│   │   │   └── queue_listener.py
│   │   ├── minio
│   │   │   ├── __init__.py
│   │   │   └── minio.py
│   │   ├── rabbitmq
│   │   │   ├── __init__.py
│   │   │   └── rabbitmq.py
│   │   ├── redis
│   │   │   ├── __init__.py
│   │   │   └── redis.py
│   │   └── sms
│   │       ├── __init__.py
│   │       └── tasks.py
│   ├── signals
│   │   ├── __init__.py
│   │   ├── receivers.py
│   │   └── signals.py
│   ├── tests
│   │   ├── admin
│   │   │   └── __init__.py
│   │   ├── base_test.py
│   │   ├── __init__.py
│   │   └── users
│   │       ├── __init__.py
│   │       └── test_user_login.py
│   ├── urls
│   │   ├── admin
│   │   │   ├── admin.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   └── users.py
│   └── utils
│       ├── helper.py
│       ├── __init__.py
│       ├── messages.py
│       └── validations.py
└── manage.py

```

This structure provides a detailed view of the project's organization, including:

- API versioning (`api/v1`)
- Custom management commands
- Model definitions
- Service integrations (Elasticsearch, Kafka, Minio, RabbitMQ, Redis, SMS)
- Serializers for different parts of the application
- Test structure
- URL configurations
- Utility functions and helpers


### Docker configuration 

```bash
$ docker-compose up --build

[+] Running 3/0
 ⠿ Container django_design_pattern-minio-1     Created                                0.0s
 ⠿ Container django_design_pattern-redis-1     Created                                0.0s
 ⠿ Container django_design_pattern-postgres-1  Created                                0.0s
Attaching to django_design_pattern-minio-1, django_design_pattern-postgres-1, django_design_pattern-redis-1
django_design_pattern-postgres-1  | 
django_design_pattern-postgres-1  | PostgreSQL Database directory appears to contain a database; Skipping initialization
django_design_pattern-postgres-1  | 
django_design_pattern-postgres-1  | 2024-11-09 06:12:45.569 GMT [1] LOG:  redirecting log output to logging collector process
django_design_pattern-postgres-1  | 2024-11-09 06:12:45.569 GMT [1] HINT:  Future log output will appear in directory "pg_log".
django_design_pattern-redis-1     | 1:C 09 Nov 2024 06:12:45.707 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
django_design_pattern-redis-1     | 1:C 09 Nov 2024 06:12:45.707 * Redis version=7.4.1, bits=64, commit=00000000, modified=0, pid=1, just started
django_design_pattern-redis-1     | 1:C 09 Nov 2024 06:12:45.707 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.708 * monotonic clock: POSIX clock_gettime
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * Running mode=standalone, port=6379.
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * Server initialized
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * Loading RDB produced by version 7.4.1
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * RDB age 8 seconds
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * RDB memory usage when created 0.90 Mb
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * Done loading RDB, keys loaded: 0, keys expired: 0.
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * DB loaded from disk: 0.000 seconds
django_design_pattern-redis-1     | 1:M 09 Nov 2024 06:12:45.709 * Ready to accept connections tcp
django_design_pattern-minio-1     | MinIO Object Storage Server
django_design_pattern-minio-1     | Copyright: 2015-2024 MinIO, Inc.
django_design_pattern-minio-1     | License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
django_design_pattern-minio-1     | Version: RELEASE.2024-11-07T00-52-20Z (go1.23.3 linux/amd64)
django_design_pattern-minio-1     | 
django_design_pattern-minio-1     | API: http://192.168.160.3:9000  http://127.0.0.1:9000 
django_design_pattern-minio-1     | WebUI: http://192.168.160.3:45897 http://127.0.0.1:45897 
django_design_pattern-minio-1     | 
django_design_pattern-minio-1     | Docs: https://docs.min.io

```
