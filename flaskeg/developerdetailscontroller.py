from flaskeg.datastore import get_developer, save_developer, new_developer
from flaskeg.authentication import EDIT_USER_PERMISSION
from flask import render_template, request, redirect
from flask.views import MethodView

class DeveloperDetailsController(MethodView):
    "Developer Details Controller"

    def get(self):
        "Respond to GET request by sending developer details"
        developer_name = request.args.get('name')
        print("Displaying {}".format(developer_name))
        if developer_name:
            developer = get_developer(developer_name)
        else:
            developer = new_developer()
        return render_template('developer.html', developer=developer)


    @EDIT_USER_PERMISSION.require()
    def post(self):
        "Response to POST request by saving the details passed"
        print("Saving {}".format(request.form))
        if request.form.get('Save'):
            save_developer({'name': request.form.get('name'),
                            'cell': request.form.get('cell'),
                            'favouritefruit': request.form.get('favouritefruit')})
        return redirect('/')
