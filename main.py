from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)

# Speichert die Formulardaten in einer Textdatei
def save_to_file(name, email, company):
    file_path = 'form.txt'  # Pfad zur Datei, in der die Daten gespeichert werden
    with open(file_path, 'a') as f:
        f.write(name + '\n')
        f.write(email + '\n')
        f.write(company + '\n')  # Hier wird der Unternehmensname gespeichert

# Hauptroute für die Seite
@app.route('/', methods=['GET', 'POST'])
def index():
    name = email = company = ''
    button_python = button_telegram = button_scratch = button_unity = ''

    # Wenn die Anfrage eine POST-Anfrage ist
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')  # Hier wird der Unternehmensname verarbeitet

        # Speichern der Daten in der Textdatei
        save_to_file(name, email, company)

        # Dynamische Werte für Skills
        button_python = request.form.get('button_python')
        button_telegram = request.form.get('button_telegram')
        button_scratch = request.form.get('button_scratch')
        button_unity = request.form.get('button_unity')

        # Weiterleitung zur gleichen Seite mit den Formulardaten
        return render_template('index.html', 
                               name=name,
                               email=email,
                               company=company,
                               button_python=button_python,
                               button_telegram=button_telegram,
                               button_scratch=button_scratch,
                               button_unity=button_unity)

    # Wenn die Anfrage eine GET-Anfrage ist
    return render_template('index.html')


# Route für das Formular
@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)