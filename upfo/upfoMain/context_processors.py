import settings
# The context processor function
def app_id(request):
    app_id = settings.FACEBOOK_APP_ID

    return {
        'APP_ID': app_id,
    }