 @flaskapp.route("/log_injections")
 def log_injections():
     data = request.args.get("data")
     logging.debug(data)
     return jsonify(data="Log injection vulnerability"), 200


 @flaskapp.route("/config/")
 def config():
     try:
         command = "cat prod.config.yaml"
         data = subprocess.check_output(command, shell=True) 
         return data
     except:
         return jsonify(data="Command didn't run"), 200


 @flaskapp.route("/read-bad-file")
 def read_bad_file():
     file = request.args.get("file")
     with open(file, "r") as f:
         data = f.read()
     logging.debug(data)
     return jsonify(data="Uncontrolled data use in path expression"), 200


 @flaskapp.route("/hello")
 def hello():
     if request.args.get("name"):
         name = request.args.get("name")
         template = f"""<div><h1>Hello</h1>{name}</div>"""
         logging.debug(str(template))
         return render_template_string(template)


  @flaskapp.route("/get_users")
 def get_users():
     try:
         hostname = request.args.get("hostname")
         command = "dig " + hostname
         data = subprocess.check_output(command, shell=True) 
         return data
     except:
         data = str(hostname) + " username not found"
         return data
