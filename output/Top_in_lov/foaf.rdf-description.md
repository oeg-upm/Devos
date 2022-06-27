```mermaid
	classDiagram

    
    class OnlineGamingAccount {
    
    }

    class Document {
    
    }

    class Person {
    
    }

    class OnlineAccount {
    
    }

    class PersonalProfileDocument {
    
    }

    class LabelProperty {
    
    }

    class Organization {
    
    }

    class Image {
    
    }

    class Agent {
    
    }

    class SpatialThing {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class OnlineChatAccount {
    
    }



Person  --> Person   :knows  

Person  --> Thing   :pastProject  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> OnlineAccount   :account  

SpatialThing  --> SpatialThing   :based_near  

Person  --> Document   :publications  

Agent  --> Document   :tipjar  

Person  --> Thing   :currentProject  

Agent  --> Thing   :made  

Document  --> Thing   :topic  

Person  --> Document   :workInfoHomepage  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

Person  --> Image   :img  

Agent  --> Document   :interest  

Agent  --> Document   :openid  

Group  --> Agent   :member  

Thing  --> Document   :homepage  

Image  --> Thing   :depicts  

Agent  --> Thing   :mbox  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Document   :weblog  

Person  --> Document   :workplaceHomepage  

Image  --> Image   :thumbnail  

Thing  --> Image   :depiction  

Person  --> Document   :schoolHomepage  

Thing  --> Document   :page  

```