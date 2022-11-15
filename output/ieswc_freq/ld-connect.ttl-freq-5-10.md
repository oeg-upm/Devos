```mermaid
	classDiagram

    
    class Publication {
    
    }

    class List {
    
    }

    class Journal {
    
    }

    class Series {
    
    }

    class Volume {
    
    }



List  --> List   :first  

Isssue  --> Volume   :issueInVolume  

Publication  --> Accessibility   :publicationAccessibility  

Series  --> Category   :category  

Volume  --> Journal   :volumeInJournal  

Publication  --> ContributorList   :publicationEditorList  

List  --> List   :rest  

Book  --> Series   :bookInSeries  

Journal  --> Category   :category  

```