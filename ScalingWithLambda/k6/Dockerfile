FROM grafana/k6:latest
WORKDIR /app
COPY test.js /app/
ENTRYPOINT ["k6"]
CMD ["run", "test.js"]
