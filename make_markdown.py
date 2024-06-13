import os
import pandas as pd


schools = { "Calgary": [
    {
        "school_name": "A. E. Cross School",
        "type": "Public",
        "address": "3445 37 Street SW, Calgary, Alberta T3E 3C2",
        "phone": "403-777-7410",
        "website": "https://school.cbe.ab.ca/school/aecross/",
        "student_count": "TODO"
    },
    {
        "school_name": "Abbeydale School",
        "type": "Public",
        "address": "320 Abergale Drive NE, Calgary, Alberta T2A 6W2",
        "phone": "403-777-6970",
        "website": "https://school.cbe.ab.ca/school/abbeydale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Acadia School",
        "type": "Public",
        "address": "9603 5 Street SE, Calgary, Alberta T2J 1K4",
        "phone": "403-777-8440",
        "website": "https://school.cbe.ab.ca/school/acadia/",
        "student_count": "TODO"
    },
    {
        "school_name": "Alexander Ferguson School",
        "type": "Public",
        "address": "1704 26 Street SW, Calgary, Alberta T3C 1K5",
        "phone": "403-777-8310",
        "website": "https://school.cbe.ab.ca/school/alexanderferguson/",
        "student_count": "TODO"
    },
    {
        "school_name": "Andrew Sibbald School",
        "type": "Public",
        "address": "1711 Lake Bonavista Drive SE, Calgary, Alberta T2J 2X9",
        "phone": "403-777-6830",
        "website": "https://school.cbe.ab.ca/school/andrewsibbald/",
        "student_count": "TODO"
    },
    {
        "school_name": "Annie Gale School",
        "type": "Public",
        "address": "577 Whiteridge Way NE, Calgary, Alberta T1Y 4S8",
        "phone": "403-777-7680",
        "website": "https://school.cbe.ab.ca/school/anniegale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Arbour Lake School",
        "type": "Public",
        "address": "27 Arbour Crest Drive NW, Calgary, Alberta T3G 4H3",
        "phone": "403-777-7310",
        "website": "https://school.cbe.ab.ca/school/arbourlake/",
        "student_count": "TODO"
    },
    {
        "school_name": "Beddington Heights School",
        "type": "Public",
        "address": "95 Bermuda Road NW, Calgary, Alberta T3K 2J6",
        "phone": "403-777-6610",
        "website": "https://school.cbe.ab.ca/school/beddingtonheights/",
        "student_count": "TODO"
    },
    {
        "school_name": "Belvedere Parkway School",
        "type": "Public",
        "address": "4631 85 Street NW, Calgary, Alberta T3B 2R8",
        "phone": "403-777-6010",
        "website": "https://school.cbe.ab.ca/school/belvedereparkway/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bob Edwards School",
        "type": "Public",
        "address": "4424 Marlborough Drive NE, Calgary, Alberta T2A 2Z5",
        "phone": "403-777-7770",
        "website": "https://school.cbe.ab.ca/school/bobedwards/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bowcroft School",
        "type": "Public",
        "address": "3940 73 Street NW, Calgary, Alberta T3B 2L1",
        "phone": "403-777-6020",
        "website": "https://school.cbe.ab.ca/school/bowcroft/",
        "student_count": "TODO"
    },
    {
        "school_name": "Branton School",
        "type": "Public",
        "address": "2103 20 Street NW, Calgary, Alberta T2M 3W1",
        "phone": "403-777-7440",
        "website": "https://school.cbe.ab.ca/school/branton/",
        "student_count": "TODO"
    },
    {
        "school_name": "Brentwood School",
        "type": "Public",
        "address": "1231 Northmount Drive NW, Calgary, Alberta T2L 0C9",
        "phone": "403-777-6130",
        "website": "https://school.cbe.ab.ca/school/brentwood/",
        "student_count": "TODO"
    },
    {
        "school_name": "Briar Hill School",
        "type": "Public",
        "address": "1233 21 Street NW, Calgary, Alberta T2N 2L8",
        "phone": "403-777-6140",
        "website": "https://school.cbe.ab.ca/school/briarhill/",
        "student_count": "TODO"
    },
    {
        "school_name": "Buchanan School",
        "type": "Public",
        "address": "3717 Centre Street NW, Calgary, Alberta T2E 2Y2",
        "phone": "403-777-6260",
        "website": "https://school.cbe.ab.ca/school/buchanan/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cambrian Heights School",
        "type": "Public",
        "address": "640 Northmount Drive NW, Calgary, Alberta T2K 3J5",
        "phone": "403-777-6150",
        "website": "https://school.cbe.ab.ca/school/cambrianheights/",
        "student_count": "TODO"
    },
    {
        "school_name": "Captain John Palliser School",
        "type": "Public",
        "address": "1484 Northmount Drive NW, Calgary, Alberta T2L 0G6",
        "phone": "403-777-6170",
        "website": "https://school.cbe.ab.ca/school/captainjohnpalliser/",
        "student_count": "TODO"
    },
    {
        "school_name": "Captain Nichola Goddard School",
        "type": "Public",
        "address": "405 Panatella Boulevard NW, Calgary, Alberta T3K 0P3",
        "phone": "403-817-3300",
        "website": "https://school.cbe.ab.ca/school/cngoddard/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cecil Swanson School",
        "type": "Public",
        "address": "4820 Rundlewood Drive NE, Calgary, Alberta T1Y 5V9",
        "phone": "403-777-6690",
        "website": "https://school.cbe.ab.ca/school/cecilswanson/",
        "student_count": "TODO"
    },
    {
        "school_name": "Centennial High School",
        "type": "Public",
        "address": "55 Sun Valley Boulevard SE, Calgary, Alberta T2X 3W7",
        "phone": "403-256-8140",
        "website": "https://school.cbe.ab.ca/school/centennial/",
        "student_count": "TODO"
    },
    {
        "school_name": "Central Memorial High School",
        "type": "Public",
        "address": "5111 21 Street SW, Calgary, Alberta T3E 1R9",
        "phone": "403-243-8880",
        "website": "https://school.cbe.ab.ca/school/centralmemorial/",
        "student_count": "TODO"
    },
    {
        "school_name": "Chaparral School",
        "type": "Public",
        "address": "480 Chaparral Drive SE, Calgary, Alberta T2X 3X8",
        "phone": "403-777-6424",
        "website": "https://school.cbe.ab.ca/school/chaparral/",
        "student_count": "TODO"
    },
    {
        "school_name": "Chris Akkerman School",
        "type": "Public",
        "address": "5004 Marbank Drive NE, Calgary, Alberta T2A 3J3",
        "phone": "403-777-8120",
        "website": "https://school.cbe.ab.ca/school/chrisakkerman/",
        "student_count": "TODO"
    },
    {
        "school_name": "Christine Meikle School",
        "type": "Public",
        "address": "3525 50 Street NW, Calgary, Alberta T3A 0S8",
        "phone": "403-817-3524",
        "website": "https://school.cbe.ab.ca/school/christinemeikle/",
        "student_count": "TODO"
    },
    {
        "school_name": "Citadel Park School",
        "type": "Public",
        "address": "808 Citadel Drive NW, Calgary, Alberta T3G 4B8",
        "phone": "403-777-8063",
        "website": "https://school.cbe.ab.ca/school/citadelpark/",
        "student_count": "TODO"
    },
    {
        "school_name": "Clarence Sansom School",
        "type": "Public",
        "address": "5840 24 Avenue NE, Calgary, Alberta T1Y 6G4",
        "phone": "403-777-7700",
        "website": "https://school.cbe.ab.ca/school/clarencesansom/",
        "student_count": "TODO"
    },
    {
        "school_name": "Colonel Irvine School",
        "type": "Public",
        "address": "412 Northmount Drive NW, Calgary, Alberta T2K 3H6",
        "phone": "403-777-7280",
        "website": "https://school.cbe.ab.ca/school/colonelirvine/",
        "student_count": "TODO"
    },
    {
        "school_name": "Colonel J. Fred Scott School",
        "type": "Public",
        "address": "171 Whitehorn Road NE, Calgary, Alberta T1Y 3C4",
        "phone": "403-777-6710",
        "website": "https://school.cbe.ab.ca/school/coloneljfredscott/",
        "student_count": "TODO"
    },
    {
        "school_name": "Connaught School",
        "type": "Public",
        "address": "1121 12 Avenue SW, Calgary, Alberta T2R 0J8",
        "phone": "403-777-8560",
        "website": "https://school.cbe.ab.ca/school/connaught/",
        "student_count": "TODO"
    },
    {
        "school_name": "Coventry Hills School",
        "type": "Public",
        "address": "12350 Coventry Hills Way NE, Calgary, Alberta T3K 5S9",
        "phone": "403-777-6025",
        "website": "https://school.cbe.ab.ca/school/coventryhills/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cranston School",
        "type": "Public",
        "address": "205 Cranston Drive SE, Calgary, Alberta T3M 1E8",
        "phone": "403-777-6267",
        "website": "https://school.cbe.ab.ca/school/cranston/",
        "student_count": "TODO"
    },
    {
        "school_name": "Crescent Heights High School",
        "type": "Public",
        "address": "1019 1 Street NW, Calgary, Alberta T2M 2S2",
        "phone": "403-276-5521",
        "website": "https://school.cbe.ab.ca/school/crescentheights/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dalhousie School",
        "type": "Public",
        "address": "4440 Dallyn Street NW, Calgary, Alberta T3A 1K3",
        "phone": "403-777-6030",
        "website": "https://school.cbe.ab.ca/school/dalhousie/",
        "student_count": "TODO"
    },
    {
        "school_name": "David Thompson School",
        "type": "Public",
        "address": "9320 Arbour Crescent SE, Calgary, Alberta T2J 0X8",
        "phone": "403-777-7470",
        "website": "https://school.cbe.ab.ca/school/davidthompson/",
        "student_count": "TODO"
    },
    {
        "school_name": "Deer Run School",
        "type": "Public",
        "address": "2127 146 Avenue SE, Calgary, Alberta T2J 6P8",
        "phone": "403-777-6840",
        "website": "https://school.cbe.ab.ca/school/deerrun/",
        "student_count": "TODO"
    },
    {
        "school_name": "Douglas Harkness School",
        "type": "Public",
        "address": "6203 24 Avenue NE, Calgary, Alberta T1Y 3M5",
        "phone": "403-777-7475",
        "website": "https://school.cbe.ab.ca/school/douglasharkness/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. E. P. Scarlett High School",
        "type": "Public",
        "address": "220 Canterbury Drive SW, Calgary, Alberta T2W 1H4",
        "phone": "403-281-3366",
        "website": "https://school.cbe.ab.ca/school/epscarlett/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Gordon Higgins School",
        "type": "Public",
        "address": "155 Rundlehill Drive NE, Calgary, Alberta T1Y 2W9",
        "phone": "403-777-7060",
        "website": "https://school.cbe.ab.ca/school/drgordonhiggins/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. J. K. Mulloy School",
        "type": "Public",
        "address": "7440 10 Street NW, Calgary, Alberta T2K 1H6",
        "phone": "403-777-6640",
        "website": "https://school.cbe.ab.ca/school/drjkmulloy/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Oakley School",
        "type": "Public",
        "address": "2839 30 Street SW, Calgary, Alberta T3E 2M2",
        "phone": "403-777-8300",
        "website": "https://school.cbe.ab.ca/school/droakley/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Roberta Bondar School",
        "type": "Public",
        "address": "1580 Strathcona Drive SW, Calgary, Alberta T3H 5B1",
        "phone": "403-777-8600",
        "website": "https://school.cbe.ab.ca/school/drrobertabondar/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Gladys McKelvie Egbert School",
        "type": "Public",
        "address": "6033 Madigan Drive NE, Calgary, Alberta T2A 5G9",
        "phone": "403-777-7780",
        "website": "https://school.cbe.ab.ca/school/drgladys/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Martha Cohen School",
        "type": "Public",
        "address": "116 Brightondale Park SE, Calgary, Alberta T2Z 0V1",
        "phone": "403-817-3548",
        "website": "https://school.cbe.ab.ca/school/drmarthacohen/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. George Stanley School",
        "type": "Public",
        "address": "585 Cranston Drive SE, Calgary, Alberta T3M 0J4",
        "phone": "403-817-3556",
        "website": "https://school.cbe.ab.ca/school/drgeorgestanley/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Freda Miller School",
        "type": "Public",
        "address": "211 Everbrook Drive SW, Calgary, Alberta T2Y 0E4",
        "phone": "403-817-3432",
        "website": "https://school.cbe.ab.ca/school/drfredamiller/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edgemont School",
        "type": "Public",
        "address": "55 Edgevalley Circle NW, Calgary, Alberta T3A 4X1",
        "phone": "403-777-6340",
        "website": "https://school.cbe.ab.ca/school/edgemont/",
        "student_count": "TODO"
    },
    {
        "school_name": "Elboya School",
        "type": "Public",
        "address": "4804 6 Street SW, Calgary, Alberta T2S 2N3",
        "phone": "403-777-7760",
        "website": "https://school.cbe.ab.ca/school/elboya/",
        "student_count": "TODO"
    },
    {
        "school_name": "Elbow Park School",
        "type": "Public",
        "address": "721 38 Avenue SW, Calgary, Alberta T2T 2H8",
        "phone": "403-817-3408",
        "website": "https://school.cbe.ab.ca/school/elbowpark/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ernest Morrow School",
        "type": "Public",
        "address": "1212 18 Street NE, Calgary, Alberta T2E 4V8",
        "phone": "403-777-7800",
        "website": "https://school.cbe.ab.ca/school/ernestmorrow/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ernest Manning High School",
        "type": "Public",
        "address": "20 Springborough Boulevard SW, Calgary, Alberta T3H 0N7",
        "phone": "403-249-3131",
        "website": "https://school.cbe.ab.ca/school/ernestmanning/",
        "student_count": "TODO"
    },
    {
        "school_name": "Evergreen School",
        "type": "Public",
        "address": "367 Everstone Drive SW, Calgary, Alberta T2Y 0L5",
        "phone": "403-777-6288",
        "website": "https://school.cbe.ab.ca/school/evergreen/",
        "student_count": "TODO"
    },
    {
        "school_name": "Falconridge School",
        "type": "Public",
        "address": "1331 Falconridge Drive NE, Calgary, Alberta T3J 1R2",
        "phone": "403-777-6720",
        "website": "https://school.cbe.ab.ca/school/falconridge/",
        "student_count": "TODO"
    },
    {
        "school_name": "Fish Creek School",
        "type": "Public",
        "address": "1039 Suncastle Drive SE, Calgary, Alberta T2X 2Z1",
        "phone": "403-777-6400",
        "website": "https://school.cbe.ab.ca/school/fishcreek/",
        "student_count": "TODO"
    },
    {
        "school_name": "Forest Lawn High School",
        "type": "Public",
        "address": "1304 44 Street SE, Calgary, Alberta T2A 1M8",
        "phone": "403-272-6665",
        "website": "https://school.cbe.ab.ca/school/forestlawn/",
        "student_count": "TODO"
    },
    {
        "school_name": "Georges P. Vanier School",
        "type": "Public",
        "address": "509 32 Avenue NE, Calgary, Alberta T2E 2H3",
        "phone": "403-777-7460",
        "website": "https://school.cbe.ab.ca/school/georgesvanier/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glamorgan School",
        "type": "Public",
        "address": "50 Grafton Drive SW, Calgary, Alberta T3E 4W3",
        "phone": "403-777-8310",
        "website": "https://school.cbe.ab.ca/school/glamorgan/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glenbrook School",
        "type": "Public",
        "address": "4725 33 Avenue SW, Calgary, Alberta T3E 3V1",
        "phone": "403-777-8320",
        "website": "https://school.cbe.ab.ca/school/glenbrook/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glendale School",
        "type": "Public",
        "address": "2415 17 Avenue SW, Calgary, Alberta T3E 0A8",
        "phone": "403-777-8330",
        "website": "https://school.cbe.ab.ca/school/glendale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glenmeadows School",
        "type": "Public",
        "address": "4931 Grove Hill Road SW, Calgary, Alberta T3E 4G4",
        "phone": "403-777-8430",
        "website": "https://school.cbe.ab.ca/school/glenmeadows/",
        "student_count": "TODO"
    },
    {
        "school_name": "Guy Weadick School",
        "type": "Public",
        "address": "5612 Templehill Road NE, Calgary, Alberta T1Y 4W7",
        "phone": "403-777-6740",
        "website": "https://school.cbe.ab.ca/school/guyweadick/",
        "student_count": "TODO"
    },
    {
        "school_name": "H. D. Cartwright School",
        "type": "Public",
        "address": "5500 Dalhart Road NW, Calgary, Alberta T3A 1V6",
        "phone": "403-777-7420",
        "website": "https://school.cbe.ab.ca/school/hdcartwright/",
        "student_count": "TODO"
    },
    {
        "school_name": "Hawkwood School",
        "type": "Public",
        "address": "650 Hawkwood Boulevard NW, Calgary, Alberta T3G 2V7",
        "phone": "403-777-6410",
        "website": "https://school.cbe.ab.ca/school/hawkwood/",
        "student_count": "TODO"
    },
    {
        "school_name": "Henry Wise Wood High School",
        "type": "Public",
        "address": "910 75 Avenue SW, Calgary, Alberta T2V 0S6",
        "phone": "403-253-2261",
        "website": "https://school.cbe.ab.ca/school/henrywisewood/",
        "student_count": "TODO"
    },
    {
        "school_name": "Highwood School",
        "type": "Public",
        "address": "11 Holmwood Avenue NW, Calgary, Alberta T2K 2G5",
        "phone": "403-777-6200",
        "website": "https://school.cbe.ab.ca/school/highwood/",
        "student_count": "TODO"
    },
    {
        "school_name": "Hillhurst School",
        "type": "Public",
        "address": "1418 7 Avenue NW, Calgary, Alberta T2N 0Z2",
        "phone": "403-777-6240",
        "website": "https://school.cbe.ab.ca/school/hillhurst/",
        "student_count": "TODO"
    },
    {
        "school_name": "Haysboro School",
        "type": "Public",
        "address": "1123 87 Avenue SW, Calgary, Alberta T2V 0W2",
        "phone": "403-777-8530",
        "website": "https://school.cbe.ab.ca/school/haysboro/",
        "student_count": "TODO"
    },
    {
        "school_name": "Huntington Hills School",
        "type": "Public",
        "address": "820 64 Avenue NW, Calgary, Alberta T2K 0M5",
        "phone": "403-777-6650",
        "website": "https://school.cbe.ab.ca/school/huntingtonhills/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ian Bazalgette School",
        "type": "Public",
        "address": "3909 26 Avenue SE, Calgary, Alberta T2B 0C6",
        "phone": "403-777-7360",
        "website": "https://school.cbe.ab.ca/school/ianbazalgette/",
        "student_count": "TODO"
    },
    {
        "school_name": "Jennie Elliott School",
        "type": "Public",
        "address": "3031 Lindsay Drive SW, Calgary, Alberta T3E 6A9",
        "phone": "403-777-8350",
        "website": "https://school.cbe.ab.ca/school/jennieelliott/",
        "student_count": "TODO"
    },
    {
        "school_name": "John G. Diefenbaker High School",
        "type": "Public",
        "address": "6620 4 Street NW, Calgary, Alberta T2K 1C2",
        "phone": "403-274-2240",
        "website": "https://school.cbe.ab.ca/school/johngdiefenbaker/",
        "student_count": "TODO"
    },
    {
        "school_name": "John Ware School",
        "type": "Public",
        "address": "10020 19 Street SW, Calgary, Alberta T2V 1R2",
        "phone": "403-777-7930",
        "website": "https://school.cbe.ab.ca/school/johnware/",
        "student_count": "TODO"
    },
    {
        "school_name": "Keeler School",
        "type": "Public",
        "address": "4807 Forego Avenue SE, Calgary, Alberta T2A 2C4",
        "phone": "403-777-8180",
        "website": "https://school.cbe.ab.ca/school/keeler/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kenneth D. Taylor School",
        "type": "Public",
        "address": "30 Evanscove Circle NW, Calgary, Alberta T3P 0A1",
        "phone": "403-817-3500",
        "website": "https://school.cbe.ab.ca/school/kennethdtaylor/",
        "student_count": "TODO"
    },
    {
        "school_name": "King George School",
        "type": "Public",
        "address": "2108 10 Street NW, Calgary, Alberta T2M 3M4",
        "phone": "403-777-6210",
        "website": "https://school.cbe.ab.ca/school/kinggeorge/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kingsland School",
        "type": "Public",
        "address": "7430 5 Street SW, Calgary, Alberta T2V 1B2",
        "phone": "403-777-8380",
        "website": "https://school.cbe.ab.ca/school/kingsland/",
        "student_count": "TODO"
    },
    {
        "school_name": "Langevin School",
        "type": "Public",
        "address": "107 6A Street NE, Calgary, Alberta T2E 0B7",
        "phone": "403-777-7350",
        "website": "https://school.cbe.ab.ca/school/langevin/",
        "student_count": "TODO"
    },
    {
        "school_name": "Le Roi Daniels School",
        "type": "Public",
        "address": "47 Fyffe Road SE, Calgary, Alberta T2H 1C6",
        "phone": "403-777-6420",
        "website": "https://school.cbe.ab.ca/school/leroidaniels/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lester B. Pearson High School",
        "type": "Public",
        "address": "3020 52 Street NE, Calgary, Alberta T1Y 5P4",
        "phone": "403-280-6565",
        "website": "https://school.cbe.ab.ca/school/lesterbpearson/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lord Beaverbrook High School",
        "type": "Public",
        "address": "9019 Fairmount Drive SE, Calgary, Alberta T2H 0Z4",
        "phone": "403-259-5585",
        "website": "http://school.cbe.ab.ca/school/LordBeaverbrook",
        "student_count": "TODO"
    },
    {
        "school_name": "Lord Shaughnessy High School",
        "type": "Public",
        "address": "2336 53 Avenue SW, Calgary, Alberta T3E 1L2",
        "phone": "403-243-4500",
        "website": "https://school.cbe.ab.ca/school/LordShaughnessy",
        "student_count": "TODO"
    },
    {
        "school_name": "Louis Riel School",
        "type": "Public",
        "address": "9632 Oakfield Drive SW, Calgary, Alberta T2V 0L1",
        "phone": "403-777-7650",
        "website": "https://school.cbe.ab.ca/school/LouisRiel",
        "student_count": "TODO"
    },
    {
        "school_name": "Manmeet Singh Bhullar School",
        "type": "Public",
        "address": "1027 Martindale Boulevard NE, Calgary, Alberta T3J 4Z1",
        "phone": "403-817-3504",
        "website": "https://school.cbe.ab.ca/school/ManmeetSinghBhullar",
        "student_count": "TODO"
    },
    {
        "school_name": "Maple Ridge School",
        "type": "Public",
        "address": "10203 Maplemont Road SE, Calgary, Alberta T2J 1W3",
        "phone": "403-777-6280",
        "website": "https://school.cbe.ab.ca/school/MapleRidge",
        "student_count": "TODO"
    },
    {
        "school_name": "Marion Carson School",
        "type": "Public",
        "address": "5225 Varsity Drive NW, Calgary, Alberta T3A 1A7",
        "phone": "403-777-6050",
        "website": "https://school.cbe.ab.ca/school/MarionCarson",
        "student_count": "TODO"
    },
    {
        "school_name": "Marlborough School",
        "type": "Public",
        "address": "4711 Maryvale Drive NE, Calgary, Alberta T2A 3A1",
        "phone": "403-777-8170",
        "website": "https://school.cbe.ab.ca/school/Marlborough",
        "student_count": "TODO"
    },
    {
        "school_name": "McKenzie Towne School",
        "type": "Public",
        "address": "679 Prestwick Circle SE, Calgary, Alberta T2Z 0V3",
        "phone": "403-777-6185",
        "website": "https://school.cbe.ab.ca/school/McKenzieTowne",
        "student_count": "TODO"
    },
    {
        "school_name": "Midnapore School",
        "type": "Public",
        "address": "55 Midpark Rise SE, Calgary, Alberta T2X 1L7",
        "phone": "403-777-8680",
        "website": "https://school.cbe.ab.ca/school/Midnapore",
        "student_count": "TODO"
    },
    {
        "school_name": "Monterey Park School",
        "type": "Public",
        "address": "7400 California Boulevard NE, Calgary, Alberta T1Y 6R2",
        "phone": "403-777-7233",
        "website": "https://school.cbe.ab.ca/school/MontereyPark",
        "student_count": "TODO"
    },
    {
        "school_name": "Mount Royal School",
        "type": "Public",
        "address": "2234 14 Street SW, Calgary, Alberta T2T 3T3",
        "phone": "403-777-7980",
        "website": "https://school.cbe.ab.ca/school/MountRoyal",
        "student_count": "TODO"
    },
    {
        "school_name": "Mountain Park School",
        "type": "Public",
        "address": "312 Mt. Douglas Close SE, Calgary, Alberta T2Z 4Y1",
        "phone": "403-777-6442",
        "website": "https://school.cbe.ab.ca/school/MountainPark",
        "student_count": "TODO"
    },
    {
        "school_name": "New Brighton School",
        "type": "Public",
        "address": "30 New Brighton Drive SE, Calgary, Alberta T2Z 4B2",
        "phone": "403-817-3516",
        "website": "https://school.cbe.ab.ca/school/NewBrighton",
        "student_count": "TODO"
    },
    {
        "school_name": "Nickle School",
        "type": "Public",
        "address": "2500 Lake Bonavista Drive SE, Calgary, Alberta T2J 2Y6",
        "phone": "403-777-7720",
        "website": "https://school.cbe.ab.ca/school/Nickle",
        "student_count": "TODO"
    },
    {
        "school_name": "North Haven School",
        "type": "Public",
        "address": "4922 North Haven Drive NW, Calgary, Alberta T2K 2K2",
        "phone": "403-777-6220",
        "website": "https://school.cbe.ab.ca/school/NorthHaven",
        "student_count": "TODO"
    },
    {
        "school_name": "Northern Lights School",
        "type": "Public",
        "address": "11955 Coventry Hills Way NE, Calgary, Alberta T3K 6E4",
        "phone": "403-817-3440",
        "website": "https://school.cbe.ab.ca/school/NorthernLights",
        "student_count": "TODO"
    },
    {
        "school_name": "Nose Creek School",
        "type": "Public",
        "address": "135 Covepark Square NE, Calgary, Alberta T3K 5W9",
        "phone": "403-817-3508",
        "website": "https://school.cbe.ab.ca/school/nosecreek/",
        "student_count": "TODO"
    },
    {
        "school_name": "Olympic Heights School",
        "type": "Public",
        "address": "875 Strathcona Drive SW, Calgary, Alberta T3H 2Z7",
        "phone": "403-777-8370",
        "website": "https://school.cbe.ab.ca/school/olympicheights/",
        "student_count": "TODO"
    },
    {
        "school_name": "Panorama Hills School",
        "type": "Public",
        "address": "1057 Panorama Hills Drive NW, Calgary, Alberta T3K 0S4",
        "phone": "403-777-6062",
        "website": "https://school.cbe.ab.ca/school/panoramahills/",
        "student_count": "TODO"
    },
    {
        "school_name": "Parkdale School",
        "type": "Public",
        "address": "1914 12 Avenue NW, Calgary, Alberta T2N 1J2",
        "phone": "403-777-6550",
        "website": "https://school.cbe.ab.ca/school/parkdale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Penbrooke Meadows School",
        "type": "Public",
        "address": "5645 Pensacola Crescent SE, Calgary, Alberta T2A 2G4",
        "phone": "403-777-8230",
        "website": "https://school.cbe.ab.ca/school/penbrookemeadows/",
        "student_count": "TODO"
    },
    {
        "school_name": "Peter Lougheed School",
        "type": "Public",
        "address": "148 Saddletree Close NE, Calgary, Alberta T3J 5J1",
        "phone": "403-817-3500",
        "website": "https://school.cbe.ab.ca/school/peterlougheed/",
        "student_count": "TODO"
    },
    {
        "school_name": "Piitoayis Family School",
        "type": "Public",
        "address": "1921 9 Avenue SE, Calgary, Alberta T2G 0V3",
        "phone": "403-777-6730",
        "website": "https://school.cbe.ab.ca/school/piitoayis/",
        "student_count": "TODO"
    },
    {
        "school_name": "Prince of Wales School",
        "type": "Public",
        "address": "253 Parkland Way SE, Calgary, Alberta T2J 3Y9",
        "phone": "403-777-6880",
        "website": "https://school.cbe.ab.ca/school/princeofwales/",
        "student_count": "TODO"
    },
    {
        "school_name": "Queen Elizabeth High School",
        "type": "Public",
        "address": "512 18 Street NW, Calgary, Alberta T2N 2G5",
        "phone": "403-777-6380",
        "website": "https://school.cbe.ab.ca/school/queenelizabeth/",
        "student_count": "TODO"
    },
    {
        "school_name": "Radisson Park School",
        "type": "Public",
        "address": "2805 Radcliffe Drive SE, Calgary, Alberta T2A 0C8",
        "phone": "403-777-8430",
        "website": "https://school.cbe.ab.ca/school/radissonpark/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ranchlands School",
        "type": "Public",
        "address": "610 Ranchlands Boulevard NW, Calgary, Alberta T3G 2C5",
        "phone": "403-777-6350",
        "website": "https://school.cbe.ab.ca/school/ranchlands/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rideau Park School",
        "type": "Public",
        "address": "829 Rideau Road SW, Calgary, Alberta T2S 0S2",
        "phone": "403-777-7480",
        "website": "https://school.cbe.ab.ca/school/rideaupark/",
        "student_count": "TODO"
    },
    {
        "school_name": "Riverbend School",
        "type": "Public",
        "address": "65 Rivervalley Drive SE, Calgary, Alberta T2C 3Z7",
        "phone": "403-777-6510",
        "website": "https://school.cbe.ab.ca/school/riverbend/",
        "student_count": "TODO"
    },
    {
        "school_name": "Robert Thirsk High School",
        "type": "Public",
        "address": "8777 Nose Hill Drive NW, Calgary, Alberta T3G 5T3",
        "phone": "403-817-3400",
        "website": "https://school.cbe.ab.ca/school/robertthirsk/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rosedale School",
        "type": "Public",
        "address": "905 13 Avenue NW, Calgary, Alberta T2M 0G3",
        "phone": "403-777-7530",
        "website": "https://school.cbe.ab.ca/school/rosedale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rosscarrock School",
        "type": "Public",
        "address": "1406 40 Street SW, Calgary, Alberta T3C 1W7",
        "phone": "403-777-8400",
        "website": "https://school.cbe.ab.ca/school/rosscarrock/",
        "student_count": "TODO"
    },
    {
        "school_name": "Royal Oak School",
        "type": "Public",
        "address": "9100 Royal Birch Boulevard NW, Calgary, Alberta T3G 5R8",
        "phone": "403-777-6279",
        "website": "https://school.cbe.ab.ca/school/royaloak/",
        "student_count": "TODO"
    },
    {
        "school_name": "Saddle Ridge School",
        "type": "Public",
        "address": "368 Saddlecrest Boulevard NE, Calgary, Alberta T3J 5L6",
        "phone": "403-777-6249",
        "website": "https://school.cbe.ab.ca/school/saddleridge/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sam Livingston School",
        "type": "Public",
        "address": "12011 Bonaventure Drive SE, Calgary, Alberta T2J 3G7",
        "phone": "403-777-6890",
        "website": "https://school.cbe.ab.ca/school/samlivingston/",
        "student_count": "TODO"
    },
    {
        "school_name": "Scenic Acres School",
        "type": "Public",
        "address": "50 Scurfield Way NW, Calgary, Alberta T3L 1T2",
        "phone": "403-777-6193",
        "website": "https://school.cbe.ab.ca/school/scenicacres/",
        "student_count": "TODO"
    },
    {
        "school_name": "Senator Patrick Burns School",
        "type": "Public",
        "address": "2155 Chilcotin Road NW, Calgary, Alberta T2L 0X2",
        "phone": "403-777-7400",
        "website": "https://school.cbe.ab.ca/school/senatorpatrickburns/",
        "student_count": "TODO"
    },
    {
        "school_name": "Simon Fraser School",
        "type": "Public",
        "address": "5215 33 Street NW, Calgary, Alberta T2L 1V3",
        "phone": "403-777-7290",
        "website": "https://school.cbe.ab.ca/school/simonfraser/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sir John A. Macdonald School",
        "type": "Public",
        "address": "6600 4 Street NW, Calgary, Alberta T2K 1C2",
        "phone": "403-777-7670",
        "website": "https://school.cbe.ab.ca/school/sirjohnamacdonald/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sir Wilfrid Laurier School",
        "type": "Public",
        "address": "819 32 Street SE, Calgary, Alberta T2A 0Y9",
        "phone": "403-777-7370",
        "website": "https://school.cbe.ab.ca/school/sirwilfridlaurier/",
        "student_count": "TODO"
    },
    {
        "school_name": "Somerset School",
        "type": "Public",
        "address": "150 Somerset Manor SW, Calgary, Alberta T2Y 4S2",
        "phone": "403-777-7001",
        "website": "https://school.cbe.ab.ca/school/somerset/",
        "student_count": "TODO"
    },
    {
        "school_name": "Southwood School",
        "type": "Public",
        "address": "10832 6 Street SW, Calgary, Alberta T2W 1Y5",
        "phone": "403-777-6870",
        "website": "https://school.cbe.ab.ca/school/southwood/",
        "student_count": "TODO"
    },
    {
        "school_name": "Stanley Jones School",
        "type": "Public",
        "address": "950 6 Street NE, Calgary, Alberta T2E 8M3",
        "phone": "403-777-6800",
        "website": "https://school.cbe.ab.ca/school/stanleyjones/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sunalta School",
        "type": "Public",
        "address": "536 Sonora Avenue SW, Calgary, Alberta T3C 2J9",
        "phone": "403-777-8590",
        "website": "https://school.cbe.ab.ca/school/sunalta/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sundance School",
        "type": "Public",
        "address": "200 Sunmills Drive SE, Calgary, Alberta T2X 2N9",
        "phone": "403-777-8690",
        "website": "https://school.cbe.ab.ca/school/sundance/",
        "student_count": "TODO"
    },
    {
        "school_name": "Taradale School",
        "type": "Public",
        "address": "170 Taravista Drive NE, Calgary, Alberta T3J 4T3",
        "phone": "403-777-6270",
        "website": "https://school.cbe.ab.ca/school/taradale/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ted Harrison School",
        "type": "Public",
        "address": "215 Taravista Way NE, Calgary, Alberta T3J 4L1",
        "phone": "403-817-3330",
        "website": "https://school.cbe.ab.ca/school/tedharrison/",
        "student_count": "TODO"
    },
    {
        "school_name": "Thomas B. Riley School",
        "type": "Public",
        "address": "3915 69 Street NW, Calgary, Alberta T3B 2J9",
        "phone": "403-777-7260",
        "website": "https://thomasbriley.cbe.ab.ca",
        "student_count": "TODO"
    },
    {
        "school_name": "Thorncliffe School",
        "type": "Public",
        "address": "5646 Thornton Road NW, Calgary, Alberta T2K 3C1",
        "phone": "403-777-6670",
        "website": "https://school.cbe.ab.ca/school/thorncliffe/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tom Baines School",
        "type": "Public",
        "address": "250 Edgepark Blvd NW, Calgary, Alberta T3A 3S2",
        "phone": "403-777-7190",
        "website": "https://school.cbe.ab.ca/school/tombaines/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tuscany School",
        "type": "Public",
        "address": "990 Tuscany Drive NW, Calgary, Alberta T3L 2T4",
        "phone": "403-777-8060",
        "website": "https://school.cbe.ab.ca/school/tuscany/",
        "student_count": "TODO"
    },
    {
        "school_name": "Valley Creek School",
        "type": "Public",
        "address": "10951 Hidden Valley Drive NW, Calgary, Alberta T3A 6J2",
        "phone": "403-777-7995",
        "website": "https://school.cbe.ab.ca/school/valleycreek/",
        "student_count": "TODO"
    },
    {
        "school_name": "Vanier School",
        "type": "Public",
        "address": "509 32 Avenue NE, Calgary, Alberta T2E 2H3",
        "phone": "403-777-7460",
        "website": "https://school.cbe.ab.ca/school/georgesvanier/",
        "student_count": "TODO"
    },
    {
        "school_name": "Varsity Acres School",
        "type": "Public",
        "address": "4255 40 Street NW, Calgary, Alberta T3A 0H7",
        "phone": "403-777-6090",
        "website": "https://school.cbe.ab.ca/school/varsityacres/",
        "student_count": "TODO"
    },
    {
        "school_name": "Vincent Massey School",
        "type": "Public",
        "address": "939 45 Street SW, Calgary, Alberta T3C 2B9",
        "phone": "403-777-7870",
        "website": "https://school.cbe.ab.ca/school/vincentmassey/",
        "student_count": "TODO"
    },
    {
        "school_name": "Vista Heights School",
        "type": "Public",
        "address": "2411 Vermilion Street NE, Calgary, Alberta T2E 6J3",
        "phone": "403-777-6000",
        "website": "https://school.cbe.ab.ca/school/vistaheights/",
        "student_count": "TODO"
    },
    {
        "school_name": "W. O. Mitchell School",
        "type": "Public",
        "address": "511 Silvergrove Drive NW, Calgary, Alberta T3B 4R9",
        "phone": "403-777-6100",
        "website": "https://school.cbe.ab.ca/school/womitchell/",
        "student_count": "TODO"
    },
    {
        "school_name": "West Dalhousie School",
        "type": "Public",
        "address": "6502 58 Street NW, Calgary, Alberta T3A 2B4",
        "phone": "403-777-6135",
        "website": "https://school.cbe.ab.ca/school/westdalhousie/",
        "student_count": "TODO"
    },
    {
        "school_name": "West Ridge School",
        "type": "Public",
        "address": "8903 Wentworth Avenue SW, Calgary, Alberta T3H 5N9",
        "phone": "403-817-3552",
        "website": "https://school.cbe.ab.ca/school/westridge/",
        "student_count": "TODO"
    },
    {
        "school_name": "West Springs School",
        "type": "Public",
        "address": "8999 Wentworth Avenue SW, Calgary, Alberta T3H 0P7",
        "phone": "403-777-6244",
        "website": "https://school.cbe.ab.ca/school/westsprings/",
        "student_count": "TODO"
    },
    {
        "school_name": "Western Canada High School",
        "type": "Public",
        "address": "641 17 Avenue SW, Calgary, Alberta T2S 0B5",
        "phone": "403-228-5363",
        "website": "https://school.cbe.ab.ca/school/westerncanada/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westgate School",
        "type": "Public",
        "address": "150 Westminster Drive SW, Calgary, Alberta T3C 2T3",
        "phone": "403-777-8420",
        "website": "https://school.cbe.ab.ca/school/westgate/",
        "student_count": "TODO"
    },
    {
        "school_name": "Wildwood School",
        "type": "Public",
        "address": "120 45 Street SW, Calgary, Alberta T3C 2B3",
        "phone": "403-777-8430",
        "website": "https://school.cbe.ab.ca/school/wildwood/",
        "student_count": "TODO"
    },
    {
        "school_name": "William Aberhart High School",
        "type": "Public",
        "address": "3009 Morley Trail NW, Calgary, Alberta T2M 4G9",
        "phone": "403-289-2551",
        "website": "https://williamaberhart.cbe.ab.ca/",
        "student_count": "1300"
    },
    {
        "school_name": "William D. Pratt School",
        "type": "Public",
        "address": "9850 Royal Oak Way NW, Calgary, Alberta T3G 0A4",
        "phone": "403-817-3520",
        "website": "https://school.cbe.ab.ca/school/williamdpratt/",
        "student_count": "TODO"
    },
    {
        "school_name": "Willow Park School",
        "type": "Public",
        "address": "343 Willow Park Drive SE, Calgary, Alberta T2J 0K7",
        "phone": "403-777-6900",
        "website": "https://school.cbe.ab.ca/school/willowpark/",
        "student_count": "TODO"
    },
    {
        "school_name": "Wilma Hansen School",
        "type": "Public",
        "address": "963 Queensland Drive SE, Calgary, Alberta T2J 5E5",
        "phone": "403-777-7430",
        "website": "https://school.cbe.ab.ca/school/wilmahansen/",
        "student_count": "TODO"
    },
    {
        "school_name": "Woodbine School",
        "type": "Public",
        "address": "27 Woodfield Way SW, Calgary, Alberta T2W 5E1",
        "phone": "403-777-8630",
        "website": "https://school.cbe.ab.ca/school/woodbine/",
        "student_count": "TODO"
    },
    {
        "school_name": "Woodlands School",
        "type": "Public",
        "address": "88 Woodgreen Drive SW, Calgary, Alberta T2W 4W9",
        "phone": "403-777-8640",
        "website": "https://school.cbe.ab.ca/school/woodlands/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ascension of Our Lord School",
        "type": "Separate/Catholic",
        "address": "509 Harvest Hills Drive NE, Calgary, Alberta T3K 4G9",
        "phone": "403-500-2105",
        "website": "https://www.cssd.ab.ca/schools/ascension/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bishop Carroll High School",
        "type": "Separate/Catholic",
        "address": "4624 Richard Road SW, Calgary, Alberta T3E 6L1",
        "phone": "403-500-2056",
        "website": "https://www.cssd.ab.ca/schools/bishopcarroll/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bishop Grandin High School",
        "type": "Separate/Catholic",
        "address": "111 Haddon Road SW, Calgary, Alberta T2V 2Y2",
        "phone": "403-500-2047",
        "website": "https://www.cssd.ab.ca/schools/bishopgrandin/",
        "student_count": "TODO"
    },
    {
        "school_name": "Blessed Cardinal Newman School",
        "type": "Separate/Catholic",
        "address": "16201 McKenzie Lake Way SE, Calgary, Alberta T2Z 2R3",
        "phone": "403-500-2099",
        "website": "https://www.cssd.ab.ca/schools/cardinalnewman/",
        "student_count": "TODO"
    },
    {
        "school_name": "Christ the King School",
        "type": "Separate/Catholic",
        "address": "333 Cranston Way SE, Calgary, Alberta T3M 1K6",
        "phone": "403-500-2113",
        "website": "https://www.cssd.ab.ca/schools/christtheking/",
        "student_count": "TODO"
    },
    {
        "school_name": "Father Lacombe High School",
        "type": "Separate/Catholic",
        "address": "3615 Radcliffe Drive SE, Calgary, Alberta T2A 6B4",
        "phone": "403-500-2056",
        "website": "https://fatherlacombe.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Cross School",
        "type": "Separate/Catholic",
        "address": "3719 26 Avenue SE, Calgary, Alberta T2B 0C6",
        "phone": "403-500-2033",
        "website": "https://holycross.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Name School",
        "type": "Separate/Catholic",
        "address": "3011 35 Street SW, Calgary, Alberta T3E 2Y7",
        "phone": "403-500-2006",
        "website": "https://holyname.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John Paul II School",
        "type": "Separate/Catholic",
        "address": "119 Shawnessy Drive SW, Calgary, Alberta T2Y 2W2",
        "phone": "403-500-2055",
        "website": "https://johnpaulii.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Monsignor J. S. Smith School",
        "type": "Separate/Catholic",
        "address": "2919 Douglasdale Boulevard SE, Calgary, Alberta T2Z 1X2",
        "phone": "403-500-2045",
        "website": "https://monsignorjssmith.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Our Lady of the Assumption School",
        "type": "Separate/Catholic",
        "address": "7311 34 Avenue NW, Calgary, Alberta T3B 1N5",
        "phone": "403-500-2044",
        "website": "https://ourladyoftheassumption.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Our Lady of Peace School",
        "type": "Separate/Catholic",
        "address": "14826 Millrise Hill SW, Calgary, Alberta T2Y 2B4",
        "phone": "403-500-2089",
        "website": "https://ourladyofpeace.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Alphonsus School",
        "type": "Separate/Catholic",
        "address": "928 Radnor Avenue NE, Calgary, Alberta T2E 5H5",
        "phone": "403-500-2016",
        "website": "https://stalexander.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Ambrose School",
        "type": "Separate/Catholic",
        "address": "1500 Arbour Lake Road NW, Calgary, Alberta T3G 4X9",
        "phone": "403-500-2100",
        "website": "https://stambrose.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Anne Academic Centre",
        "type": "Separate/Catholic",
        "address": "1010 21 Avenue SE, Calgary, Alberta T2G 1N2",
        "phone": "403-500-2012",
        "website": "https://stanne.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Augustine School",
        "type": "Separate/Catholic",
        "address": "7112 7 Street SW, Calgary, Alberta T2V 1H8",
        "phone": "403-500-2028",
        "website": "https://staugustine.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Basil School",
        "type": "Separate/Catholic",
        "address": "919 Centre Street NW, Calgary, Alberta T2E 2P6",
        "phone": "403-500-2041",
        "website": "https://stbasil.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Bonaventure School",
        "type": "Separate/Catholic",
        "address": "1710 Acadia Drive SE, Calgary, Alberta T2J 3K4",
        "phone": "403-500-2062",
        "website": "https://stbonaventure.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Catherine School",
        "type": "Separate/Catholic",
        "address": "14830 Deer Ridge Drive SE, Calgary, Alberta T2J 6T6",
        "phone": "403-500-2071",
        "website": "https://stcatherine.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Cecilia School",
        "type": "Separate/Catholic",
        "address": "610 Agate Crescent SE, Calgary, Alberta T2J 0Z3",
        "phone": "403-500-2040",
        "website": "https://stcecilia.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Dominic School",
        "type": "Separate/Catholic",
        "address": "4820 Dalhart Road NW, Calgary, Alberta T3A 1C2",
        "phone": "403-500-2050",
        "website": "https://stdominic.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Elizabeth Seton School",
        "type": "Separate/Catholic",
        "address": "10845 Hidden Valley Drive NW, Calgary, Alberta T3A 6K3",
        "phone": "403-500-2105",
        "website": "https://stelizabethseton.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Francis High School",
        "type": "Separate/Catholic",
        "address": "877 Northmount Drive NW, Calgary, Alberta T2L 0A3",
        "phone": "403-500-2026",
        "website": "https://stfrancis.cssd.ab.ca/",
        "student_count": "2006"
    },
    {
        "school_name": "St. Gabriel the Archangel School",
        "type": "Separate/Catholic",
        "address": "197 Invermere Drive, Chestermere, Alberta T1X 1M7",
        "phone": "403-500-2110",
        "website": "https://stgabriel.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Gerard School",
        "type": "Separate/Catholic",
        "address": "1204 96 Avenue SW, Calgary, Alberta T2V 0Y1",
        "phone": "403-500-2048",
        "website": "https://stgerard.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Gregory School",
        "type": "Separate/Catholic",
        "address": "5340 26 Avenue SW, Calgary, Alberta T3E 0R6",
        "phone": "403-500-2047",
        "website": "https://stgregory.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Helena School",
        "type": "Separate/Catholic",
        "address": "320 64 Avenue NW, Calgary, Alberta T2K 0L8",
        "phone": "403-500-2049",
        "website": "https://sthelena.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Isabella School",
        "type": "Separate/Catholic",
        "address": "855 Copperfield Boulevard SE, Calgary, Alberta T2Z 4V4",
        "phone": "403-500-2112",
        "website": "https://stisabella.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. James School",
        "type": "Separate/Catholic",
        "address": "2227 58 Avenue SW, Calgary, Alberta T3E 1N5",
        "phone": "403-500-2042",
        "website": "https://stjames.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Jean Brebeuf School",
        "type": "Separate/Catholic",
        "address": "5030 Northland Drive NW, Calgary, Alberta T2L 2J6",
        "phone": "403-500-2043",
        "website": "https://stjeanbrebeuf.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Jerome School",
        "type": "Separate/Catholic",
        "address": "11616 28 Street SE, Calgary, Alberta T2Z 3W1",
        "phone": "403-500-2061",
        "website": "https://stjerome.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. John XXIII School",
        "type": "Separate/Catholic",
        "address": "1420 23 Street NW, Calgary, Alberta T2N 2P1",
        "phone": "403-500-2067",
        "website": "https://stjohnxxiii.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Joseph School",
        "type": "Separate/Catholic",
        "address": "2512 5 Street NW, Calgary, Alberta T2M 3C7",
        "phone": "403-500-2009",
        "website": "https://stjoseph.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Jude School",
        "type": "Separate/Catholic",
        "address": "730 Woodbine Boulevard SW, Calgary, Alberta T2W 4W3",
        "phone": "403-500-2046",
        "website": "https://stjude.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Kateri Tekakwitha School",
        "type": "Separate/Catholic",
        "address": "1005 Panora Way NW, Calgary, Alberta T3K 0P6",
        "phone": "403-500-2115",
        "website": "https://stkateritekakwitha.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Luke School",
        "type": "Separate/Catholic",
        "address": "1232 Northmount Drive NW, Calgary, Alberta T2L 0E1",
        "phone": "403-500-2039",
        "website": "https://stluke.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Margaret School",
        "type": "Separate/Catholic",
        "address": "3320 Carol Drive NW, Calgary, Alberta T2L 0K7",
        "phone": "403-500-2025",
        "website": "https://stmargaret.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Maria Goretti School",
        "type": "Separate/Catholic",
        "address": "375 Hawkstone Drive NW, Calgary, Alberta T3G 3T7",
        "phone": "403-500-2045",
        "website": "https://stmariagoretti.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Martha School",
        "type": "Separate/Catholic",
        "address": "6020 4th Avenue NE, Calgary, Alberta T2A 4B1",
        "phone": "403-500-2074",
        "website": "https://stmartha.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Matthew School",
        "type": "Separate/Catholic",
        "address": "416 83 Avenue SE, Calgary, Alberta T2H 1N3",
        "phone": "403-500-2034",
        "website": "https://stmatthew.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Michael School",
        "type": "Separate/Catholic",
        "address": "4511 8 Avenue SW, Calgary, Alberta T3C 0G9",
        "phone": "403-500-2021",
        "website": "https://stmichael.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Monica School",
        "type": "Separate/Catholic",
        "address": "235 18 Avenue SW, Calgary, Alberta T2S 0C2",
        "phone": "403-500-2001",
        "website": "https://stmonica.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Patrick School",
        "type": "Separate/Catholic",
        "address": "6006 Rundlehorn Drive NE, Calgary, Alberta T1Y 2X1",
        "phone": "403-500-2040",
        "website": "https://stpatrick.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Pius X School",
        "type": "Separate/Catholic",
        "address": "2312 18 Street NW, Calgary, Alberta T2M 3T5",
        "phone": "403-500-2017",
        "website": "https://stpiusx.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Rita School",
        "type": "Separate/Catholic",
        "address": "7811 Ranchview Drive NW, Calgary, Alberta T3G 2B3",
        "phone": "403-500-2083",
        "website": "https://strita.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Rose of Lima School",
        "type": "Separate/Catholic",
        "address": "2419 50 Street NE, Calgary, Alberta T1Y 1Z5",
        "phone": "403-500-2053",
        "website": "https://strose.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Rupert School",
        "type": "Separate/Catholic",
        "address": "111 Rundlehill Drive NE, Calgary, Alberta T1Y 5M2",
        "phone": "403-500-2070",
        "website": "https://strupert.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Sebastian School",
        "type": "Separate/Catholic",
        "address": "65 Chaparral Drive SE, Calgary, Alberta T2X 3K8",
        "phone": "403-500-2114",
        "website": "https://stsebastian.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Stephen School",
        "type": "Separate/Catholic",
        "address": "10910 Elbow Drive SW, Calgary, Alberta T2W 1G5",
        "phone": "403-500-2032",
        "website": "https://ststephen.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Sylvester School",
        "type": "Separate/Catholic",
        "address": "7318 Silver Springs Boulevard NW, Calgary, Alberta T3B 4N1",
        "phone": "403-500-2078",
        "website": "https://stsylvester.cssd.ab.ca/",
        "student_count": "TODO"
    },
    {"school_name": "St. Timothy School", "type": "Separate/Catholic", "address": "TODO", "phone": "TODO", "website": "TODO", "student_count": "TODO"},
    {"school_name": "St. Vincent de Paul School", "type": "Separate/Catholic", "address": "4525 - 49 Street N.W., Calgary, AB T3A 0K4", "phone": "403-500-2051", "website": "https://stvincent.cssd.ab.ca", "student_count": "TODO"},
    {"school_name": "St. William School", "type": "Separate/Catholic", "address": "11020 Fairmount Dr SE, Calgary, AB T2J 0T1", "phone": "403-500-2055", "website": "https://stwilliam.cssd.ab.ca", "student_count": "TODO"},
    {"school_name": "École de la Source", "type": "Francophone", "address": "360 94 Avenue SE, Calgary, AB T2J 0E8", "phone": "403-255-6724", "website": "https://lasource.francosud.ca", "student_count": "TODO"},
    {"school_name": "École de la Rose Sauvage", "type": "Francophone", "address": "2512 4 Street NW, Calgary, AB T2M 2Z9", "phone": "403-230-3112", "website": "http://larosesauvage.francosud.ca", "student_count": "TODO"},
    {"school_name": "École de la Mosaïque", "type": "Francophone", "address": "TODO", "phone": "TODO", "website": "TODO", "student_count": "TODO"},
    {"school_name": "École Notre-Dame-de-la-Paix", "type": "Francophone", "address": "454 rue Caisse, Verdun, QC H4G 2C8", "phone": "(514) 765-7565", "website": "https://nddlp.ecoleverdun.com", "student_count": "TODO"},
    {"school_name": "École Sainte-Marguerite-Bourgeoys", "type": "Francophone", "address": "4700 Richard Road S.W., Calgary, AB T3E 6L1", "phone": "403-240-2007", "website": "https://smb.francosud.ca", "student_count": "TODO"},
    {"school_name": "École Terre des Jeunes", "type": "Francophone", "address": "3416 17 Ave SE, Calgary, AB T2A 0R4", "phone": "403-234-9930", "website": "https://terredesjeunes.francosud.ca", "student_count": "TODO"},
    {"school_name": "Almadina Language Charter Academy", "type": "Charter", "address": "2031 Sable Dr SE, Calgary, AB T2B 1R9", "phone": "403-543-5070", "website": "http://esl-almadina.com", "student_count": "TODO"},
    {"school_name": "Calgary Arts Academy", "type": "Charter", "address": "640 14 Avenue SE, Calgary, AB T2G 1E8",
     "phone": "403-532-3020", "website": "https://www.caaschool.com", "student_count": "TODO"},
    {"school_name": "Calgary Girls' School", "type": "Charter", "address": "6304 Larkspur Way SW, Calgary, AB T3E 5P7",
     "phone": "403-220-0745", "website": "http://www.calgarygirlsschool.com", "student_count": "TODO"},
    {"school_name": "Calgary Science School", "type": "Charter", "address": "108 - 12 Avenue NW, Calgary, AB T2M 0C9",
     "phone": "403-282-2890", "website": "http://www.csschool.com", "student_count": "TODO"},
    {"school_name": "Connect Charter School", "type": "Charter", "address": "5915 Lewis Drive SW, Calgary, AB T3E 5Z4",
     "phone": "403-282-2890", "website": "http://www.connectcharter.ca", "student_count": "TODO"},
    {"school_name": "Foundations for the Future Charter Academy", "type": "Charter",
     "address": "12345 40 Street SE, Calgary, AB T2Z 4E6", "phone": "403-520-3206",
     "website": "https://www.ffca-calgary.com", "student_count": "TODO"},
    {"school_name": "Westmount Charter School", "type": "Charter", "address": "728 - 32 Street NW, Calgary, AB T2N 2V9",
     "phone": "403-217-0426", "website": "http://www.westmountcharter.com", "student_count": "TODO"},
    {"school_name": "Bearspaw Christian School", "type": "Private",
     "address": "15001 69 Street NW, Calgary, AB T3R 1C5", "phone": "403-295-2566",
     "website": "http://www.bearspawschool.com", "student_count": "TODO"},
    {"school_name": "Calgary Academy", "type": "Private", "address": "1677 - 93 Street SW, Calgary, AB T3H 0R3",
     "phone": "403-686-6444", "website": "http://www.calgaryacademy.com", "student_count": "TODO"},
    {"school_name": "Calgary French & International School", "type": "Private",
     "address": "700 - 77 Street SW, Calgary, AB T3H 5R1", "phone": "403-240-1500", "website": "http://www.cfisd.com",
     "student_count": "TODO"},
    {"school_name": "Calgary Islamic School", "type": "Private", "address": "2612 - 37 Avenue NE, Calgary, AB T1Y 5L2",
     "phone": "403-248-2773", "website": "http://www.cis-calgary.ca", "student_count": "TODO"},
    {"school_name": "Calgary Waldorf School", "type": "Private", "address": "515 Cougar Ridge Dr SW, Calgary, AB T3H 5G9", "phone": "403-287-1868", "website": "http://www.calgarywaldorf.org", "student_count": "TODO"},
    {"school_name": "Clear Water Academy", "type": "Private", "address": "3910 Quesnay Wood Drive SW, Calgary, AB T3E 8G1", "phone": "403-217-8448", "website": "https://www.clearwateracademy.com", "student_count": "TODO"},
    {"school_name": "Edge School", "type": "Private", "address": "33055 Township Rd 250, Calgary, AB T3Z 1L4", "phone": "403-246-6432", "website": "http://www.edgeschool.com", "student_count": "TODO"},
    {"school_name": "Glenmore Christian Academy", "type": "Private", "address": "16520 24 Street SW, Calgary, AB T2Y 4W2", "phone": "403-254-9050", "website": "http://www.gcaschool.com", "student_count": "TODO"},
    {"school_name": "Lycée Louis Pasteur", "type": "Private", "address": "4099 Garrison Blvd SW, Calgary, AB T2T 6G2", "phone": "403-243-5420", "website": "http://www.lycee.ca", "student_count": "TODO"},
    {"school_name": "Master’s Academy & College", "type": "Private", "address": "4414 Crowchild Trail SW, Calgary, AB T2T 5J4", "phone": "403-242-7034", "website": "http://www.masters.ab.ca", "student_count": "TODO"},
    {"school_name": "North Point School for Boys", "type": "Private", "address": "2445 23 Avenue SW, Calgary, AB T2T 0W3", "phone": "403-744-5214", "website": "http://www.northpoint.school", "student_count": "TODO"},
    {"school_name": "Renert School", "type": "Private", "address": "14 Royal Vista Link NW, Calgary, AB T3R 0K4", "phone": "403-547-2435", "website": "http://www.renertschool.ca", "student_count": "TODO"},
    {"school_name": "Rundle College", "type": "Private", "address": "7379 17 Ave SW, Calgary, AB T3H 3W5", "phone": "403-291-3866", "website": "http://www.rundle.ab.ca", "student_count": "TODO"},
    {"school_name": "Strathcona-Tweedsmuir School", "type": "Private", "address": "322041 15 St E, Okotoks, AB T1S 1A2", "phone": "403-938-4431", "website": "http://www.strathconatweedsmuir.com", "student_count": "TODO"},
    {"school_name": "Webber Academy", "type": "Private", "address": "1515 93 Street SW, Calgary, AB T3H 4A8", "phone": "403-277-4700", "website": "http://www.webberacademy.ca", "student_count": "TODO"},
    {"school_name": "West Island College", "type": "Private", "address": "7410 Blackfoot Trail SE, Calgary, AB T2H 1M5",
     "phone": "403-255-5300", "website": "https://www.westislandcollege.ab.ca", "student_count": "TODO"},
    {"school_name": "Piitoayis Family School", "type": "First Nations",
     "address": "1921 9 Avenue SE, Calgary, AB T2G 0V3", "phone": "403-777-6860",
     "website": "http://school.cbe.ab.ca/school/piitoayis", "student_count": "TODO"},
    {"school_name": "Tsuu T'ina Junior Senior High School", "type": "First Nations",
     "address": "128 Macleod Trail SW, Tsuu T'ina Nation, AB T2W 1A1", "phone": "403-251-2015",
     "website": "http://www.chiefjimstarlightcentre.com", "student_count": "TODO"}
]
}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    district_name = district_name.replace(" Dist.", "").replace(" District", "").replace(" Public School District", "").replace(" School District", "").replace(" School Dist", "").replace(" Public School", "").rstrip('.')

    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name

# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All Alberta Areas/Cities]](../..) > [[All In {row['district_name']}]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        t = ""
        for key, value in row.items():

            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")
                if "cbe.ab.ca" in str(value):
                    t = "cbe"
                if "cssd.ab.ca" in str(value):
                    t = "cssd"
        if t == "cbe" or t == "cssd":
            file.write(f"**School's overall airborne virus protection grade (0-5)**: 1\n\n")
        else:
            file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        if t == "cbe":
            file.write(f"**School's policy on Ventilation**: <https://cbe.ab.ca/about-us/school-culture-and-environment/health-and-wellness-in-school/Pages/coronavirus.aspx>. Note: page has ventilation section but does not mention COVID-19 even though the URL ends with coronavirus.\n\n")
        if t == "cssd":
            file.write(f"**School's policy on Ventilation**: <https://www.cssd.ab.ca/healthy-school-environments>\n\n")
        else:
            file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/AB/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")

# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)

def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Alberta and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Alberta. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Alberta School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Alberta schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/AB/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)

# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")