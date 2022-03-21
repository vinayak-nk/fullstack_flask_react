import unittest
from app import create_app
from config import TestConfig
from exts import db

class APITestCase(unittest.TestCase):
  def setUp(self):
    self.app=create_app(TestConfig)
    self.client=self.app.test_client(self)
    
    with self.app.app_context():
      db.init_app(self.app)
      db.create_all()
  
  def test_hello(self):
    hello_response = self.client.get('/api/hello')
    json_data = hello_response.json
    
    self.assertEqual(json_data, { "msg": "hellowwwwww" })
    
  def test_signup(self):
    signup_response = self.client.post(
      '/auth/signup',
      json={
        "username":"test",
        "email":"test@test.com",
        "password":"password"
      }
    )    
    status_code = signup_response.status_code
    self.assertEqual(status_code, 201)
  
  def test_login(self):
    signup_response = self.client.post(
      '/auth/signup',
      json={
        "username":"test",
        "email":"test@test.com",
        "password":"password"
      }
    )    
    login_response = self.client.post(
      '/auth/login',
      json={
        "username":"test",
        "password":"password"
      }
    )    
    status_code = login_response.status_code
    self.assertEqual(status_code, 200)    
  
  def tearDown(self):
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == '__main__':
  unittest.main()