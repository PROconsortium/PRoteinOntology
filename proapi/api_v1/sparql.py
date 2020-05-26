import csv
import requests
from .apimodels import Error, PROTerm, Annotation, Evidence, PAF, Parent, Ancestor, Decendant, Children
from itertools import chain
from collections import defaultdict

# SPARQL configuration class
class Config:

    def __init__(self):
        self.cfg = dict()
        self.graph = dict()
        self.where = dict()
        self.select = dict()
        self.where = dict()
        self.pafDSP = dict()
        self.pafQueryCondition = dict()
        self.oboQuerySelect = dict()
        self.oboQueryCondition = dict()


        self.cfg['logfile'] = '/data/chenc/pro/log/textsearch_sparql.log'
        self.cfg['sparql_endpoint'] = 'https://sparql.proconsortium.org/virtuoso/sparql?default-graph-uri='
        #self.cfg['format'] = '&format=text%2Ftab-separated-values&timeout=0&debug=on&quote=false'
        self.cfg['prefix'] = """
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX paf: <http://pir.georgetown.edu/pro/paf#>
PREFIX pr_extra: <https://proconsortium.org/pr_extra#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pr: <http://purl.obolibrary.org/obo/pr#>
"""

        self.graph['paf'] = '<http://pir.georgetown.edu/pro/paf>'
        self.graph['pro'] = '<http://purl.obolibrary.org/obo/pr>'
        self.graph['pro_extra'] = '<https://proconsortium.org/pr_extra>'


        self.where["ACETYLATED_FORMS"] = """
        {
            #?PRO_term oboInOwl:id ?PRO_ID .
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT,'(was)') && (CONTAINS(?Label, 'acetylated') || CONTAINS(?Label,'-acetylated')) && !CONTAINS(?Label, 'unacetylated'))
        }
        """

        self.where["ALL_MODIFIED_FORMS"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT, '(was)') && !CONTAINS(?Label, 'unmodified'))
        }
        """

        self.where['ANY_RELATIONSHIP'] = """
        {
            ?PRO_term  pr_extra:hasRelationshipWith ?AnyRelationship .
        }        
        """

        self.where['CATEGORY'] = """
        {
            ?PRO_term rdfs:comment ?Category .
            FILTER(CONTAINS(?Category, 'Category='))
        }       
        """

        self.where['CHILD'] = """
        {
            ?child rdfs:subClassOf ?PRO_term .
            ?child oboInOwl:id ?Child_ID .
        }       
        """

        self.where['CHILDREN'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            ?child rdfs:subClassOf ?PRO_term .
            ?child oboInOwl:id ?Child_ID .
        }       
        """

        self.where['DESCENDANT'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            ?descendant rdfs:subClassOf+ ?PRO_term .
            ?descendant oboInOwl:id ?Descendant_ID .
        }       
        """

        self.where['COMMENT'] = """
        {
            ?PRO_term rdfs:comment ?Comment .
        }      
        """

        self.where["COMPLEX"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='complex')
        }
        """
        self.where["ORGANISM_COMPLEX"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='organism-complex')
        }
        """

        self.where['DBREF'] = """
        {
            ?xdbref  oboInOwl:hasDbXref ?DbRef .
            ?xdbref a owl:Axiom .
            ?xdbref owl:annotatedProperty obo:IAO_0000115 .
            ?xdbref owl:annotatedSource ?PRO_term .
        }   
        """

        self.where['DB_ID'] = """
        {
            #?PRO_term  oboInOwl:hasDbXref ?DbRef .
            [ a                      owl:Axiom ;
  oboInOwl:hasDbXref     ?DbRef ;
  owl:annotatedProperty  obo:IAO_0000115 ;
  owl:annotatedSource    ?PRO_term ;
  owl:annotatedTarget    ?termDef
] .
        }   
        """

        self.where['ECOCYC_ID'] = """
        {
            ?PRO_term oboInOwl:hasDbXref ?EcoCycID .
            FILTER(STRSTARTS(STR(?EcoCycID),'EcoCyc:'))
        }   
        """

        self.where["FAMILY"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='family')
        }
        """
        self.where["GENE"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='gene')
        }
        """

        self.where["ORGANISM_GENE"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='organism-gene')
        }
        """

        self.where['GENE_NAME'] = """
        {
            ?PRO_term rdfs:subClassOf ?r .
            ?r owl:onProperty pr:has_gene_template .
            ?r owl:someValuesFrom ?gn_id .
            ?gn_id rdfs:label ?g
        }  
        """

        self.where["GLYCOSYLATED_FORMS"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT,'(was)') && (CONTAINS(?Label, 'glycosylated') || CONTAINS(?Label,'-glycosylated')) && !CONTAINS(?Label, 'unglycosylated'))
        }
        """

        self.where['HGNC_ID'] = """
        {
            ?PRO_term rdfs:subClassOf ?xhgnc .
            ?xhgnc owl:onProperty pr:has_gene_template.
            ?xhgnc owl:someValuesFrom ?h .
            ?h oboInOwl:id ?HGNC_ID .
            FILTER(STRSTARTS(STR(?HGNC_ID), 'HGNC:'))
        }
        """
        self.where['ID'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            FILTER(STRSTARTS(?PRO_ID, 'PR:')|| STRSTARTS(?PRO_ID, 'GO:'))
        }
        """
        self.where['INTERACTION_WITH'] = """
        {
            ?xinteractionwith a rdf:Statement .
            ?xinteractionwith rdf:subject ?PRO_term .
            ?xinteractionwith paf:interactionWith ?InteractionWith_PRO_term .
            ?InteractionWith_PRO_term oboInOwl:id ?InteractionWith .
        }
        """

        self.where["METHYLATED_FORMS"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT,'(was)') && (STRSTARTS(?Label, 'methylated') ||CONTAINS(?Label,' methylated ') || CONTAINS(?Label,'-methylated')) && !CONTAINS(?Label, 'unmethylated'))
        }
        """
        self.where['MGI_ID'] = """
        {
            ?PRO_term rdfs:subClassOf ?xmgi .
            ?xmgi owl:onProperty pr:has_gene_template .
            ?xmgi owl:someValuesFrom ?m .
            ?m oboInOwl:id ?MGI_ID .
            FILTER(STRSTARTS(STR(?MGI_ID), 'MGI:'))
        }
        """

        self.where['ONTOLOGY_ID'] = """
        {
            ?xoid a rdf:Statement .
            ?xoid rdf:subject ?PRO_term .
            ?xoid rdf:object [
                paf:ontologyID ?Ontology_ID ;
            ] .
        }
        """

        self.where['ONTOLOGY_TERM'] = """
        {
            ?xoid a rdf:Statement .
            ?xoid rdf:subject ?PRO_term .
            ?xoid rdf:object [
                paf:ontologyTerm ?Ontology_Term ;
            ] .
        }
        """
        self.where['ORTHO_ISOFORM'] = """
        {
            ?PRO_term pr_extra:hasOrthoIsoform ?Ortho_isoform .
            OPTIONAL {
                ?Ortho_isoform oboInOwl:id ?Ortho_isoform_ID .
            }
        }
        """
        self.where['ORTHO_MODFORM'] = """
        {
            ?PRO_term pr_extra:hasOrthoModifiedForm ?Ortho_modform .
            OPTIONAL {
                ?Ortho_modform oboInOwl:id ?Ortho_modform_ID .
            }
        }
        """

        self.where["PANTHER_ID"] = """
        {
            ?PRO_term  oboInOwl:hasDbXref ?PANTHER_ID .
            FILTER(STRSTARTS(STR(?PANTHER_ID),'PANTHER:'))
        }
        """

        self.where['PARENT'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            ?PRO_term rdfs:subClassOf ?parent .
            ?parent oboInOwl:id ?Parent_ID .
        }
        """
        self.where['PARENTS'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            ?PRO_term rdfs:subClassOf ?parent .
            ?parent oboInOwl:id ?Parent_ID .
            FILTER(STRSTARTS(STR(?Parent_ID), "PR:"))
        }
        """
        self.where['ANCESTOR'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            ?PRO_term rdfs:subClassOf+ ?ancestor .
            ?ancestor oboInOwl:id ?Ancestor_ID .
            FILTER(STRSTARTS(STR(?Ancestor_ID), "PR:"))
        }
        """

        self.where['PIRSF_ID'] = """
        {
            ?PRO_term  oboInOwl:hasDbXref ?PIRSF_ID .
            FILTER(STRSTARTS(STR(?PIRSF_ID),'PIRSF:'))
        }
        """
        self.where['PMID'] = """
        {
            ?xpmid  oboInOwl:hasDbXref ?PMID .
            ?xpmid a owl:Axiom .
            ?xpmid owl:annotatedProperty obo:IAO_0000115 .
            ?xpmid owl:annotatedSource ?PRO_term .
            FILTER(STRSTARTS(STR(?PMID),'PMID:'))
        }
        """

        self.where['PRO_TERM_DEFINITION'] = """
        {
            ?PRO_term obo:IAO_0000115 ?PRO_termDef .
        }
        """

        self.where['PRO_NAME'] = """
        {
            ?PRO_term rdfs:label ?Label .
        }
        """
        self.where['PRO_NAMESPACE'] = """
        {
            ?PRO_term oboInOwl:hasOBONamespace ?Namespace .
        }
        """
        self.where['ALT_ID'] = """
        {
            ?PRO_term oboInOwl:hasAlternativeId ?ALT_ID .
        }
        """

        self.where['PRO_NAME_SYNONYMS'] = """
        {
            {
                ?xsynonyms 
                    a owl:Axiom ;
                    owl:annotatedProperty oboInOwl:hasExactSynonym ;
                    owl:annotatedSource ?PRO_term ;
                    owl:annotatedTarget ?exactSyn .
                    OPTIONAL {?xsynonyms oboInOwl:hasSynonymType ?synonymType. }
                    OPTIONAL {?xsynonyms oboInOwl:hasDbXref ?dbxref .}
                    BIND(CONCAT('"', STR( ?exactSyn ),'"', ' EXACT ', strafter(str(?synonymType), '#'), ' [', ?dbxref, ']')  AS ?synonym) . 
            }   
            UNION {
                ?PRO_term oboInOwl:hasExactSynonym ?exactSyn .
                BIND(CONCAT('"', STR( ?exactSyn ),'"', ' EXACT')  AS ?synonym)  .
            }
            UNION {
                ?xxsynonyms 
                    a owl:Axiom ;
                    owl:annotatedProperty oboInOwl:hasRelatedSynonym ;
                    owl:annotatedSource ?PRO_term ;
                    owl:annotatedTarget ?relatedSyn .
                    OPTIONAL {?xxsynonyms oboInOwl:hasSynonymType ?synonymType. }
                    OPTIONAL {?xxsynonyms oboInOwl:hasDbXref ?dbxref .}
                    BIND(CONCAT('"', STR( ?relatedSyn ),'"', ' RELATED Gene-based ', '[', ?dbxref, ']')  AS ?synonym)  .
            }
            UNION {
                [ a                      owl:Axiom ;
                  oboInOwl:hasDbXref     ?dbxref ;
                  owl:annotatedProperty  oboInOwl:hasBroadSynonym ;
                  owl:annotatedSource    ?PRO_term ;
                  owl:annotatedTarget    ?broadSyn
                ] .
                BIND(CONCAT('"', STR( ?broadSyn ), '"', ' BROAD ', '[', ?dbxref, ']')  AS ?synonym)  .
            }
            UNION {
                          [ a    owl:Axiom ;
                          oboInOwl:hasDbXref       ?dbxref ;
                          oboInOwl:hasSynonymType  pr:Gene-based ;
                          owl:annotatedProperty    oboInOwl:hasNarrowSynonym ;
                          owl:annotatedSource      ?PRO_term ;
                          owl:annotatedTarget      ?narrowSyn
                        ] .
                    BIND(CONCAT('"', STR( ?narrowSyn ), '"', ' NARROW ', '[', ?dbxref, ']')  AS ?synonym)  .
            }
        }
        """
        self.where["PHOSPHORYLATED_FORMS"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT, '(was)') && (CONTAINS(?Label, 'phosphorylated') || CONTAINS(?Label, '-phosphorylated')) && !CONTAINS(?Label, 'unphosphorylated'))
        }
        """
        self.where['PRO_ID'] = """
        {
            ?PRO_term oboInOwl:id ?PRO_ID .
            FILTER(STRSTARTS(?PRO_ID, 'PR:')|| STRSTARTS(?PRO_ID, 'GO:'))
        }
        """

        self.where['QUALIFIER'] = """
        {
            ?xqualifier a rdf:Statement .
            ?xqualifier rdf:subject ?PRO_term .
            ?xqualifier paf:modifier ?Modifier .
        }
        """

        self.where['REACTOME_ID'] = """
        {
            ?PRO_term  oboInOwl:hasDbXref ?REACTOME_ID .
            FILTER(STRSTARTS(STR(?REACTOME_ID),'Reactome:'))
        }
        """

        self.where['RELATION'] = """
        {
            ?xrelation rdf:subject ?PRO_term .
            ?xrelation rdf:predicate [ 
                paf:relation ?Relation
            ] .
        }
        """
        self.where["SEQUENCE"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='sequence')
        }
        """
        self.where["ORGANISM_SEQUENCE"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            BIND(STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?CAT)
            FILTER(?CAT='organism-sequence')
        }
                """
        self.where["SALIVA_BIOMARKERS"] = """
        {
            ?PRO_term obo:IAO_0000115 ?PRO_termDef .
            ?xsaliva  oboInOwl:hasDbXref ?DbRef .
            ?xsaliva a owl:Axiom .
            ?xsaliva owl:annotatedProperty obo:IAO_0000115 .
            ?xsaliva owl:annotatedSource ?PRO_term .
            FILTER(CONTAINS(?DbRef,'SALO:AJ'))
        }
        """

        self.where['TAXON_ID'] = """
        {
            ?PRO_term
                rdfs:subClassOf [
                    a owl:Restriction ;
                    owl:onProperty obo:RO_0002160 ;
                    owl:someValuesFrom ?ncbi ] .
            ?ncbi
                oboInOwl:hasOBONamespace 'ncbi_taxonomy' ;
                oboInOwl:id ?NCBITaxon_ID .
        }
        """
        self.where["UBIQUITINATED_FORMS"] = """
        {
            ?PRO_term rdfs:comment ?Category .
            ?PRO_term rdfs:label ?Label .
            BIND(strafter(strbefore(STR(?Category), '.'), '=') as ?CAT)
            FILTER(CONTAINS(?CAT, 'modification') && !CONTAINS(?CAT,'(was)') && (STRSTARTS(?Label, 'ubiquitinated') || CONTAINS(?Label,'-ubiquitinated') || CONTAINS(?Label,' ubiquitinated ')) && !CONTAINS(?Label, 'unubiquitinated'))
        }
        """

        self.where["UNIPROTKB_ID"] = """
        {
            ?PRO_term  oboInOwl:hasDbXref ?UNIPROTKB_ID .
            FILTER(STRSTARTS(STR(?UNIPROTKB_ID),'UniProtKB:'))
        }
        """

        self.select["ANNOTATION"] = "STR('null') as ?annotation"
        self.select["ANY_RELATIONSHIP"] = "STR(?AnyRelationship) as ?anyRelationship"
        self.select["CATEGORY"] = "STRAFTER(STRBEFORE(STR(?Category), '.'), '=') as ?category"
        self.select["CHILD"] = "(GROUP_CONCAT(DISTINCT ?Child_ID; separator=', ') as ?child)"
        self.select["CHILDREN"] = "(GROUP_CONCAT(DISTINCT ?Child_ID; separator=', ') as ?child)"
        self.select["DESCENDANT"] = "(GROUP_CONCAT(DISTINCT ?Descendant_ID; separator=', ') as ?descendant)"
        self.select["COMMENT"] = "STR(?Comment) as ?comment"
        self.select["CONSIDER"] = "STR('null') as ?consider"
        self.select["DBREF"] = "(GROUP_CONCAT(DISTINCT ?DbRef; separator=', ') as ?dbref)"
        self.select["DB_ID"] = "(GROUP_CONCAT(DISTINCT ?DbRef; separator='; ') as ?dbID)"
        #self.dsp["ECOCYC_ID_DSP"] = "strafter(STR(?EcoCycID), 'EcoCyc:') as ?ecoCycID"
        self.select["ECOCYC_ID"] = "STR(?EcoCycID)as ?ecoCycID"
        #self.select["GENE_NAME"] = "STRAFTER(STR(?g), ' (') as ?geneName"
        self.select["GENE_NAME"] = "STRBEFORE(STR(?g), ' (') as ?geneName"
        #self.dsp["HGNC_ID_DSP"] = "(group_concat(distinct strafter(STR(?HGNC_ID),'HGNC:'); separator=', ') as ?hgncID)"
        self.select["HGNC_ID"] = "(GROUP_CONCAT(DISTINCT STR(?HGNC_ID); separator=', ') as ?hgncID)"
        self.select["ID"] = "DISTINCT STR(?PRO_ID) as ?id"
        self.select["ALT_ID"] = "STR(?ALT_ID) as ?alt_id"
        self.select["PRO_ID"] = "STR(?PRO_ID) as ?proID"
        self.select["PFAM_ID"] = "?pfamID"
        self.select["PFAM_NAME"] = "?pfamName"
        #self.dsp["MGI_ID_DSP"] = "(group_concat(distinct strafter(STR(?MGI_ID),'MGI:'); separator=', ') as ?mgiID)"
        self.select["MGI_ID"] = "(GROUP_CONCAT(DISTINCT STR(?MGI_ID); separator=', ') as ?mgiID)"
        self.select["OBSOLETE"] = "STR('null') as ?obsolete"
        self.select["ORTHO_ISOFORM"] = "(GROUP_CONCAT(DISTINCT ?Ortho_isoform_ID; separator=', ') as ?orthoIsoform)"
        self.select["ORTHO_MODFORM"] = "(GROUP_CONCAT(DISTINCT ?Ortho_modform_ID; separator=', ') as ?orthoModform)"
        #self.dsp["PANTHER_ID_DSP"] = "strafter(STR(?PANTHER_ID),'PANTHER:') as ?pantherID"
        self.select["PANTHER_ID"] = "STR(?PANTHER_ID) as ?pantherID"
        self.select["PARENT"] = "(GROUP_CONCAT(DISTINCT ?Parent_ID; separator=', ') as ?parent)"
        self.select["PARENTS"] = "(GROUP_CONCAT(DISTINCT ?Parent_ID; separator=', ') as ?parent)"
        self.select["ANCESTOR"] = "(GROUP_CONCAT(DISTINCT ?Ancestor_ID; separator=', ') as ?ancestor)"
        #self.dsp["PIRSF_ID_DSP"] = "strafter(STR(?PIRSF_ID),'PIRSF:') as ?pirsfID"
        self.select["PIRSF_ID"] = "STR(?PIRSF_ID) as ?pirsfID"
        #self.dsp["PMID_DSP"] = "(group_concat(distinct strafter(STR(?PMID),'PMID:'); separator=', ') as ?pmID)"
        self.select["PMID"] = "(GROUP_CONCAT(DISTINCT STR(?PMID); separator=', ') as ?pmID)"
        #self.dsp["PRO_DEF_TXT_DSP"] = "concat(concat(concat(STR(?PRO_termDef), ' ['), (group_concat(distinct ?dbID; separator='; '))), ']') as ?termDef"

        #self.select["PRO_TERM_DEFINITION"] = "CONCAT(CONCAT(CONCAT(STR(?PRO_termDef), ' ['), (group_concat(distinct ?dbref; separator=', '))), ']') as ?termDef"
        self.select["PRO_TERM_DEFINITION"] = "STR(?PRO_termDef) as ?termDef"
        self.select["PRO_NAME"] = "STR(?Label) as ?name"
        self.select["PRO_NAMESPACE"] = "STR(?Namespace) as ?namespace"
        self.select["PRO_NAME_SYNONYMS"] = "(GROUP_CONCAT(DISTINCT ?synonym; separator='; ') as ?synonym)"
        #self.dsp["REACTOME_ID_DSP"] = "(group_concat(distinct strafter(STR(?REACTOME_ID),'Reactome:'); separator=', ') as ?reactomeID)"
        self.select["REACTOME_ID"] = "(GROUP_CONCAT(DISTINCT STR(?REACTOME_ID); separator=', ') as ?reactomeID)"
        self.select["REPLACED_BY"] = "STR('null') as ?replacedBy"
        #self.dsp["TAXON_DSP"] = "strafter(STR(?NCBITaxon_ID),'NCBITaxon:') as ?ncbiTaxonID"
        self.select["TAXON_ID"] = "STR(?NCBITaxon_ID) as ?taxonID"
        #self.dsp["UNIPROTKB_ID_DSP"] = "(group_concat(distinct strafter(STR(?UNIPROTKB_ID),'UniProtKB:'); separator=', ') as ?uniprotKBID)"
        self.select["UNIPROTKB_ID"] = "(GROUP_CONCAT(DISTINCT STR(?UNIPROTKB_ID); separator=', ') as ?uniprotKBID)"

        self.pafHeader = ["PRO_ID", "QUALIFIER_DSP", "RELATION_DSP", "ONTOLOGY_ID_DSP", "ONTOLOGY_TERM_TXT_DSP", "RELATIVE_TO_DSP", "INTERACTION_WITH_DSP", "EVIDENCE_SOURCE_DSP", "EVIDENCE_CODE_DSP", "INFERRED_FROM_DSP"]

        self.pafDSP["PAF_DSP"] = """
STR(?PRO_ID) as ?proID
STR(?Modifier) as ?modifier
STR(?Relation) as ?relation
STR(?Ontology_ID) as ?ontologyID
STR(?Ontology_Term) as ?ontologyTerm
STR(?RelativeTo) as ?relativeTo
STR(?InteractionWith) as ?interactionWith
group_concat(distinct STR(?EvidenceSource) ; separator = ', ') AS ?evidenceSource
group_concat(distinct STR(?EvidenceCode) ; separator = ', ') AS ?evidenceCode
STR(strafter(STR(?NCBITaxon_ID),'NCBITaxon:')) as ?taxonID
group_concat(distinct STR(?InferredFrom) ; separator =', ') AS ?inferredFrom
"""
        self.pafFileDSP = """
DISTINCT STR(?PRO_ID) as ?PRO_ID
STR(?Object_term) as ?Object_term  
(GROUP_CONCAT(DISTINCT ?Object_synonym ; separator = '; ') AS ?Object_syny) 
STR(?Modifier) as ?Modifier  
STR(?Relation) as ?Relation  
STR(?Ontology_ID) as ?Ontology_ID  
STR(?Ontology_Term) as ?Ontology_term 
STR(?RelativeTo) as ?Relative_to 
STR(?Interaction_with) as ?Interaction_with 
GROUP_CONCAT(DISTINCT STR(?EvidenceSource) ; separator = '|') AS ?Evidence_source
GROUP_CONCAT(DISTINCT STR(?EvidenceCode) ; separator = ', ') AS ?Evidence_code      
STR(strafter(STR(?NCBITaxon_ID),'NCBITaxon:')) as ?Taxon
GROUP_CONCAT(DISTINCT STR(?InferredFrom) ; separator = '|') as ?Inferred_from 
GROUP_CONCAT(DISTINCT STR(?DB_ID) ; separator = '|') AS ?DB_ID
REPLACE(STR(?Date), '-', '') as ?Date 
GROUP_CONCAT(DISTINCT STR(?Assigned_by) ; separator = ', ') AS ?Assigned_by
STR(?Comments) as ?Comment
"""
        self.pafFileQuery = """
{
        ?PRO_term paf:objectTerm ?Object_term .  
        ?PRO_term oboInOwl:id ?PRO_ID .
        ?x a rdf:Statement .
        ?x rdf:subject ?PRO_term .
                OPTIONAL { ?x rdf:predicate [ paf:relation ?Relation] .}
        OPTIONAL {
                ?x rdf:object [
                        paf:ontologyID ?Ontology_ID ;
                        paf:ontologyTerm ?Ontology_Term ;
                ] .
        }
        OPTIONAL { ?x paf:modifier ?Modifier .}
        OPTIONAL { ?x paf:relativeTo ?RelativeTo_PRO_term . ?RelativeTo_PRO_term oboInOwl:id ?RelativeTo .}
        OPTIONAL { ?x paf:interactionWith ?InteractionWith_PRO_term . ?InteractionWith_PRO_term oboInOwl:id ?Interaction_with .}
        OPTIONAL { ?x paf:evidenceSource ?EvidenceSource .}
        OPTIONAL { ?x paf:evidenceCode ?EvidenceCode .}
        OPTIONAL { ?x paf:inferredFrom ?InferredFrom .}
        OPTIONAL { ?x paf:dbID ?DB_ID .}
        OPTIONAL { ?x paf:taxon ?NCBITaxon_ID .}
        OPTIONAL {
                ?PRO_term
                        rdfs:subClassOf [
                        a owl:Restriction ;
                        owl:onProperty obo:RO_0002160 ;
                        owl:someValuesFrom ?ncbi ] .
                ?ncbi
                oboInOwl:hasOBONamespace 'ncbi_taxonomy' ;
                oboInOwl:id ?NCBITaxon_ID .
        }
        OPTIONAL { ?x paf:date ?Date .}
        OPTIONAL { ?x paf:comments ?Comments .}
        OPTIONAL { ?x paf:assigned_by ?Assigned_by .}
        OPTIONAL { ?PRO_term oboInOwl:hasExactSynonym ?Object_synonym .}
}
"""

        self.pafQueryCondition["PAF_DSP"] = """
{
        ?x a rdf:Statement .
        ?x rdf:subject ?PRO_term .
        ?x rdf:predicate [ paf:relation ?Relation] .
        OPTIONAL {
                ?x rdf:object [
                        paf:ontologyID ?Ontology_ID ;
                        paf:ontologyTerm ?Ontology_Term ;
                ] .
        }
        OPTIONAL { ?x paf:modifier ?Modifier .}
        OPTIONAL { ?x paf:relativeTo ?RelativeTo_PRO_term . ?RelativeTo_PRO_term oboInOwl:id ?RelativeTo .}
        OPTIONAL { ?x paf:interactionWith ?InteractionWith_PRO_term . ?InteractionWith_PRO_term oboInOwl:id ?InteractionWith .}
        OPTIONAL { ?x paf:evidenceSource ?EvidenceSource .}
        OPTIONAL { ?x paf:evidenceCode ?EvidenceCode .}
        OPTIONAL { ?x paf:inferredFrom ?InferredFrom .}
        OPTIONAL { ?x paf:taxon ?NCBITaxon_ID .}
        OPTIONAL {
                ?PRO_term
                        rdfs:subClassOf [
                        a owl:Restriction ;
                        owl:onProperty obo:RO_0002160 ;
                        owl:someValuesFrom ?ncbi ] .
                ?ncbi
                oboInOwl:hasOBONamespace 'ncbi_taxonomy' ;
                oboInOwl:id ?NCBITaxon_ID .
        }
 }
?PRO_term oboInOwl:id ?PRO_ID .
"""

        self.oboQuerySelect["basic"] = """
STR(?id) as ?id
STR(?ALT_ID) as ?alt_id
STR(?name) as ?name
STR(?namespace) as ?namespace
STR(?comment) as ?comment
CONCAT(CONCAT(CONCAT('\"',STR(?PRO_termDef),'\"', ' ['), (group_concat(distinct ?dbref; separator=', '))), ']') as ?def
GROUP_CONCAT(DISTINCT STR(?xref); separator = ' ^|^ ') AS ?xref
GROUP_CONCAT(DISTINCT ?is_a; separator=' ^|^ ') as ?is_a
STR(?is_obsolete) as ?is_obsolete
STR(?replaced_by) as ?replaced_by
STR(?consider) as ?consider
"""
        self.oboQueryCondition["basic"] = """
{
        ?PRO_term oboInOwl:id ?id .
        OPTIONAL { ?PRO_term rdfs:label ?name .}
        OPTIONAL { ?PRO_term oboInOwl:hasOBONamespace ?namespace .}
        OPTIONAL { 
                []
          oboInOwl:hasDbXref ?dbref ;
          a owl:Axiom ;
          owl:annotatedProperty obo:IAO_0000115 ;
          owl:annotatedSource ?PRO_term ;
          owl:annotatedTarget ?PRO_termDef .
        }
        OPTIONAL { ?PRO_term rdfs:comment ?comment .}
        #OPTIONAL { ?PRO_term oboInOwl:hasDbXref ?xref .}
        OPTIONAL {
            ?PRO_term oboInOwl:id ?id .
                [ a                      owl:Axiom ;
                  rdfs:label             ?label ;
                  owl:annotatedProperty  oboInOwl:hasDbXref ;
                  owl:annotatedSource    ?PRO_term ;
                  owl:annotatedTarget    ?_xref 
                ] .
                BIND(CONCAT(STR(?_xref), ' "', STR( ?label ), '" ' )  AS ?xref)  .
        }
        OPTIONAL { 
                ?PRO_term rdfs:subClassOf ?Parent . 
                ?Parent rdfs:label ?ParentName .
                ?Parent oboInOwl:id ?ParentID .
                BIND(CONCAT(STR( ?ParentID ), ' ! ', ?ParentName)  AS ?is_a)  .
        }
        OPTIONAL { ?PRO_term owl:deprecated ?is_obsolete  . }
        OPTIONAL { ?PRO_term obo:IAO_0100001 ?replaced_by . }
        OPTIONAL { ?PRO_term oboInOwl:hasAlternativeId ?ALT_ID . }
        OPTIONAL { ?PRO_term oboInOwl:consider ?consider .  }
}
"""
        self.oboQuerySelect["synonym"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?synonym; separator=' ^|^ ') as ?synonym
"""
        self.oboQueryCondition["synonym"] = """
{
        ?PRO_term oboInOwl:id ?id .
    {
            ?xe a owl:Axiom ;
              owl:annotatedProperty oboInOwl:hasExactSynonym ;
              owl:annotatedSource ?PRO_term ;
              owl:annotatedTarget ?exactSyn .
              OPTIONAL {?xe oboInOwl:hasSynonymType ?synonymType. }
              OPTIONAL {?xe oboInOwl:hasDbXref ?dbxref .}
              BIND(CONCAT('"', STR(?exactSyn), '"', ' EXACT ', strafter(str(?synonymType), '#'), ' [', ?dbxref, ']')  AS ?synonym)  .
    }
    UNION {
            ?PRO_term oboInOwl:hasExactSynonym ?exactSyn .
            FILTER NOT EXISTS {
                    ?xne a owl:Axiom ;
                    owl:annotatedProperty oboInOwl:hasExactSynonym ;
                    owl:annotatedSource ?PRO_term ;
                    owl:annotatedTarget ?exactSyn .
            }
            BIND(CONCAT('"', STR( ?exactSyn ),'"', ' EXACT')  AS ?synonym)  .
    }
    UNION {
            ?xr a owl:Axiom ;
              owl:annotatedProperty oboInOwl:hasRelatedSynonym ;
              owl:annotatedSource ?PRO_term ;
              owl:annotatedTarget ?relatedSyn .
              OPTIONAL {?xr oboInOwl:hasSynonymType ?synonymType. }
              OPTIONAL {?xr oboInOwl:hasDbXref ?dbxref .}
              BIND(CONCAT('"', STR( ?relatedSyn ),'"', ' RELATED Gene-based ', '[', ?dbxref, ']')  AS ?synonym)  .
    }
    UNION {
                [ a                      owl:Axiom ;
              oboInOwl:hasDbXref     ?dbxref ;
              owl:annotatedProperty  oboInOwl:hasBroadSynonym ;
              owl:annotatedSource    ?PRO_term ;
              owl:annotatedTarget    ?broadSyn
            ] .
            BIND(CONCAT('"', STR( ?broadSyn ), '"', ' BROAD ', '[', ?dbxref, ']')  AS ?synonym)  .
    }
    UNION {
            [ a      owl:Axiom ;
          oboInOwl:hasDbXref       ?dbxref ;
          oboInOwl:hasSynonymType  pr:Gene-based ;
          owl:annotatedProperty    oboInOwl:hasNarrowSynonym ;
          owl:annotatedSource      ?PRO_term ;
          owl:annotatedTarget      ?narrowSyn
        ] .
        BIND(CONCAT('"', STR( ?narrowSyn ),'"', ' NARROW ', '[', ?dbxref, ']')  AS ?synonym)  .
    }
}
"""
        self.oboQuerySelect["union_of"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?unionOf; separator=' ^|^ ') as ?union_of
"""
        self.oboQueryCondition["union_of"] = """
{
        ?PRO_term oboInOwl:id ?id .
        ?PRO_term owl:equivalentClass/owl:unionOf/(rdf:rest*/rdf:first)* ?unionTerm .
        FILTER(!CONTAINS(STR(?unionTerm), 'node'))
        ?unionTerm oboInOwl:id ?unionTermId .
        ?unionTerm rdfs:label ?unionTermName .
        BIND(CONCAT(STR( ?unionTermId ), ' ! ', ?unionTermName) as ?unionOf) .
}
"""
        self.oboQuerySelect["intersection_of"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?intersectionOf; separator=' ^|^ ') as ?intersection_of
"""
        self.oboQueryCondition["intersection_of"] = """
{
        ?PRO_term oboInOwl:id ?id .
        ?PRO_term owl:equivalentClass/owl:intersectionOf/(rdf:rest*/rdf:first)* ?intersectionTerm .
        {
                {
                        ?intersectionTerm 
                                oboInOwl:id ?intersectionTermID ; 
                                rdfs:label ?intersectionTermName .
                        BIND(CONCAT(STR( ?intersectionTermID ), ' ! ', ?intersectionTermName) as ?intersectionOf) .
                }
                UNION {
                        ?intersectionTerm 
                                a owl:Restriction ;
                                owl:onProperty ?Property ;
                                owl:someValuesFrom ?Term .
                                ?Term
                                        oboInOwl:id ?TermID;
                                        rdfs:label ?TermName .
                                        ?Property rdfs:label ?Label .
                                BIND(CONCAT(?Label, ' ', STR( ?TermID ), ' ! ', ?TermName) as ?intersectionOf) .
                }
                UNION {
                ?intersectionTerm 
                        a owl:Restriction ;
                        owl:onClass               ?component ;
                        owl:onProperty            obo:RO_0002180 ;
                        owl:qualifiedCardinality  ?cardinality .
                obo:RO_0002180 rdfs:label ?ro_label .
                ?component rdfs:label ?component_label .
                ?component oboInOwl:id ?component_id .
                BIND(CONCAT(STR(?ro_label), ' ', STR(?component_id), ' {cardinality="', ?cardinality, '"}', ' ! ', ?component_label) AS ?intersectionOf). 
                }
        }
 }
 """
        self.oboQuerySelect["disjoint_from"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?disjoint_from; separator=' ^|^ ') as ?disjoint_from
"""
        self.oboQueryCondition["disjoint_from"] = """
{
        ?PRO_term oboInOwl:id ?id .
        ?PRO_term owl:disjointWith ?Term .
        ?Term
                oboInOwl:id ?TermID;
                rdfs:label ?TermName .
        BIND(CONCAT(STR( ?TermID ), ' ! ', ?TermName) as ?disjoint_from) .
}
"""
        self.oboQuerySelect["equivalent_to"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?equivalent_to; separator=' ^|^ ') as ?equivalent_to
"""
        self.oboQueryCondition["equivalent_to"] = """
{
        ?PRO_term oboInOwl:id ?id .
        ?PRO_term owl:equivalentClass ?Term  .
        FILTER(!CONTAINS(STR(?Term), 'node'))
        ?Term
                oboInOwl:id ?TermID;
                rdfs:label ?TermName .
        BIND(CONCAT(STR( ?TermID ), ' ! ', ?TermName) as ?equivalent_to) .      
}
"""

        self.oboQuerySelect["relationship"] = """
STR(?id) as ?id
GROUP_CONCAT(DISTINCT ?relationship; separator=' ^|^ ') as ?relationship
"""
        self.oboQueryCondition["relationship"] = """
    {
        ?PRO_term oboInOwl:id ?id .
        {
            ?PRO_term rdfs:subClassOf  [
                    a owl:Restriction ;
                    owl:onProperty ?Property ;
                    owl:someValuesFrom ?Term
            ].
            ?Property rdfs:label ?PropertyName .
            ?Term 
                    oboInOwl:id ?TermID ;
                    rdfs:label ?TermName .
            BIND(CONCAT(STR(?PropertyName), ' ', STR( ?TermID ), ' ! ', ?TermName )  AS ?relationship)  .
        }
        UNION {
            ?PRO_term
            rdfs:subClassOf           [ a                         owl:Restriction ;
                                    owl:onClass               ?component ;
                                    owl:onProperty            obo:RO_0002180 ;
                                    owl:qualifiedCardinality  ?cardinality
                                  ] .
            obo:RO_0002180 rdfs:label ?ro_label .
            ?component rdfs:label ?component_label .
            ?component oboInOwl:id ?component_id .
            BIND(CONCAT(STR(?ro_label), ' ', STR(?component_id), ' {cardinality="', ?cardinality, '"}', ' ! ', ?component_label) AS ?relationship). 
        }
}
"""

        self.allPROIDsQuery = """
SELECT
STR(?PRO_ID) as ?PRO_ID
WHERE {
   ?PRO_term oboInOwl:id ?PRO_ID .
   FILTER(STRSTARTS(STR(?PRO_ID), 'PR:')||STRSTARTS(STR(?PRO_ID), 'GO:') ||STRSTARTS(STR(?PRO_ID), 'UniProtKB:'))
}
"""
        self.proNameQuery = """
SELECT
STR(?PRO_ID) as ?PRO_ID
STR(?PRO_Name) as ?PRO_Name
WHERE {
   ?PRO_term oboInOwl:id ?PRO_ID .
   ?PRO_term rdfs:label ?PRO_Name .
   FILTER(STRSTARTS(STR(?PRO_ID), 'PR:')||STRSTARTS(STR(?PRO_ID), 'GO:') ||STRSTARTS(STR(?PRO_ID), 'UniProtKB:'))
}
"""
        self.hierarchyWithCategory = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT distinct ?PRO_ID ?PRO_category ?PRO_name ?Parent_ID ?Parent_category ?Parent_name
WHERE 
{
    {
        SELECT distinct ?ancestor as ?PRO STR(?ancestor_id) as ?PRO_ID ?PRO_name ?directParent as ?Parent STR(?directParent_id) as ?Parent_ID ?Parent_name
        WHERE
        {
            {
                SELECT distinct ?ancestor
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?PRO_term rdfs:subClassOf ?parent .
                    ?parent rdfs:subClassOf* ?ancestor .
                }
            }
            UNION 
            {
                values ?ancestor {obo:PR_XXXXXXXXX}
                ?ancestor oboInOwl:id ?ancestor_id .
            }
            ?ancestor rdfs:subClassOf ?directParent .
            ?directParent oboInOwl:id ?directParent_id .
            ?ancestor oboInOwl:id ?ancestor_id .
            ?ancestor rdfs:label ?ancestor_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
            FILTER (!isBlank(?ancestor))
            BIND(str(?ancestor_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
        }
    }
    UNION 
    {
        SELECT distinct ?children as ?PRO STR(?children_id) as ?PRO_ID ?PRO_name ?directParent as ?Parent STR(?directParent_id) as ?Parent_ID ?Parent_name
        WHERE
        {
            {
                SELECT distinct ?children
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?children rdfs:subClassOf* ?PRO_term .
                }
            }
            UNION 
            {
                values ?children {obo:PR_XXXXXXXXX}
                ?children oboInOwl:id ?children_id .
            }
            ?children rdfs:subClassOf ?directParent .
            ?directParent rdfs:subClassOf* obo:PR_XXXXXXXXX .
            ?directParent oboInOwl:id ?directParent_id .
            ?children oboInOwl:id ?children_id .
            ?children rdfs:label ?children_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?children_id, 'PR:')|| STRSTARTS(?children_id, 'GO:'))
            FILTER (!isBlank(?children))
            BIND(str(?children_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
        }
    }
    OPTIONAL {
        ?PRO rdfs:comment ?pa .
        BIND(STRAFTER(STRBEFORE(STR(?pa), '.'), '=') as ?PRO_category) .
    }
    OPTIONAL {
        ?Parent rdfs:comment ?pra . 
        BIND(STRAFTER(STRBEFORE(STR(?pra), '.'), '=') as ?Parent_category) .
    }
}
"""
        self.hierarchy1="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT distinct ?PRO_ID ?PRO_name ?Parent_ID ?Parent_name
WHERE 
{
    {
        SELECT distinct STR(?ancestor_id) as ?PRO_ID ?PRO_name STR(?directParent_id) as ?Parent_ID ?Parent_name
        WHERE
        {
            {
                SELECT distinct ?ancestor
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?PRO_term rdfs:subClassOf ?parent .
                    ?parent rdfs:subClassOf* ?ancestor .
                }
            }
            UNION 
            {
                values ?ancestor {obo:PR_XXXXXXXXX}
                ?ancestor oboInOwl:id ?ancestor_id .
            }
            ?ancestor rdfs:subClassOf ?directParent .
            ?directParent oboInOwl:id ?directParent_id .
            ?ancestor oboInOwl:id ?ancestor_id .
            ?ancestor rdfs:label ?ancestor_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
            FILTER (!isBlank(?ancestor))
            BIND(str(?ancestor_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
        }
    }
    UNION 
    {
        SELECT distinct STR(?children_id) as ?PRO_ID ?PRO_name STR(?directParent_id) as ?Parent_ID ?Parent_name
        WHERE
        {
            {
                SELECT distinct ?children
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?children rdfs:subClassOf* ?PRO_term .
                }
            }
            UNION 
            {
                values ?children {obo:PR_XXXXXXXXX}
                ?children oboInOwl:id ?children_id .
            }
            ?children rdfs:subClassOf ?directParent .
            ?directParent rdfs:subClassOf* obo:PR_XXXXXXXXX .
            ?directParent oboInOwl:id ?directParent_id .
            ?children oboInOwl:id ?children_id .
            ?children rdfs:label ?children_label .
            ?directParent rdfs:label ?directParent_label .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?children_id, 'PR:')|| STRSTARTS(?children_id, 'GO:'))
            FILTER (!isBlank(?children))
            BIND(str(?children_label) as ?PRO_name) .
            BIND(str(?directParent_label) as ?Parent_name) .
        }
    }
}
"""
        self.parentQuery = """
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT DISTINCT ?PRO_ID ?Parent_ID
WHERE 
{
    VALUES
    ?PRO_term rdfs:subClassOf ?parent .
    ?PRO_term oboInOwl:id ?PRO_ID .
    ?parent oboInOwl:id ?Parent_ID .
    FILTER(STRSTARTS(STR(?PRO_ID), "PR:"))
  	FILTER(STRSTARTS(STR(?Parent_ID), "PR:"))
}      
"""
        self.ancestorQuery = """
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT DISTINCT ?PRO_ID ?Ancestor_ID
WHERE 
{
    VALUES
    ?PRO_term rdfs:subClassOf+ ?ancestor .
    ?PRO_term oboInOwl:id ?PRO_ID .
    ?ancestor oboInOwl:id ?Ancestor_ID .
    FILTER(STRSTARTS(STR(?PRO_ID), "PR:"))
    FILTER(STRSTARTS(STR(?Ancestor_ID), "PR:"))
}      
"""
        self.childrenQuery="""
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT DISTINCT ?PRO_ID ?Children_ID
WHERE 
{
    VALUES
    ?children rdfs:subClassOf ?PRO_term  .
    ?PRO_term oboInOwl:id ?PRO_ID .
    ?children oboInOwl:id ?Children_ID .
    FILTER(STRSTARTS(STR(?PRO_ID), "PR:"))
  	FILTER(STRSTARTS(STR(?Children_ID), "PR:"))
}        
"""

        self.descendantQuery="""
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT DISTINCT ?PRO_ID ?Descendant_ID
WHERE 
{
    VALUES
    ?descendant rdfs:subClassOf+ ?PRO_term  .
    ?PRO_term oboInOwl:id ?PRO_ID .
    ?descendant oboInOwl:id ?Descendant_ID .
    FILTER(STRSTARTS(STR(?PRO_ID), "PR:"))
  	FILTER(STRSTARTS(STR(?Descendant_ID), "PR:"))
}
"""

        self.hierarchyQuery="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

SELECT distinct ?PRO_ID ?Parent_ID
WHERE 
{
    {
        SELECT distinct STR(?ancestor_id) as ?PRO_ID STR(?directParent_id) as ?Parent_ID
        WHERE
        {
            {
                SELECT distinct ?ancestor
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?PRO_term rdfs:subClassOf ?parent .
                    ?parent rdfs:subClassOf* ?ancestor .
                }
            }
            UNION 
            {
                values ?ancestor {obo:PR_XXXXXXXXX}
                ?ancestor oboInOwl:id ?ancestor_id .
            }
            ?ancestor rdfs:subClassOf ?directParent .
            ?directParent oboInOwl:id ?directParent_id .
            ?ancestor oboInOwl:id ?ancestor_id .
            # FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER(STRSTARTS(?directParent_id, 'PR:'))
            FILTER (!isBlank(?directParent))
            #FILTER(STRSTARTS(?ancestor_id, 'PR:')|| STRSTARTS(?ancestor_id, 'GO:'))
            FILTER(STRSTARTS(?ancestor_id, 'PR:'))
            FILTER (!isBlank(?ancestor))
        }
    }
    UNION 
    {
        SELECT distinct STR(?children_id) as ?PRO_ID STR(?directParent_id) as ?Parent_ID
        WHERE
        {
            {
                SELECT distinct ?children
                WHERE
                {
                    values ?PRO_term {obo:PR_XXXXXXXXX}
                    ?children rdfs:subClassOf* ?PRO_term .
                }
            }
            UNION 
            {
                values ?children {obo:PR_XXXXXXXXX}
                ?children oboInOwl:id ?children_id .
            }
            ?children rdfs:subClassOf ?directParent .
            ?directParent rdfs:subClassOf* obo:PR_XXXXXXXXX .
            ?directParent oboInOwl:id ?directParent_id .
            ?children oboInOwl:id ?children_id .
            FILTER(STRSTARTS(?directParent_id, 'PR:')|| STRSTARTS(?directParent_id, 'GO:'))
            FILTER (!isBlank(?directParent))
            FILTER(STRSTARTS(?children_id, 'PR:')|| STRSTARTS(?children_id, 'GO:'))
            FILTER (!isBlank(?children))
        }
    }
}
"""

class SparqlSearch:
    debug = True;
    conf = Config();

    def executeQuery(self, query):
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout" : 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            #print(response.txt)
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        #print(result)
        return result, error



    def getOBOPart(self, proID, type):
        values = "VALUES ?PRO_term {obo:" + proID.replace(':', '_') + "}\n"
        query = self.conf.cfg['prefix'] + "\n"
        query += "SELECT\n"
        query += self.conf.oboQuerySelect[type]+"\n"
        query += "WHERE {\n"
        query += values
        query += self.conf.oboQueryCondition[type]+"\n"
        query += "}\n"
        query += "ORDER BY ?id\n"
        # if type == "relationship":
        #     print(query)
        obo, error = self.executeQuery(query)

        #    print(obo)
        if(obo):
            return obo[0], error
        else:
            return [], error

    def oboSearch(self, searchParamter):
        proIDs = searchParamter.searchValue.split();
        allStanza = ""
        for proID in proIDs:
            obo = dict();
            stanza, error = self.getOBOPart(proID, 'basic')
            obo = stanza
            stanza, error = self.getOBOPart(proID, 'synonym')
            obo = self.mergeDicts(obo, stanza)
            # stanza, error = self.getOBOPart(proID, 'xref')
            # obo = self.mergeDicts(obo, stanza)
            stanza, error = self.getOBOPart(proID, 'relationship')
            obo = self.mergeDicts(obo, stanza)
            stanza, error = self.getOBOPart(proID, 'union_of')
            obo = self.mergeDicts(obo, stanza)
            stanza, error = self.getOBOPart(proID, 'intersection_of')
            obo = self.mergeDicts(obo, stanza)
            stanza, error = self.getOBOPart(proID, 'disjoint_from')
            obo = self.mergeDicts(obo, stanza)
            stanza, error = self.getOBOPart(proID, 'equivalent_to')
            obo = self.mergeDicts(obo, stanza)
            stanza = self.createOBOStanza(obo)
            allStanza += stanza +"\n"

        return allStanza.rstrip("\n"), error

    def mergeDicts(self, dict1, dict2):
        if dict2:
            for k in dict2.keys():
                if k in dict1:
                    if dict1[k] != dict2[k]:

                        print(k+" | "+dict1[k]+ " | "+ dict2[k])
                        print(dict2[k].find(dict1[k]))
                        if dict2[k].find(dict1[k]) == False:
                            dict1[k] += "<|>" + dict2[k]
                else:
                    dict1[k] = dict2[k]
        return dict1

    # def mergeDicts(self, dict1, dict2):
    #     dict3 = defaultdict(list)
    #     for k, v in chain(dict1.items(), dict2.items()):
    #         dict3[k].append(v)
    #     return dict3

    # def mergeDicts(self, dict1, dict2):
    #     dict3 = dict()
    #
    #     for k1 in dict1.keys():
    #         v1 = dict1[k1]
    #         if k1 in dict3.keys:
    #             dict3[k1].append(v1)
    #         else:
    #             dict3[k1] = []
    #             dict3[k1].append(v1)
    #     for k2 in dict2.keys():
    #         v2 = dict2[k2]
    #         if k2 in dict3 and dict3[k2]:
    #             dict3[k2].append(v2)
    #         else:
    #             dict3[k2] = []
    #             dict3[k2].append(v2)
    #     return dict3

    def createOBOStanza(self, data):
        #print(data)
        stanza = "[Term]\n"

        if 'id' in data.keys() and data['id']:
            stanza += "id: "+data['id']+"\n"
        if 'name' in data.keys() and data['name']:
            stanza += "name: "+data['name']+"\n"
        if 'namespace' in data.keys() and data['namespace']:
            stanza += "namespace: "+data['namespace']+"\n"
        if 'alt_id' in data.keys() and data['alt_id']:
            records = data['alt_id'].split(" ^|^ ")
            for record in records:
                stanza += "alt_id: "+record+"\n"
        if 'def' in data.keys() and data['def']:
            temp = data['def'].replace('""', '')
            if temp != " []":
                stanza += "def: "+temp+"\n"
        if 'comment' in data.keys() and data['comment']:
            stanza += "comment: "+data['comment']+"\n"
        if 'synonym' in data.keys() and data['synonym']:
            records = data['synonym'].split(" ^|^ ")
            #print(records)
            for record in records:
                stanza += "synonym: "+ record.replace('""', '')+"\n"
        if 'xref' in data.keys() and data['xref']:
            records = data['xref'].split(" ^|^ ")
            for record in records:
                stanza += "xref: " + record+"\n"
        if 'is_a' in data.keys() and data['is_a']:
            records = data['is_a'].split(" ^|^ ")
            for record in records:
                stanza += "is_a: " + record+"\n"
        if 'is_obsolete' in data.keys() and data['is_obsolete']:
            records = data['is_obsolete'].split(" ^|^ ")
            for record in records:
                stanza += "is_obsolete: " + record + "\n"
        if 'replaced_by' in data.keys() and data['replaced_by']:
            records = data['replaced_by'].split(" ^|^ ")
            for record in records:
                stanza += "replaced_by: " + record + "\n"
        if 'consider' in data.keys() and data['consider']:
            records = data['consider'].split(" ^|^ ")
            for record in records:
                stanza += "consider: " + record + "\n"
        if 'union_of' in data.keys() and data['union_of']:
            records = data['union_of'].split(" ^|^ ")
            for record in records:
                stanza += "union_of: " + record + "\n"
        if 'disjoint_from' in data.keys() and data['disjoint_from']:
            records = data['disjoint_from'].split(" ^|^ ")
            for record in records:
                stanza += "disjoint_from: " + record + "\n"
        if 'equivalent_to' in data.keys() and data['equivalent_to']:
            records = data['equivalent_to'].split(" ^|^ ")
            for record in records:
                stanza += "equivalent_to: " + record + "\n"
        if 'intersection_of' in data.keys() and data['intersection_of']:
            records = data['intersection_of'].split(" ^|^ ")
            for record in records:
                stanza += "intersection_of: " + record + "\n"
        if 'relationship' in data.keys() and data['relationship']:
            records = data['relationship'].split(" ^|^ ")
            for record in records:
                stanza += "relationship: " + record + "\n"
        return stanza

    def proDescendant(self, searchParameter):
        query = self.conf.descendantQuery
        proIds = searchParameter.searchValue
        values = ""
        for proId in proIds.split(' '):
            values += "obo:"+proId.replace(":", "_") +" "
        VALUES = "VALUES ?PRO_term {"+values+"}"
        query = query.replace("VALUES", VALUES)
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        hierarchy = []
        descendants = []
        proIds = set()
        for descendantDict in result:
            descendant = Decendant()
            descendant.proId = descendantDict['PRO_ID']
            descendant.descendantId = descendantDict['Descendant_ID']
            proIds.add(descendant.proId)
            proIds.add(descendant.descendantId)
            descendants.append(descendant)
        proTerms = [];
        for proId in proIds:
            proTerm = PROTerm()
            # print(proId)
            proTerm.id = proId
            proTerms.append(proTerm)
        proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        PROs = {}
        for proTerm in proTerms:
            PROs.update({proTerm.id: proTerm})

        for descendant in descendants:
            hierarchy.append({"pro": PROs.get(descendant.proId), "pro_descendant": PROs.get(descendant.descendantId)})
        return hierarchy, error

    def proChildren(self, searchParameter):
        query = self.conf.childrenQuery
        proIds = searchParameter.searchValue
        values = ""
        for proId in proIds.split(' '):
            values += "obo:"+proId.replace(":", "_") +" "
        VALUES = "VALUES ?PRO_term {"+values+"}"
        query = query.replace("VALUES", VALUES)
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        hierarchy = []
        childrens = []
        proIds = set()
        for childrenDict in result:
            children = Children()
            children.proId = childrenDict['PRO_ID']
            children.childrenId = childrenDict['Children_ID']
            proIds.add(children.proId)
            proIds.add(children.childrenId)
            childrens.append(children)
        proTerms = [];
        for proId in proIds:
            proTerm = PROTerm()
            # print(proId)
            proTerm.id = proId
            proTerms.append(proTerm)
        proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        PROs = {}
        for proTerm in proTerms:
            PROs.update({proTerm.id: proTerm})

        for children in childrens:
            hierarchy.append({"pro": PROs.get(children.proId), "pro_children": PROs.get(children.childrenId)})
        return hierarchy, error

    def proAncestor(self, searchParameter):
        query = self.conf.ancestorQuery
        proIds = searchParameter.searchValue
        values = ""
        for proId in proIds.split(' '):
            values += "obo:"+proId.replace(":", "_") +" "
        VALUES = "VALUES ?PRO_term {"+values+"}"
        query = query.replace("VALUES", VALUES)
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        hierarchy = []
        ancestors = []
        proIds = set()
        for ancestorDict in result:
            ancestor = Ancestor()
            ancestor.proId = ancestorDict['PRO_ID']
            ancestor.ancestorId = ancestorDict['Ancestor_ID']
            proIds.add(ancestor.proId)
            proIds.add(ancestor.ancestorId)
            ancestors.append(ancestor)
        proTerms = [];
        for proId in proIds:
            proTerm = PROTerm()
            # print(proId)
            proTerm.id = proId
            proTerms.append(proTerm)
        proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        PROs = {}
        for proTerm in proTerms:
            PROs.update({proTerm.id: proTerm})

        for ancestor in ancestors:
            hierarchy.append({"pro": PROs.get(ancestor.proId), "pro_ancestor": PROs.get(ancestor.ancestorId)})
        return hierarchy, error

    def proParent(self, searchParameter):
        query = self.conf.parentQuery
        proIds = searchParameter.searchValue
        values = ""
        for proId in proIds.split(' '):
            values += "obo:"+proId.replace(":", "_") +" "
        VALUES = "VALUES ?PRO_term {"+values+"}"
        query = query.replace("VALUES", VALUES)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        hierarchy = []
        parents = []
        proIds = set()
        for parentDict in result:
            parent = Parent()
            parent.proId = parentDict['PRO_ID']
            parent.parentId = parentDict['Parent_ID']
            proIds.add(parent.proId)
            proIds.add(parent.parentId)
            parents.append(parent)
        proTerms = [];
        for proId in proIds:
            proTerm = PROTerm()
            # print(proId)
            proTerm.id = proId
            proTerms.append(proTerm)
        proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        PROs = {}
        for proTerm in proTerms:
            PROs.update({proTerm.id: proTerm})

        for parent in parents:
            hierarchy.append({"pro": PROs.get(parent.proId), "pro_parent": PROs.get(parent.parentId)})
        return hierarchy, error

    def proHierarchy(self, searchParameter):
        query = self.conf.hierarchyQuery
        proId = searchParameter.searchValue.replace(':', '_')
        query = query.replace("PR_XXXXXXXXX", proId)
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)
        hierarchy = []
        parents = []
        proIds = set()
        for parentDict in result:
            parent = Parent()
            parent.proId = parentDict['PRO_ID']
            parent.parentId = parentDict['Parent_ID']
            proIds.add(parent.proId)
            proIds.add(parent.parentId)
            parents.append(parent)
        proTerms = [];
        for proId in proIds:
            proTerm = PROTerm()
            #print(proId)
            proTerm.id = proId
            proTerms.append(proTerm)
        proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        PROs = {}
        for proTerm in proTerms:
            PROs.update( {proTerm.id : proTerm} )

        for parent in parents:
            hierarchy.append({"pro" : PROs.get(parent.proId), "pro_parent" : PROs.get(parent.parentId)})
        return hierarchy, error

    def pafSearch(self, searchParameter):
        select = self.conf.pafFileDSP
        #values = "VALUES ?PRO_term {obo:"+searchParameter.searchValue.replace(':', '_')+"}\n"
        valuesStatement = "VALUES ?PRO_term {"
        value = searchParameter.searchValue.replace(':', '_')
        values = value.split()
        for v in values:
            valuesStatement += "obo:"+v +" "
        valuesStatement += "}\n"
        where = valuesStatement + self.conf.pafFileQuery
        query = self.conf.cfg['prefix'] + "\n"
        query += "SELECT\n"
        query += select + "\n"
        query += "WHERE\n"
        query += "{\n"
        query += where + "\n"
        query += "}\n"
        query += "ORDER BY DESC(?PRO_ID) ASC(?Ontology_Term)\n"
        #print(query)
        url = self.conf.cfg['sparql_endpoint']
        params = {'query': query, "format": "text/tab-separated-values", "timeout": 0, "debug": "on"}
        response = requests.post(url, data=params)
        error = Error
        result = []
        if (response.status_code != 200):
            error.code = response.status_code
            error.message = response.text
        else:
            error = None
            #print(response.text)
            reader = csv.DictReader(response.text.split('\n'), delimiter='\t')

            for line in reader:
                result.append(line)

        pafs = []
        for pafDict in result:
            keys = pafDict.keys()
            paf = PAF()
            for key in keys:
                if key == 'PRO_ID':
                    paf.PRO_ID = pafDict[key]
                if key == 'Object_term':
                    paf.Object_term= pafDict[key]
                if key == 'Object_syny':
                    paf.Object_syny = pafDict[key]
                if key == 'Modifier':
                    paf.Modifier= pafDict[key]
                if key == 'Relation':
                    paf.Relation= pafDict[key]
                if key == 'Ontology_ID':
                    paf.Ontology_ID= pafDict[key]
                if key == 'Ontology_term':
                    paf.Ontology_term= pafDict[key]
                if key == 'Relative_to':
                    paf.Relative_to= pafDict[key]
                if key == 'Interaction_with':
                    paf.Interaction_with= pafDict[key]
                if key == 'Evidence_source':
                    paf.Evidence_source= pafDict[key]
                if key == 'Evidence_code':
                    paf.Evidence_code= pafDict[key]
                if key == 'Taxon':
                    paf.Taxon= pafDict[key]
                if key == 'Inferred_from':
                    paf.Inferred_from= pafDict[key]
                if key == 'DB_ID':
                    paf.DB_ID= pafDict[key]
                if key == 'Date':
                    paf.Date= pafDict[key]
                if key == 'Assigned_by':
                    paf.Assigned_by= pafDict[key]
                if key == 'Comment':
                    paf.Comment= pafDict[key]

            pafs.append(paf)

        return pafs, error

    def proSearch(self, searchParameter, restriction):
        proIDsQuery, searchParameter = self.constructProIDsQuery(searchParameter, restriction)
        #print(proIDsQuery)
        proIDs, error = self.executeQuery(proIDsQuery)
        proTerms = [];
        if error == None:
            for proId in proIDs:
                proTerm = PROTerm()
                #print(proId['id'])
                proTerm.id = proId['id']
                proTerms.append(proTerm)
            proTerms, error = self.getPROTermsInfo(proTerms, searchParameter)
        return proTerms, error

    def getDisplayFieldKeys(self, searchParameter):
        displayFieldKeys = ["ID", "DB_ID"];
        if searchParameter.showAltID == True:
            displayFieldKeys.append("ALT_ID")
        if searchParameter.showAncestor == True:
            displayFieldKeys.append("ANCESTOR")
        if searchParameter.showAnnotation == True:
            displayFieldKeys.append("ANNOTATION")
        if searchParameter.showAnyRelationship == True:
            displayFieldKeys.append("ANY_RELATIONSHIP")
        if searchParameter.showCategory == True:
            displayFieldKeys.append("CATEGORY")
        if searchParameter.showChild == True:
            displayFieldKeys.append("CHILD")
        if searchParameter.showComment == True:
            displayFieldKeys.append("COMMENT")
        if searchParameter.showDescendant == True:
            displayFieldKeys.append("DESCENDANT")
        if searchParameter.showEcoCycID == True:
            displayFieldKeys.append(("ECOCYC_ID"))
        if searchParameter.showGeneName == True:
            displayFieldKeys.append("GENE_NAME")
        if searchParameter.showHGNCID == True:
            displayFieldKeys.append("HGNC_ID")
        if searchParameter.showMGIID == True:
            displayFieldKeys.append("MGI_ID")
        if searchParameter.showOrthoIsoform == True:
            displayFieldKeys.append("ORTHO_ISOFORM")
        if searchParameter.showOrthoModform == True:
            displayFieldKeys.append("ORTHO_MODFORM")
        if searchParameter.showPANTHERID == True:
            displayFieldKeys.append("PANTHER_ID")
        if searchParameter.showPIRSFID == True:
            displayFieldKeys.append("PIRSF_ID")
        if searchParameter.showPMID == True:
            displayFieldKeys.append("PMID")
        if searchParameter.showPROName == True:
            displayFieldKeys.append("PRO_NAME")
        if searchParameter.showPRONamespace == True:
            displayFieldKeys.append("PRO_NAMESPACE")
        if searchParameter.showPROTermDefinition == True:
            displayFieldKeys.append("PRO_TERM_DEFINITION")
        if searchParameter.showParent == True:
            displayFieldKeys.append("PARENT")
        if searchParameter.showReactomeID == True:
            displayFieldKeys.append("REACTOME_ID")
        if searchParameter.showSynonym == True:
            displayFieldKeys.append("PRO_NAME_SYNONYMS")
        if searchParameter.showTaxonID == True:
            displayFieldKeys.append("TAXON_ID")
        if searchParameter.showUniProtKBID == True:
            displayFieldKeys.append("UNIPROTKB_ID")

        return displayFieldKeys

    def getPROTermsInfo(self, proTerms, searchParameter):

        #print(searchParameter.showAnnotation)
        if searchParameter.showAnnotation == True:
            proTerms, error = self.getAnnotationInfo(proTerms, searchParameter)
        proTerms, error = self.getNonAnnotationInfo(proTerms, searchParameter)

        return proTerms, error

    def getNonAnnotationInfo(self, proTerms, searchParameter):
        #print(searchParameter)
        proInfoQuery = self.constructPROInfoQuery(proTerms, searchParameter)
        #print(proInfoQuery)
        proInfoDicts, error = self.executeQuery(proInfoQuery)
            #print(proInfoDicts)
        #print(proInfoDicts)
        if error == None:
            for proInfoDict in proInfoDicts:
                keys = proInfoDict.keys()
                proTerm = self.getProTerm(proTerms, proInfoDict['id'])
                for key in keys:
                    if key == 'id':
                        proTerm.id = proInfoDict[key]
                    if key == 'alt_id':
                        proTerm.alt_id = proInfoDict[key]
                    if key == 'name':
                        proTerm.name = proInfoDict[key]
                    if key == 'namespace':
                        proTerm.namespace = proInfoDict[key]
                    if key == 'termDef':
                        proTerm.termDef = proInfoDict[key]
                        if proInfoDict['dbID']:
                            proTerm.termDef += " ["+proInfoDict['dbID']+"]"
                    if key == 'category':
                        proTerm.category = proInfoDict['category']
                    if key == 'anyRelationship':
                        proTerm.anyRelationship = proInfoDict['anyRelationship']
                    if key == 'child':
                        for child in proInfoDict['child'].split(", "):
                            proTerm.child.append(child)
                    if key == 'descendant':
                        for descendant in proInfoDict['descendant'].split(", "):
                            proTerm.descendant.append(descendant)
                    if key == 'comment':
                        proTerm.comment = proInfoDict['comment']
                    if key == 'ecoCycID':
                        proTerm.ecoCycID = proInfoDict['ecoCycID']
                    if key == 'geneName':
                        proTerm.geneName = proInfoDict['geneName']
                    if key == 'hgncID':
                        for hgncID in proInfoDict['hgncID'].split(", "):
                            proTerm.hgncID.append(hgncID)
                    if key == 'mgiID':
                        for mgiID in proInfoDict['mgiID'].split(", "):
                            proTerm.mgiID.append(mgiID)
                    if key == 'orthoIsoform':
                        for orthoIsoform in proInfoDict['orthoIsoform'].split(", "):
                            proTerm.orthoIsoform.append(orthoIsoform)
                    if key == 'orthoModform':
                        for orthoModform in proInfoDict['orthoModform'].split(", "):
                            proTerm.orthoModform.append(orthoModform)
                    if key == 'pantherID':
                        proTerm.pantherID = proInfoDict['pantherID']
                    if key == 'parent':
                        for parent in proInfoDict['parent'].split(", "):
                            proTerm.parent.append(parent)
                    if key == 'ancestor':
                        for ancestor in proInfoDict['ancestor'].split(", "):
                            proTerm.ancestor.append(ancestor)
                    if key == 'pirsfID':
                        proTerm.pirsfID = proInfoDict['pirsfID']
                    if key == 'pmID':
                        for pmID in proInfoDict['pmID'].split(", "):
                            proTerm.pmID.append(pmID)
                    if key == 'reactomeID':
                        for reactomeID in proInfoDict['reactomeID'].split(", "):
                            proTerm.reactomeID.append(reactomeID)
                    if key == 'synonym':
                        for synonym in proInfoDict['synonym'].split(", "):
                            proTerm.synonym.append(synonym)
                    if key == 'taxonID':
                        proTerm.taxonID = proInfoDict['taxonID']
                    if key == 'uniprotKBID':
                        for uniprotKBID in proInfoDict['uniprotKBID'].split(", "):
                            proTerm.uniprotKBID.append(uniprotKBID)
        #print(proTerms)
        return proTerms, error

    def getPROInfoOneByOne(self, proTerms, searchParameter, restriction):
        displayFieldKeys = self.getDisplayFieldKeys(searchParameter)
        proInfoDicts = []
        for proTerm in proTerms:
            values = "VALUES ?PRO_term {\n"
            id = proTerm.id
            id = id.lstrip('"')
            id = id.rstrip('"')
            id = id.replace(':', '_')
            values += "obo:" + id + " "
            values += "}\n"
            query = self.conf.cfg['prefix'] + "\n"
            select = ""
            where = values
            for field in displayFieldKeys:
                select += self.conf.select[field] + "\n"
                if field != "ANNOTATION" and self.conf.where[field] != None:
                    where += "OPTIONAL " + self.conf.where[field] + "\n"
            query += "SELECT\n"
            query += select + "\n"
            query += "WHERE\n"
            query += "{\n"
            query += where + "\n"
            query += "}\n"
            query += "ORDER BY DESC(?PRO_ID)\n"
            dict, error = self.executeQuery(query)

            proInfoDicts.append(dict)
            #print(proInfoDicts)
        return proInfoDicts, error



    def constructPROInfoQuery(self, proTerms, searchParameter):
        #print(searchParameter)
        displayFieldKeys = self.getDisplayFieldKeys(searchParameter)
        values = self.getValuesStatement(proTerms)
        query = self.conf.cfg['prefix'] + "\n"
        select = ""
        where = values
        for field in displayFieldKeys:
            select += self.conf.select[field]+"\n"
            if field != "ANNOTATION" and self.conf.where[field] != None:
                where += "OPTIONAL "+ self.conf.where[field]+"\n"
        query += "SELECT\n"
        query += select +"\n"
        query += "WHERE\n"
        query += "{\n"
        query += where+"\n"
        query += "}\n"
        query += "ORDER BY DESC(?PRO_ID)\n"

        #print(query)
        return query


    def constructPAFQuery(self, proTerms, searchParameter):
        select = self.conf.pafDSP['PAF_DSP']
        values = self.getValuesStatement(proTerms)
        where = values + self.conf.pafQueryCondition['PAF_DSP']
        query = self.conf.cfg['prefix'] + "\n"
        query += "SELECT\n"
        query += select+"\n"
        query += "WHERE\n"
        query += "{\n"
        query += where+"\n"
        query += "}\n"
        query += "ORDER BY DESC(?PRO_ID) ASC(?Ontology_Term)\n"
        return query

    def getAnnotationInfo(self, proTerms, searchParameter):
        pafQuery = self.constructPAFQuery(proTerms, searchParameter)
        #print(pafQuery)
        annotationDicts, error = self.executeQuery(pafQuery)
        # print(annotationDicts)
        if error == None:
            for annotationDict in annotationDicts:
                proID = annotationDict["proID"]
                annotation = Annotation()
                annotation.modifier = annotationDict['modifier']
                annotation.relation = annotationDict['relation']
                annotation.ontologyID = annotationDict['ontologyID']
                annotation.ontologyTerm = annotationDict['ontologyTerm']
                annotation.relativeTo = annotationDict['relativeTo']
                annotation.interactionWith = annotationDict['interactionWith']
                annotation.ncbiTaxonId = annotationDict['taxonID']
                annotation.inferredFrom = annotationDict['inferredFrom']
                evidence = Evidence()
                evidence.evidenceCode = annotationDict['evidenceCode']
                for source in annotationDict['evidenceSource'].split(", "):
                    evidence.evidenceSource.append(source)
                annotation.evidence = evidence
                proTerm = self.getProTerm(proTerms, proID)
                if proTerm != None:
                    proTerm.annotation.append(annotation)
        return proTerms, error

    def getProTerm(self, proTerms, proID):
        for proTerm in proTerms:
            if proTerm.id == proID:
                return proTerm
        return None

    def getValuesStatement(self, proTerms):
        values = "VALUES ?PRO_term {\n"
        for proTerm in proTerms:
            id = proTerm.id
            id = id.lstrip('"')
            id = id.rstrip('"')
            id = id.replace(':', '_')
            values += "obo:"+id+" "
        values += "}\n"
        return values



    def constructProIDsQuery(self, searchParameter, restriction):
        query = self.conf.cfg['prefix']+"\n"
        query += "SELECT " + self.conf.select['ID'] + "\n"
        query += "WHERE {"
        if (restriction == "ANCESTOR" or restriction == "DESCENDANT"):
            pass
        else:
            query += self.conf.where[restriction]
        filterQuery, updatedSearchParameter = self.constructFilterQuery(searchParameter)
        searchParameter = updatedSearchParameter
        query += filterQuery
        query += "}\n"
        query += "ORDER BY DESC(?PRO_ID)\n"
        query += "OFFSET "+searchParameter.offset+"\n"
        query += "LIMIT "+searchParameter.limit+"\n"
        #print(query)
        return query, searchParameter



    def constructFilterQuery(self, searchParameter):
        #print(searchParameter.searchField)
        query = ""
        value = searchParameter.searchValue.strip().replace('"', '').upper()
        if searchParameter.searchField.upper() == "ALLFIELDS" or searchParameter.searchField.upper() == "ANY_FIELD":
            if value == "" or value == "NOT NULL":
                query += self.conf.where['ID']
            else:
                query += "{\n"
                query += "      ?PRO_term oboInOwl:id ?PRO_ID .\n"
                query += "      ?PRO_term  pr_extra:allFields ?fieldValue . \n"
                query += "      ?fieldValue bif:contains \"'"+value+"'\"\n"
                query += "}\n"
                #searchField = searchParameter.searchField.upper()
                # query += "{\n"
                # query += self.conf.where['PRO_ID']
                # query += "}\n"
                # q, searchParameter = self.contructAllFieldFilterQuery("", searchField, searchParameter, value)
                # query += "{" + q +"}"
                #print(query)
        else:
            searchField = searchParameter.searchField.upper()
            query += "{\n"
            query += self.conf.where['PRO_ID']
            query += "}\n"
            query, searchParameter = self.contructFilterQuery(query, searchField, searchParameter, value)
        return query, searchParameter

    def contructAllFieldFilterQuery(self, query, searchField, searchParameter, value):
        allFieldQuery = ""
        allFieldQuery += "OPTIONAL {\n"
        ancestorFilterQuery, searchParameter = self.constructPRONameFilterQuery(query, searchParameter, value)
        allFieldQuery += ancestorFilterQuery
        allFieldQuery += "}\n"

        if searchField == "ALT_ID":
            query, searchParameter = self.constructAltIDFilterQuery(query, searchParameter, value)
        if searchField == "ANY_RELATIONSHIP":
            query, searchParameter = self.constructAnyRelationshipFilterQuery(query, searchParameter, value)
        if searchField == "CATEGORY":
            query, searchParameter = self.construtCategoryFilterQuery(query, searchParameter, value)
        if searchField == "CATEGORY_NOT_ORG":
            query, searchParameter = self.constructCategoryNotOrgFilterQuery(query, searchParameter, value)
        if searchField == "CHILD":
            query, searchParameter = self.constructChildFilterQuery(query, searchParameter, value)
        if searchField == "CHILDREN":
            query, searchParameter = self.constructChildrenFilterQuery(query, searchParameter, value)
        if searchField == "COMMENT":
            query, searchParameter = self.constructCommentFilterQuery(query, searchParameter, value)
        if searchField == "DESCENDANT":
            query, searchParameter = self.constructDescendantFilterQuery(query, searchParameter, value)
        if searchField == "ECOCYC_ID":
            query, searchParameter = self.constructEcoCycFilterQuery(query, searchParameter, value)
        if searchField == "GENE_NAME":
            query, searchParameter = self.constructGeneNameFilterQuery(query, searchParameter, value)
        if searchField == "HGNC_ID":
            query, searchParameter = self.constructHGNCFilterQuery(query, searchParameter, value)
        if searchField == "INTERACTION_WITH":
            query, searchParameter = self.constructIneractionWithFilterQuery(query, searchParameter, value)
        if searchField == "MGI_ID":
            query, searchParameter = self.constructMGIFilterQuery(query, searchParameter, value)
        if searchField == "ORTHO_ISOFORM":
            query, searchParameter = self.constructOrthoIsoformFilterQuery(query, searchParameter, value)
        if searchField == "ORTHO_MODFORM":
            query, searchParameter = self.constructOrthoModformFilterQuery(query, searchParameter, value)
        if searchField == "ONTOLOGY_ID":
            query, searchParameter = self.constructOntologyIDFilterQuery(query, searchParameter, value)
        if searchField == "ONTOLOGY_TERM":
            query, searchParameter = self.constructOntologyTermFilterQuery(query, searchParameter, value)
        if searchField == "PANTHER_ID":
            query, searchParameter = self.constructPantherIDFilterQuery(query, searchParameter, value)
        if searchField == "PRO_ID":
            query = self.constructPROIDFilterQuery(query, value)
        if searchField == "PARENT":
            query, searchParameter = self.constructParentFilterQuery(query, searchParameter, value)
        if searchField == "PARENTS":
            query, searchParameter = self.constructParentsFilterQuery(query, searchParameter, value)
        if searchField == "PIRSF_ID":
            query, searchParameter = self.constructPIRSFIDFilterQuery(query, searchParameter, value)
        if searchField == "PMID":
            query, searchParameter = self.constructPMIDFilterQuery(query, searchParameter, value)
        if searchField == "PRO_TERM_DEFINITION":
            query, searchParameter = self.constructPROTermDefFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAME":
            query, searchParameter = self.constructPRONameFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAMESPACE":
            query, searchParameter = self.constructPRONamespaceFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAME_SYNONYMS":
            query, searchParameter = self.constructPRONameSynonymsFilterQuery(query, searchParameter, value)
        if searchField == "REACTOME_ID":
            query, searchParameter = self.constructReactomeIDFilterQuery(query, searchParameter, value)
        if searchField == "RELATION":
            query, searchParameter = self.constructRelationFilterQuery(query, searchParameter, value)
        if searchField == "TAXON_ID":
            query, searchParameter = self.constructTaxonIDFilterQuery(query, searchParameter, value)
        if searchField == "UNIPROTKB_ID":
            query, searchParameter = self.constructUniProtKBIDFilterQuery(query, searchParameter, value)
        return allFieldQuery, searchParameter

    def contructFilterQuery(self, query, searchField, searchParameter, value):
        #print(searchParameter)
        if searchField == "ANCESTOR":
            query, searchParameter = self.constructAncestorFilterQuery(query, searchParameter, value)
        if searchField == "ANY_RELATIONSHIP":
            #print("????")
            query, searchParameter = self.constructAnyRelationshipFilterQuery(query, searchParameter, value)
        if searchField == "CATEGORY":
            query, searchParameter = self.construtCategoryFilterQuery(query, searchParameter, value)
        if searchField == "CATEGORY_NOT_ORG":
            query, searchParameter = self.constructCategoryNotOrgFilterQuery(query, searchParameter, value)
        if searchField == "CHILD":
            query, searchParameter = self.constructChildFilterQuery(query, searchParameter, value)
        if searchField == "CHILDREN":
            query, searchParameter = self.constructChildrenFilterQuery(query, searchParameter, value)
        if searchField == "COMMENT":
            query, searchParameter = self.constructCommentFilterQuery(query, searchParameter, value)
        if searchField == "DESCENDANT":
            query, searchParameter = self.constructDescendantFilterQuery(query, searchParameter, value)
        if searchField == "ECOCYC_ID":
            query, searchParameter = self.constructEcoCycFilterQuery(query, searchParameter, value)
        if searchField == "GENE_NAME":
            query, searchParameter = self.constructGeneNameFilterQuery(query, searchParameter, value)
        if searchField == "HGNC_ID":
            query, searchParameter = self.constructHGNCFilterQuery(query, searchParameter, value)
        if searchField == "INTERACTION_WITH":
            query, searchParameter = self.constructIneractionWithFilterQuery(query, searchParameter, value)
        if searchField == "MGI_ID":
            query, searchParameter = self.constructMGIFilterQuery(query, searchParameter, value)
        if searchField == "ORTHO_ISOFORM":
            query, searchParameter = self.constructOrthoIsoformFilterQuery(query, searchParameter, value)
        if searchField == "ORTHO_MODFORM":
            query, searchParameter = self.constructOrthoModformFilterQuery(query, searchParameter, value)
        if searchField == "ONTOLOGY_ID":
            query, searchParameter = self.constructOntologyIDFilterQuery(query, searchParameter, value)
        if searchField == "ONTOLOGY_TERM":
            query, searchParameter = self.constructOntologyTermFilterQuery(query, searchParameter, value)
        if searchField == "PANTHER_ID":
            query, searchParameter = self.constructPantherIDFilterQuery(query, searchParameter, value)
        if searchField == "PRO_ID":
            query = self.constructPROIDFilterQuery(query, value)
        if searchField == "PARENT":
            query, searchParameter = self.constructParentFilterQuery(query, searchParameter, value)
        if searchField == "PARENTS":
            query, searchParameter = self.constructParentsFilterQuery(query, searchParameter, value)
        if searchField == "PIRSF_ID":
            query, searchParameter = self.constructPIRSFIDFilterQuery(query, searchParameter, value)
        if searchField == "PMID":
            query, searchParameter = self.constructPMIDFilterQuery(query, searchParameter, value)
        if searchField == "PRO_TERM_DEFINITION":
            query, searchParameter = self.constructPROTermDefFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAME":
            query, searchParameter = self.constructPRONameFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAMESPACE":
            query, searchParameter = self.constructPRONamespaceFilterQuery(query, searchParameter, value)
        if searchField == "PRO_NAME_SYNONYMS":
            query, searchParameter = self.constructPRONameSynonymsFilterQuery(query, searchParameter, value)
        if searchField == "REACTOME_ID":
            query, searchParameter = self.constructReactomeIDFilterQuery(query, searchParameter, value)
        if searchField == "RELATION":
            query, searchParameter = self.constructRelationFilterQuery(query, searchParameter, value)
        if searchField == "TAXON_ID":
            query, searchParameter = self.constructTaxonIDFilterQuery(query, searchParameter, value)
        if searchField == "UNIPROTKB_ID":
            query, searchParameter = self.constructUniProtKBIDFilterQuery(query, searchParameter, value)
        return query, searchParameter

    def constructUniProtKBIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showUniProtKBID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["UNIPROTKB_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["UNIPROTKB_ID"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["UNIPROTKB_ID"]
            # query += "     FILTER(STRSTARTS(UCASE(STR(?UNIPROTKB_ID)),UCASE('UniProtKB:"+value+"'))|| CONTAINS(UCASE(STR(?UNIPROTKB_ID)), UCASE('"+value+"')))\n"
            # query += "}\n"
            query += "{\n"
            query += self.conf.where["UNIPROTKB_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?UNIPROTKB_ID)), UCASE('UniProtKB:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?UNIPROTKB_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter



    def constructTaxonIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showTaxonID = True
        query += "{\n"
        query += self.conf.where['PRO_ID']
        query += "}\n"
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["TAXON_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["TAXON_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["TAXON_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?NCBITaxon_ID)), UCASE('NCBITaxon_"+val+"')) ||"
                filter += "CONTAINS(UCASE(STR(?NCBITaxon_ID)), UCASE('"+val+"')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructRelationFilterQuery(self, query, searchParameter, value):
        searchParameter.showAnnotation = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["RELATION"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["RELATION"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["RELATION"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Relation)), UCASE('"+val+"')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructReactomeIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showReactomeID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["REACTOME_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["REACTOME_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["REACTOME_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?REACTOME_ID)), UCASE('Reactome:"+val+"')) ||"
                filter += "CONTAINS(UCASE(STR(?REACTOME_ID)), UCASE('"+val+"')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructPRONameSynonymsFilterQuery(self, query, searchParameter, value):
        searchParameter.showSynonym = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PRO_NAME_SYNONYMS"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PRO_NAME_SYNONYMS"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["PRO_NAME_SYNONYMS"]
            query += "     FILTER(CONTAINS(UCASE(STR(?synonym)), UCASE('"+value+"')))\n"
            query += "}\n"
        return query, searchParameter


    def constructPRONameFilterQuery(self, query, searchParameter, value):
        searchParameter.showPROName = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PRO_NAME"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PRO_NAME"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["PRO_NAME"]
            query += "  FILTER(CONTAINS(UCASE(STR(?Label)), UCASE('"+value+"')))\n"
            query += "}\n"
        return query, searchParameter

    def constructPRONamespaceFilterQuery(self, query, searchParameter, value):
        searchParameter.showPROName = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PRO_NAMESPACE"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PRO_NAMESPACE"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["PRO_NAMESPACE"]
            query += "  FILTER(CONTAINS(UCASE(STR(?Namspace)), UCASE('"+value+"')))\n"
            query += "}\n"
        return query, searchParameter


    def constructPROTermDefFilterQuery(self, query, searchParameter, value):
        searchParameter.showPROTermDefinition = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PRO_TERM_DEFINITION"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PRO_TERM_DEFINITION"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["PRO_TERM_DEFINITION"]
            query += "  FILTER(CONTAINS(UCASE(STR(?PRO_termDef)), UCASE('"+value+"')))\n"
            query += "}\n"
        return query, searchParameter

    def constructPMIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showPMID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PMID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PMID"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["PMID"]
            # query += "     FILTER(STRSTARTS(UCASE(STR(?PMID)),UCASE('PMID:"+value+"'))||CONTAINS(UCASE(STR(?PMID)), UCASE('"+value+"')))\n"
            # query += "}\n"
            query += "{\n"
            query += self.conf.where["PMID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?PMID)), UCASE('PMID:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?PMID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructPIRSFIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showPIRSFID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PIRSF_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PIRSF_ID"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["PIRSF_ID"]
            # query += "     FILTER(STRSTARTS(UCASE(STR(?PIRSF_ID)),UCASE('PIRSF:"+value+"'))||CONTAINS(UCASE(STR(?PIRSF_ID)), UCASE('"+value+"')))\n"
            # query += "}\n"
            query += "{\n"
            query += self.conf.where["PIRSF_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?PIRSF_ID)), UCASE('PIRSF:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?PIRSF_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructParentFilterQuery(self, query, searchParameter, value):
        searchParameter.showParent = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PARENT"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PARENT"]
            query += "}\n"
        else:
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Parent_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += "{\n"
            query += self.conf.where["PARENT"]
            query += filter + ")\n"
            #query += "     FILTER(CONTAINS(UCASE(STR(?Parent_ID)), UCASE('"+value+"')))\n"
            query += "}\n"
        return query, searchParameter


    def constructPantherIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showPANTHERID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PANTHER_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PANTHER_ID"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["PANTHER_ID"]
            # query += "     FILTER(STRSTARTS(UCASE(STR(?PANTHER_ID)),UCASE('PANTHER:"+value+"'))|| CONTAINS(UCASE(STR(?PANTHER_ID)), UCASE('"+value+"')))\n"
            # query += "}\n"
            query += "{\n"
            query += self.conf.where["PANTHER_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?PANTHER_ID)), UCASE('PANTHER:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?PANTHER_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructOntologyTermFilterQuery(self, query, searchParameter, value):
        searchParameter.showAnnotation = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ONTOLOGY_TERM"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ONTOLOGY_TERM"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ONTOLOGY_TERM"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Ontology_Term)), UCASE('"+val+"')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructOntologyIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showAnnotation = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ONTOLOGY_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ONTOLOGY_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ONTOLOGY_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Ontology_ID)), UCASE('"+val+"')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructOrthoModformFilterQuery(self, query, searchParameter, value):
        searchParameter.showOrthoModform = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ORTHO_MODFORM"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ORTHO_MODFORM"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ORTHO_MODFORM"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Ortho_modform)), UCASE('" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?Ortho_modform)), UCASE('" + val.replace(":", "_") + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructOrthoIsoformFilterQuery(self, query, searchParameter, value):
        searchParameter.showOrthoIsoform = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ORTHO_ISOFORM"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ORTHO_ISOFORM"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ORTHO_ISOFORM"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?Ortho_isoform_ID)), UCASE('" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?Ortho_isoform_ID)), UCASE('" + val.replace(":", "_") + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructIneractionWithFilterQuery(self, query, searchParameter, value):
        searchParameter.showAnnotation = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["INTERACTION_WITH"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["INTERACTION_WITH"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["INTERACTION_WITH"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "CONTAINS(UCASE(STR(?InteractionWith)), UCASE('" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?InteractionWith)), UCASE('" + val.replace(":", "_") + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructPROIDFilterQuery(self, query, value):
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PRO_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PRO_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["PRO_ID"]
            values = value.split()
            filter = "      FILTER("
            for v in values:
                filter += "UCASE(STR(?PRO_ID))=UCASE('PR:" + v + "') ||"
                filter += "UCASE(STR(?PRO_ID))=UCASE('PR_" + v + "') ||"
                filter += "UCASE(STR(?PRO_ID))=UCASE('" + v + "') ||"
                filter += "UCASE(STR(?PRO_ID))=UCASE('" + v.replace(":", "_") + "') ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query

    def constructMGIFilterQuery(self, query, searchParameter, value):
        searchParameter.showMGIID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["MGI_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["MGI_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["MGI_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?MGI_ID)), UCASE('MGI:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?MGI_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructHGNCFilterQuery(self, query, searchParameter, value):
        searchParameter.showHGNCID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["HGNC_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["HGNC_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["HGNC_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?HGNC_ID)), UCASE('HGNC:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?HGNC_ID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructGeneNameFilterQuery(self, query, searchParameter, value):
        searchParameter.showGeneName = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["GENE_NAME"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["GENE_NAME"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["GENE_NAME"]
            query += "     FILTER(CONTAINS(UCASE(STR(?g)), '" + value + "'))\n"
            query += "}\n"
        return query, searchParameter

    def constructEcoCycFilterQuery(self, query, searchParameter, value):
        searchParameter.showEcoCycID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ECOCYC_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ECOCYC_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ECOCYC_ID"]
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "STRSTARTS(UCASE(STR(?EcoCycID)), UCASE('EcoCyc:" + val + "')) ||"
                filter += "CONTAINS(UCASE(STR(?EcoCycID)), UCASE('" + val + "')) ||"
            filter = filter[:-2]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter


    def constructCommentFilterQuery(self, query, searchParameter, value):
        searchParameter.showComment = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["COMMENT"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["COMMENT"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["COMMENT"]
            query += "     FILTER(CONTAINS(UCASE(STR(?Comment)), '" + value + "'))\n"
            query += "}\n"
        return query, searchParameter

    def constructChildFilterQuery(self, query, searchParameter, value):
        searchParameter.showChild = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["CHILD"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["CHILD"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["CHILD"]
            query += "     FILTER(CONTAINS(UCASE(STR(?Child_ID)), UCASE('" + value + "')))\n"
            query += "}\n"
        return query, searchParameter

    def constructCategoryNotOrgFilterQuery(self, query, searchParameter, value):
        searchParameter.showCategory = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["CATEGORY_NOT_ORG"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["CATEGORY_NOT_ORG"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["CATEGORY_NOT_ORG"]
            query += "      FILTER(CONTAINS(UCASE(STR(?Category)), 'CATEGORY=" + value + "') && !CONTAINS(UCASE(STR(?Category)), UCASE('Category=organism')))\n"
            query += "}\n"
        return query, searchParameter

    def construtCategoryFilterQuery(self, query, searchParameter, value):
        searchParameter.showCategory = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["CATEGORY"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["CATEGORY"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["CATEGORY"]
            query += "      FILTER(CONTAINS(UCASE(STR(?Category)), 'CATEGORY=" + value + "') || CONTAINS(UCASE(STR(?Category)), '" + value + "'))\n"
            query += "}\n"
        return query, searchParameter

    def constructAnyRelationshipFilterQuery(self, query, searchParameter, value):
        searchParameter.showAnyRelationship = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += "      ?PRO_term  pr_extra:hasRelationshipWith ?AnyRelationship .\n"
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += "      ?PRO_term  pr_extra:hasRelationshipWith ?AnyRelationship .\n"
            query += "}\n"
        else:
            query += "{\n"
            query += "      ?PRO_term oboInOwl:id ?PRO_ID .\n"
            query += "      ?PRO_term  pr_extra:hasRelationshipWith ?AnyRelationship .\n"
            query += "      FILTER(bif:contains(?AnyRelationship, '\"" + value + "\"'))\n"
            query += "}\n"
        #print(query)
        return query, searchParameter

    def constructAncestorFilterQuery(self, query, searchParameter, value):
        searchParameter.showParent = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ANCESTOR"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ANCESTOR"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["ANCESTOR"]
            # query += "     FILTER(UCASE(STR(?PRO_ID)) = UCASE('"+value+"'))\n"
            # query += "}\n"
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "UCASE(STR(?PRO_ID)) = UCASE('" + val + "') ||"
            filter = filter[:-2]
            query += "{\n"
            query += self.conf.where["ANCESTOR"]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructDescendantFilterQuery(self, query, searchParameter, value):
        searchParameter.showParent = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["DESCENDANT"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["DESCENDANT"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["DESCENDANT"]
            # query += "     FILTER(UCASE(STR(?PRO_ID)) = UCASE('"+value+"'))\n"
            # query += "}\n"
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "UCASE(STR(?PRO_ID)) = UCASE('" + val + "') ||"
            filter = filter[:-2]
            query += "{\n"
            query += self.conf.where["DESCENDANT"]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructParentsFilterQuery(self, query, searchParameter, value):
        searchParameter.showParent = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["PARENTS"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["PARENTS"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["PARENTS"]
            # query += "     FILTER(UCASE(STR(?PRO_ID)) = UCASE('"+value+"'))\n"
            # query += "}\n"
            # query += "     FILTER(CONTAINS(UCASE(STR(?Parent_ID)), UCASE('"+value+"')))\n"
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "UCASE(STR(?PRO_ID)) = UCASE('" + val + "') ||"
            filter = filter[:-2]
            query += "{\n"
            query += self.conf.where["PARENT"]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructChildrenFilterQuery(self, query, searchParameter, value):
        searchParameter.showParent = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["CHILDREN"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["CHILDREN"]
            query += "}\n"
        else:
            # query += "{\n"
            # query += self.conf.where["CHILDREN"]
            # query += "     FILTER(UCASE(STR(?PRO_ID)) = UCASE('"+value+"'))\n"
            # query += "}\n"
            values = value.split()
            filter = "      FILTER("
            for val in values:
                filter += "UCASE(STR(?PRO_ID)) = UCASE('" + val + "') ||"
            filter = filter[:-2]
            query += "{\n"
            query += self.conf.where["CHILDREN"]
            query += filter + ")\n"
            query += "}\n"
        return query, searchParameter

    def constructAltIDFilterQuery(self, query, searchParameter, value):
        searchParameter.showAltID = True
        if value == "NULL" or value == "":
            query += "FILTER NOT EXISTS {\n"
            query += self.conf.where["ALT_ID"]
            query += "}\n"
        elif value == "NOT NULL":
            query += "{\n"
            query += self.conf.where["ALT_ID"]
            query += "}\n"
        else:
            query += "{\n"
            query += self.conf.where["ALT_ID"]
            query += "  FILTER(CONTAINS(UCASE(STR(?ALT_ID)), UCASE('" + value + "')))\n"
            query += "}\n"
        return query, searchParameter






