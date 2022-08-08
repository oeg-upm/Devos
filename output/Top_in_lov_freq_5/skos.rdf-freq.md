```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Nfaf3d61c85f1446b80cf05feabc5d969 {
    
    }

    class RDFList {
    
    }



SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

```