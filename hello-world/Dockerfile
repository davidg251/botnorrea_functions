FROM node:17-slim

WORKDIR /application

COPY main.js /application

COPY package.json /application

RUN npm install

CMD ["node", "/application/main.js"]