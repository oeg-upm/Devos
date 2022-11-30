```mermaid
	classDiagram

    
    class Object Property {
    
    }

    class Datatype Property {
    
    }

    class Functional Property {
    
    }

    class Contributor List {
    
    }

    class Named Individual {
    
    }

    class Class {
    
    }

    class List {
    
    }



Publication  --> Contributor List   :Editor List  

Publication  --> Contributor List   :Author List  

List  --> List   :rest  

List  --> List   :first  

```