from molly.utils.views import BaseView
from molly.utils.breadcrumbs import Breadcrumb, BreadcrumbFactory, lazy_reverse

class IndexView(BaseView):
    
    def get_metadata(self, request):
        return {
            'title': self.conf.title,
            'additional': 'View the status of transit lines'
        }
        
    @BreadcrumbFactory
    def breadcrumb(self, request, context):
        return Breadcrumb('transit_status', None, self.conf.title,
                          lazy_reverse('index'))

    def initial_context(self, request):
        return {}

    def handle_GET(self, request, context):
        statuses = self.conf.provider.get_status()
        
        context.update({
            'title': self.conf.title,
            'statuses': statuses
        })
        return self.render(request, context, 'transit_status/index')