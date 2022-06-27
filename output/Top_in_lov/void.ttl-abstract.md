```mermaid
	classDiagram

    
    class DatasetDescription {
    
    }

    class Linkset {
    
    }

    class TechnicalFeature {
    
    }

    class Dataset {
    
    }



Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Dataset   :subset  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :classPartition  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> RDFProperty   :linkPredicate  

Linkset  --> Dataset   :target  

```