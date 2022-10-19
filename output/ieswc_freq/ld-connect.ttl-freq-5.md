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



List  --> List   :rest  

Publication  --> Issue   :publicationInIssue  

Publication  --> ContributorList   :publicationAuthorList  

Journal  --> Category   :category  

Series  --> Category   :category  

Volume  --> Journal   :volumeInJournal  

Article  --> Issue   :articleInIssue  

List  --> List   :first  

Publication  --> ContributorList   :publicationEditorList  

```