import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server import util


def add_pet(body):  # noqa: E501
    """Add a new pet to the store.

    Add a new pet to the store. # noqa: E501

    :param pet: Create a new pet in the store
    :type pet: dict | bytes

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    pet = body
    if connexion.request.is_json:
        pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pet(pet_id, api_key=None):  # noqa: E501
    """Deletes a pet.

    Delete a pet. # noqa: E501

    :param pet_id: Pet id to delete
    :type pet_id: int
    :param api_key: 
    :type api_key: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pets_by_status(status=None):  # noqa: E501
    """Finds Pets by status.

    Multiple status values can be provided with comma separated strings. # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: Union[List[Pet], Tuple[List[Pet], int], Tuple[List[Pet], int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pets_by_tags(tags=None):  # noqa: E501
    """Finds Pets by tags.

    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: Union[List[Pet], Tuple[List[Pet], int], Tuple[List[Pet], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_pet_by_id(pet_id):  # noqa: E501
    """Find pet by ID.

    Returns a single pet. # noqa: E501

    :param pet_id: ID of pet to return
    :type pet_id: int

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_pet(body):  # noqa: E501
    """Update an existing pet.

    Update an existing pet by Id. # noqa: E501

    :param pet: Update an existent pet in the store
    :type pet: dict | bytes

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    pet = body
    if connexion.request.is_json:
        pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pet_with_form(pet_id, name=None, status=None):  # noqa: E501
    """Updates a pet in the store with form data.

    Updates a pet resource based on the form data. # noqa: E501

    :param pet_id: ID of pet that needs to be updated
    :type pet_id: int
    :param name: Name of pet that needs to be updated
    :type name: str
    :param status: Status of pet that needs to be updated
    :type status: str

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    return 'do some magic!'


def upload_file(pet_id, additional_metadata=None, body=None):  # noqa: E501
    """Uploads an image.

    Upload image of the pet. # noqa: E501

    :param pet_id: ID of pet to update
    :type pet_id: int
    :param additional_metadata: Additional Metadata
    :type additional_metadata: str
    :param body: 
    :type body: str

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    body = body
    return 'do some magic!'
