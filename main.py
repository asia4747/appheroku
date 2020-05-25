from flask import Flask, render_template #render template  pozwala nam na wyświetlanie pliku html


aplikacja = Flask(__name__)
#@adnotacja
#app- nazwa naszej aplikacji
#route -metoda route(ścieżka)
@aplikacja.route("/")
def index():                    #tworzymy funkcję index(główną stronę- tak przyjęte ogólnie)
    return render_template("index.html")              #spraiwa, że wyświetli nam się napis "Witaj"

#www.przykładowa strona.pl/kontakt
@aplikacja.route("/kontakt")
def kontakt():
    return render_template("templates/kontakt.html")

@aplikacja.route("/o_nas")
def o_nas():
    return render_template("templates/index.html")

if __name__ == '__main__':     #konstrukcja warunkowa
    aplikacja.run()