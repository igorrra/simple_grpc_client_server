#!/usr/bin/env python3.7

"""Simple gRPC Python Client."""

import grpc

import demo_pb2_grpc
import demo_pb2

from constants import SERVER_ADDRESS


def simple_post_method(stub):
    print("Call SimplePostMethod Begin")

    address_book = demo_pb2.AddressBook()
    # Add an address.
    person = address_book.people.add()
    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")
    person.email = input("Enter email address: ")
    print("Data to save: ", person)

    request = demo_pb2.Request(request_data=person)
    response = stub.SimplePostMethod(request)
    print("Response from server:\n", response.response_data)
    print("Call SimplePostMethod End.\n")


def simple_get_method(stub):
    print("Call SimpleGetMethod Begin")
    request = demo_pb2.StrRequest(request_data="Get address book contents")
    response = stub.SimpleGetMethod(request)
    print("Response from server:\n", response.response_data)

    print("Parsed Address book:\n")
    for person in response.response_data.people:
        print("\tPerson ID:", person.id)
        print("\tPerson name: ", person.name)
        print("\tPerson email: ", person.email, "\n")

    print("Call SimpleGetMethod End")


def main():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = demo_pb2_grpc.GRPCDemoStub(channel)

        simple_post_method(stub)

        simple_get_method(stub)


if __name__ == '__main__':
    main()
