from fluent import sender

logger = sender.FluentSender('api', host='fluentd', port=24224)


if logger.emit('path', {'message': 'Hello, Fluentd!', 'status': 'ok'}):
    print("Fluentd OK")
else:
    print("Fluentd not-ok")
