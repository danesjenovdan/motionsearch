# start with the nodejs image, calling it 'build'
FROM node:alpine as build

# install node modules
COPY package.json yarn.lock /
RUN yarn

# build assets
COPY . .
RUN yarn && yarn build

# change base image
FROM nginx:alpine

# copy built files from the 'build' container into the nginx container
COPY --from=build dist /usr/share/nginx/html

# copy nginx config to "try_files"
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
