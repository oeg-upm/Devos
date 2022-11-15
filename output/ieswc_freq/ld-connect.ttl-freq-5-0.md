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



Publication  --> ContributorList   :publicationEditorList  

Publication  --> string   :sourceFile  

Publication  --> Accessibility   :publicationAccessibility  

Publication  --> Issue   :publicationInIssue  

Series  --> Category   :category  

Book  --> Series   :bookInSeries  

Journal  --> Category   :category  

Publication  --> ContributorList   :publicationAuthorList  

Volume  --> Journal   :volumeInJournal  

List  --> List   :rest  

Publication  --> Chapter   :publicationInChapter  

Isssue  --> Volume   :issueInVolume  

List  --> List   :first  

```