from flask import Flask, render_template, request
from PIL import Image
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
        
    if request.method == 'POST':
        img = request.files['img']
        options = request.form['options']
        
        if  img and (options != 'escolha'):
            im = Image.open(img)
            
            if options == 'png':
                im.save(str(datetime.now()) + ".png", 'PNG' )
            elif options == 'jpg':
                im.save(str(datetime.now()) + ".jpg", 'JPG' )
            elif options == 'jpeg':
                im.save(str(datetime.now()) + ".jpeg", 'JPEG' )
            else:
                msg = 'invalid format'
                return render_template('index.html', msg=msg)
            
            success = "successfully converted"
            return render_template('index.html', success=success)
        
        msg = 'choose image and format'
        return render_template('index.html', msg=msg)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

