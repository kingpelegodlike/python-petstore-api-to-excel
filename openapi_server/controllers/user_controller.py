import datetime
import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.reader.excel import ExcelReader


# Convert worksheet data to a list of dictionaries
def sheet_to_dict(sheet):
    data = []
    headers = [cell.value for cell in sheet[1]]  # First row as headers
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}
        for key, value in zip(headers, row):
            row_data[key] = value
        data.append(row_data)
    
    return data


def create_user(body=None):  # noqa: E501
    """Create user.

    This can only be done by the logged in user. # noqa: E501

    :param user: Created user object
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    # reader = ExcelReader("sample.xlsx")
    # reader.read()
    # wb = Workbook()
    # wb = reader.wb
    wb = load_workbook('sample.xlsx', read_only=False, data_only=False)

    # grab the active worksheet
    ws = wb.active
    
    # data_dict = sheet_to_dict(ws)
    # for row in data_dict:
    #     print(row)
    #     if row['ID'] == user.id:
    #         return Error('800', 'ID already exist')
    max_row = 2
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] == user.id:
            print("ID already exist")
            return Error('800', 'ID already exist')
        if row[0] is None:
            break
        print(row)
        max_row += 1
    print(f"Max row:{max_row}")

    # Data can be assigned directly to cells
    # ws['A3'] = user.id
    data = [user.id, user.username, user.first_name, user.email, datetime.datetime.now()]

    # Rows can also be appended
    # ws.append([user.username, user.first_name, user.email])
    # ws.append(data)
    for col_idx, cell_value in enumerate(data, start=1):
        print(f"Add col_idx:{col_idx}, cell_value:{cell_value}")
        ws.cell(row=max_row, column=col_idx, value=cell_value)

    # Python types will automatically be converted
    # ws['A4'] = datetime.datetime.now()

    # Save the file
    wb.save("sample.xlsx")
    return 'do some magic!'


def create_users_with_list_input(body=None):  # noqa: E501
    """Creates list of users with given input array.

    Creates list of users with given input array. # noqa: E501

    :param user: 
    :type user: list | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user resource.

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name.

    Get user detail based on username. # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing
    :type username: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def login_user(username=None, password=None):  # noqa: E501
    """Logs user into the system.

    Log into the system. # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session.

    Log user out of the system. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_user(username, body=None):  # noqa: E501
    """Update user resource.

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param user: Update an existent user in the store
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
