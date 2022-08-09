```mermaid
	classDiagram

    
    class ProperInterval {
    
    }

    class TemporalEntity {
    
    }

    class Instant {
    
    }

    class GeneralDateTimeDescription {
    
    }

    class DayOfWeek {
    
    }



Instant  --> TimePosition   :inTimePosition  

GeneralDateTimeDescription  --> TimeZone   :timeZone  

ProperInterval  --> ProperInterval   :intervalAfter  

ProperInterval  --> ProperInterval   :intervalMetBy  

ProperInterval  --> ProperInterval   :intervalIn  

ProperInterval  --> ProperInterval   :intervalStarts  

ProperInterval  --> ProperInterval   :intervalOverlaps  

ProperInterval  --> ProperInterval   :intervalDuring  

ProperInterval  --> ProperInterval   :intervalEquals  

TemporalEntity  --> TemporalEntity   :after  

Instant  --> TemporalPosition   :inTemporalPosition  

ProperInterval  --> ProperInterval   :intervalBefore  

ProperInterval  --> ProperInterval   :intervalStartedBy  

ProperInterval  --> ProperInterval   :intervalMeets  

TemporalEntity  --> Instant   :hasEnd  

ProperInterval  --> ProperInterval   :intervalDisjoint  

DateTimeInterval  --> GeneralDateTimeDescription   :hasDateTimeDescription  

ProperInterval  --> ProperInterval   :intervalFinishedBy  

ProperInterval  --> ProperInterval   :intervalFinishes  

Interval  --> Instant   :inside  

GeneralDateTimeDescription  --> DayOfWeek   :dayOfWeek  

ProperInterval  --> ProperInterval   :intervalOverlappedBy  

GeneralDateTimeDescription  --> MonthOfYear   :monthOfYear  

Instant  --> GeneralDateTimeDescription   :inDateTime  

TemporalEntity  --> TemporalEntity   :before  

TemporalEntity  --> Instant   :hasBeginning  

ProperInterval  --> ProperInterval   :intervalContains  

TemporalEntity  --> TemporalDuration   :hasTemporalDuration  

```