#------------  Relative path to namespaces
import os
import sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/sources")


#------------  Tap into required namespaces 
import unittest
import json
import time
import xmlrunner
from http_request import *
from http_response import *
from http_methods import *


class TestDisney_API(unittest.TestCase):


    def setUp(self):

        # Load json data file
        with open(PARAM_FILE) as file:
            self.payloads = json.load(file)



    def test_verify_new_post_by_id(self):
        

        # Signup
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        payload_signup = {'username': self.payloads['username'] + time_stamp, 'name': self.payloads['name'], 'password': self.payloads['password']}
        postSignup = post_method(HTTP_PROTOCOL + BASE_URL + PORT + SIGNUP_URL, data=payload_signup)        
        # Login
        payload_login = {'username': self.payloads['username'] + time_stamp, 'password': self.payloads['password']}
        login_post = post_method(HTTP_PROTOCOL + BASE_URL + PORT + LOGIN_URL, data=payload_login)
        # Create new post
        payload_new_post = {'author': self.payloads['author'], 'title': self.payloads['title'], 'body': self.payloads['body']}
        create_post = post_method(HTTP_PROTOCOL + BASE_URL + PORT + POST_NEW_BLOG_URL , data=payload_new_post)    
        # Assert new post id is in response body
        fetch_post_id = get_method(HTTP_PROTOCOL + BASE_URL + PORT + GET_BLOG_URL + create_post.json()['author'] + "?limit=" + self.payloads['limit'])
        self.assertIn(str(create_post.json()["id"]),fetch_post_id.text)     





    def test_delete_new_post_by_id(self):

        # Signup
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        payload_signup = {'username': self.payloads['username'] + time_stamp, 'name': self.payloads['name'], 'password': self.payloads['password']}
        postSignup = post_method(HTTP_PROTOCOL + BASE_URL + PORT + SIGNUP_URL, data=payload_signup)        
        # Login
        payload_login = {'username': self.payloads['username'] + time_stamp, 'password': self.payloads['password']}
        login_post = post_method(HTTP_PROTOCOL + BASE_URL + PORT + LOGIN_URL, data=payload_login)
        # Create new post
        payload_new_post = {'author': self.payloads['author'], 'title': self.payloads['title'], 'body': self.payloads['body']}
        create_post = post_method(HTTP_PROTOCOL + BASE_URL + PORT + POST_NEW_BLOG_URL , data=payload_new_post)
        # Delete new post
        delete_post_id = post_method(HTTP_PROTOCOL + BASE_URL + PORT + GET_BLOG_URL + create_post.json()['author'] + "/" + str(create_post.json()["id"]) + "/delete")
        fetch_post_id = get_method(HTTP_PROTOCOL + BASE_URL + PORT + GET_BLOG_URL + create_post.json()['author'] + "?limit=" + self.payloads['limit'])
        # Assert deleted post is no longer in thge posts list 
        self.assertNotIn(str(create_post.json()["id"]),fetch_post_id.text)


        

    def test_verify_cannot_have_duplicate_username(self):

        # Signup once
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        payload = {'username': self.payloads['username'] + time_stamp, 'name': self.payloads['name'], 'password': self.payloads['password']}
        signup_once = post_method(HTTP_PROTOCOL + BASE_URL + PORT + SIGNUP_URL, data=payload)
        # Signup twice
        payload = {'username': self.payloads['username'] + time_stamp, 'name': self.payloads['name'], 'password': self.payloads['password']}
        signup_twice = post_method(HTTP_PROTOCOL + BASE_URL + PORT + SIGNUP_URL, data=payload)
        self.assertEqual(str(signup_twice.text), "Username is already taken")

        

        
        
if __name__ == "__main__":
    # Output all the test results in a xml file
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDisney_API)
    time_stamp = time.strftime("%Y%m%d-%H%M%S")
    try:
        with open('test_report_' + time_stamp + '.xml', 'w') as output:
            xmlrunner.XMLTestRunner(output=output, verbosity=2).run(suite)
    except KeyboardInterrupt: # Stop running by pressing Ctrl + C
            print ('Tests stopped.')



