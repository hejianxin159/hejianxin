from fdfs_client.client import Fdfs_client
from django.core.files.storage import Storage

class FDFSStorage(Storage):
    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        #创建一个fdfs_client对象
        client = Fdfs_client('./fdfs/client.conf')
        res = client.upload_by_buffer(content.read())
        if res.get('Status') != 'Upload successed.':
            raise Exception('失败')
        print(res)
        filename = res.get('Remote file_id')
        return filename

    def exists(self, name):
        return False

    def url(self, name):
        return 'http://192.168.20.130:8888/' + name
