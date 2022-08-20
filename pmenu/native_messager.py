import json
import os
import struct
import subprocess
import sys

from pmenu import utils

# Read a message from stdin and decode it.
def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        raise

    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)

# Encode a message for transmission, given its content.
def encode_message(message_content):
    encoded_content = json.dumps(message_content).encode("utf-8")
    encoded_length = struct.pack('=I', len(encoded_content))
    #  use struct.pack("10s", bytes), to pack a string of the length of 10 characters
    return {'length': encoded_length, 'content': struct.pack(str(len(encoded_content))+"s",encoded_content)}

# Send an encoded message to stdout.
def send_message(encoded_message):
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()

def main():
    while True:
        try:
            message = get_message()
        except Exception as e:
            print(e, file=sys.stderr)
            continue

        url = message["url"]
        result = subprocess.run(['passmenu2'],
            env={ **os.environ, 'PASSWORD_STORE_DIR': utils.fake_pass_base(url) },
            capture_output=True
        )
        output = result.stdout.decode().strip()
        username, password, *_ = output.split("\n")

        send_message(encode_message({"username": username, "password": password, "id": message["id"]}))
