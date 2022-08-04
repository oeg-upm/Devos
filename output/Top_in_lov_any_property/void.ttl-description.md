```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class DatasetDescription {
    
    }



Dataset  --> Dataset   :classPartition  

Dataset  --> RDFSResource   :dataDump  

Document  --> Dataset   :inDataset  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Document   :openSearchDescription  

Linkset  --> Dataset   :target  

```