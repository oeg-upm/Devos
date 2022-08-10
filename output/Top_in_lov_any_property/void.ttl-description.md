```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class DatasetDescription {
    
    }



Dataset  --> TechnicalFeature   :feature  

Linkset  --> Dataset   :target  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :classPartition  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Dataset   :subset  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :propertyPartition  

```