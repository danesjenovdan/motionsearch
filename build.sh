#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH BACKEND
sudo docker build -f backend/Dockerfile -t motion-search-backend:latest ./backend
sudo docker tag motion-search-backend:latest rg.fr-par.scw.cloud/djnd/motion-search-backend:latest
sudo docker push rg.fr-par.scw.cloud/djnd/motion-search-backend:latest

# BUILD AND PUBLISH FRONTEND
sudo docker build -f frontend/Dockerfile -t motion-search-frontend:latest ./frontend
sudo docker tag motion-search-frontend:latest rg.fr-par.scw.cloud/djnd/motion-search-frontend:latest
sudo docker push rg.fr-par.scw.cloud/djnd/motion-search-frontend:latest
