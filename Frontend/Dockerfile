FROM node:latest as node

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build --prod

FROM nginx:alpine
COPY --from=build-step /app/dist/Frontend /usr/share/nginx/html