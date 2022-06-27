```mermaid
	classDiagram

    
    class جُغرافیائی_سیاسیات_تنظیم {
    
    }

    class آبادی_والی_جگہ۔ {
    
    }

    class Person {
    
    }

    class TheatreDirector {
    
    }

    class Animal {
    
    }

    class GolfPlayer {
    
    }

    class HistoricalSettlement {
    
    }

    class TopicalConcept {
    
    }

    class FormerMunicipality {
    
    }

    class Place {
    
    }

    class Municipality {
    
    }

    class PersonFunction {
    
    }

    class GeopoliticalOrganisation {
    
    }

    class OfficeHolder {
    
    }

    class TheologicalConcept {
    
    }

    class MathematicalConcept {
    
    }

    class HotSpring {
    
    }

    class Theatre {
    
    }

    class Station {
    
    }

    class ChristianDoctrine {
    
    }

    class Embryology {
    
    }

    class Windmill {
    
    }

    class Instrument {
    
    }

    class SupremeCourtOfTheUnitedStatesCase {
    
    }

    class Athlete {
    
    }

    class Work {
    
    }

    class Broadcaster {
    
    }

    class Publisher {
    
    }

    class Library {
    
    }

    class NobleFamily {
    
    }

    class Settlement {
    
    }

    class PhilosophicalConcept {
    
    }

    class PopulatedPlace {
    
    }

    class Colour {
    
    }

    class AdministrativeRegion {
    
    }

    class OlympicResult {
    
    }

    class Island {
    
    }

    class Judge {
    
    }

    class University {
    
    }

    class DBpedian {
    
    }

    class Play {
    
    }

    class Man {
    
    }

    class Cinema {
    
    }

    class ScientificConcept {
    
    }

    class MusicGenre {
    
    }

    class PoliticalParty {
    
    }

    class ChartsPlacements {
    
    }

    class Athletics {
    
    }

    class Woman {
    
    }

    class StatedResolution {
    
    }

    class SnookerPlayer {
    
    }

    class Species {
    
    }

    class NationalAnthem {
    
    }

    class گرم_پانی_کاقدرتی_چشم {
    
    }

    class Deity {
    
    }

    class File {
    
    }



Olympics  --> Person   :officialOpenedBy  

Person  --> Person   :seiyu  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

EducationalInstitution  --> Person   :alumni  

Place  --> Place   :supply  

Person  --> Tournament   :continentalTournament  

TelevisionShow  --> Person   :creativeDirector  

School  --> Person   :headteacher  

RouteOfTransportation  --> Place   :routeEndLocation  

Island  --> PopulatedPlace   :highestRegion  

Place  --> Species   :flower  

Person  --> Person   :collaboration  

Scientist  --> Person   :doctoralAdvisor  

Band  --> Person   :bandMember  

River  --> Place   :sourceConfluenceRegion  

SportsEvent  --> Athlete   :mostSuccessfulPlayer  

Person  --> Person   :opponent  

Broadcaster  --> BroadcastNetwork   :formerBroadcastNetwork  

Work  --> Place   :releaseLocation  

Man  --> Person   :son  

Settlement  --> Person   :bourgmestre  

Work  --> Person   :chiefEditor  

Broadcaster  --> Broadcaster   :network  

PopulatedPlace  --> Population   :population  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

Person  --> SKOSConcept   :endReign  

Artwork  --> Person   :painter  

Sport  --> Person   :footedness  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Work  --> Work   :subsequentWork  

FictionalCharacter  --> Species   :enemy  

Organisation  --> Person   :trustee  

Island  --> PopulatedPlace   :governmentPlace  

River  --> PopulatedPlace   :sourceConfluenceState  

School  --> Person   :vicePrincipal  

Scientist  --> Person   :academicAdvisor  

Person  --> Diploma   :diploma  

Work  --> Agent   :producer  

AdministrativeRegion  --> Place   :administrativeCenter  

SportsEvent  --> Person   :bronzeMedalist  

Person  --> RadioStation   :radio  

Settlement  --> Place   :settlementAttached  

SportsEvent  --> Athlete   :championInDoubleMale  

Athlete  --> Country   :sportCountry  

Place  --> Place   :westPlace  

Settlement  --> Place   :wilaya  

Department  --> PopulatedPlace   :subprefecture  

Person  --> Work   :debutWork  

Person  --> Country   :stateOfOrigin  

Organisation  --> PopulatedPlace   :headquarter  

Band  --> Person   :formerBandMember  

Animal  --> Animal   :damsire  

Island  --> Mountain   :capitalMountain  

MusicGenre  --> MusicGenre   :derivative  

Island  --> PopulatedPlace   :lowestState  

Place  --> Place   :southWestPlace  

GrandPrix  --> Person   :secondDriver  

Place  --> PersonFunction   :politicalLeader  

Species  --> Taxon   :subFamily  

Person  --> Organisation   :employer  

PopulatedPlace  --> Population   :previousPopulation  

Athlete  --> Sport   :horseRidingDiscipline  

Island  --> PopulatedPlace   :capitalPlace  

Island  --> Island   :leftChild  

Race  --> Person   :recentWinner  

Island  --> PopulatedPlace   :governmentRegion  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Person  --> List   :relatedFunctions  

Person  --> Person   :copilote  

Document  --> File   :galleryItem  

Shrine  --> Deity   :enshrinedDeity  

Woman  --> Person   :mother  

OlympicResult  --> OlympicResult   :winterAppearances  

Island  --> Island   :rightChild  

FigureSkater  --> Person   :currentPartner  

PopulatedPlace  --> Department   :department  

PoliticalParty  --> Person   :spokesperson  

GrandPrix  --> Person   :firstDriver  

PopulatedPlace  --> Person   :leaderName  

Animal  --> Place   :deathPlace  

Species  --> Species   :species  

Person  --> Organisation   :federation  

TelevisionShow  --> Person   :presenter  

Municipality  --> FormerMunicipality   :hasAbsorbedMunicipality  

Athlete  --> SportsTeam   :stateOfOriginTeam  

GrandPrix  --> Person   :fastestDriver  

Place  --> Organisation   :governingBody  

SportsEvent  --> Athlete   :championInMixedDouble  

Person  --> EducationalInstitution   :college  

Athlete  --> SportsTeam   :currentTeam  

EducationalInstitution  --> Person   :actingHeadteacher  

SoccerClub  --> Place   :ground  

Species  --> Species   :family  

SportsTeam  --> Person   :currentMember  

Work  --> MusicalArtist   :musicComposer  

Work  --> Person   :coverArtist  

PublicTransitSystem  --> Station   :importantStation  

Person  --> Place   :bodyDiscovered  

Canal  --> Place   :originalStartPoint  

Legislature  --> PoliticalParty   :politicalPartyInLegislature  

Canal  --> Place   :originalEndPoint  

Family  --> Person   :primogenitor  

SportsEvent  --> Athlete   :championInDouble  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Person  --> Person   :spouse  

Ship  --> Place   :homeport  

Place  --> PopulatedPlace   :sovereignCountry  

SportsTeam  --> Person   :generalManager  

Athlete  --> SportsTeam   :oldTeamCoached  

SportsEvent  --> Athlete   :champion  

Island  --> Island   :majorIsland  

FictionalCharacter  --> Species   :entourage  

Race  --> Person   :firstWinner  

Person  --> Person   :child  

Person  --> Person   :parent  

Person  --> Person   :sibling  

Organisation  --> Place   :regionServed  

Settlement  --> PopulatedPlace   :administrativeDistrict  

BodyOfWater  --> Island   :island  

Place  --> Place   :northWestPlace  

Work  --> Actor   :starring  

School  --> Person   :nobelLaureates  

Person  --> Work   :created  

Legislature  --> Settlement   :meetingCity  

EducationalInstitution  --> Person   :custodian  

Place  --> Place   :northEastPlace  

Place  --> PopulatedPlace   :district  

PopulatedPlace  --> PopulatedPlace   :borough  

Place  --> Place   :hasOutsidePlace  

Athlete  --> SportsTeam   :juniorTeam  

File  --> File   :fileURL  

Canal  --> Person   :principalEngineer  

Person  --> Place   :educationPlace  

Person  --> Project   :project  

Person  --> EthnicGroup   :ethnicity  

Place  --> PopulatedPlace   :nearestCity  

TelevisionShow  --> Person   :storyEditor  

Place  --> Place   :hasInsidePlace  

Work  --> Person   :mainCharacter  

Settlement  --> PoliticalParty   :politicalMajority  

Person  --> Film   :movie  

Work  --> Language   :originalLanguage  

SportsEvent  --> Athlete   :championInDoubleFemale  

Legislature  --> PoliticalParty   :politicalPartyOfLeader  

FigureSkater  --> Person   :formerCoach  

GrandPrix  --> Person   :thirdDriver  

Person  --> Person   :friend  

MusicalWork  --> PopulatedPlace   :recordedIn  

PopulatedPlace  --> Place   :touristicSite  

Place  --> Place   :eastPlace  

Person  --> CareerStation   :careerStation  

Island  --> PopulatedPlace   :capitalDistrict  

TelevisionShow  --> Work   :openingTheme  

EducationalInstitution  --> Person   :principal  

LegalCase  --> Person   :solicitorGeneral  

Broadcaster  --> Broadcaster   :sisterStation  

Person  --> Person   :dubber  

PopulatedPlace  --> City   :capital  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

LegalCase  --> Person   :attorneyGeneral  

Athlete  --> SportsTeam   :ncaaTeam  

Man  --> Person   :brother  

Person  --> SportsTeam   :currentTeamManager  

PopulatedPlace  --> PopulatedPlace   :sheading  

Film  --> Person   :makeupArtist  

Saint  --> Person   :beatifiedBy  

Road  --> PopulatedPlace   :ruralMunicipality  

Person  --> SKOSConcept   :world  

Film  --> Person   :editing  

Island  --> Place   :subdivisionName  

Work  --> Person   :composer  

Place  --> Place   :previousEntity  

Athlete  --> SportsTeam   :teamCoached  

Film  --> Person   :specialEffects  

Place  --> River   :river  

Mountain  --> Person   :firstAscentPerson  

Place  --> Place   :endPoint  

Island  --> PopulatedPlace   :managementRegion  

Person  --> SportsLeague   :leagueManager  

Organisation  --> Person   :superintendent  

Person  --> Person   :detractor  

PopulatedPlace  --> Legislature   :legislature  

PoliticalParty  --> PoliticalParty   :splitFromParty  

Person  --> SKOSConcept   :startReign  

Place  --> PopulatedPlace   :regency  

PopulatedPlace  --> Language   :regionalLanguage  

Athlete  --> SportsTeam   :managerClub  

Person  --> SKOSConcept   :mastersWins  

Person  --> EducationalInstitution   :almaMater  

Place  --> PopulatedPlace   :lowestPlace  

PopulatedPlace  --> Area   :agglomerationArea  

Athlete  --> SportsTeam   :youthClub  

Place  --> Place   :subregion  

Scientist  --> Person   :notableStudent  

NobleFamily  --> Family   :mainFamilyBranch  

Family  --> Person   :lastFamilyMember  

FormerMunicipality  --> Municipality   :municipalityAbsorbedBy  

Person  --> Tournament   :worldTournament  

Settlement  --> PopulatedPlace   :federalState  

PopulatedPlace  --> PopulatedPlace   :principalArea  

River  --> PopulatedPlace   :mouthRegion  

Place  --> SpatialThing   :lowestPosition  

Organisation  --> PersonFunction   :leaderFunction  

RouteOfTransportation  --> Station   :routeJunction  

VideoGame  --> Person   :gameArtist  

Restaurant  --> Person   :headChef  

Work  --> Person   :author  

Instrument  --> MusicalArtist   :musicians  

Person  --> SKOSConcept   :usopenWins  

Athlete  --> Sport   :sportSpecialty  

Saint  --> PopulatedPlace   :beatifiedPlace  

Species  --> Species   :fossil  

Athlete  --> SportsTeam   :coachClub  

Person  --> SportsTeam   :teamManager  

Island  --> SpatialThing   :capitalPosition  

Person  --> SKOSConcept   :britishWins  

Scientist  --> Person   :doctoralStudent  

Restaurant  --> Person   :chef  

Work  --> Person   :translator  

PopulatedPlace  --> Person   :viceLeader  

Place  --> Area   :wholeArea  

River  --> PopulatedPlace   :mouthDistrict  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Man  --> Person   :father  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :mainIsland  

MilitaryUnit  --> Person   :fourthCommander  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> Place   :announcedFrom  

Person  --> Country   :nationality  

Man  --> Person   :uncle  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

PopulatedPlace  --> Agglomeration   :agglomeration  

Species  --> Taxon   :superFamily  

TelevisionEpisode  --> Person   :guest  

Organisation  --> Person   :ceo  

Person  --> Contest   :contest  

Monarch  --> Person   :heir  

FormerMunicipality  --> Municipality   :presentMunicipality  

Artist  --> Instrument   :instrument  

River  --> PopulatedPlace   :mouthState  

Album  --> Person   :compiler  

Olympics  --> Person   :olympicOathSwornBy  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

MilitaryUnit  --> Person   :notableCommander  

Film  --> Person   :cinematography  

SportsEvent  --> Person   :medalist  

Settlement  --> Place   :daira  

LegalCase  --> Judge   :judge  

Place  --> Province   :province  

Place  --> Province   :provinceLink  

Settlement  --> Settlement   :mergedSettlement  

School  --> Person   :executiveHeadteacher  

Film  --> Person   :setDesigner  

TelevisionShow  --> Person   :showJudge  

Person  --> Person   :relative  

RouteOfTransportation  --> Place   :routeStartLocation  

Organisation  --> Person   :secretaryGeneral  

Athlete  --> SportsLeague   :currentLeague  

Work  --> Person   :writer  

Species  --> Species   :tribus  

Settlement  --> Settlement   :canton  

Species  --> Species   :subTribus  

Newspaper  --> Person   :associateEditor  

Person  --> Place   :residence  

Work  --> Agent   :publisher  

Settlement  --> Group   :minority  

MilitaryUnit  --> Person   :secondCommander  

Place  --> Species   :tree  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Settlement  --> PopulatedPlace   :largestMetro  

AdministrativeRegion  --> Person   :landeshauptmann  

Settlement  --> PopulatedPlace   :frazioni  

Settlement  --> PopulatedPlace   :jointCommunity  

Person  --> Place   :livingPlace  

Place  --> Species   :bird  

TelevisionShow  --> Person   :coExecutiveProducer  

Person  --> Person   :student  

Person  --> Sport   :sportDiscipline  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Woman  --> Person   :daughter  

EducationalInstitution  --> Person   :dean  

Animal  --> Place   :birthPlace  

RouteOfTransportation  --> Station   :routeStart  

Musical  --> Person   :musicBy  

Person  --> Person   :relation  

PopulatedPlace  --> Language   :officialLanguage  

SportsTeam  --> Person   :manager  

Place  --> Altitude   :lowestAltitude  

Film  --> Person   :director  

Organisation  --> Person   :chaplain  

WrittenWork  --> Person   :prefaceBy  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Settlement  --> Place   :lowestPoint  

Organisation  --> Person   :chairperson  

Animal  --> Animal   :sire  

Settlement  --> Settlement   :twinTown  

Athlete  --> SportsTeam   :nflTeam  

Place  --> Depth   :depths  

Place  --> Place   :northPlace  

Place  --> PopulatedPlace   :biggestCity  

Place  --> Place   :land  

Person  --> Person   :cousurper  

Place  --> Mountain   :lowestMountain  

Broadcaster  --> BroadcastNetwork   :broadcastNetwork  

Animal  --> Animal   :grandsire  

Person  --> Tournament   :olympicGames  

Place  --> Place   :closeTo  

Work  --> Work   :basedOn  

Place  --> RouteStop   :isRouteStop  

Island  --> PopulatedPlace   :capitalRegion  

MusicGenre  --> MusicGenre   :musicFusionGenre  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Family  --> Person   :headOfFamily  

SportsEvent  --> Athlete   :championInSingleFemale  

Place  --> Place   :southEastPlace  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

AnatomicalStructure  --> Embryology   :precursor  

Species  --> Species   :superTribus  

NobleFamily  --> Family   :otherFamilyBranch  

Politician  --> Person   :prefect  

Person  --> MilitaryService   :militaryService  

Olympics  --> Person   :olympicOathSwornByJudge  

Person  --> SportsEvent   :competitionTitle  

University  --> Person   :officerInCharge  

Saint  --> PopulatedPlace   :canonizedPlace  

Saint  --> Person   :canonizedBy  

Place  --> Altitude   :altitude  

Athlete  --> Person   :trainer  

Island  --> Building   :building  

Settlement  --> Settlement   :adjacentSettlement  

Athlete  --> Athletics   :athleticsDiscipline  

Settlement  --> Population   :agglomerationPopulation  

Athlete  --> SportsTeam   :formerTeam  

Settlement  --> Place   :highestPoint  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Person  --> SpatialThing   :restingPlacePosition  

PopulatedPlace  --> Saint   :saint  

MilitaryUnit  --> PopulatedPlace   :garrison  

Place  --> Sea   :sea  

OlympicResult  --> OlympicResult   :summerAppearances  

MusicalWork  --> Person   :lyrics  

FigureSkater  --> Person   :choreographer  

Person  --> Tournament   :nationalTournament  

RouteOfTransportation  --> Station   :routeEnd  

Island  --> Country   :governmentCountry  

Newspaper  --> Person   :managingEditor  

Athlete  --> SportsTeam   :debutTeam  

EducationalInstitution  --> Person   :rector  

Woman  --> Person   :sister  

Agent  --> Settlement   :hometown  

Place  --> Place   :nextEntity  

Organisation  --> Person   :administrator  

Olympics  --> Person   :torchBearer  

Athlete  --> Athletics   :otherSportsExperience  

OfficeHolder  --> PoliticalParty   :otherParty  

HistoricBuilding  --> Person   :pastor  

Person  --> PersonFunction   :otherOccupation  

Language  --> PopulatedPlace   :spokenIn  

SkiResort  --> Place   :massif  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Person  --> Person   :colleague  

FigureSkater  --> Person   :formerChoreographer  

Food  --> Person   :creatorOfDish  

WrittenWork  --> Person   :illustrator  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

PopulatedPlace  --> Demographics   :previousDemographics  

Magazine  --> Person   :previousEditor  

Place  --> Place   :locatedInArea  

OlympicResult  --> OlympicResult   :otherAppearances  

Island  --> PopulatedPlace   :lowestRegion  

Athlete  --> SportsTeam   :club  

```