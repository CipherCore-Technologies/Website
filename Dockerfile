FROM nginx:alpine
COPY templates /usr/share/nginx/html
COPY static /usr/share/nginx/html/static   # ← add this line
EXPOSE 80
