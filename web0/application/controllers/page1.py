import web
import app
render = web.template.render('application/views/')
class Page1:
    def GET(self):
        data=[]
        data.append("Carmen")
        data.append(10)
        data.append(15)
        return render.page1(data)

if __name__ == "__main__":
    web.config.debug= False
    app.run()