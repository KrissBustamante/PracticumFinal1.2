from flask import Flask, render_template, request, redirect, url_for , jsonify , make_response
import pickle

app = Flask(__name__)
vector_bayes = pickle.load(open('Modelos/count_vector.sav', 'rb'))
modelo_bayes = pickle.load(open('Modelos/naive_bayes.sav', 'rb'))

modelo_KNN = pickle.load(open('Modelos/knn_modelo.sav', 'rb'))

vector_svm = pickle.load(open('Modelos/svm_count_vector.sav', 'rb'))
modelo_svm = pickle.load(open('Modelos/xvm_modelo.sav', 'rb'))
# desata la url  pagina raiz

@app.route('/', methods=["GET","POST"])
def main():
    # pickling the vectorizer

    m=''
    s=''
    if request.method == "POST":
        inp = request.form.get("inp")
        texto_bayes = vector_bayes.transform([inp])
        sentiment = modelo_bayes.predict(texto_bayes)

        if sentiment[0] == 'P':
            m = "Sentimiento Positivo 🙂🙂 "
        elif sentiment[0] == 'N':
            m = " Sentimiento Negativo 😔😔"
        elif sentiment[0] == 'NEU':
            m = "Sentimiento Neutro 😐😐"

        texto_svm = vector_bayes.transform([inp])
        sentiment = modelo_bayes.predict(texto_svm)   
        if sentiment[0] == 'P':
            s = "Sentimiento Positivo 🙂🙂 "
        elif sentiment[0] == 'N':
            s = " Sentimiento Negativo 😔😔"
        elif sentiment[0] == 'NEU':
            s = "Sentimiento Neutro 😐😐"
            

    return render_template  ('home.html', m = m, s= s)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
