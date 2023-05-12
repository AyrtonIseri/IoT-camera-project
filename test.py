# from scripts.Connector.Connectors.S3Connector import S3Connector
from scripts.QueueManagers.QueueManager import Manager

# connector = S3Connector('nema')

# picture = './photo-queue/test-file.png'
# connector.load_picture(picture)

mgmt = Manager('nema', './photo-queue')
mgmt.process_queue()