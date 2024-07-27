import pika
import json

# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐를 선언
channel.queue_declare(queue='sample-queue', durable=True)

# 메시지를 처리할 콜백 함수
def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    # 여기서 message를 원하는 대로 처리
    # 예: message['key'] 등을 사용

# 큐로부터 메시지를 가져와 콜백 함수로 전달
channel.basic_consume(queue='sample-queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
