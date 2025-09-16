from flask import Flask , render_template_string
import datetime, socket

app = Flask(__name__)
@app.route("/")
def home():
    hostname = socket.gethostname()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_ip = socket.gethostbyname(hostname)
    html = """
   <html>
     <head>
       <title>Cupcake's Coffee Server</title>
       <style>
         body {
            background-color:#f5f5dc;
            font-family: 'Trebuchet MS' , sans-serif;
            color: #5c4033; text-align:center;
            margin: 0;
           padding: 0px;
         }
         .content {
              paddin-bottom: 100px;
         }
         h1 { font-size: 3em; margin-bottom:20px; }
         h2 { font-size: 24px; }
        .footer {
           position: fixed;
           bottom: 10px;
           width: 100%;
           text-align: center;
           font-size: 0.9em;
           color: #3e2723;
         }
         button {
           backgroud: brown;
           color: white;
           border: none;
           padding: 10px 20px;
           border-radius: 8px;
           font-size: 18px;
           margin-bottom: 20px;
           cursor: pointer;
         }
         button:hover { background: #4b2e2e; }
       </style>
     </head>
     <body>
       <div class="content">
         <h1> Cupcake's Coffee Server</h1>
         <img src= "  "coffee cup" width: 300px; border-radius: 20px; margin-top: 20px; ><br><br>
         <br>
         <button onclick="location.reload()"> Sip Again</button>
       </div>
       <div class="footer">
          <h2>Server: {{hostname}} | IP: {{server_ip}} | Time: {{server_time}}</h2>
       </div>
     </body>
   </html>
    """
    return render_template_string(html, hostname=hostname, server_ip=server_ip, server_time=server_time)
if __name__=="__main__":
   app.run(host="0.0.0.0", port=5001)
