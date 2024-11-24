# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        text_Top = request.form.get('textTop')

        text_Bottom = request.form.get('textBottom')        

        # Görev #3. Metnin konumunu almak
        textTop_y = request.form.get('textTop_y') 

        textBottom_y = request.form.get('textBottom_y') 

        textTop_x = request.form.get('textTop_x') 

        textBottom_x = request.form.get('textBottom_x') 
       
        # Görev #3. Metnin rengini almak
        reng = request.form.get('color-selector')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               text_Top = text_Top,
                               text_Bottom = text_Bottom,

                               # Görev #3. Rengi görüntüleme
                               reng = reng,
                               
                               # Görev #3. Metnin konumunu görüntüleme 
                               textTop_y = textTop_y,
                               textBottom_y = textBottom_y,
                               textTop_x = textTop_x,
                               textBottom_x = textBottom_x

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
