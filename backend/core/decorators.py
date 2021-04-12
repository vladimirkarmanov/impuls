def login_not_required(view):
    view.login_exempt = True
    return view
