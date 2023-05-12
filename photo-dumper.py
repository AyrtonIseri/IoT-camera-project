import sys

from scripts.QueueManagers.QueueManager import Manager

if __name__ == '__main__':
    client=sys.argv[1]
    queue_path=sys.argv[2]

    mgmt = Manager(client=client, queue_path=queue_path)

    mgmt.process_queue()