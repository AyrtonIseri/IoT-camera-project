from scripts.Connector.Connectors.S3Connector import S3Connector

connector = S3Connector('nema')

picture = './photo-queue/test-file.png'
connector.load_picture(picture)