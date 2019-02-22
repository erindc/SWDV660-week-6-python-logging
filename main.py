import base64
import logging
import logstash
import sys
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('3.95.174.252', 5959, version=1))


def decode(encoding):
    decode = ""
    while decode!= "y" or decode != "n":
        decode = raw_input("Do you want to decode? (y/n): ")
        if decode == "y":
            decoded = base64.b64decode(encoding).decode("utf-8")
            print(decoded)
            logger.info("decoded", extra={
                "value": decoded
            })
            return
        elif decode == "n":
            logger.info("user input to decode", extra={
                "value": decode
            })
            return
        else:
            print("Invalid option! Please enter y or n")
            logger.info("invalid user input to decode", extra={
                "value": decode
            })

def main():
    while True:
        stop = ""
        byteInput = raw_input("Enter something to encode: ").encode()
        logger.info("user input to encode", extra={
            "value": byteInput.decode("utf-8")
        })
        encoded = base64.b64encode(byteInput)
        string = encoded.decode("utf-8")
        logger.info("base64 encoding", extra={
            "value": string
        })
        print(string)
        decode(encoded)
        while stop != "n" and stop != "y":
            stop = raw_input("Continue? (y/n): ")
            logger.info("user input to continue", extra={
                "value": stop
            })
            if stop == "n":
                exit()

main()