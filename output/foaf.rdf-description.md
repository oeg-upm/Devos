```mermaid
	classDiagram

    
    class SpatialThing {
    
    }

    class LabelProperty {
    
    }

    class OnlineGamingAccount {
    
    }

    class Group {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class Image {
    
    }

    class Project {
    
    }

    class OnlineChatAccount {
    
    }

    class OnlineAccount {
    
    }

    class Person {
    
    }

    class Agent {
    
    }

    class Organization {
    
    }

    class Document {
    
    }

    class PersonalProfileDocument {
    
    }

    class SpatialThing {
    
    }

    class Group {
    
    }

    class Image {
    
    }

    class OnlineAccount {
    
    }

    class Person {
    
    }

    class Agent {
    
    }

    class Document {
    
    }



SpatialThing  --> SpatialThing   :based_near  

Group  --> Agent   :member  

Image  --> Thing   :depicts  

Image  --> Image   :thumbnail  

Person  --> Image   :img  

Thing  --> Image   :depiction  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> OnlineAccount   :account  

Agent  --> OnlineAccount   :holdsAccount  

Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Thing  --> Document   :homepage  

Agent  --> Document   :weblog  

Agent  --> Document   :openid  

Agent  --> Document   :tipjar  

Person  --> Document   :workplaceHomepage  

Person  --> Document   :workInfoHomepage  

Person  --> Document   :schoolHomepage  

Agent  --> Document   :interest  

Person  --> Document   :publications  

Thing  --> Document   :page  

Person  --> Person   :knows  

Person  --> Thing   :currentProject  

Person  --> Thing   :pastProject  

Agent  --> Thing   :mbox  

Agent  --> Thing   :made  

Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

```