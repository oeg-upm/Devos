```mermaid
	classDiagram

    
    class Agent {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class LabelProperty {
    
    }

    class OnlineAccount {
    
    }

    class SpatialThing {
    
    }

    class Image {
    
    }

    class Document {
    
    }

    class Organization {
    
    }

    class PersonalProfileDocument {
    
    }

    class OnlineGamingAccount {
    
    }

    class Person {
    
    }

    class OnlineChatAccount {
    
    }



Person  --> Person   :knows  

Person  --> Document   :schoolHomepage  

Person  --> Thing   :pastProject  

Person  --> Image   :img  

Document  --> Thing   :primaryTopic  

Image  --> Image   :thumbnail  

Agent  --> Document   :weblog  

Person  --> Document   :workInfoHomepage  

Agent  --> Thing   :mbox  

Thing  --> Document   :homepage  

Agent  --> Thing   :made  

OnlineAccount  --> Document   :accountServiceHomepage  

Person  --> Document   :workplaceHomepage  

Agent  --> Document   :interest  

SpatialThing  --> SpatialThing   :based_near  

Person  --> Thing   :currentProject  

Thing  --> Agent   :maker  

Thing  --> Image   :depiction  

Group  --> Agent   :member  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Thing   :topic_interest  

Document  --> Thing   :topic  

Agent  --> OnlineAccount   :account  

Person  --> Document   :publications  

Thing  --> Document   :page  

Image  --> Thing   :depicts  

Agent  --> Document   :tipjar  

Agent  --> Document   :openid  

```