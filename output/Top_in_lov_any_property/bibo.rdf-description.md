```mermaid
	classDiagram

    
    class LegalDocument {
    
    }

    class Document {
    
    }

    class AudioDocument {
    
    }

    class DocumentPart {
    
    }

    class LegalCaseDocument {
    
    }

    class PersonalCommunicationDocument {
    
    }

    class DocumentStatus {
    
    }

    class CollectedDocument {
    
    }

    class AudioVisualDocument {
    
    }



Document  --> Nf67297da0fab40eaa57dcc325708c8dc   :authorList  

D  --> T   :C  

Document  --> RDFSResource   :reviewOf  

PersonalCommunicationDocument  --> Agent   :recipient  

LegalDocument  --> Organization   :court  

AudioVisualDocument  --> Agent   :director  

Document  --> Document   :translationOf  

Document  --> DocumentStatus   :status  

Event  --> Document   :presents  

Document  --> N8c641edc335644d0a599ad2e64d61bf3   :contributorList  

Document  --> N08824c58c5f1436aa6b5abda27602723   :editorList  

Document  --> Event   :presentedAt  

Document  --> Document   :reproducedIn  

Document  --> Document   :cites  

Document  --> Document   :citedBy  

Document  --> RDFSResource   :transcriptOf  

```