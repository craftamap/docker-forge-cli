FROM node:latest
ARG FORGE_VERSION=latest
RUN npm install -g @forge/cli@0.29.0
CMD ["forge"]
