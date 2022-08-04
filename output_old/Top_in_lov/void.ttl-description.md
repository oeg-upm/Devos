```mermaid
	classDiagram

    
    class Linkset {
    
    }

    class TechnicalFeature {
    
    }

    class DatasetDescription {
    
    }

    class Dataset {
    
    }



Dataset  --> RDFSResource   :exampleResource  

Dataset  --> RDFSResource   :dataDump  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> Dataset   :classPartition  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Document   :openSearchDescription  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> Dataset   :target  

Dataset  --> Dataset   :subset  

```