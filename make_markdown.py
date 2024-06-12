import os
import pandas as pd


schools = { "Edmonton": [
    {
        "school_name": "A. Blair McPherson School",
        "type": "Public",
        "address": "430 Tamarack Green NW, Edmonton, Alberta T6T 0J4",
        "phone": "780-468-4361",
        "website": "https://ablairmcpherson.epsb.ca/",
        "student_count": 1069
    },
    {
        "school_name": "Abbott School",
        "type": "Public",
        "address": "12045 34 Street NW, Edmonton, Alberta T5W 1Z5",
        "phone": "780-477-7310",
        "website": "https://abbott.epsb.ca/",
        "student_count": 197
    },
    {
        "school_name": "Academy at King Edward",
        "type": "Public",
        "address": "8525 101 Street NW, Edmonton, Alberta T6E 3Z4",
        "phone": "780-439-1368",
        "website": "https://academyatkingedward.epsb.ca/",
        "student_count": 324
    },
    {
        "school_name": "Alberta School for the Deaf",
        "type": "Public",
        "address": "6240 113 Street NW, Edmonton, Alberta T6H 3L2",
        "phone": "780-439-3323",
        "website": "https://asd.epsb.ca/",
        "student_count": 109
    },
    {
        "school_name": "Aldergrove School",
        "type": "Public",
        "address": "8525 182 Street NW, Edmonton, Alberta T5T 1X1",
        "phone": "780-487-5182",
        "website": "https://aldergrove.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Aleda Patterson School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Alex Janvier School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Allendale School",
        "type": "Public",
        "address": "6415 106 Street NW, Edmonton, Alberta T6H 2V3",
        "phone": "780-434-6756",
        "website": "https://allendale.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Amiskwaciy Academy",
        "type": "Public",
        "address": "101 Airport Road NW, Edmonton, Alberta T5G 0W6",
        "phone": "780-424-1270",
        "website": "https://amiskwaciy.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Anne Fitzgerald School",
        "type": "Public",
        "address": "6010 144 Avenue NW, Edmonton, Alberta T5A 1K5",
        "phone": "780-476-7616",
        "website": "https://annefitzgerald.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Athlone School",
        "type": "Public",
        "address": "12940 129 Street NW, Edmonton, Alberta T5L 1J3",
        "phone": "780-455-5823",
        "website": "https://athlone.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Avonmore School",
        "type": "Public",
        "address": "7835 76 Avenue NW, Edmonton, Alberta T6C 2N1",
        "phone": "780-466-2976",
        "website": "https://avonmore.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Balwin School",
        "type": "Public",
        "address": "7055 132 Avenue NW, Edmonton, Alberta T5C 2A4",
        "phone": "780-475-3646",
        "website": "https://balwin.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bannerman School",
        "type": "Public",
        "address": "14112 23 Street NW, Edmonton, Alberta T5Y 1L6",
        "phone": "780-478-4982",
        "website": "https://bannerman.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Baranow School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Belgravia School",
        "type": "Public",
        "address": "11605 74 Avenue NW, Edmonton, Alberta T6G 0G9",
        "phone": "780-435-5560",
        "website": "https://belgravia.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Belmont School",
        "type": "Public",
        "address": "3310 132A Avenue NW, Edmonton, Alberta T5A 3T1",
        "phone": "780-475-5036",
        "website": "https://belmont.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Belvedere School",
        "type": "Public",
        "address": "13359 62 Street NW, Edmonton, Alberta T5A 0V5",
        "phone": "780-476-2022",
        "website": "https://belvedere.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bessie Nichols School",
        "type": "Public",
        "address": "189 Hemingway Road NW, Edmonton, Alberta T6M 0S6",
        "phone": "780-484-2266",
        "website": "https://bessienichols.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bisset School",
        "type": "Public",
        "address": "3020 37 Street NW, Edmonton, Alberta T6L 5X1",
        "phone": "780-450-6536",
        "website": "https://bisset.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Brander Gardens School",
        "type": "Public",
        "address": "14865 56 Avenue NW, Edmonton, Alberta T6H 4P9",
        "phone": "780-437-0913",
        "website": "https://brandergardens.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Braemar School",
        "type": "Public",
        "address": "9359 67A Street NW, Edmonton, Alberta T6B 1R6",
        "phone": "780-469-4233",
        "website": "https://braemar.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Britannia School",
        "type": "Public",
        "address": "16018 104 Avenue NW, Edmonton, Alberta T5P 0S3",
        "phone": "780-489-5300",
        "website": "https://britannia.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Brookside School",
        "type": "Public",
        "address": "5504 143 Street NW, Edmonton, Alberta T6H 4E8",
        "phone": "780-435-7825",
        "website": "https://brookside.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Brander Gardens School",
        "type": "Public",
        "address": "14865 56 Avenue NW, Edmonton, Alberta T6H 4P9",
        "phone": "780-437-0913",
        "website": "https://brandergardens.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Callingwood School",
        "type": "Public",
        "address": "17335 76 Avenue NW, Edmonton, Alberta T5T 2B1",
        "phone": "780-487-0727",
        "website": "https://callingwood.epsb.ca/",
        "student_count": 300
    },
    {
        "school_name": "Capilano School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Caernarvon School",
        "type": "Public",
        "address": "14820 118 Street NW, Edmonton, Alberta T5X 1T4",
        "phone": "780-456-7020",
        "website": "https://caernarvon.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Calder School",
        "type": "Public",
        "address": "12950 118 Street NW, Edmonton, Alberta T5E 5L2",
        "phone": "780-454-4313",
        "website": "https://calder.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Centennial School",
        "type": "Public",
        "address": "17420 57 Avenue NW, Edmonton, Alberta T6M 1K4",
        "phone": "780-481-5590",
        "website": "https://centennial.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Clara Tyner School",
        "type": "Public",
        "address": "9420 Ottewell Road NW, Edmonton, Alberta T6B 2E2",
        "phone": "780-469-5339",
        "website": "https://claratyner.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Crawford Plains School",
        "type": "Public",
        "address": "4210 12 Avenue NW, Edmonton, Alberta T6L 5V6",
        "phone": "780-463-7211",
        "website": "https://crawfordplains.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Crestwood School",
        "type": "Public",
        "address": "9735 144 Street NW, Edmonton, Alberta T5N 2T3",
        "phone": "780-452-4525",
        "website": "https://crestwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Daly Grove School",
        "type": "Public",
        "address": "1888 37 Street NW, Edmonton, Alberta T6L 2R2",
        "phone": "780-450-1532",
        "website": "https://dalygrove.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Delwood School",
        "type": "Public",
        "address": "7315 Delwood Road NW, Edmonton, Alberta T5C 3A9",
        "phone": "780-476-3969",
        "website": "https://delwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Donald R. Getty School",
        "type": "Public",
        "address": "8102 Chappelle Way SW, Edmonton, Alberta T6W 3L7",
        "phone": "587-489-4708",
        "website": "https://donaldrgetty.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dovercourt School",
        "type": "Public",
        "address": "13910 122 Avenue NW, Edmonton, Alberta T5L 2W3",
        "phone": "780-455-6171",
        "website": "https://dovercourt.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Dr. Donald Massey School",
        "type": "Public",
        "address": "5435 162 Avenue NW, Edmonton, Alberta T5Y 0E8",
        "phone": "780-457-5435",
        "website": "https://donaldmassey.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Duggan School",
        "type": "Public",
        "address": "10616 36A Avenue NW, Edmonton, Alberta T6J 0C9",
        "phone": "780-434-0319",
        "website": "https://duggan.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Earl Buxton School",
        "type": "Public",
        "address": "250 Rhatigan Road East NW, Edmonton, Alberta T6R 2H7",
        "phone": "780-435-1577",
        "website": "https://earlbuxton.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Eastglen School",
        "type": "Public",
        "address": "11430 68 Street NW, Edmonton, Alberta T5B 1P1",
        "phone": "780-479-1991",
        "website": "https://eastglen.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edith Rogers School",
        "type": "Public",
        "address": "8308 Mill Woods Road NW, Edmonton, Alberta T6K 1Y7",
        "phone": "780-462-3310",
        "website": "https://edithrogers.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ekota School",
        "type": "Public",
        "address": "1395 Knottwood Road East NW, Edmonton, Alberta T6K 2P5",
        "phone": "780-462-5112",
        "website": "https://ekota.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Elmwood School",
        "type": "Public",
        "address": "16325 83 Avenue NW, Edmonton, Alberta T5R 3V8",
        "phone": "780-489-6749",
        "website": "https://elmwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Emily Murphy School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Evansdale School",
        "type": "Public",
        "address": "9303 150 Avenue NW, Edmonton, Alberta T5E 2N7",
        "phone": "780-476-3331",
        "website": "https://evansdale.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Forest Heights School",
        "type": "Public",
        "address": "10304 81 Street NW, Edmonton, Alberta T6A 3X4",
        "phone": "780-466-0312",
        "website": "https://forestheights.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Fraser School",
        "type": "Public",
        "address": "14904 21 Street NW, Edmonton, Alberta T5Y 2L6",
        "phone": "780-472-0131",
        "website": "https://fraser.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Garneau School",
        "type": "Public",
        "address": "10925 87 Avenue NW, Edmonton, Alberta T6G 0X4",
        "phone": "780-433-1390",
        "website": "https://garneau.epsb.ca/",
        "student_count": 331
    },
    {
        "school_name": "George H. Luck School",
        "type": "Public",
        "address": "300 Bulyea Road NW, Edmonton, Alberta T6R 2L4",
        "phone": "780-438-5011",
        "website": "https://georgehluck.epsb.ca/",
        "student_count": 525
    },
    {
        "school_name": "George P. Nicholson School",
        "type": "Public",
        "address": "1120 113 Street NW, Edmonton, Alberta T6J 7J4",
        "phone": "780-439-9314",
        "website": "https://georgepnicholson.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glengarry School",
        "type": "Public",
        "address": "9211 135 Avenue NW, Edmonton, Alberta T5E 1N7",
        "phone": "780-476-5373",
        "website": "https://glengarry.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Glenora School",
        "type": "Public",
        "address": "13520 102 Avenue NW, Edmonton, Alberta T5N 0P5",
        "phone": "780-452-4948",
        "website": "https://glenora.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Gold Bar School",
        "type": "Public",
        "address": "10524 46 Street NW, Edmonton, Alberta T6A 1K5",
        "phone": "780-466-6525",
        "website": "https://goldbar.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Grace Martin School",
        "type": "Public",
        "address": "8210 36 Avenue NW, Edmonton, Alberta T6K 3J4",
        "phone": "780-462-2161",
        "website": "https://gracemartin.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Grandview Heights School",
        "type": "Public",
        "address": "6225 127 Street NW, Edmonton, Alberta T6H 3W8",
        "phone": "780-434-2464",
        "website": "https://grandviewheights.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Greenfield School",
        "type": "Public",
        "address": "3735 114 Street NW, Edmonton, Alberta T6J 1M3",
        "phone": "780-435-2847",
        "website": "https://greenfield.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Grovenor School",
        "type": "Public",
        "address": "10345 144 Street NW, Edmonton, Alberta T5N 2V2",
        "phone": "780-455-0832",
        "website": "https://grovenor.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Hardisty School",
        "type": "Public",
        "address": "10534 62 Street NW, Edmonton, Alberta T6A 2L3",
        "phone": "780-466-2292",
        "website": "https://hardisty.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Harry Ainlay School",
        "type": "Public",
        "address": "4350 111 Street NW, Edmonton, Alberta T6J 0X8",
        "phone": "780-413-2700",
        "website": "https://harryainlay.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Hazeldean School",
        "type": "Public",
        "address": "6715 97 Street NW, Edmonton, Alberta T6E 3J3",
        "phone": "780-439-2218",
        "website": "https://hazeldean.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Hillcrest School",
        "type": "Public",
        "address": "16400 80 Avenue NW, Edmonton, Alberta T5R 3M1",
        "phone": "780-483-3420",
        "website": "https://hillcrest.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holyrood School",
        "type": "Public",
        "address": "7920 94 Avenue NW, Edmonton, Alberta T6C 1G8",
        "phone": "780-466-2299",
        "website": "https://holyrood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Homesteader School",
        "type": "Public",
        "address": "448 Holmwood Avenue NW, Edmonton, Alberta T5A 4C6",
        "phone": "780-478-1771",
        "website": "https://homesteader.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Horse Hill School",
        "type": "Public",
        "address": "19355 Meridian Street NW, Edmonton, Alberta T5Y 6E6",
        "phone": "780-475-1256",
        "website": "https://horsehill.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Inglewood School",
        "type": "Public",
        "address": "11515 127 Street NW, Edmonton, Alberta T5M 0V5",
        "phone": "780-455-2601",
        "website": "https://inglewood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "J. Percy Page School",
        "type": "Public",
        "address": "2707 Mill Woods Road NW, Edmonton, Alberta T6K 4A6",
        "phone": "780-462-3322",
        "website": "https://jpercypage.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Jackson Heights School",
        "type": "Public",
        "address": "3505 43 Avenue NW, Edmonton, Alberta T6L 4Z4",
        "phone": "780-465-9726",
        "website": "https://jacksonheights.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "James Gibbons School",
        "type": "Public",
        "address": "8860 110A Avenue NW, Edmonton, Alberta T5H 1Z3",
        "phone": "780-477-1833",
        "website": "https://jamesgibbons.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Jasper Place School",
        "type": "Public",
        "address": "8950 163 Street NW, Edmonton, Alberta T5R 2P2",
        "phone": "780-408-9000",
        "website": "https://jasperplace.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John A. McDougall School",
        "type": "Public",
        "address": "10930 107 Street NW, Edmonton, Alberta T5H 2Z6",
        "phone": "780-426-1660",
        "website": "https://johnamcdougall.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John Barnett School",
        "type": "Public",
        "address": "14840 72 Street NW, Edmonton, Alberta T5C 0P1",
        "phone": "780-478-1101",
        "website": "https://johnbarnett.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John D. Bracco School",
        "type": "Public",
        "address": "3150 139 Avenue NW, Edmonton, Alberta T5Y 1R7",
        "phone": "780-475-4024",
        "website": "https://johndbracco.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John Paul I School",
        "type": "Public",
        "address": "TODO",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Julia Kiniski School",
        "type": "Public",
        "address": "4304 41 Avenue NW, Edmonton, Alberta T6L 5Y6",
        "phone": "780-462-4622",
        "website": "https://juliakiniski.epsb.ca/",
        "student_count": 445
    },
    {
        "school_name": "Kameyosek School",
        "type": "Public",
        "address": "250 Lakewood Road East NW, Edmonton, Alberta T6K 3L4",
        "phone": "780-462-8724",
        "website": "https://kameyosek.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kate Chegwin School",
        "type": "Public",
        "address": "3119 48 Street NW, Edmonton, Alberta T6L 6P5",
        "phone": "780-469-0470",
        "website": "https://katechegwin.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kensington School",
        "type": "Public",
        "address": "13420 119 Street NW, Edmonton, Alberta T5E 5N1",
        "phone": "780-455-1323",
        "website": "https://kensington.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kildare School",
        "type": "Public",
        "address": "13503 74 Street NW, Edmonton, Alberta T5C 0Y5",
        "phone": "780-476-0266",
        "website": "https://kildare.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Kirkness School",
        "type": "Public",
        "address": "600 Kirkness Road NW, Edmonton, Alberta T5Y 2M4",
        "phone": "780-476-6091",
        "website": "https://kirkness.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "L. Y. Cairns School",
        "type": "Public",
        "address": "10510 45 Avenue NW, Edmonton, Alberta T6H 0A1",
        "phone": "780-434-9561",
        "website": "https://lycairns.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lago Lindo School",
        "type": "Public",
        "address": "17305 95 Street NW, Edmonton, Alberta T5Z 1N5",
        "phone": "780-456-2234",
        "website": "https://lagolindo.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lansdowne School",
        "type": "Public",
        "address": "12323 51 Avenue NW, Edmonton, Alberta T6H 0M6",
        "phone": "780-434-1510",
        "website": "https://lansdowne.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lauderdale School",
        "type": "Public",
        "address": "10610 129 Avenue NW, Edmonton, Alberta T5E 0N3",
        "phone": "780-475-4028",
        "website": "https://lauderdale.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Laurier Heights School",
        "type": "Public",
        "address": "8210 142 Street NW, Edmonton, Alberta T5R 0M1",
        "phone": "780-487-3759",
        "website": "https://laurierheights.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lee Ridge School",
        "type": "Public",
        "address": "440 Millbourne Road East NW, Edmonton, Alberta T6K 1P3",
        "phone": "780-463-7411",
        "website": "https://leeridge.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lendrum School",
        "type": "Public",
        "address": "11330 54 Avenue NW, Edmonton, Alberta T6H 0V5",
        "phone": "780-434-1047",
        "website": "https://lendrum.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lillian Osborne School",
        "type": "Public",
        "address": "2019 Leger Road NW, Edmonton, Alberta T6R 0R9",
        "phone": "780-391-2450",
        "website": "https://lillianosborne.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Londonderry School",
        "type": "Public",
        "address": "7104 144 Avenue NW, Edmonton, Alberta T5C 1R7",
        "phone": "780-476-3120",
        "website": "https://londonderry.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lorelei School",
        "type": "Public",
        "address": "16237 103 Street NW, Edmonton, Alberta T5X 3A2",
        "phone": "780-456-1791",
        "website": "https://lorelei.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Lynnwood School",
        "type": "Public",
        "address": "15451 84 Avenue NW, Edmonton, Alberta T5R 3Y1",
        "phone": "780-489-5540",
        "website": "https://lynnwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "M. E. LaZerte School",
        "type": "Public",
        "address": "6804 144 Avenue NW, Edmonton, Alberta T5C 3C7",
        "phone": "780-408-9800",
        "website": "https://melazerte.epsb.ca/",
        "student_count": 2325
    },
    {
        "school_name": "Malmo School",
        "type": "Public",
        "address": "4716 115 Street NW, Edmonton, Alberta T6H 3N8",
        "phone": "780-435-2207",
        "website": "https://malmo.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Malcolm Tweddle School",
        "type": "Public",
        "address": "3935 54 Street NW, Edmonton, Alberta T6L 2H9",
        "phone": "780-462-2707",
        "website": "https://malcolmtweddle.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "McArthur School",
        "type": "Public",
        "address": "13535 135 Street NW, Edmonton, Alberta T5L 1Y1",
        "phone": "780-451-0010",
        "website": "https://mcarthur.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "McKee School",
        "type": "Public",
        "address": "10725 McKee Road NW, Edmonton, Alberta T6J 5H6",
        "phone": "780-438-1541",
        "website": "https://mckee.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "McKernan School",
        "type": "Public",
        "address": "11330 76 Avenue NW, Edmonton, Alberta T6G 0K2",
        "phone": "780-434-1325",
        "website": "https://mckernan.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "McLeod School",
        "type": "Public",
        "address": "14715 59 Street NW, Edmonton, Alberta T5A 1Y3",
        "phone": "780-476-0191",
        "website": "https://mcleod.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Meadowlark School",
        "type": "Public",
        "address": "15920 92 Avenue NW, Edmonton, Alberta T5R 5A8",
        "phone": "780-489-4747",
        "website": "https://meadowlark.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mee-Yah-Noh School",
        "type": "Public",
        "address": "9228 146 Avenue NW, Edmonton, Alberta T5E 2J9",
        "phone": "780-476-0521",
        "website": "https://meeyahnoh.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Meyokumin School",
        "type": "Public",
        "address": "5703 19A Avenue NW, Edmonton, Alberta T6L 2L8",
        "phone": "780-462-2101",
        "website": "https://meyokumin.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Michael A. Kostek School",
        "type": "Public",
        "address": "5303 184 Street NW, Edmonton, Alberta T6M 2G4",
        "phone": "780-487-1818",
        "website": "https://mikekostek.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mill Creek School",
        "type": "Public",
        "address": "9735 80 Avenue NW, Edmonton, Alberta T6E 1S8",
        "phone": "780-439-1441",
        "website": "https://millcreek.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Millwoods Christian School",
        "type": "Public",
        "address": "8710 Mill Woods Road NW, Edmonton, Alberta T6K 3J3",
        "phone": "780-463-7600",
        "website": "https://millwoods.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Minchau School",
        "type": "Public",
        "address": "3615 Mill Woods Road East NW, Edmonton, Alberta T6L 5K7",
        "phone": "780-463-7415",
        "website": "https://minchau.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Montrose School",
        "type": "Public",
        "address": "11941 52 Street NW, Edmonton, Alberta T5W 3G4",
        "phone": "780-479-8264",
        "website": "https://montrose.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mount Pleasant School",
        "type": "Public",
        "address": "10541 60A Avenue NW, Edmonton, Alberta T6H 1K4",
        "phone": "780-433-0501",
        "website": "https://mountpleasant.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mount Royal School",
        "type": "Public",
        "address": "11303 55 Street NW, Edmonton, Alberta T5W 3P9",
        "phone": "780-479-0650",
        "website": "https://mountroyal.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Northmount School",
        "type": "Public",
        "address": "14020 88A Street NW, Edmonton, Alberta T5E 3H9",
        "phone": "780-478-0490",
        "website": "https://northmount.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Norwood School",
        "type": "Public",
        "address": "9520 111 Avenue NW, Edmonton, Alberta T5G 0A6",
        "phone": "780-477-1002",
        "website": "https://norwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Oliver School",
        "type": "Public",
        "address": "10227 118 Street NW, Edmonton, Alberta T5K 2V4",
        "phone": "780-488-1221",
        "website": "https://oliver.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ormsby School",
        "type": "Public",
        "address": "6323 184 Street NW, Edmonton, Alberta T5T 3K1",
        "phone": "780-489-1834",
        "website": "https://ormsby.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ottewell School",
        "type": "Public",
        "address": "9435 73 Street NW, Edmonton, Alberta T6B 2A5",
        "phone": "780-466-7331",
        "website": "https://ottewell.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Overlanders School",
        "type": "Public",
        "address": "10615 31 Street NW, Edmonton, Alberta T5W 4R7",
        "phone": "780-479-5131",
        "website": "https://overlanders.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Parkallen School",
        "type": "Public",
        "address": "6703 112 Street NW, Edmonton, Alberta T6H 3J5",
        "phone": "780-434-8503",
        "website": "https://parkallen.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Parkdale School",
        "type": "Public",
        "address": "11648 85 Street NW, Edmonton, Alberta T5B 3E5",
        "phone": "780-477-5577",
        "website": "https://parkdale.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Patricia Heights School",
        "type": "Public",
        "address": "16220 78 Avenue NW, Edmonton, Alberta T5R 3M7",
        "phone": "780-487-8925",
        "website": "https://patriciaheights.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Pollard Meadows School",
        "type": "Public",
        "address": "1150 Knottwood Road East NW, Edmonton, Alberta T6K 2J6",
        "phone": "780-462-0049",
        "website": "https://pollardmeadows.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Princeton School",
        "type": "Public",
        "address": "7720 130 Avenue NW, Edmonton, Alberta T5C 1X4",
        "phone": "780-475-6565",
        "website": "https://princeton.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Queen Alexandra School",
        "type": "Public",
        "address": "7730 106 Street NW, Edmonton, Alberta T6E 4W3",
        "phone": "780-439-5455",
        "website": "https://queenalexandra.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Queen Elizabeth School",
        "type": "Public",
        "address": "9425 132 Avenue NW, Edmonton, Alberta T5E 0Y4",
        "phone": "780-476-8671",
        "website": "https://queenelizabeth.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Richard Secord School",
        "type": "Public",
        "address": "4025 117 Street NW, Edmonton, Alberta T6J 1T7",
        "phone": "780-438-1420",
        "website": "https://richardsecord.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rideau Park School",
        "type": "Public",
        "address": "10605 42 Avenue NW, Edmonton, Alberta T6J 2W9",
        "phone": "780-436-7424",
        "website": "https://rideaupark.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rio Terrace School",
        "type": "Public",
        "address": "7608 154 Street NW, Edmonton, Alberta T5R 1R7",
        "phone": "780-487-4600",
        "website": "https://rioterrace.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Riverbend School",
        "type": "Public",
        "address": "14820 53 Avenue NW, Edmonton, Alberta T6H 4C8",
        "phone": "780-434-7914",
        "website": "https://riverbend.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ross Sheppard School",
        "type": "Public",
        "address": "13546 111 Avenue NW, Edmonton, Alberta T5M 2P2",
        "phone": "780-448-5000",
        "website": "https://rosssheppard.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Rutherford School",
        "type": "Public",
        "address": "8620 91 Street NW, Edmonton, Alberta T6C 3N1",
        "phone": "780-466-2891",
        "website": "https://rutherford.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sakaw School",
        "type": "Public",
        "address": "5730 11A Avenue NW, Edmonton, Alberta T6L 4H2",
        "phone": "780-462-4404",
        "website": "https://sakaw.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Scott Robertson School",
        "type": "Public",
        "address": "13515 107 Street NW, Edmonton, Alberta T5E 4W3",
        "phone": "780-454-9202",
        "website": "https://scottrobertson.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Secord School",
        "type": "Public",
        "address": "9730 182 Street NW, Edmonton, Alberta T5T 3T9",
        "phone": "780-489-7287",
        "website": "https://secord.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sherwood School",
        "type": "Public",
        "address": "9550 152 Street NW, Edmonton, Alberta T5P 1X9",
        "phone": "780-489-2516",
        "website": "https://sherwood.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sifton School",
        "type": "Public",
        "address": "7835 132 Avenue NW, Edmonton, Alberta T5C 2C6",
        "phone": "780-476-4576",
        "website": "https://sifton.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Spruce Avenue School",
        "type": "Public",
        "address": "11424 102 Street NW, Edmonton, Alberta T5G 2E6",
        "phone": "780-477-0256",
        "website": "https://spruceavenue.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Steinhauer School",
        "type": "Public",
        "address": "10717 32A Avenue NW, Edmonton, Alberta T6J 3A3",
        "phone": "780-435-4523",
        "website": "https://steinhauer.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Strathcona School",
        "type": "Public",
        "address": "10450 72 Avenue NW, Edmonton, Alberta T6E 0Z6",
        "phone": "780-439-3957",
        "website": "https://strathcona.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Sweet Grass School",
        "type": "Public",
        "address": "11351 31 Avenue NW, Edmonton, Alberta T6J 4T6",
        "phone": "780-437-0366",
        "website": "https://sweetgrass.epsb.ca/",
        "student_count": 360
    },
    {
        "school_name": "T. D. Baker School",
        "type": "Public",
        "address": "1750 Mill Woods Road East NW, Edmonton, Alberta T6L 5C5",
        "phone": "780-463-2520",
        "website": "https://tdbaker.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Thorncliffe School",
        "type": "Public",
        "address": "8215 175 Street NW, Edmonton, Alberta T5T 1V2",
        "phone": "780-487-2641",
        "website": "https://thorncliffe.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tipaskan School",
        "type": "Public",
        "address": "1200 Lakewood Road West NW, Edmonton, Alberta T6K 3B6",
        "phone": "780-462-2516",
        "website": "https://tipaskan.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tofield School",
        "type": "Public",
        "address": "5401 50 Street, Tofield, Alberta T0B 4J0",
        "phone": "780-662-3133",
        "website": "https://tofield.brsd.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tomahawk School",
        "type": "Public",
        "address": "6119 Township Road 512, Tomahawk, Alberta T0E 2H0",
        "phone": "780-339-3935",
        "website": "https://tomahawk.psd.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Victoria School",
        "type": "Public",
        "address": "10210 108 Avenue NW, Edmonton, Alberta T5H 1A8",
        "phone": "780-392-3534",
        "website": "https://victoria.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Virginia Park School",
        "type": "Public",
        "address": "7324 109 Avenue NW, Edmonton, Alberta T5B 0H9",
        "phone": "780-477-5791",
        "website": "https://virginiapark.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "W. P. Wagner School",
        "type": "Public",
        "address": "6310 Wagner Road NW, Edmonton, Alberta T6E 4N5",
        "phone": "780-469-1315",
        "website": "https://wpwagner.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Waverley School",
        "type": "Public",
        "address": "6825 89 Avenue NW, Edmonton, Alberta T6B 0N1",
        "phone": "780-469-1331",
        "website": "https://waverley.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Weinlos School",
        "type": "Public",
        "address": "2911 48 Street NW, Edmonton, Alberta T6L 5G7",
        "phone": "780-463-7624",
        "website": "https://weinlos.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westbrook School",
        "type": "Public",
        "address": "11915 40 Avenue NW, Edmonton, Alberta T6J 0S1",
        "phone": "780-435-8353",
        "website": "https://westbrook.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westglen School",
        "type": "Public",
        "address": "10950 127 Street NW, Edmonton, Alberta T5M 0T1",
        "phone": "780-455-3667",
        "website": "https://westglen.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westlawn School",
        "type": "Public",
        "address": "9520 165 Street NW, Edmonton, Alberta T5P 3S7",
        "phone": "780-484-5444",
        "website": "https://westlawn.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westmount School",
        "type": "Public",
        "address": "11125 131 Street NW, Edmonton, Alberta T5M 1C1",
        "phone": "780-452-3844",
        "website": "https://westmount.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westminster School",
        "type": "Public",
        "address": "13712 104 Avenue NW, Edmonton, Alberta T5N 0W7",
        "phone": "780-455-1117",
        "website": "https://westminster.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westview Village School",
        "type": "Public",
        "address": "10770 Winterburn Road NW, Edmonton, Alberta T5S 1T5",
        "phone": "780-489-9400",
        "website": "https://westviewvillage.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westridge School",
        "type": "Public",
        "address": "10550 56 Avenue NW, Edmonton, Alberta T6H 4P9",
        "phone": "780-437-0913",
        "website": "https://westridge.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Winterburn School",
        "type": "Public",
        "address": "9527 Winterburn Road NW, Edmonton, Alberta T5T 4W1",
        "phone": "780-489-4594",
        "website": "https://winterburn.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Woodcroft School",
        "type": "Public",
        "address": "13750 Woodcroft Avenue NW, Edmonton, Alberta T5M 3M4",
        "phone": "780-455-5455",
        "website": "https://woodcroft.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "York School",
        "type": "Public",
        "address": "15920 92 Avenue NW, Edmonton, Alberta T5R 5A8",
        "phone": "780-489-4747",
        "website": "https://york.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Anne Fitzgerald Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "699 Clareview Road NW, Edmonton, Alberta T5A 4G3",
        "phone": "780-475-6919",
        "website": "https://annefitzgerald.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Annunciation Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "9325 165 Street NW, Edmonton, Alberta T5R 2S5",
        "phone": "780-487-7941",
        "website": "https://annunciation.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Archbishop Joseph MacNeil Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "750 Leger Way NW, Edmonton, Alberta T6R 3A3",
        "phone": "780-486-7000",
        "website": "https://archbishopmacneil.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Archbishop MacDonald Catholic High School",
        "type": "Separate/Catholic",
        "address": "14219 109 Avenue NW, Edmonton, Alberta T5N 1H5",
        "phone": "780-451-1470",
        "website": "https://archbishopmacdonald.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Austin O'Brien Catholic High School",
        "type": "Separate/Catholic",
        "address": "6110 95 Avenue NW, Edmonton, Alberta T6B 1A5",
        "phone": "780-466-3161",
        "website": "https://austinobrien.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ben Calf Robe - St. Clare Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "11833 64 Street NW, Edmonton, Alberta T5W 4J2",
        "phone": "780-471-2360",
        "website": "https://bencalfrobe.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bishop David Motiuk Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "9735 182 Street NW, Edmonton, Alberta T5T 3T9",
        "phone": "780-484-7952",
        "website": "https://bishopdavidmotiuk.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bishop Greschuk Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "175 McConachie Drive NW, Edmonton, Alberta T5Y 0K6",
        "phone": "780-457-0770",
        "website": "https://bishopgreschuk.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Bishop Savaryn Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "16221 109 Street NW, Edmonton, Alberta T5X 2R3",
        "phone": "780-456-3650",
        "website": "https://bishopsavaryn.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cardinal Collins Catholic Academic Centre",
        "type": "Separate/Catholic",
        "address": "3802 139 Avenue NW, Edmonton, Alberta T5Y 3G6",
        "phone": "780-944-2002",
        "website": "https://cardinalcollins.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cardinal Léger Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "8808 144 Avenue NW, Edmonton, Alberta T5E 6G8",
        "phone": "780-476-8030",
        "website": "https://cardinalleger.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Cardinal Newman Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "16210 105 Avenue NW, Edmonton, Alberta T5P 4V8",
        "phone": "780-489-1981",
        "website": "https://cardinalnewman.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Christ the King Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "180 McConachie Drive NW, Edmonton, Alberta T5Y 0K3",
        "phone": "780-473-1557",
        "website": "https://christtheking.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Father Michael Troy Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "3630 23 Street NW, Edmonton, Alberta T6T 1W8",
        "phone": "780-465-5262",
        "website": "https://fathermichaeltroy.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Father Leo Green Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "7512 144 Avenue NW, Edmonton, Alberta T5C 2R7",
        "phone": "780-475-3565",
        "website": "https://fatherleogreen.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Father Lacombe Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "5210 144 Avenue NW, Edmonton, Alberta T5A 3N4",
        "phone": "780-473-8629",
        "website": "https://fatherlacombe.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Good Shepherd Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "18111 57 Avenue NW, Edmonton, Alberta T6M 1V2",
        "phone": "780-483-1725",
        "website": "https://goodshepherd.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Cross Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "15120 104 Avenue NW, Edmonton, Alberta T5P 4G5",
        "phone": "780-489-1981",
        "website": "https://holycross.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Family Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "1710 Mill Woods Road East NW, Edmonton, Alberta T6L 5J1",
        "phone": "780-440-3408",
        "website": "https://holyfamily.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Rosary Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "11425 133 Street NW, Edmonton, Alberta T5M 1G5",
        "phone": "780-453-2020",
        "website": "https://holyrosary.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Holy Trinity Catholic High School",
        "type": "Separate/Catholic",
        "address": "7007 28 Avenue NW, Edmonton, Alberta T6K 4A5",
        "phone": "780-462-5777",
        "website": "https://holytrinity.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "J. J. Bowlen Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "6110 144 Avenue NW, Edmonton, Alberta T5A 1K5",
        "phone": "780-475-3730",
        "website": "https://jjbowlen.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Jean Vanier Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "109 Georgian Way, Sherwood Park, Alberta T8A 3K9",
        "phone": "780-467-3633",
        "website": "https://jeanvanierschool.eics.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "John Paul I Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "13115 111 Avenue NW, Edmonton, Alberta T5M 2P8",
        "phone": "780-452-7255",
        "website": "https://johnpauli.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Louis St. Laurent Catholic Junior/Senior High School",
        "type": "Separate/Catholic",
        "address": "11230 43 Avenue NW, Edmonton, Alberta T6J 0X8",
        "phone": "780-435-3964",
        "website": "https://louisstlaurent.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mary Hanley Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "15430 90 Street NW, Edmonton, Alberta T5E 3V5",
        "phone": "780-456-2928",
        "website": "https://maryhanley.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Monsignor Fee Otterson Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "1834 Rutherford Road SW, Edmonton, Alberta T6W 2J4",
        "phone": "780-433-5633",
        "website": "https://monsignorfeeotterson.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mother Margaret Mary Catholic High School",
        "type": "Separate/Catholic",
        "address": "2010 Leger Road NW, Edmonton, Alberta T6R 0R9",
        "phone": "780-988-2279",
        "website": "https://mothermargaretmary.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Notre Dame Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "15425 91 Avenue NW, Edmonton, Alberta T5R 5C8",
        "phone": "780-484-3448",
        "website": "https://notredame.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Our Lady of Mount Carmel Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "10524 76 Avenue NW, Edmonton, Alberta T6E 1L3",
        "phone": "780-433-1062",
        "website": "https://ourladyofmountcarmel.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Our Lady of Peace Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "15911 110A Avenue NW, Edmonton, Alberta T5P 0A7",
        "phone": "780-483-1824",
        "website": "https://ourladyofpeace.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Alphonsus Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "11624 81 Street NW, Edmonton, Alberta T5B 2S2",
        "phone": "780-477-0124",
        "website": "https://stalponsus.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Angela Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "13430 132A Avenue NW, Edmonton, Alberta T5L 3T6",
        "phone": "780-455-1310",
        "website": "https://stangela.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Basil Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "10210 115 Avenue NW, Edmonton, Alberta T5G 0L8",
        "phone": "780-477-3584",
        "website": "https://stbasil.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Benedict Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "180 McConachie Drive NW, Edmonton, Alberta T5Y 0K6",
        "phone": "780-457-4674",
        "website": "https://stbenedict.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Bonaventure Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "15635 109 Avenue NW, Edmonton, Alberta T5P 1A2",
        "phone": "780-489-1981",
        "website": "https://stbonaventure.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Brendan Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "5812 132 Avenue NW, Edmonton, Alberta T5A 3V5",
        "phone": "780-475-3565",
        "website": "https://stbrendan.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Catherine Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "10915 110 Street NW, Edmonton, Alberta T5H 3E3",
        "phone": "780-451-2324",
        "website": "https://stcatherine.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Cecilia Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "8830 132 Avenue NW, Edmonton, Alberta T5E 0X1",
        "phone": "780-462-4641",
        "website": "https://stcecilia.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Charles Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "12345 127 Street NW, Edmonton, Alberta T5L 0Z7",
        "phone": "780-455-0188",
        "website": "https://stcharles.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Dominic Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "5804 144 Avenue NW, Edmonton, Alberta T5A 1K5",
        "phone": "780-456-6600",
        "website": "https://stdominic.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Elizabeth Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "7712 144 Avenue NW, Edmonton, Alberta T5C 2R7",
        "phone": "780-475-3565",
        "website": "https://stelizabeth.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Francis of Assisi Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "11904 47 Street NW, Edmonton, Alberta T5W 2X4",
        "phone": "780-479-3220",
        "website": "https://stfrancis.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Gabriel Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "5540 106 Avenue NW, Edmonton, Alberta T6A 1G3",
        "phone": "780-466-0220",
        "website": "https://stgabriel.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Gerard Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "12415 85 Street NW, Edmonton, Alberta T5B 3H3",
        "phone": "780-477-5858",
        "website": "https://stgerard.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Hilda Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "8808 144 Avenue NW, Edmonton, Alberta T5E 6G8",
        "phone": "780-476-8030",
        "website": "https://sthilda.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. James Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "7814 83 Street NW, Edmonton, Alberta T6C 2Y8",
        "phone": "780-469-5351",
        "website": "https://stjames.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Jerome Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "3310 107 Avenue NW, Edmonton, Alberta T5W 0C9",
        "phone": "780-474-4944",
        "website": "https://stjerome.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. John Bosco Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "13544 111 Avenue NW, Edmonton, Alberta T5M 2P4",
        "phone": "780-455-5541",
        "website": "https://stjohnbosco.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. John XXIII Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "3650 139 Avenue NW, Edmonton, Alberta T5Y 3G9",
        "phone": "780-475-3565",
        "website": "https://stjohnxxiii.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Joseph Catholic High School",
        "type": "Separate/Catholic",
        "address": "10830 109 Street NW, Edmonton, Alberta T5H 3C1",
        "phone": "780-424-5890",
        "website": "https://stjoseph.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Justin Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "11425 42 Avenue NW, Edmonton, Alberta T6J 0W9",
        "phone": "780-437-5604",
        "website": "https://stjustin.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Kateri Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "3807 41 Avenue NW, Edmonton, Alberta T6L 6M6",
        "phone": "780-462-2056",
        "website": "https://stkateri.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Kevin Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "10425 84 Street NW, Edmonton, Alberta T6A 2G8",
        "phone": "780-466-3100",
        "website": "https://stkevin.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Lucy Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "11750 139 Avenue NW, Edmonton, Alberta T5X 3N7",
        "phone": "780-456-7390",
        "website": "https://stlucy.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Maria Goretti Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "4210 42 Avenue NW, Edmonton, Alberta T6L 4J6",
        "phone": "780-462-5527",
        "website": "https://stmariagoretti.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Martha Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "11010 153 Avenue NW, Edmonton, Alberta T5X 2P3",
        "phone": "780-457-1551",
        "website": "https://stmartha.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Martin Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "11510 40 Avenue NW, Edmonton, Alberta T6J 0R3",
        "phone": "780-434-1218",
        "website": "https://stmartin.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Mary Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "175 McConachie Drive NW, Edmonton, Alberta T5Y 0K6",
        "phone": "780-456-0332",
        "website": "https://stmary.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Matthew Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "8735 132 Avenue NW, Edmonton, Alberta T5E 0X6",
        "phone": "780-476-7676",
        "website": "https://stmatthew.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Nicholas Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "12835 120 Street NW, Edmonton, Alberta T5E 5N8",
        "phone": "780-473-2457",
        "website": "https://stnicholas.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Patrick Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "10524 144 Avenue NW, Edmonton, Alberta T5E 2H5",
        "phone": "780-478-1995",
        "website": "https://stpatrick.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Paul Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "14410 96 Street NW, Edmonton, Alberta T5E 5Y3",
        "phone": "780-478-7595",
        "website": "https://stpaul.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Peter Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "13710 110 Avenue NW, Edmonton, Alberta T5M 2M2",
        "phone": "780-455-6366",
        "website": "https://stpeter.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Philip Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "14420 80 Avenue NW, Edmonton, Alberta T5R 3M3",
        "phone": "780-484-7327",
        "website": "https://stphilip.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Pius X Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "12735 127 Street NW, Edmonton, Alberta T5L 1A4",
        "phone": "780-452-2980",
        "website": "https://stpiusx.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Richard Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "5704 Mill Woods Road South NW, Edmonton, Alberta T6L 1Y4",
        "phone": "780-462-7490",
        "website": "https://strichard.ecsd.net/",
        "student_count": "TODO"
    },
{
        "school_name": "St. Rose Catholic Junior High School",
        "type": "Separate/Catholic",
        "address": "8815 145 Street NW, Edmonton, Alberta T5R 0T7",
        "phone": "780-483-2695",
        "website": "https://strose.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Stanislaus Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "4215 129 Avenue NW, Edmonton, Alberta T5A 3C8",
        "phone": "780-475-3565",
        "website": "https://ststanislaus.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Teresa of Calcutta Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "6508 132 Avenue NW, Edmonton, Alberta T5C 2A2",
        "phone": "780-475-3565",
        "website": "https://stteresacalcutta.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Thomas Aquinas Catholic Elementary/Junior High School",
        "type": "Separate/Catholic",
        "address": "420 Desrochers Blvd SW, Edmonton, Alberta T6W 4N3",
        "phone": "780-471-2442",
        "website": "https://stthomasaquinas.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Timothy Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "14330 117 Street NW, Edmonton, Alberta T5X 4H7",
        "phone": "780-457-1777",
        "website": "https://sttimothy.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Vladimir Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "7510 132 Avenue NW, Edmonton, Alberta T5C 2A2",
        "phone": "780-476-4085",
        "website": "https://stvladimir.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Vincent Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "10520 135 Avenue NW, Edmonton, Alberta T5E 1X5",
        "phone": "780-478-3367",
        "website": "https://stvincent.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "St. Vital Catholic Elementary School",
        "type": "Separate/Catholic",
        "address": "13230 109 Avenue NW, Edmonton, Alberta T5M 2P8",
        "phone": "780-453-1012",
        "website": "https://stvital.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "École La Mission Francophone School",
        "type": "Francophone",
        "address": "46 Heritage Drive, St. Albert, Alberta T8N 7R5",
        "phone": "780-458-8324",
        "website": "https://mission.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Alexandre-Taché",
        "type": "Francophone",
        "address": "30 Erin Ridge Drive, St. Albert, Alberta T8N 6J3",
        "phone": "780-458-4878",
        "website": "https://alexandretache.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Gabrielle-Roy",
        "type": "Francophone",
        "address": "8728 93 Avenue NW, Edmonton, Alberta T6C 1T8",
        "phone": "780-457-2100",
        "website": "https://gr.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Maurice-Lavallée",
        "type": "Francophone",
        "address": "8828 95 Street NW, Edmonton, Alberta T6C 4H9",
        "phone": "780-465-5461",
        "website": "https://mauricelavallee.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Sainte-Jeanne-d'Arc",
        "type": "Francophone",
        "address": "3807 109 Avenue NW, Edmonton, Alberta T5W 0C6",
        "phone": "780-468-0007",
        "website": "https://sja.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École À la Découverte",
        "type": "Francophone",
        "address": "1111 Giffard Street, Edmonton, Alberta T5L 4X4",
        "phone": "780-466-7941",
        "website": "https://aladecouverte.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Desrochers",
        "type": "Francophone",
        "address": "4336 53 Avenue, Jasper, Alberta T0E 1E0",
        "phone": "780-852-4566",
        "website": "https://desrochers.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Notre-Dame",
        "type": "Francophone",
        "address": "9310 195 Avenue, Edmonton, Alberta T5T 4M5",
        "phone": "780-474-2352",
        "website": "https://notredame.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Père-Lacombe",
        "type": "Francophone",
        "address": "10715 131A Avenue, Edmonton, Alberta T5E 0X5",
        "phone": "780-474-9155",
        "website": "https://perelacombe.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Saint-Christophe",
        "type": "Francophone",
        "address": "13225 113A Street NW, Edmonton, Alberta T5E 5C2",
        "phone": "780-477-2773",
        "website": "https://saint-christophe.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Saint-Vital",
        "type": "Francophone",
        "address": "10315 135 Avenue NW, Edmonton, Alberta T5E 1N4",
        "phone": "780-456-2256",
        "website": "https://saint-vital.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "École Sainte-Marguerite-Bourgeoys",
        "type": "Francophone",
        "address": "3804 139 Avenue NW, Edmonton, Alberta T5Y 2R4",
        "phone": "780-478-8874",
        "website": "https://smb.centrenord.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Boyle Street Education Centre",
        "type": "Charter",
        "address": "10312 105 Street NW, Edmonton, Alberta T5J 1E6",
        "phone": "780-428-1420",
        "website": "https://bsec.ab.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Centre High Campus",
        "type": "Charter",
        "address": "10310 102 Avenue NW, Edmonton, Alberta T5J 1B9",
        "phone": "780-425-6753",
        "website": "https://centrehigh.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edmonton Islamic Academy",
        "type": "Charter",
        "address": "14525 127 Street NW, Edmonton, Alberta T6V 0B3",
        "phone": "780-453-2220",
        "website": "https://www.islamicacademy.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mother Earth's Children's Charter School",
        "type": "Charter",
        "address": "PO Box 108, Warburg, Alberta T0C 2T0",
        "phone": "780-702-7531",
        "website": "https://meccs.org/",
        "student_count": "TODO"
    },
    {
        "school_name": "New Horizons School",
        "type": "Charter",
        "address": "1000 Strathcona Drive, Sherwood Park, Alberta T8A 3R6",
        "phone": "780-416-2353",
        "website": "https://newhorizons.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Suzuki Charter School",
        "type": "Charter",
        "address": "10720 54 Street NW, Edmonton, Alberta T6A 2H9",
        "phone": "780-468-2598",
        "website": "https://www.suzukischool.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Valhalla Community School",
        "type": "Charter",
        "address": "PO Box 143, Valhalla Centre, Alberta T0H 3M0",
        "phone": "780-356-2370",
        "website": "https://vcs.education/",
        "student_count": "TODO"
    },
    {
        "school_name": "Westmount Charter School",
        "type": "Charter",
        "address": "728 32 Street NW, Calgary, Alberta T2N 2V9",
        "phone": "403-217-0426",
        "website": "https://www.westmountcharter.com/",
        "student_count": "TODO"
    },
    {
        "school_name": "Aurora Charter School",
        "type": "Private",
        "address": "14201 23 Avenue NW, Edmonton, Alberta T6R 3B5",
        "phone": "780-408-7945",
        "website": "https://auroraschool.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edmonton Academy",
        "type": "Private",
        "address": "810 Edmonton Trail NE, Calgary, Alberta T2E 3J8",
        "phone": "403-243-1811",
        "website": "https://www.edmontonacademy.com/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edmonton Christian Schools",
        "type": "Private",
        "address": "14304 109 Avenue NW, Edmonton, Alberta T5N 1H6",
        "phone": "780-476-6281",
        "website": "https://www.edmchristian.org/",
        "student_count": "TODO"
    },
    {
        "school_name": "Edmonton Islamic Academy",
        "type": "Private",
        "address": "14525 127 Street NW, Edmonton, Alberta T6V 0B3",
        "phone": "780-453-2220",
        "website": "https://www.islamicacademy.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Progressive Academy",
        "type": "Private",
        "address": "13212 106 Avenue NW, Edmonton, Alberta T5N 1A3",
        "phone": "780-455-8344",
        "website": "https://progressiveacademy.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Tempo School",
        "type": "Private",
        "address": "5603 148 Street NW, Edmonton, Alberta T6H 4T7",
        "phone": "780-434-1190",
        "website": "https://www.temposchool.org/",
        "student_count": "TODO"
    },
    {
        "school_name": "The Academy at King Edward",
        "type": "Private",
        "address": "8520 101 Street NW, Edmonton, Alberta T6E 3Y8",
        "phone": "780-433-4050",
        "website": "https://theacademyofkingedward.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "The Edmonton Academy",
        "type": "Private",
        "address": "810 Edmonton Trail NE, Calgary, Alberta T2E 3J8",
        "phone": "403-243-1811",
        "website": "https://www.edmontonacademy.com/",
        "student_count": "TODO"
    },
    {
        "school_name": "The Progressive Academy",
        "type": "Private",
        "address": "13212 106 Avenue NW, Edmonton, Alberta T5N 1A3",
        "phone": "780-455-8344",
        "website": "https://progressiveacademy.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "The Tempo School",
        "type": "Private",
        "address": "5603 148 Street NW, Edmonton, Alberta T6H 4T7",
        "phone": "780-434-1190",
        "website": "https://www.temposchool.org/",
        "student_count": "TODO"
    },
    {
        "school_name": "Vimy Ridge Academy",
        "type": "Private",
        "address": "8205 90 Avenue NW, Edmonton, Alberta T6C 1N8",
        "phone": "780-465-5461",
        "website": "https://vimyridge.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Waldorf Independent School of Edmonton",
        "type": "Private",
        "address": "7211 96 Street NW, Edmonton, Alberta T6E 3A4",
        "phone": "780-466-3312",
        "website": "https://www.waldorfedmonton.org/",
        "student_count": "TODO"
    },
    {
        "school_name": "Amiskwaciy Academy",
        "type": "First Nations",
        "address": "101 Airport Road NW, Edmonton, Alberta T5G 0W6",
        "phone": "780-424-1270",
        "website": "https://amiskwaciy.epsb.ca/",
        "student_count": "TODO"
    },
    {
        "school_name": "Ben Calf Robe - St. Clare Catholic Elementary/Junior High School",
        "type": "First Nations",
        "address": "11833 64 Street NW, Edmonton, Alberta T5W 4J2",
        "phone": "780-471-2360",
        "website": "https://bencalfrobe.ecsd.net/",
        "student_count": "TODO"
    },
    {
        "school_name": "Mother Earth's Children's Charter School",
        "type": "First Nations",
        "address": "PO Box 108, Warburg, Alberta T0C 2T0",
        "phone": "780-702-7531",
        "website": "https://meccs.org/",
        "student_count": "TODO"
    }
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
        for key, value in row.items():
            t = ""
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")
                if "ecsd" in str(value):
                   t = "ecsd"
                if "epsb" in str(value):
                   t = "epsb"
        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        if t == "ecsd":
            file.write(f"**School's policy on Ventilation**: <https://www.ecsd.net/strengthening-ventilation-in-schools>\n\n")
        if t == "epsb":
            file.write(f"**School's policy on Ventilation**: <https://epsb.ca/schools/goingtoschool/schoolre-entry/>\n\n")
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