# tests/test_app.py

import json
import pytest
from app import app, posts

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_create_post(client):
    post_data = {'username': 'user1', 'caption': 'Test caption'}
    response = client.post('/createpost', data=json.dumps(post_data), content_type='application/json')
    assert response.status_code == 200

def test_create_post_invalid_data(client):
    response = client.post('/createpost', data=json.dumps({'invalid': 'data'}), content_type='application/json')
    assert response.status_code == 400

def test_view_posts(client):
    response = client.get('/viewposts')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data['posts']) == len(posts)

def test_delete_post(client):
    post_data = {'username': 'user1', 'caption': 'Test caption'}
    response = client.post('/createpost', data=json.dumps(post_data), content_type='application/json')
    post_id = json.loads(response.data)['post_id']

    response = client.delete(f'/deletepost/{post_id}')
    assert response.status_code == 200
    assert len(posts) == 0

def test_delete_nonexistent_post(client):
    response = client.delete('/deletepost/999')
    assert response.status_code == 404
