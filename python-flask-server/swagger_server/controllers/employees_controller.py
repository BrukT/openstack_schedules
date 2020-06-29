import connexion
import pprint
import openstack
import pprint
import json
import time

from swagger_server.models.employee import Employee  # noqa: E501
from swagger_server import util


def add_employee(body):  # noqa: E501
    """Add a new employee

     # noqa: E501

    :param body: Employee data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return "random"


def delete_employee(employeeId):  # noqa: E501
    """Deletes an employee

     # noqa: E501

    :param employeeId: Employee id to delete
    :type employeeId: int

    :rtype: None
    """
    return 'do some magic!'


def get_employee_by_id(employeeId):  # noqa: E501
    """Find employee by ID

    Returns a single employee # noqa: E501

    :param employeeId: ID of Employee to return
    :type employeeId: int

    :rtype: Employee

    print("request arrived")
    data = jsonify({
        "id": 0,
        "name": "bruk",
        "photoUrls": "http://mywebsite.org/mypic.jpg"
    })
    pprint.pprint(data)
    """
    conn = openstack.connect()
    print("Servers List:")
    servers = [server.to_dict() for server in conn.compute.servers()]
    for server in servers:
        pprint.pprint(server)
    return servers


def update_employee(body):  # noqa: E501
    """Update an existing employee

     # noqa: E501

    :param body: Employee object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_employee_with_form(employeeId, name=None, status=None):  # noqa: E501
    """Updates an employee in the store with form data

     # noqa: E501

    :param employeeId: ID of employe that needs to be updated
    :type employeeId: int
    :param name: Updated name of the employee
    :type name: str
    :param status: Updated status of the employee
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
