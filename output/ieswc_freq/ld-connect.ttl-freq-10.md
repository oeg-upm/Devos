```mermaid
	classDiagram

    
    class Issue {
    
    }

    class ContributorList {
    
    }

    class List {
    
    }

    class Category {
    
    }

    class Journal {
    
    }

    class Volume {
    
    }

    class Series {
    
    }

    class Book {
    
    }

    class Chapter {
    
    }

    class Accessibility {
    
    }



Publication  --> Accessibility   :publicationAccessibility  

Article  --> Issue   :articleInIssue  

Publication  --> ContributorList   :publicationEditorList  

Chapter  --> Book   :chapterInBook  

Publication  --> ContributorList   :publicationAuthorList  

Publication  --> Issue   :publicationInIssue  

List  --> List   :first  

Publication  --> Chapter   :publicationInChapter  

Volume  --> Journal   :volumeInJournal  

Journal  --> Category   :category  

Series  --> Category   :category  

Book  --> Series   :bookInSeries  

Isssue  --> Volume   :issueInVolume  

List  --> List   :rest  

```