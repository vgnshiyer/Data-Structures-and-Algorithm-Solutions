# Your team is developing a web application in Node.js and needs to build a lightweight Docker image for reusability. Create a Dockerfile to containerize the project. The image must be standalone, so must contain all project files and required dependencies.
# Your task
# Create a Dockerfile according to the following expectations:
# • Use the official node Docker image from the Docker Hub;
# • Node.js version can be configured with the NODE_VERSION build argument and defaults to 13;
# • A lightweight Alpine version of the Node.js image is used, so when the version is set to 13 the base image should be node: 13-alpine;
# • To make sure project files are both available and run from /us/src/app, change the working directory to this specific path;
# • Copy all project files from the local . /project directory to the current working directory;
# • Install all dependencies with the pm install command;
# • Expose port 8080, as our project is a web server listening on this specific TCP port;
# • The application keeps its state on disk under /var / lib/project, so make sure this directory is set as a volume;
# • Set node server. js as a default command to execute when starting a container, leaving the entry point empty.

ARG NODE_VERSION=13
FROM node:${NODE_VERSION}-alpine

WORKDIR /usr/src/app

COPY ./project .

RUN npm install

EXPOSE 8080

VOLUME ["/var/lib/project"]

CMD ["node", "server.js"]