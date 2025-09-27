def simple_middleware(get_response):
    def middleware(request):
        #This code gets passed beforre the view ecrt
        
        response = get_response(request)
        
        #This code gets passed after the view
        return response
    return middleware