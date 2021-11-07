
import html
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/hemlo', methods = ['POST', 'GET'])
def hemlo():
   name = ''
   if request.method == 'POST':
       name = '<p style="color:#ffc300;"><br>hello %s! :D<br><br>' %(request.form['name'])

   template = """
   <html>
      <style>
      p {text-align: center;}
      </style>
      <body style="background-color: #008080; background-image: url(/static/comf.gif); background-position: 12&percnt; 0&percnt;; background-repeat: no-repeat;">
         <form action = "/hemlo" method = "POST">
            <p><h1 style="color:#ffc300; text-align: center;">E P I C S T U F F . C O M</h1></p>
            <p><input type = 'text' name = 'name'/></p>
            <p><input type = 'submit' value = 'Submit'/></p>
         </form>
      %s
      </body>
   </html>
   """ %(name)
   return render_template_string(template)

