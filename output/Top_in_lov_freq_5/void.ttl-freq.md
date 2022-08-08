```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class RDFSResource {
    
    }

    class TechnicalFeature {
    
    }

    class RDFProperty {
    
    }

    class Document {
    
    }



Dataset  --> Dataset   :subset  

Dataset  --> Document   :openSearchDescription  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Dataset   :propertyPartition  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :classPartition  

Dataset  --> RDFSResource   :exampleResource  

Linkset  --> Dataset   :target  

```