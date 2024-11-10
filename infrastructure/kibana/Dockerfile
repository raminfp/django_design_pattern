# Use the official Kibana image
FROM docker.elastic.co/kibana/kibana:8.15.3

# Set the environment variable to connect to Elasticsearch
ENV ELASTICSEARCH_HOSTS=http://elasticsearch:9200

# Copy any custom configuration files if needed
# COPY kibana.yml /usr/share/kibana/config/kibana.yml

# Expose the default port for Kibana
EXPOSE 5601
