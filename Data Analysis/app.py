from flask import Flask, render_template
import vendor_show,user_show
app=Flask(__name__)

@app.route('/vendor')
def vendor():
   return render_template('v.html')

@app.route('/buyer')
def buyer():
   return render_template('u.html')
    
    
if __name__=="__main__":
    app.run(port="1818",debug=True)