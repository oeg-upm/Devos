```mermaid
	classDiagram

    
    class LegalDocument {
    
    }

    class AudioVisualDocument {
    
    }

    class Document {
    
    }

    class DocumentStatus {
    
    }

    class DocumentPart {
    
    }

    class LegalCaseDocument {
    
    }

    class AudioDocument {
    
    }

    class CollectedDocument {
    
    }

    class PersonalCommunicationDocument {
    
    }



AudioVisualDocument  --> Agent   :director  

Document  --> Document   :citedBy  

Document  --> N95e6068e22b248678644ba531b870ebf   :editorList  

Event  --> Document   :presents  

Document  --> Document   :cites  

LegalDocument  --> Organization   :court  

Document  --> RDFSResource   :transcriptOf  

D  --> T   :C  

Document  --> RDFSResource   :reviewOf  

Document  --> DocumentStatus   :status  

Document  --> N2168c291ce454aa09fc04d97fbf8042c   :authorList  

PersonalCommunicationDocument  --> Agent   :recipient  

Document  --> Document   :translationOf  

Document  --> Document   :reproducedIn  

Document  --> Event   :presentedAt  

Document  --> Nced81265d5e043db88c1ab44e0c9a061   :contributorList  

```