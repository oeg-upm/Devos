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

    class Book {
    
    }

    class Chapter {
    
    }

    class Contributor {
    
    }

    class Organization {
    
    }

    class GeocodedLocation {
    
    }



Journal  --> Category   :category  

Isssue  --> Volume   :issueInVolume  

Contributor  --> Organization   :contributorAffiliation  

Publication  --> Chapter   :publicationInChapter  

Volume  --> Journal   :volumeInJournal  

Chapter  --> Book   :chapterInBook  

List  --> List   :first  

Publication  --> string   :sourceFile  

Publication  --> Accessibility   :publicationAccessibility  

GeocodedLocation  --> Geometry   :geometry  

Publication  --> Issue   :publicationInIssue  

Publication  --> ContributorList   :publicationEditorList  

Series  --> Category   :category  

Organization  --> GeocodedLocation   :geocodingOutput  

Book  --> Series   :bookInSeries  

Contributor  --> Role   :contributorRole  

List  --> List   :rest  

Publication  --> ContributorList   :publicationAuthorList  

```