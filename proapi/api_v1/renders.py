from django.utils.encoding import smart_text
from rest_framework import renderers
from .serializers import PAFSerialzier


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        #return data.encode(self.charset)
        return data


class TsvRenderer(renderers.BaseRenderer):
    media_type = 'text/tab-separated-values'
    format = 'tsv'

    def render(self, data, media_type=None, renderer_context=None):

        # TSV format:
        # Column Names first row
        # Tab separated per row
        # Using Fields defined in the ImageSerializer to create fields and add values

        tabbedData = ''
        #print(data)
        # Column names
        first = True
        for columnName in PAFSerialzier.Meta.fields:
            if first == True:
                tabbedData = '%s' %(columnName)
                first = False
            else:
                tabbedData = '%s\t%s' %(tabbedData,columnName)

        tabbedData = '%s\n' %tabbedData

        # Column values
        first = True
        for lineItem in data:

            for columnName in PAFSerialzier.Meta.fields:
                # print(lineItem)
                # print(columnName)
                if first == True:
                    tabbedData = '%s%s' %(tabbedData,lineItem[columnName])
                    first = False
                else:
                    tabbedData = '%s\t%s' %(tabbedData,lineItem[columnName])

            tabbedData = '%s\n' %tabbedData
            first = True

        return tabbedData
