```mermaid
	classDiagram

    
    class Person {
    
    }

    class PersonalProfileDocument {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class Group {
    
    }

    class Agent {
    
    }

    class OnlineGamingAccount {
    
    }

    class OnlineAccount {
    
    }

    class Document {
    
    }

    class Image {
    
    }

    class Organization {
    
    }

    class OnlineChatAccount {
    
    }

    class Project {
    
    }

    class Person {
    
    }

    class Group {
    
    }

    class Agent {
    
    }

    class SpatialThing {
    
    }

    class Document {
    
    }

    class OnlineAccount {
    
    }

    class Image {
    
    }



Person  --> Image   :img  

Person  --> Document   :interest  

Person  --> Person   :knows  

Person  --> Document   :publications  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workInfoHomepage  

Person  --> Document   :workplaceHomepage  

Group  --> Agent   :member  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Document   :tipjar  

Agent  --> Document   :weblog  

OnlineAccount  --> Document   :accountServiceHomepage  

SpatialThing  --> SpatialThing   :based_near  

Image  --> Image   :thumbnail  

```