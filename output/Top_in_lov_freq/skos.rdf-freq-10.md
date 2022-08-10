```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Nd4710cac099d4d70a1427f142be80884 {
    
    }

    class RDFList {
    
    }



SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

```