
# Protein Ontology RESTful APIs

This project implements RESTful APIs for Protein Ontology using Django REST framework

## Requirement
Python 2.7+

## Installation
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
## Usage
Example: get information about PRO term PR:000025934.

http://127.0.0.1:8000/pros/PR:000025934/?showPROName=true&showPRONamespace=true&showPROTermDefinition=true&showCategory=true&showComment=true&showEcoCycID=true&showGeneName=true&showHGNCID=true&showMGIID=true&showOrthoIsoform=true&showOrthoModifiedForm=true&showPANTHERID=true&showPIRSFID=true&showPMID=true&showReactomeID=true&showSynonym=true&showTaxonID=true&showUniProtKBID=true

For details, please see the [documentation](https://lod.proconsortium.org/api.html) as defined by [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification) and implemented by [Swagger UI](https://swagger.io/tools/swagger-ui/).
