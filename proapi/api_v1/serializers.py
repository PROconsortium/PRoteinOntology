from rest_framework import serializers
from collections import OrderedDict

SEARCH_FIELD_CHOICES = [("All Field", "All Field"), ("Alternative ID", "Alternative ID"), ("Any relationship", "Any relationship"), ("Category", "Category"),
                        ("Child", "Child"), ("Comment", "Comment"), ("EcoCyc ID", "EcoCyc ID"),
                        ("Gene Name", "Gene Name"), ("HGNC ID", "HGNC ID"), ("PRO ID", "PRO ID"),
                        ("Interaction with", "Interaction with"), ("MGI ID", "MGI ID"), ("Modifier", "Modifier"),
                        ("Ontology ID", "Ontology ID"), ("Ontology term", "Ontology term"),
                        ("Ortho-isoform", "Ortho-isoform"), ("Ortho-modform", "Ortho-modform"),
                        ("Panther ID", "Panther ID"), ("Parent", "Parent"), ("PIRSF ID", "PIRSF ID"), ("PMID", "PMID"),
                        ("PRO term definition", "PRO term definition"), ("PRO name", "PRO name"), ("PRO namespace", "PRO namespace"),
                        ("PRO name synonyms", "PRO name synonyms"), ("Reactiome id", "Reactiome id"),
                        ("Relation", "Relation"), ("Taxon ID", "Taxon ID"), ("UniProKB ID", "UniProKB ID")]


class ErrorSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    message = serializers.CharField(required=False, allow_blank=True)

class EvidenceSerializer(serializers.Serializer):
    evidenceSource = serializers.ListField(required=False)
    evidenceCode = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        ret = super(EvidenceSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class SearchParameterSerializer(serializers.Serializer):
    searchField = serializers.CharField(default="All Field")
    searchValue = serializers.CharField(required=False, allow_blank=True,
                                   help_text="Search Value - Can be any string or 'null' or 'not null'")
    showAltID = serializers.BooleanField(default=True)
    showPROName = serializers.BooleanField(default=True)
    showPRONamespace = serializers.BooleanField(default=True)
    showPROTermDefinition = serializers.BooleanField(default=True)
    showCategory = serializers.BooleanField(default=True)
    showParent = serializers.BooleanField(default=True)
    showAncestor = serializers.BooleanField(default=False)
    showAnnotation = serializers.BooleanField(default=False)
    showAnyRelationship = serializers.BooleanField(default=False)
    showChild = serializers.BooleanField(default=False)
    showDescendant = serializers.BooleanField(default=False)
    showComment = serializers.BooleanField(default=False)
    showEcoCycID = serializers.BooleanField(default=False)
    showGeneName = serializers.BooleanField(default=False)
    showHGNCID = serializers.BooleanField(default=False)
    showMGIID = serializers.BooleanField(default=False)
    showOrthoIsoform = serializers.BooleanField(default=False)
    showOrthoModform = serializers.BooleanField(default=False)
    showPANTHERID = serializers.BooleanField(default=False)
    showPIRSFID = serializers.BooleanField(default=False)
    showPMID = serializers.BooleanField(default=False)
    showReactomeID = serializers.BooleanField(default=False)
    showSynonym = serializers.BooleanField(default=False)
    showUniProtKBID = serializers.BooleanField(default=False)
    offset = serializers.IntegerField(default=0,
                                 help_text="The number of items to skip before starting to collect the result set.")
    limit = serializers.IntegerField(default=50, help_text="The numbers of items to return.")


class AnnotationSerialzier(serializers.Serializer):
    modifier = serializers.CharField(required=False, allow_blank=True)
    relation = serializers.CharField(required=False, allow_blank=True)
    ontologyID = serializers.CharField(required=False, allow_blank=True)
    ontologyTerm = serializers.CharField(required=False, allow_blank=True)
    relativeTo = serializers.CharField(required=False, allow_blank=True)
    interactionWith = serializers.CharField(required=False, allow_blank=True)
    evidence = EvidenceSerializer(required=False)
    ncbiTaxonId = serializers.CharField(required=False, allow_blank=True)
    inferredFrom = serializers.ListField(required=False)

    class Meta(object):
        fields = ('modifier', 'relation', 'ontologyID', 'ontologyTerm', 'relativeTo', 'interactionWith',
                  'evidence', 'ncbiTaxonID', 'inferredFrom')
        fields_order = ['modifier', 'relation', 'ontologyID', 'ontologyTerm', 'relativeTo', 'interactionWith',
                  'evidence', 'ncbiTaxonID', 'inferredFrom']

    def to_representation(self, instance):
        ret = super(AnnotationSerialzier, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PAFSerialzier(serializers.Serializer):
    PRO_ID = serializers.CharField(required=True)
    Object_term = serializers.CharField(required=False, allow_blank=True)
    Object_syny = serializers.CharField(required=False, allow_blank=True)
    Modifier = serializers.CharField(required=False, allow_blank=True)
    Relation = serializers.CharField(required=False, allow_blank=True)
    Ontology_ID = serializers.CharField(required=False, allow_blank=True)
    Ontology_term = serializers.CharField(required=False, allow_blank=True)
    Relative_to = serializers.CharField(required=False, allow_blank=True)
    Interaction_with = serializers.CharField(required=False, allow_blank=True)
    Evidence_source = serializers.CharField(required=False, allow_blank=True)
    Evidence_code = serializers.CharField(required=False, allow_blank=True)
    Taxon = serializers.CharField(required=False, allow_blank=True)
    Inferred_from = serializers.CharField(required=False, allow_blank=True)
    DB_ID = serializers.CharField(required=False, allow_blank=True)
    Date = serializers.CharField(required=False, allow_blank=True)
    Assigned_by = serializers.CharField(required=False, allow_blank=True)
    Comment = serializers.CharField(required=False, allow_blank=True)

    class Meta(object):
        fields = ('PRO_ID', 'Object_term', 'Object_syny', "Modifier", "Relation",
                  "Ontology_ID", "Ontology_term", "Relative_to", "Interaction_with",
                  "Evidence_source", "Evidence_code", "Taxon", "Inferred_from", "DB_ID",
                  "Date", "Assigned_by", "Comment")
        fields_order = ['PRO_ID', 'Object_term', 'Object_syny', "Modifier", "Relation",
                  "Ontology_ID", "Ontology_term", "Relative_to", "Interaction_with",
                  "Evidence_source", "Evidence_code", "Taxon", "Inferred_from", "DB_ID",
                  "Date", "Assigned_by", "Comment"]

    # def to_representation(self, instance):
    #     ret = super(PAFSerialzier, self).to_representation(instance)
    #     ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
    #     return ret

class PROTermSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, allow_blank=True)
    alt_id = serializers.CharField(required=True, allow_blank=True)
    name = serializers.CharField(required=False, allow_blank=True)
    namespace = serializers.CharField(required=False, allow_blank=True)
    termDef = serializers.CharField(required=False, allow_blank=True)
    category = serializers.CharField(required=False, allow_blank=True)
    ancestor = serializers.ListField(required=False)
    annotation = AnnotationSerialzier(required=False, many=True)
    anyRelationship = serializers.CharField(required=False, allow_blank=True)
    child = serializers.ListField(required=False)
    comment = serializers.CharField(required=False, allow_blank=True)
    descendant = serializers.ListField(required=False)
    ecoCycID = serializers.CharField(required=False, allow_blank=True)
    geneName = serializers.CharField(required=False, allow_blank=True)
    hgncID = serializers.ListField(required=False)
    mgiID = serializers.ListField(required=False)
    orthoIsoform = serializers.ListField(required=False)
    orthoModform = serializers.ListField( required=False)
    pantherID = serializers.CharField(required=False, allow_blank=True)
    parent = serializers.ListField(required=False)
    pirsfID = serializers.CharField(required=False, allow_blank=True)
    pmID = serializers.ListField(required=False)
    reactomeID = serializers.ListField(required=False)
    synonym = serializers.CharField(required=False)
    taxonID = serializers.CharField(required=False)
    uniprotKBID = serializers.ListField(required=False)

    class Meta(object):
        fields = ('id', 'alt_id', 'name', 'namespace', 'termDef', 'category', 'ancestor', 'annotation', 'anyRelationship'
        ,'child', 'comment', 'descendant', 'ecoCycID', 'geneName', 'hgncID', 'mgiID', 'orthoIsoform',
        'orthoModform', 'pantherID', 'parent', 'pirsfID', 'pmID', 'reactomeID', 'synonym', 'taxonID', 'uniprotKBID')
        fields_order = ['id', 'alt_id', 'name', 'namespace', 'termDef', 'category', 'ancestor', 'annotation', 'anyRelationship'
                  , 'child', 'comment', 'descendant', 'ecoCycID', 'geneName', 'hgncID', 'mgiID', 'orthoIsoform',
                  'orthoModform', 'pantherID', 'parent', 'pirsfID', 'pmID', 'reactomeID', 'synonym', 'taxonID',
                  'uniprotKBID']


    def to_representation(self, instance):
        ret = super(PROTermSerializer, self).to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PROHierarchySerializer(serializers.Serializer):
    pro = PROTermSerializer(required=True)
    pro_parent = PROTermSerializer(required=True)

    class Meta(object):
        fields = ('pro', 'pro_parent')
        fields_order = ['pro', 'pro_parent']

    def to_representation(self, instance):
        ret = super(PROHierarchySerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PROParentSerializer(serializers.Serializer):
    pro = PROTermSerializer(required=True)
    pro_parent = PROTermSerializer(required=True)

    class Meta(object):
        fields = ('pro', 'pro_parent')
        fields_order = ['pro', 'pro_parent']

    def to_representation(self, instance):
        ret = super(PROParentSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PROAncestorSerializer(serializers.Serializer):
    pro = PROTermSerializer(required=True)
    pro_ancestor = PROTermSerializer(required=True)

    class Meta(object):
        fields = ('pro', 'pro_ancestor')
        fields_order = ['pro', 'pro_ancestor']

    def to_representation(self, instance):
        ret = super(PROAncestorSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PROChildrenSerializer(serializers.Serializer):
    pro = PROTermSerializer(required=True)
    pro_children = PROTermSerializer(required=True)

    class Meta(object):
        fields = ('pro', 'pro_children')
        fields_order = ['pro', 'pro_children']

    def to_representation(self, instance):
        ret = super(PROChildrenSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PRODescendantSerializer(serializers.Serializer):
    pro = PROTermSerializer(required=True)
    pro_descendant = PROTermSerializer(required=True)

    class Meta(object):
        fields = ('pro', 'pro_descendant')
        fields_order = ['pro', 'pro_descendant']

    def to_representation(self, instance):
        ret = super(PRODescendantSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret
