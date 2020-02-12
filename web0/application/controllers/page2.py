import web
import app
render = web.template.render('application/views/')
class Page2:
    def GET(self):
        data=[]
        data.append(0)
        data.append(0)
        data.append(0)
        return render.page2(data)
        
    def POST(self):
        formu=web.input()
        number1 = int(formu["number1"])
        number2 = int(formu["number2"])
        add= number1 + number2
        
        data=[]
        data.append(number1)
        data.append(number2)
        data.append(add)
        return  render.page2(data)
if __name__ == "__main__":
    web.config.debug= True
    app.run()