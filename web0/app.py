import web #pip instal web.py

urls = ( # Variables rutas 
    '/page0', 'application.controllers.page0.Page0',
    '/page1','application.controllers.page1.Page1',
    '/page2','application.controllers.page2.Page2',
    '/calculadora','application.controllers.calculadora.Calculadora'


)
app = web.application(urls, globals()) # Configura la aplicacion

render = web.template.render('/application/views/')

class Page0:
    def GET(self):
        name = "Kaplan"
        number = 10
        number1 = 15
        return render.page0(name, number, number1)

class Page1:
    def GET(self):
        data = []
        data.append("Carmen")
        data.append(10)
        data.append(15)
        return  render.page1(data)


class Page2:
    def GET(self):
        data = []
        data.append(0)
        data.append(0)
        data.append(0)
        return  render.page2(data)

class Calculadora:
    def GET(self):
        data = []
        data.append(0)
        data.append(0)
        data.append(0)
        return  render.calculadora(data)

    def POST(self):
        form = web.input()
        number1 = int(form["number1"])
        number2 = int(form["number2"])
        add = number1 + number2
        
        data = []
        data.append(number1)
        data.append(number2)
        data.append(add)

        return  render.calculadora(data)


if __name__ == "__main__":
    # web.config.debug = False
    app.run()