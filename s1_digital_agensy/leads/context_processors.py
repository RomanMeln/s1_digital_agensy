from .forms import ProjectStartForm

def project_forms(request):
    """Делает форму заявки доступной на всех страницах сайта"""
    return {
        'lead_form': ProjectStartForm()
    }
