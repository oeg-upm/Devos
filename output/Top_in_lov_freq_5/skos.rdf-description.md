```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Nb51330ff1fbc45099115566ffe38c15f {
    
    }

    class RDFList {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```