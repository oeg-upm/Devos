```mermaid
	classDiagram

    
    class Person {
    
    }

    class PopulatedPlace {
    
    }

    class Place {
    
    }

    class SportsTeam {
    
    }

    class Award {
    
    }

    class Organisation {
    
    }

    class MeanOfTransportation {
    
    }

    class Country {
    
    }

    class Species {
    
    }

    class Agent {
    
    }



Olympics  --> Person   :torchBearer  

Family  --> Person   :lastFamilyMember  

PoliticalParty  --> Person   :spokesperson  

WrittenWork  --> Agent   :firstPublisher  

EducationalInstitution  --> Person   :actingHeadteacher  

Person  --> Person   :friend  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Settlement  --> Place   :lowestPoint  

Place  --> Place   :subregion  

WrittenWork  --> Person   :prefaceBy  

Athlete  --> SportsTeam   :formerTeam  

ResearchProject  --> Organisation   :fundedBy  

MilitaryUnit  --> MeanOfTransportation   :aircraftBomber  

MilitaryUnit  --> MeanOfTransportation   :aircraftTransport  

Saint  --> PopulatedPlace   :canonizedPlace  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> SKOSConcept   :usopenWins  

School  --> Person   :headteacher  

Person  --> Country   :nationality  

Actor  --> Award   :nationalFilmAward  

Man  --> Person   :brother  

Species  --> Taxon   :superFamily  

Olympics  --> Person   :olympicOathSwornByJudge  

Band  --> Person   :bandMember  

Species  --> Species   :fossil  

Person  --> SportsTeam   :teamManager  

Island  --> PopulatedPlace   :capitalDistrict  

Species  --> Species   :subTribus  

Person  --> Work   :debutWork  

FigureSkater  --> Person   :currentPartner  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterMultirole  

River  --> PopulatedPlace   :sourceConfluenceState  

Place  --> Place   :hasInsidePlace  

SportsTeam  --> Person   :generalManager  

Place  --> Species   :bird  

Organisation  --> City   :locationCity  

GrandPrix  --> Country   :secondDriverCountry  

Person  --> EducationalInstitution   :almaMater  

Country  --> Continent   :continent  

HistoricBuilding  --> Person   :pastor  

Place  --> Place   :closeTo  

FigureSkater  --> Person   :formerChoreographer  

Actor  --> Award   :geminiAward  

Place  --> PopulatedPlace   :regency  

Place  --> Province   :provinceLink  

ResearchProject  --> Organisation   :projectCoordinator  

MilitaryUnit  --> Person   :notableCommander  

MeanOfTransportation  --> MeanOfTransportation   :relatedMeanOfTransportation  

Person  --> Person   :colleague  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Film  --> Person   :setDesigner  

Island  --> Country   :governmentCountry  

Department  --> PopulatedPlace   :subprefecture  

Race  --> Person   :recentWinner  

Olympics  --> Person   :olympicOathSwornBy  

Person  --> Tournament   :worldTournament  

Saint  --> PopulatedPlace   :beatifiedPlace  

Work  --> Person   :composer  

Mountain  --> Person   :firstAscentPerson  

Work  --> Person   :writer  

Organisation  --> PopulatedPlace   :headquarter  

PopulatedPlace  --> Population   :population  

TermOfOffice  --> Person   :presidentGeneralCouncil  

River  --> PopulatedPlace   :mouthDistrict  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Settlement  --> PopulatedPlace   :largestMetro  

Monarch  --> Person   :heir  

TelevisionShow  --> Person   :presenter  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Settlement  --> Place   :daira  

Work  --> Person   :coverArtist  

Organisation  --> Person   :chairperson  

Place  --> Place   :northWestPlace  

EducationalInstitution  --> Person   :principal  

Organisation  --> Person   :chaplain  

Settlement  --> Place   :highestPoint  

Species  --> Species   :family  

Person  --> Person   :detractor  

GrandPrix  --> Person   :fastestDriver  

Scientist  --> Person   :academicAdvisor  

MusicalWork  --> Person   :lyrics  

Person  --> RadioStation   :radio  

Actor  --> Award   :goldenRaspberryAward  

Person  --> Work   :created  

Comedian  --> Award   :britishComedyAwards  

Artist  --> Award   :filmFareAward  

Person  --> Person   :student  

Person  --> Sport   :sportDiscipline  

Woman  --> Person   :mother  

LegalCase  --> Person   :solicitorGeneral  

Work  --> Person   :chiefEditor  

Actor  --> Award   :naacpImageAward  

FictionalCharacter  --> Species   :enemy  

Place  --> Place   :southEastPlace  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Restaurant  --> Person   :chef  

Film  --> Person   :editing  

Place  --> Place   :mainIsland  

Person  --> Place   :educationPlace  

Person  --> Person   :parent  

Film  --> Person   :specialEffects  

Person  --> Contest   :contest  

PopulatedPlace  --> Place   :touristicSite  

Film  --> Person   :director  

GrandPrix  --> Person   :firstDriver  

Work  --> Agent   :producer  

MilitaryUnit  --> PopulatedPlace   :garrison  

TelevisionShow  --> Person   :creativeDirector  

Person  --> SpatialThing   :restingPlacePosition  

Place  --> PopulatedPlace   :biggestCity  

Agent  --> Artist   :artPatron  

Artist  --> Award   :academyAward  

SportsTeam  --> TeamMember   :currentTeamMember  

Place  --> Place   :nextEntity  

Artist  --> Award   :emmyAward  

Actor  --> Award   :goldenCalfAward  

Musical  --> Person   :musicBy  

Island  --> PopulatedPlace   :managementRegion  

Species  --> Species   :superTribus  

Family  --> Person   :headOfFamily  

EducationalInstitution  --> Person   :alumni  

EducationalInstitution  --> Person   :dean  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterAttack  

Agent  --> TermOfOffice   :regionalCouncil  

MilitaryUnit  --> Person   :secondCommander  

Olympics  --> Person   :officialOpenedBy  

Place  --> Place   :southWestPlace  

Person  --> Tournament   :nationalTournament  

Settlement  --> Place   :settlementAttached  

Person  --> Place   :residence  

Person  --> Person   :relation  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterTransport  

Animal  --> Place   :deathPlace  

GrandPrix  --> Person   :thirdDriver  

PopulatedPlace  --> Population   :previousPopulation  

Place  --> Place   :eastPlace  

Agent  --> Settlement   :hometown  

Actor  --> Award   :iftaAward  

Place  --> Place   :previousEntity  

PopulatedPlace  --> Demographics   :previousDemographics  

PopulatedPlace  --> Person   :viceLeader  

GrandPrix  --> SportsTeam   :secondTeam  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterObservation  

MilitaryUnit  --> Person   :fourthCommander  

Athlete  --> Country   :sportCountry  

TelevisionShow  --> Person   :showJudge  

Artist  --> Award   :gaudiAward  

University  --> Person   :officerInCharge  

PopulatedPlace  --> Language   :officialLanguage  

Person  --> SportsEvent   :competitionTitle  

Place  --> SpatialThing   :lowestPosition  

Species  --> Taxon   :subFamily  

GrandPrix  --> Country   :fastestDriverCountry  

Actor  --> Award   :laurenceOlivierAward  

Person  --> Person   :collaboration  

Organisation  --> Person   :administrator  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Person  --> Project   :project  

Person  --> SKOSConcept   :britishWins  

Ship  --> Place   :homeport  

Island  --> PopulatedPlace   :lowestState  

Island  --> PopulatedPlace   :governmentRegion  

PopulatedPlace  --> Language   :regionalLanguage  

River  --> Country   :sourceConfluenceCountry  

Work  --> Person   :translator  

Island  --> Place   :subdivisionName  

Magazine  --> Person   :previousEditor  

MilitaryUnit  --> MeanOfTransportation   :aircraftRecon  

Artist  --> Award   :goldenGlobeAward  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Person  --> Person   :dubber  

Person  --> Diploma   :diploma  

SoccerClub  --> Place   :ground  

Food  --> Person   :creatorOfDish  

Woman  --> Person   :sister  

Film  --> Person   :cinematography  

Aircraft  --> Organisation   :aircraftUser  

Cartoon  --> Agent   :animator  

PopulatedPlace  --> PopulatedPlace   :sheading  

Person  --> Person   :copilote  

Species  --> Species   :species  

River  --> PopulatedPlace   :mouthRegion  

River  --> PopulatedPlace   :mouthState  

Person  --> Person   :sibling  

Person  --> Person   :spouse  

Country  --> TopLevelDomain   :topLevelDomain  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> Species   :flower  

Person  --> MilitaryService   :militaryService  

MilitaryUnit  --> MeanOfTransportation   :aircraftTrainer  

Place  --> Mountain   :lowestMountain  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Place  --> RouteStop   :isRouteStop  

PublicTransitSystem  --> MeanOfTransportation   :vehiclesInFleet  

SkiResort  --> Place   :massif  

Person  --> Country   :stateOfOrigin  

Canal  --> Place   :originalEndPoint  

Settlement  --> PopulatedPlace   :federalState  

Person  --> SKOSConcept   :startReign  

Artist  --> Award   :cesarAward  

Person  --> Place   :announcedFrom  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

Person  --> Tournament   :continentalTournament  

Place  --> Organisation   :governingBody  

SpaceMission  --> MeanOfTransportation   :lunarRover  

TelevisionEpisode  --> Person   :guest  

RouteOfTransportation  --> Place   :routeEndLocation  

AdministrativeRegion  --> Place   :administrativeCenter  

RouteOfTransportation  --> Place   :routeStartLocation  

Organisation  --> Person   :secretaryGeneral  

Place  --> Place   :westPlace  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

SportsEvent  --> Person   :medalist  

Person  --> SKOSConcept   :mastersWins  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Stream  --> Country   :sourceCountry  

Road  --> PopulatedPlace   :ruralMunicipality  

Organisation  --> PersonFunction   :leaderFunction  

Place  --> Sea   :sea  

Place  --> Place   :endPoint  

Man  --> Person   :son  

Scientist  --> Person   :notableStudent  

FictionalCharacter  --> Species   :entourage  

SportsEvent  --> Person   :bronzeMedalist  

PopulatedPlace  --> Person   :leaderName  

Man  --> Person   :uncle  

Place  --> PopulatedPlace   :nearestCity  

Artist  --> Award   :afiAward  

TelevisionShow  --> Person   :coExecutiveProducer  

Film  --> Person   :makeupArtist  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Island  --> PopulatedPlace   :highestRegion  

Place  --> PopulatedPlace   :lowestPlace  

Work  --> Place   :releaseLocation  

Newspaper  --> Person   :managingEditor  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

EducationalInstitution  --> Person   :rector  

Person  --> SportsLeague   :leagueManager  

Organisation  --> Organisation   :childOrganisation  

SportsTeam  --> Person   :currentMember  

Animal  --> Place   :birthPlace  

Sport  --> Agent   :currentWorldChampion  

Person  --> SportsTeam   :currentTeamManager  

Settlement  --> Person   :bourgmestre  

Comedian  --> Award   :olivierAward  

Saint  --> Person   :beatifiedBy  

Person  --> Place   :bodyDiscovered  

EducationalInstitution  --> Person   :custodian  

Place  --> Place   :northPlace  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

VideoGame  --> Person   :gameArtist  

Artist  --> Award   :tonyAward  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

MilitaryUnit  --> MeanOfTransportation   :aircraftElectronic  

PopulatedPlace  --> City   :capital  

Place  --> River   :river  

MusicalWork  --> PopulatedPlace   :recordedIn  

Sport  --> Person   :footedness  

Person  --> Organisation   :federation  

MilitaryUnit  --> MeanOfTransportation   :aircraftFighter  

Island  --> PopulatedPlace   :capitalPlace  

Athlete  --> SportsTeam   :oldTeamCoached  

SoccerPlayer  --> SportsTeam   :trainerClub  

Athlete  --> SportsTeam   :club  

Agent  --> Ideology   :ideology  

Place  --> Depth   :depths  

Man  --> Person   :father  

Organisation  --> Organisation   :mergedWith  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopter  

Person  --> Person   :opponent  

Athlete  --> SportsTeam   :juniorTeam  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Person  --> Person   :child  

Place  --> Area   :wholeArea  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Person  --> Person   :cousurper  

Athlete  --> SportsTeam   :currentTeam  

Newspaper  --> Person   :associateEditor  

YearInSpaceflight  --> Country   :countryWithFirstSatelliteLaunched  

Athlete  --> SportsTeam   :managerClub  

Island  --> PopulatedPlace   :capitalRegion  

MilitaryUnit  --> MeanOfTransportation   :aircraftPatrol  

Work  --> Agent   :publisher  

Person  --> Film   :movie  

Politician  --> Person   :prefect  

Person  --> Person   :seiyu  

FigureSkater  --> Person   :choreographer  

Place  --> Altitude   :altitude  

Scientist  --> Person   :doctoralAdvisor  

PopulatedPlace  --> Agglomeration   :agglomeration  

Place  --> Province   :province  

Athlete  --> SportsTeam   :nflTeam  

Organisation  --> Person   :superintendent  

School  --> Person   :executiveHeadteacher  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

FigureSkater  --> Person   :formerCoach  

Place  --> Species   :tree  

PopulatedPlace  --> Legislature   :legislature  

Person  --> Person   :relative  

LegalCase  --> Person   :attorneyGeneral  

Place  --> PersonFunction   :politicalLeader  

PopulatedPlace  --> PopulatedPlace   :borough  

Athlete  --> SportsTeam   :youthClub  

Organisation  --> City   :foundationPlace  

Person  --> List   :relatedFunctions  

TelevisionShow  --> Person   :storyEditor  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

ArchitecturalStructure  --> Organisation   :tenant  

Person  --> Place   :livingPlace  

Athlete  --> SportsTeam   :coachClub  

Place  --> Place   :northEastPlace  

School  --> Person   :nobelLaureates  

Restaurant  --> Person   :headChef  

Settlement  --> PopulatedPlace   :frazioni  

Place  --> Place   :supply  

Settlement  --> PopulatedPlace   :jointCommunity  

MusicalWork  --> Agent   :artist  

Person  --> SKOSConcept   :endReign  

Athlete  --> SportsTeam   :teamCoached  

Rocket  --> Country   :countryOrigin  

YearInSpaceflight  --> Country   :countryWithFirstAstronaut  

ResearchProject  --> Organisation   :projectParticipant  

Species  --> Species   :tribus  

Island  --> PopulatedPlace   :governmentPlace  

Person  --> Tournament   :olympicGames  

Organisation  --> Person   :ceo  

Saint  --> Person   :canonizedBy  

Place  --> Place   :hasOutsidePlace  

Work  --> Person   :author  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

GrandPrix  --> Person   :secondDriver  

Athlete  --> SportsTeam   :debutTeam  

Person  --> EthnicGroup   :ethnicity  

Person  --> PersonFunction   :otherOccupation  

Place  --> Place   :land  

Agent  --> Thing   :owns  

MilitaryUnit  --> MeanOfTransportation   :aircraftInterceptor  

Artist  --> Award   :grammyAward  

Saint  --> Organisation   :veneratedIn  

Scientist  --> Person   :doctoralStudent  

Person  --> Organisation   :employer  

Person  --> Person   :usurper  

Agent  --> TermOfOffice   :generalCouncil  

Settlement  --> PopulatedPlace   :administrativeDistrict  

WrittenWork  --> Person   :illustrator  

Woman  --> Person   :daughter  

Island  --> PopulatedPlace   :lowestRegion  

Athlete  --> SportsTeam   :ncaaTeam  

Person  --> EducationalInstitution   :college  

Work  --> Person   :mainCharacter  

PopulatedPlace  --> Area   :agglomerationArea  

Organisation  --> Person   :trustee  

Band  --> Person   :formerBandMember  

Family  --> Person   :primogenitor  

Place  --> PopulatedPlace   :district  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

Actor  --> Award   :arielAward  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Artwork  --> Person   :painter  

Language  --> PopulatedPlace   :spokenIn  

Place  --> Altitude   :lowestAltitude  

Country  --> Country   :twinCountry  

Person  --> SKOSConcept   :world  

AdministrativeRegion  --> Person   :landeshauptmann  

Settlement  --> Place   :wilaya  

Canal  --> Person   :principalEngineer  

River  --> Place   :sourceConfluenceRegion  

Album  --> Person   :compiler  

PopulatedPlace  --> Saint   :saint  

Athlete  --> Person   :trainer  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

PopulatedPlace  --> Department   :department  

Actor  --> Award   :screenActorsGuildAward  

Organisation  --> Place   :regionServed  

School  --> Person   :vicePrincipal  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Person  --> CareerStation   :careerStation  

Place  --> Place   :locatedInArea  

SportsTeam  --> Person   :manager  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> PopulatedPlace   :sovereignCountry  

GrandPrix  --> Country   :firstDriverCountry  

Agent  --> Event   :roleInEvent  

Canal  --> Place   :originalStartPoint  

Race  --> Person   :firstWinner  

```