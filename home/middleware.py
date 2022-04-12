from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin


class BlackListMiddleware(MiddlewareMixin):
    # sayta girmek isteyen userlerim ip yaziriq
    # hansiki bu ipli user sie daxil ola bilmesin
    IP_BLACKLIST=[
        
        '127.0.0.5'
    
    ]

    def process_view(self, request, *args,  **kwargs):
        ip=request.META['REMOTE_ADDR']
        print(ip ,"my IP : ")
        if ip in self.IP_BLACKLIST:
            raise PermissionDenied()




# Bu funksiya onu yoxluyurki meta ya gelen ip 
# black liste  yoxdusa sayt ac  varsa erorr ver
# META - sayta gelen Ip 
# REMOTE_ADDR - REMOTE ADDRESS