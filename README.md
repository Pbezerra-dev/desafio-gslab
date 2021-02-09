![CI](https://github.com/Pbezerra-dev/desafio-gslab/workflows/CI/badge.svg)

># Desafio - GsLab

## Como rodar o projeto localmente?
```bash
git clone https://github.com/Pbezerra-dev/desafio-gslab.git
cd desafio-gslab
cp backend/contrib/env-dev-sample backend/.env
cp backend/contrib/env-db-sample backend/.db.env
docker-compose build --no-cache
docker-compose up -d
docker-compose run api python manage.py migrate
docker-compose run api python manage.py createsuperuser
```
### PS: Use login e senha criados, para fazer o [login](http://localhost:8080/login) no front!

---

## **Backend**

### Rode o lint
```bash
docker-compose run api flake8 --config=.flake8
```

### Rode os testes
```bash
docker-compose run api pytest --cov=products
```

---
## **Frontend**

### Rode o lint
```bash
docker-compose run frontend npm run lint
```
---
## **Endpoints**
```
login/
products/
products/<int:pk>/update
products/<int:pk>/delete
products/<int:pk>
```
