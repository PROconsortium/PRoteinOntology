from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from .renders import PlainTextRenderer, TsvRenderer

from .apimodels import SearchParameter
from .serializers import SearchParameterSerializer, ErrorSerializer, PROTermSerializer,\
    AnnotationSerialzier, PAFSerialzier, PROHierarchySerializer, PROParentSerializer, PROChildrenSerializer, PROAncestorSerializer, PRODescendantSerializer
from .sparql import SparqlSearch

@api_view(['GET'])
@renderer_classes((PlainTextRenderer,))
#@permission_classes((permissions.AllowAny,))
def getOBOByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchField = "OBO"
    searchParameter.searchValue = proIds
    return searchAndRenderResponse(searchParameter, "OBO")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getParentByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchField = "PARENT"
    searchParameter.searchValue = proIds
    searchParameter.showParent = True
    return searchAndRenderResponse(searchParameter, "PARENT")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getAncestorByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchField = "ANCESTOR"
    searchParameter.searchValue = proIds
    searchParameter.showAncestor = True
    return searchAndRenderResponse(searchParameter, "ANCESTOR")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getChildrenByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchField = "CHILDREN"
    searchParameter.searchValue = proIds
    searchParameter.showChild = True
    return searchAndRenderResponse(searchParameter, "CHILDREN")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getDescendantByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchValue = proIds
    searchParameter.searchField ="DESCENDANT"
    searchParameter.showDescendant = True
    return searchAndRenderResponse(searchParameter, "DESCENDANT")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
def getHierarchyByID(request, proId):
    searchParameter = getSearchParameter(request)
    searchParameter.searchValue = proId
    searchParameter.searchField ="HIERARCHY"
    #searchParameter.showDescendant = True
    return searchAndRenderResponse(searchParameter, "HIERARCHY")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer,TsvRenderer))
#@permission_classes((permissions.AllowAny,))
def getPAFByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.showAnnotation = True
    searchParameter.searchValue = proIds
    return searchAndRenderResponse(searchParameter, "PAF")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getUniProtKBIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showUniProtKBID = True
    return searchAndRenderResponse(searchParameter, "UNIPROTKB_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getNCBITaxonIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showTaxonID = True
    return searchAndRenderResponse(searchParameter, "TAXON_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getReactomeIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showReactomeID = True
    return searchAndRenderResponse(searchParameter, "REACTOME_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getPMIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showPMID = True
    return searchAndRenderResponse(searchParameter, "PMID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getPIRSFIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showPIRSFID = True
    return searchAndRenderResponse(searchParameter, "PIRSF_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getPANTHERIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showPANTHERID = True
    return searchAndRenderResponse(searchParameter, "PANTHER_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getOntologyIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showAnnotation = True
    return searchAndRenderResponse(searchParameter, "ONTOLOGY_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getMGIIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showMGIID = True
    return searchAndRenderResponse(searchParameter, "MGI_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getHGNCIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showHGNCID = True
    return searchAndRenderResponse(searchParameter, "HGNC_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getEcoCycIDs(request):
    searchParameter = getSearchParameter(request)
    searchParameter.showEcoCycID = True
    return searchAndRenderResponse(searchParameter, "ECOCYC_ID")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getSpeciesSpecificComplexForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ORGANISM_COMPLEX")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getSpeciesNonSpecificComplexForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "COMPLEX")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getOrganismGeneForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ORGANISM_GENE")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getGeneForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "GENE")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getFamilyForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "FAMILY")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getOrganismSequenceForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ORGANISM_SEQUENCE")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getSequenceForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "SEQUENCE")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getOrthoIsoForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ORTHO_ISOFORM")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getOrthoModForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ORTHO_MODFORM")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getGlycosylatedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "GLYCOSYLATED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getUbiquitinatedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "UBIQUITINATED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getAcetylatedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ACETYLATED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getMethylatedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "METHYLATED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getPhosphorylatedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "PHOSPHORYLATED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getAllModifiedForms(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "ALL_MODIFIED_FORMS")

@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def getPROByIDs(request, proIds):
    searchParameter = getSearchParameter(request)
    searchParameter.searchField = "PRO_ID"
    searchParameter.searchValue = proIds
    return searchAndRenderResponse(searchParameter, "PRO_ID")


def searchAndRenderResponse(searchParameter, restriction):
    sparqlSearch = SparqlSearch()
    if restriction == "PAF":
        pafs, error = sparqlSearch.pafSearch(searchParameter)
        if error == None:
            serializer = PAFSerialzier(pafs, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    elif restriction == "OBO":
        obos, error = sparqlSearch.oboSearch(searchParameter)
        if error == None:
            serializer = PlainTextRenderer()
        else:
            serializer = ErrorSerializer(error)
        #return Response(serializer.render(obos))
        return Response(serializer.render(obos))

    elif restriction == "HIERARCHY":
        hiearchy, error = sparqlSearch.proHierarchy(searchParameter)
        if error == None:
            serializer = PROHierarchySerializer(hiearchy, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    # PARENT
    elif restriction == "PARENT":
        parent, error = sparqlSearch.proParent(searchParameter)
        if error == None:
            serializer = PROParentSerializer(parent, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    elif restriction == "ANCESTOR":
        parent, error = sparqlSearch.proAncestor(searchParameter)
        if error == None:
            serializer = PROAncestorSerializer(parent, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    elif restriction == "CHILDREN":
        parent, error = sparqlSearch.proChildren(searchParameter)
        if error == None:
            serializer = PROChildrenSerializer(parent, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    elif restriction == "DESCENDANT":
        parent, error = sparqlSearch.proDescendant(searchParameter)
        #print(parent)
        if error == None:
            serializer = PRODescendantSerializer(parent, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)
    else:
        proTerms, error = sparqlSearch.proSearch(searchParameter, restriction)
        #print(proTerms[0])
        if error == None:
            serializer = PROTermSerializer(proTerms, many=True)
        else:
            serializer = ErrorSerializer(error)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes((JSONRenderer,XMLRenderer))
#@permission_classes((permissions.AllowAny,))
def proSearch(request):
    searchParameter = getSearchParameter(request)
    return searchAndRenderResponse(searchParameter, "PRO_ID")

def getSearchParameter(request):
    searchParameter = SearchParameter()
    #print(searchParameter)
    # print("????")
    if request.GET.get('searchField'):
        searchParameter.searchField = request.GET.get('searchField')
    if request.GET.get('searchValue'):
        searchParameter.searchValue = request.GET.get('searchValue')
    if request.GET.get('showAltID') == 'true':
        searchParameter.showAltID = True
    if request.GET.get('showAnnotation') == 'true':
        searchParameter.showAnnotation = True
    if request.GET.get('showAnyRelationship') == 'true':
        searchParameter.showAnyRelationship = True
    else:
        searchParameter.showAnyRelationship = False
    if request.GET.get('showCategory') == 'true':
        searchParameter.showCategory = True
    else:
        searchParameter.showCategory = False
    if request.GET.get('showChild') == 'true':
        searchParameter.showChild = True
    else:
        searchParameter.showChild = False
    if request.GET.get('showComment') == 'true':
        searchParameter.showComment = True
    else:
        searchParameter.showComment = False
    if request.GET.get('showEcoCycID') == 'true':
        searchParameter.showEcoCycID = True
    else:
        searchParameter.showEcoCycID = False
    if request.GET.get('showGeneName') == 'true':
        searchParameter.showGeneName = True
    else:
        searchParameter.showGeneName = False
    if request.GET.get('showHGNCID') == 'true':
        searchParameter.showHGNCID = True
    else:
        searchParameter.showHGNCID = False
    if request.GET.get('showMGIID') == 'true':
        searchParameter.showMGIID = True
    else:
        searchParameter.showMGIID = False
    if request.GET.get('showOrthoIsoform') == 'true':
        searchParameter.showOrthoIsoform = True
    else:
        searchParameter.showOrthoIsoform = False
    if request.GET.get('showOrthoModifiedForm') == 'true':
        searchParameter.showOrthoModifiedForm = True
    else:
        searchParameter.showOrthoModifiedForm = False
    if request.GET.get('showPANTHERID') == 'true':
        searchParameter.showPANTHERID = True
    else:
        searchParameter.showPANTHERID = False
    if request.GET.get('showPIRSFID') == 'true':
        searchParameter.showPIRSFID = True
    else:
        searchParameter.showPIRSFID = False
    if request.GET.get('showPMID') == 'true':
        searchParameter.showPMID = True
    else:
        searchParameter.showPMID = False
    if request.GET.get('showPROName') == 'true':
        searchParameter.showPROName = True
    else:
        searchParameter.showPROName = False
    if request.GET.get('showPRONamespace') == 'true':
        searchParameter.showPRONamespace = True
    else:
        searchParameter.showPRONamespace = False
    if request.GET.get('showPROTermDefinition') == 'true':
        searchParameter.showPROTermDefinition = True
    else:
        searchParameter.showPROTermDefinition = False
    if request.GET.get('showParent') == 'true':
        searchParameter.showParent = True
    else:
        searchParameter.showParent = False
    if request.GET.get('showReactomeID') == 'true':
        searchParameter.showReactomeID = True
    else:
        searchParameter.showReactomeID = False
    if request.GET.get('showSynonym') == 'true':
        searchParameter.showSynonym = True
    else:
        searchParameter.showSynonym = False
    if request.GET.get('showTaxonID') == 'true':
        searchParameter.showTaxonID = True
    else:
        searchParameter.showTaxonID = False
    if request.GET.get('showUniProtKBID') == 'true':
        searchParameter.showUniProtKBID = True
    else:
        searchParameter.showUniProtKBID = False
    #print(searchParameter)
    if searchParameter.searchField == "Interaction_with":
        searchParameter.showAnnotation = True
    else:
        searchParameter.showAnnotation = False
    if searchParameter.searchField == "Modifier":
        searchParameter.showAnnotation = True
    else:
        searchParameter.showAnnotation = False
    if searchParameter.searchField == "Ontology_ID":
        searchParameter.showAnnotation = True
    else:
        searchParameter.showAnnotation = False
    if searchParameter.searchField == "Ontology_term":
        searchParameter.showAnnotation = True
    else:
        searchParameter.showAnnotation = False
    if searchParameter.searchField == "Taxon_ID":
       searchParameter.showAnnotation = True

    # print(request)
    # if request.type == "text/turtle":
    #     ttl1="https://sparql.proconsortium.org/virtuoso/sparql?default-graph-uri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2Fpr&query=describe+%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F"
    #     ttl2="%3E&format=text%2Fturtle&timeout=0&debug=on"
    #     ttlUrl = ttl1+new_id.replace(':', '_')+ttl2
    #     return redirect(ttlUrl)
    # elif request.type == "application/rdf+xml":
    #     xml1 = "https://sparql.proconsortium.org/virtuoso/sparql?default-graph-uri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2Fpr&query=describe+%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F"
    #     xml2 = "%3E&format=application%2Frdf%2Bxml&timeout=0&debug=on"
    #     xmlUrl = xml1 + new_id.replace(':', '_') + xml2
    #     return redirect(xmlUrl)
    # else:
    #     pass
    return searchParameter
