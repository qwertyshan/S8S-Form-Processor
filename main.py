#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):
    def post(self):
        sender_name = cgi.escape(self.request.get("name"), quote = True)
        sender_email = cgi.escape(self.request.get("email"), quote = True)
        sender_phone = cgi.escape(self.request.get("phone"), quote = True)
        sender_message = cgi.escape(self.request.get("message"), quote = True)
        email_subject = "Message from shruti8studio.com >> Name: "+sender_name+". Email: "+sender_email+". Phone: "+sender_phone
        email_body = email_subject+"\n\n"+sender_message
        mail.send_mail(sender="shruti8studio@appspot.gserviceaccount.com",
              to="shruti.film@gmail.com",
              subject=email_subject,
              body=email_body)
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.write("Message sent.")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
