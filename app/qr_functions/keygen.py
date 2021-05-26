import uuid

def generate_key():
	return str(uuid.uuid1(node=0).hex)[:20]
