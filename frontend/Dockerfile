FROM registry.docker.ir/node:18-alpine AS base
WORKDIR /opt
COPY ./package.json .
RUN npm install

COPY . .

ENTRYPOINT ["npm", "run", "dev" ]
