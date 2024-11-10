# Use the official Elasticsearch image
FROM docker.elastic.co/elasticsearch/elasticsearch:8.15.3

# Set environment variables
ENV discovery.type=single-node

# Set Java options to limit memory usage
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m"

# Copy any custom configuration files if needed
# COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Expose the default ports
EXPOSE 9200 9300
