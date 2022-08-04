```mermaid
	classDiagram

    
    class NobleFamily {
    
    }

    class NationalAnthem {
    
    }

    class GolfPlayer {
    
    }

    class StatedResolution {
    
    }

    class PhilosophicalConcept {
    
    }

    class Publisher {
    
    }

    class SupremeCourtOfTheUnitedStatesCase {
    
    }

    class Cinema {
    
    }

    class HotSpring {
    
    }

    class Athlete {
    
    }

    class PersonFunction {
    
    }

    class جُغرافیائی_سیاسیات_تنظیم {
    
    }

    class File {
    
    }

    class گرم_پانی_کاقدرتی_چشم {
    
    }

    class MusicGenre {
    
    }

    class GeopoliticalOrganisation {
    
    }

    class TopicalConcept {
    
    }

    class University {
    
    }

    class OfficeHolder {
    
    }

    class Species {
    
    }

    class TheatreDirector {
    
    }

    class Island {
    
    }

    class Settlement {
    
    }

    class Windmill {
    
    }

    class AdministrativeRegion {
    
    }

    class Deity {
    
    }

    class Person {
    
    }

    class Broadcaster {
    
    }

    class ChristianDoctrine {
    
    }

    class Woman {
    
    }

    class Colour {
    
    }

    class Work {
    
    }

    class TheologicalConcept {
    
    }

    class آبادی_والی_جگہ۔ {
    
    }

    class Theatre {
    
    }

    class PopulatedPlace {
    
    }

    class OlympicResult {
    
    }

    class Embryology {
    
    }

    class Play {
    
    }

    class Judge {
    
    }

    class Library {
    
    }

    class Animal {
    
    }

    class PoliticalParty {
    
    }

    class Man {
    
    }

    class Athletics {
    
    }

    class Instrument {
    
    }

    class ScientificConcept {
    
    }

    class SnookerPlayer {
    
    }

    class HistoricalSettlement {
    
    }

    class Station {
    
    }

    class MathematicalConcept {
    
    }

    class Municipality {
    
    }

    class FormerMunicipality {
    
    }

    class DBpedian {
    
    }

    class ChartsPlacements {
    
    }

    class Place {
    
    }



Person  --> Place   :announcedFrom  

Place  --> Place   :closeTo  

Person  --> Place   :livingPlace  

PoliticalParty  --> PoliticalParty   :splitFromParty  

University  --> Person   :officerInCharge  

RouteOfTransportation  --> Place   :routeEndLocation  

Island  --> Island   :majorIsland  

Restaurant  --> Person   :headChef  

OlympicResult  --> OlympicResult   :summerAppearances  

Road  --> PopulatedPlace   :ruralMunicipality  

MusicGenre  --> MusicGenre   :derivative  

Broadcaster  --> BroadcastNetwork   :formerBroadcastNetwork  

RouteOfTransportation  --> Station   :routeStart  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Person  --> Organisation   :federation  

Athlete  --> SportsLeague   :currentLeague  

Person  --> Place   :bodyDiscovered  

Organisation  --> Person   :chairperson  

Sport  --> Person   :footedness  

Place  --> Area   :wholeArea  

Place  --> Place   :northWestPlace  

Place  --> PopulatedPlace   :district  

AdministrativeRegion  --> Person   :landeshauptmann  

Work  --> Person   :author  

GrandPrix  --> Person   :secondDriver  

RouteOfTransportation  --> Station   :routeJunction  

Athlete  --> SportsTeam   :ncaaTeam  

Island  --> PopulatedPlace   :managementRegion  

Species  --> Species   :family  

Settlement  --> Group   :minority  

SportsEvent  --> Athlete   :mostSuccessfulPlayer  

Organisation  --> Person   :ceo  

Band  --> Person   :bandMember  

TelevisionShow  --> Person   :presenter  

PopulatedPlace  --> Population   :population  

Person  --> SKOSConcept   :endReign  

Settlement  --> Population   :agglomerationPopulation  

Species  --> Species   :tribus  

Place  --> Place   :westPlace  

PopulatedPlace  --> Department   :department  

Person  --> SKOSConcept   :mastersWins  

Place  --> PopulatedPlace   :nearestCity  

File  --> File   :fileURL  

SportsEvent  --> Athlete   :championInMixedDouble  

Woman  --> Person   :mother  

LegalCase  --> Person   :attorneyGeneral  

Athlete  --> SportsTeam   :oldTeamCoached  

Canal  --> Person   :principalEngineer  

Athlete  --> Country   :sportCountry  

Athlete  --> SportsTeam   :debutTeam  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Place  --> PopulatedPlace   :regency  

Athlete  --> SportsTeam   :coachClub  

EducationalInstitution  --> Person   :alumni  

PopulatedPlace  --> Language   :regionalLanguage  

Person  --> SKOSConcept   :world  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Person  --> List   :relatedFunctions  

Place  --> Place   :supply  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Organisation  --> PersonFunction   :leaderFunction  

Person  --> EducationalInstitution   :college  

Person  --> Work   :created  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

BodyOfWater  --> Island   :island  

Person  --> SportsEvent   :competitionTitle  

Shrine  --> Deity   :enshrinedDeity  

Artist  --> Instrument   :instrument  

HistoricBuilding  --> Person   :pastor  

Place  --> Place   :mainIsland  

Place  --> Place   :previousEntity  

Place  --> Place   :endPoint  

SportsEvent  --> Athlete   :champion  

Person  --> RadioStation   :radio  

Place  --> River   :river  

OfficeHolder  --> PoliticalParty   :otherParty  

Species  --> Taxon   :superFamily  

PopulatedPlace  --> PopulatedPlace   :principalArea  

FormerMunicipality  --> Municipality   :municipalityAbsorbedBy  

Restaurant  --> Person   :chef  

Organisation  --> PopulatedPlace   :headquarter  

Settlement  --> Place   :daira  

Person  --> CareerStation   :careerStation  

MilitaryUnit  --> PopulatedPlace   :garrison  

PopulatedPlace  --> Area   :agglomerationArea  

TelevisionShow  --> Person   :coExecutiveProducer  

VideoGame  --> Person   :gameArtist  

Place  --> Species   :flower  

Settlement  --> Settlement   :canton  

Settlement  --> Place   :highestPoint  

Animal  --> Animal   :sire  

Work  --> Agent   :producer  

Musical  --> Person   :musicBy  

Island  --> Mountain   :capitalMountain  

Athlete  --> SportsTeam   :teamCoached  

LegalCase  --> Judge   :judge  

PopulatedPlace  --> Saint   :saint  

Island  --> Country   :governmentCountry  

RouteOfTransportation  --> Place   :routeStartLocation  

SportsTeam  --> Person   :generalManager  

Place  --> Organisation   :governingBody  

Place  --> PopulatedPlace   :lowestPlace  

Athlete  --> SportsTeam   :managerClub  

Man  --> Person   :uncle  

SportsTeam  --> Person   :manager  

Place  --> Altitude   :altitude  

Island  --> PopulatedPlace   :capitalRegion  

Species  --> Species   :subTribus  

Species  --> Species   :species  

Legislature  --> Settlement   :meetingCity  

Species  --> Species   :superTribus  

Newspaper  --> Person   :associateEditor  

SportsEvent  --> Athlete   :championInDoubleMale  

SportsEvent  --> Athlete   :championInDoubleFemale  

Work  --> Person   :chiefEditor  

EducationalInstitution  --> Person   :custodian  

Place  --> Place   :northPlace  

Athlete  --> Sport   :sportSpecialty  

Person  --> Project   :project  

Athlete  --> SportsTeam   :juniorTeam  

Person  --> Person   :parent  

GrandPrix  --> Person   :firstDriver  

Newspaper  --> Person   :managingEditor  

Man  --> Person   :brother  

TelevisionShow  --> Person   :showJudge  

Person  --> Person   :colleague  

Island  --> PopulatedPlace   :capitalDistrict  

Place  --> Place   :northEastPlace  

Place  --> Species   :bird  

Organisation  --> Place   :regionServed  

Settlement  --> Settlement   :adjacentSettlement  

River  --> PopulatedPlace   :mouthDistrict  

Person  --> SKOSConcept   :britishWins  

Athlete  --> SportsTeam   :formerTeam  

RouteOfTransportation  --> Station   :routeEnd  

Species  --> Species   :fossil  

PopulatedPlace  --> Demographics   :previousDemographics  

PopulatedPlace  --> PopulatedPlace   :borough  

Work  --> Person   :coverArtist  

Athlete  --> Person   :trainer  

School  --> Person   :headteacher  

Person  --> Person   :sibling  

PublicTransitSystem  --> Station   :importantStation  

MilitaryUnit  --> Person   :fourthCommander  

Film  --> Person   :director  

School  --> Person   :nobelLaureates  

MilitaryUnit  --> Person   :notableCommander  

Island  --> SpatialThing   :capitalPosition  

Person  --> SKOSConcept   :usopenWins  

Person  --> SpatialThing   :restingPlacePosition  

Athlete  --> SportsTeam   :youthClub  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Place   :educationPlace  

Person  --> Person   :friend  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

SoccerClub  --> Place   :ground  

TelevisionShow  --> Work   :openingTheme  

Band  --> Person   :formerBandMember  

Organisation  --> Person   :secretaryGeneral  

Animal  --> Place   :birthPlace  

FigureSkater  --> Person   :formerChoreographer  

Settlement  --> Place   :settlementAttached  

Artwork  --> Person   :painter  

Settlement  --> Settlement   :mergedSettlement  

Person  --> Diploma   :diploma  

Scientist  --> Person   :academicAdvisor  

WrittenWork  --> Person   :prefaceBy  

Album  --> Person   :compiler  

Person  --> Person   :relative  

Person  --> Person   :opponent  

River  --> PopulatedPlace   :mouthState  

Place  --> SpatialThing   :lowestPosition  

River  --> Place   :sourceConfluenceRegion  

Island  --> PopulatedPlace   :governmentRegion  

TelevisionShow  --> Person   :storyEditor  

Place  --> Place   :eastPlace  

EducationalInstitution  --> Person   :actingHeadteacher  

Species  --> Taxon   :subFamily  

Family  --> Person   :headOfFamily  

Island  --> PopulatedPlace   :capitalPlace  

School  --> Person   :executiveHeadteacher  

Place  --> Mountain   :lowestMountain  

River  --> PopulatedPlace   :sourceConfluenceState  

Race  --> Person   :recentWinner  

Legislature  --> PoliticalParty   :politicalPartyInLegislature  

SportsEvent  --> Person   :medalist  

Island  --> PopulatedPlace   :lowestState  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Ship  --> Place   :homeport  

Settlement  --> PopulatedPlace   :jointCommunity  

Instrument  --> MusicalArtist   :musicians  

Person  --> Person   :copilote  

Film  --> Person   :editing  

Person  --> Person   :child  

Department  --> PopulatedPlace   :subprefecture  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Man  --> Person   :son  

Person  --> Person   :cousurper  

Work  --> Person   :translator  

FigureSkater  --> Person   :choreographer  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

NobleFamily  --> Family   :mainFamilyBranch  

Person  --> Country   :nationality  

Person  --> Tournament   :continentalTournament  

NobleFamily  --> Family   :otherFamilyBranch  

FictionalCharacter  --> Species   :entourage  

PopulatedPlace  --> Language   :officialLanguage  

Work  --> Person   :composer  

Place  --> PopulatedPlace   :biggestCity  

SportsEvent  --> Person   :bronzeMedalist  

Language  --> PopulatedPlace   :spokenIn  

Place  --> RouteStop   :isRouteStop  

Person  --> MilitaryService   :militaryService  

Settlement  --> Settlement   :twinTown  

Place  --> Place   :subregion  

Place  --> PersonFunction   :politicalLeader  

Athlete  --> SportsTeam   :nflTeam  

Work  --> MusicalArtist   :musicComposer  

Person  --> Place   :residence  

Place  --> Place   :land  

Organisation  --> Person   :administrator  

OlympicResult  --> OlympicResult   :otherAppearances  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> Person   :leaderName  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Olympics  --> Person   :olympicOathSwornByJudge  

EducationalInstitution  --> Person   :principal  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Person  --> Sport   :sportDiscipline  

Municipality  --> FormerMunicipality   :hasAbsorbedMunicipality  

Saint  --> PopulatedPlace   :beatifiedPlace  

Broadcaster  --> Broadcaster   :sisterStation  

Place  --> Place   :locatedInArea  

Island  --> Building   :building  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

PopulatedPlace  --> Place   :touristicSite  

Saint  --> Person   :beatifiedBy  

Animal  --> Animal   :damsire  

Work  --> Actor   :starring  

Family  --> Person   :lastFamilyMember  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Athlete  --> SportsTeam   :currentTeam  

PopulatedPlace  --> Agglomeration   :agglomeration  

Island  --> PopulatedPlace   :highestRegion  

Settlement  --> Person   :bourgmestre  

Person  --> Tournament   :nationalTournament  

Island  --> Place   :subdivisionName  

GrandPrix  --> Person   :thirdDriver  

Person  --> Person   :spouse  

Work  --> Agent   :publisher  

Settlement  --> PoliticalParty   :politicalMajority  

PoliticalParty  --> Person   :spokesperson  

Magazine  --> Person   :previousEditor  

Work  --> Work   :basedOn  

Place  --> Place   :nextEntity  

Work  --> Person   :writer  

Person  --> Person   :collaboration  

Animal  --> Animal   :grandsire  

Place  --> Sea   :sea  

Person  --> EducationalInstitution   :almaMater  

Person  --> Organisation   :employer  

Film  --> Person   :cinematography  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

TelevisionShow  --> Person   :creativeDirector  

PopulatedPlace  --> City   :capital  

Food  --> Person   :creatorOfDish  

Politician  --> Person   :prefect  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Race  --> Person   :firstWinner  

Mountain  --> Person   :firstAscentPerson  

Person  --> SportsTeam   :teamManager  

Settlement  --> Place   :wilaya  

Saint  --> PopulatedPlace   :canonizedPlace  

Broadcaster  --> BroadcastNetwork   :broadcastNetwork  

Woman  --> Person   :daughter  

Settlement  --> PopulatedPlace   :federalState  

Person  --> Film   :movie  

Broadcaster  --> Broadcaster   :network  

Legislature  --> PoliticalParty   :politicalPartyOfLeader  

Document  --> File   :galleryItem  

Person  --> Person   :relation  

Athlete  --> SportsTeam   :club  

FigureSkater  --> Person   :formerCoach  

Olympics  --> Person   :torchBearer  

Person  --> EthnicGroup   :ethnicity  

Agent  --> Settlement   :hometown  

Person  --> PersonFunction   :otherOccupation  

PopulatedPlace  --> Legislature   :legislature  

Place  --> Depth   :depths  

Scientist  --> Person   :doctoralAdvisor  

SportsEvent  --> Athlete   :championInSingleFemale  

MusicalWork  --> Person   :lyrics  

Place  --> Province   :province  

Place  --> Place   :hasInsidePlace  

Island  --> Island   :rightChild  

TelevisionEpisode  --> Person   :guest  

Film  --> Person   :setDesigner  

SportsTeam  --> Person   :currentMember  

Person  --> Person   :dubber  

Organisation  --> Person   :superintendent  

Olympics  --> Person   :olympicOathSwornBy  

Person  --> Contest   :contest  

Olympics  --> Person   :officialOpenedBy  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Organisation  --> Person   :trustee  

MusicalWork  --> PopulatedPlace   :recordedIn  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Organisation  --> Person   :chaplain  

Scientist  --> Person   :doctoralStudent  

Person  --> SportsTeam   :currentTeamManager  

Place  --> Place   :southWestPlace  

GrandPrix  --> Person   :fastestDriver  

Place  --> Species   :tree  

Athlete  --> Athletics   :athleticsDiscipline  

Scientist  --> Person   :notableStudent  

Family  --> Person   :primogenitor  

Athlete  --> Athletics   :otherSportsExperience  

MilitaryUnit  --> Person   :secondCommander  

Person  --> SKOSConcept   :startReign  

Monarch  --> Person   :heir  

AnatomicalStructure  --> Embryology   :precursor  

Person  --> Work   :debutWork  

Canal  --> Place   :originalStartPoint  

River  --> PopulatedPlace   :mouthRegion  

Person  --> Person   :usurper  

PopulatedPlace  --> Population   :previousPopulation  

OlympicResult  --> OlympicResult   :winterAppearances  

Animal  --> Place   :deathPlace  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Place  --> Province   :provinceLink  

Island  --> PopulatedPlace   :lowestRegion  

FigureSkater  --> Person   :currentPartner  

PopulatedPlace  --> Person   :viceLeader  

Person  --> Country   :stateOfOrigin  

LegalCase  --> Person   :solicitorGeneral  

SportsEvent  --> Athlete   :championInDouble  

EducationalInstitution  --> Person   :rector  

Work  --> Person   :mainCharacter  

SkiResort  --> Place   :massif  

Work  --> Work   :subsequentWork  

Man  --> Person   :father  

FormerMunicipality  --> Municipality   :presentMunicipality  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Work  --> Place   :releaseLocation  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Person  --> Tournament   :olympicGames  

Place  --> Altitude   :lowestAltitude  

Person  --> Person   :student  

Settlement  --> PopulatedPlace   :administrativeDistrict  

FictionalCharacter  --> Species   :enemy  

Settlement  --> PopulatedPlace   :largestMetro  

Person  --> Tournament   :worldTournament  

PopulatedPlace  --> PopulatedPlace   :sheading  

Person  --> Person   :seiyu  

AdministrativeRegion  --> Place   :administrativeCenter  

Canal  --> Place   :originalEndPoint  

Settlement  --> Place   :lowestPoint  

EducationalInstitution  --> Person   :dean  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> SportsLeague   :leagueManager  

Island  --> PopulatedPlace   :governmentPlace  

Film  --> Person   :makeupArtist  

Island  --> Island   :leftChild  

Settlement  --> PopulatedPlace   :frazioni  

Athlete  --> Sport   :horseRidingDiscipline  

Work  --> Language   :originalLanguage  

MusicGenre  --> MusicGenre   :musicFusionGenre  

Place  --> Place   :southEastPlace  

Film  --> Person   :specialEffects  

Person  --> Person   :detractor  

Saint  --> Person   :canonizedBy  

Woman  --> Person   :sister  

WrittenWork  --> Person   :illustrator  

School  --> Person   :vicePrincipal  

```