#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Swagger Petstore - OpenAPI 3.0'},
                pythonic_params=True)
    # app.add_api('openapi.json',
                # arguments={'title': 'Swagger Petstore - OpenAPI 3.0'},
                # pythonic_params=True)

    app.run(port=5000)


if __name__ == '__main__':
    main()
