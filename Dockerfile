FROM node:alpine as angular_builder
RUN apk update && apk add --no-cache make git
RUN mkdir /app
WORKDIR /app
ADD frontend/package* /app/
RUN cd /app && npm install
ADD frontend/ /app
RUN cd /app && npx -p @angular/cli ng build --prod --build-optimizer

FROM nginx:alpine
RUN mkdir /src
COPY --from=angular_builder /app/dist /src
CMD ["nginx", "-g", "daemon off;"]
