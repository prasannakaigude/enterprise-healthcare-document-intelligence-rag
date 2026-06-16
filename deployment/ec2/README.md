# AWS EC2 Deployment Path

This folder documents how I would run the Dockerized healthcare RAG platform on an AWS EC2 instance.

Version 15 does not create an EC2 instance automatically. It prepares a clear deployment path that can be followed manually and defended honestly in an interview.

## Simple Mental Model

EC2 is a virtual server in AWS.

For this project:

- EC2 runs the application containers.
- Docker packages the backend and frontend.
- Docker Compose starts both services.
- S3 stores source healthcare PDFs.
- ChromaDB data is stored in the mounted application data volume.

## Recommended EC2 Setup

Use an Ubuntu EC2 instance for the beginner deployment path.

Suggested starting point:

- AMI: Ubuntu Server LTS
- Instance type: `t3.medium` or larger for smoother dependency builds
- Security group inbound rules:
  - SSH `22` from your IP only
  - FastAPI `8000` from your IP only while testing
  - Streamlit `8501` from your IP only while testing
- Storage: at least 30 GB

For production, do not expose ports `8000` and `8501` directly to the public internet. Put the app behind a reverse proxy, HTTPS, authentication, and stricter networking.

## Files In This Deployment Path

`deployment/ec2/user_data.sh`

Installs Docker and Docker Compose plugin on an Ubuntu EC2 instance. It does not store secrets.

`docker-compose.ec2.yml`

Adds server-friendly settings on top of the local Compose file:

- restart policies
- production environment flag
- named Docker volume for `/app/data`

## Manual Deployment Steps

1. Launch an Ubuntu EC2 instance.
2. Use `deployment/ec2/user_data.sh` as the user data script, or run it manually after connecting.
3. Copy or clone this project into `/opt/rag-healthcare`.
4. Create a real `.env` file on the EC2 instance.
5. Start the app:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build
```

6. Check containers:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml ps
```

7. Check logs:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml logs -f
```

## Runtime Environment Variables

The EC2 `.env` file should contain real runtime values such as:

```text
OPENAI_API_KEY=your_real_key_here
APP_NAME=Enterprise Healthcare Document Intelligence RAG Platform
APP_VERSION=0.15.0
ENVIRONMENT=production
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your_real_bucket_name
AWS_S3_RAW_PREFIX=healthcare-documents/raw
```

Do not commit `.env` to GitHub.

Do not paste real OpenAI or AWS secrets into chat.

## Production Security Notes

This deployment path is a learning-friendly EC2 path, not a full healthcare production architecture.

For a real production healthcare system, add:

- private S3 bucket access
- IAM role for EC2 instead of long-lived AWS keys
- HTTPS with a load balancer or reverse proxy
- authentication and authorization
- logging and monitoring
- encrypted storage
- backups
- least-privilege security groups
- vulnerability scanning
- HIPAA-aware architecture review

