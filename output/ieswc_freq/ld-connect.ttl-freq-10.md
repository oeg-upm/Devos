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



Volume  --> Journal   :volumeInJournal  

Contributor  --> Organization   :contributorAffiliation  

Contributor  --> Role   :contributorRole  

Publication  --> XSDstring   :sourceFile  

List  --> List   :rest  

Publication  --> ContributorList   :publicationEditorList  

Publication  --> Issue   :publicationInIssue  

Publication  --> Accessibility   :publicationAccessibility  

Isssue  --> Volume   :issueInVolume  

Book  --> Series   :bookInSeries  

Organization  --> GeocodedLocation   :geocodingOutput  

GeocodedLocation  --> Geometry   :geometry  

Publication  --> Chapter   :publicationInChapter  

List  --> List   :first  

Journal  --> Category   :category  

Publication  --> ContributorList   :publicationAuthorList  

Series  --> Category   :category  

Chapter  --> Book   :chapterInBook  

```