FROM postgres:13-alpine

COPY ./infrastructure/postgres/postgresql.conf /usr/share/postgresql/postgresql.conf

ENV POSTGRES_DB=your_database_name
ENV POSTGRES_USER=your_username
ENV POSTGRES_PASSWORD=your_password

#EXPOSE 5432

CMD ["postgres", "-c", "config_file=/usr/share/postgresql/postgresql.conf"]
