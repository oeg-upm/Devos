```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Nf7dbc22f11f240fba35dfe66c078d00f {
    
    }

    class RDFList {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```