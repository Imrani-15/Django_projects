from django.utils.deprecation import MiddlewareMixin

class ExecutionFlowMiddleware(MiddlewareMixin):
    def __int__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("This line printed at pre processing of request")
        response = self.get_response(request)
        print('This line printed at post processing of request')
        return response


