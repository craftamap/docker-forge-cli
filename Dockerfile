FROM node:latest
ARG FORGE_VERSION=latest
RUN npm install -g @forge/cli@${FORGE_VERSION}
CMD ["forge"]
