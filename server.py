#!/usr/bin/env python3.7

"""Simple two-method Python gRPC server."""

from concurrent import futures

import grpc

import demo_pb2_grpc
import demo_pb2

from constants import ADDRESS_BOOK_NAME, SERVER_ADDRESS


class DemoServer(demo_pb2_grpc.GRPCDemoServicer):

    def SimplePostMethod(self, request, context):
        """In a single call, the client can only send request once, and the
        server can only respond once."""
        print("SimplePostMethod request data:\n", request.request_data)
        got_person = request.request_data
        address_book = demo_pb2.AddressBook()

        try:
            # Read the existing address book.
            with open(ADDRESS_BOOK_NAME, "rb") as f:
                address_book.ParseFromString(f.read())
                print("\nCurrently stored data in "
                      "address book:\n", address_book)
        except IOError:
            print("Could not open {} file. File does not exist. "
                  "Creating a new one.".format(ADDRESS_BOOK_NAME))

        new_person = address_book.people.add()
        print("Adding ID:", new_person.id)
        new_person.id = got_person.id
        print("Adding name: ", new_person.name)
        new_person.name = got_person.name
        print("Adding email: ", new_person.email)
        new_person.email = got_person.email

        # Write updated address book back to disk.
        with open(ADDRESS_BOOK_NAME, "wb") as f:
            f.write(address_book.SerializeToString())
            print("Data has been written successfully.\n")

        return demo_pb2.StrResponse(
            response_data="Received data has been serialized successfully.")

    def SimpleGetMethod(self, request, context):
        """In a single call, the client can only send request once, and the
        server can only respond once."""
        print("SimpleGetMethod called by the message: ", request.request_data)
        # Read stored data.
        address_book = demo_pb2.AddressBook()
        # Read the existing address book.
        with open(ADDRESS_BOOK_NAME, "rb") as f:
            address_book.ParseFromString(f.read())

        print("Data have been read from a file:\n", address_book)

        return demo_pb2.Response(response_data=address_book)


def main():
    server = grpc.server(futures.ThreadPoolExecutor())
    demo_pb2_grpc.add_GRPCDemoServicer_to_server(DemoServer(), server)
    server.add_insecure_port(SERVER_ADDRESS)

    print("Starting Python gRPC server.")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
