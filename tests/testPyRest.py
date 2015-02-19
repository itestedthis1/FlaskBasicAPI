import requests
import json
import pytest


response = requests.get('http://localhost:5000/todo/api/v1.0/tasks', auth=('miguel','python'))
data = response.json()
print data['tasks'][0]
print data['tasks'][0]['uri']



def test_first_elem():
	assert data['tasks'][0] == {u'uri': u'/todo/api/v1.0/tasks/1', u'done': False, u'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', u'title': u'Buy groceries'}


def test_uri1():
	assert data['tasks'][1]['uri'] == '/todo/api/v1.0/tasks/2'