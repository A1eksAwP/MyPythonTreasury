Для настройки Kafka с использованием Docker можно использовать официальный образ Docker, предоставляемый Apache Kafka.
Вот пример базовой настройки Kafka с помощью Docker Compose:

1) Установите **Docker** и **Docker Compose** на свою систему, если они еще не установлены.

2) Создайте файл **docker-compose.yml** и добавьте следующий код:

```
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:6.2.0
    hostname: zookeeper
    ports:
      - "2181:2181"
    environment:
      - ZOOKEEPER_CLIENT_PORT=2181
      - ZOOKEEPER_TICK_TIME=2000
  
  kafka:
    image: confluentinc/cp-kafka:6.2.0
    hostname: kafka
    ports:
      - "9092:9092"
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_LISTENERS=PLAINTEXT://:9092
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
      - KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1
      - KAFKA_AUTO_CREATE_TOPICS_ENABLE=false
    depends_on:
      - zookeeper
```

3) Откройте терминал или командную строку и перейдите в каталог, где находится файл **_docker-compose.yml_**.

4) Запустите **Kafka** с помощью команды:

`docker-compose up`

Docker Compose загрузит образы ZooKeeper и Kafka, создаст контейнеры для них и настроит их связь друг с другом.
ZooKeeper будет запущен на порту 2181, а Kafka - на порту 9092.

Теперь у вас должен быть работающий экземпляр Kafka, который можно использовать для разработки и тестирования. Вы можете
создавать топики, публиковать и потреблять сообщения с помощью Kafka-клиента на вашей машине.

Обратите внимание, что это базовая конфигурация для локальной разработки и тестирования. Для более сложных сценариев или
развертывания в производственной среде потребуется более детальная настройка и конфигурация Kafka и ZooKeeper.

Кроме того, обратите внимание, что указанные версии образов могут быть устаревшими. Рекомендуется проверить официальный
репозиторий Docker Hub или сайт Apache Kafka для актуальных версий образов.