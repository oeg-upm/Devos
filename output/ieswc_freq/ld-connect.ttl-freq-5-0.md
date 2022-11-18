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



List  --> List   :rest  

Isssue  --> Volume   :issueInVolume  

Publication  --> string   :sourceFile  

Publication  --> ContributorList   :publicationAuthorList  

Book  --> Series   :bookInSeries  

Series  --> Category   :category  

Publication  --> Accessibility   :publicationAccessibility  

Publication  --> Issue   :publicationInIssue  

List  --> List   :first  

Publication  --> Chapter   :publicationInChapter  

Journal  --> Category   :category  

Volume  --> Journal   :volumeInJournal  

Publication  --> ContributorList   :publicationEditorList  

```