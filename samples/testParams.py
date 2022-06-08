import getopt
import sys

LISTEN_IP = ''
LISTEN_PORT = 0


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ipaddress=", "port="])
    except getopt.GetoptError:
        print("test.py -i <ipaddress> -p <port>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("test.py -i <ipaddress> -p <port>")
            sys.exit()
        elif opt in ("-i", "--ipaddress"):
            LISTEN_IP = arg
        elif opt in ("-p", "--port"):
            LISTEN_PORT = arg
    print('IP Address:', LISTEN_IP)
    print('Port:', LISTEN_PORT)


if __name__ == "__main__":
    main(sys.argv[1:])
