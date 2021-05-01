from flask import Flask
import pyautogui
ent=""" 

███████╗███╗   ██╗████████╗███████╗██████╗ 
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
███████╗██║ ╚████║   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                           
"""
app = Flask(__name__)
@app.route('/press')
def pressd():
    print(ent)
    pyautogui.press('enter')
    return ('', 204)

app.run(host="0.0.0.0", port=3000)
