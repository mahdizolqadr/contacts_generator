import random
import uuid
import sys

def generate_random_name():
    first_names = ["Afshin", "Aftab", "Arash", "Armin", "Arslan", "Arya", "Ashk", "Aza", "Babak", "Bahram", "Bakhtiar", "Barbak", "Bardiya", "Behnam", "Behrouz", "Bijan", "Bobak", "Darius", "Dariush", "Davood", "Dilawar", "Esfandiar", "Farbod", "Farhad", "Farhang", "Fariborz", "Farid", "Farrukhi", "Farshid", "Farzan", "Freydun", "Gurgen", "Heydar", "Homayoun", "Houshang", "Hushang", "Iliyan", "Irad", "Iraj", "Jahan", "Jahangir", "Jamshid", "Jan", "Javad", "Jawad", "Jawed", "Kamran", "Kayvan", "Khorshid", "Khosrow", "Khosrow", "Kian", "Kourosh", "Manuchehr", "Mehran", "Mehrdad", "Mufaddal", "Nariman", "Nawaz", "Nawazish", "Nima", "Omid", "Parviz", "Pejman", "Peyman", "Pourang", "Pouria", "Ramin", "Raushan", "Rostam", "Salar", "Saman", "Sepehr", "Shahram", "Shahrokh", "Shahruz", "Shahriyar", "Shahzad", "Shapur", "Shayan", "Siamak", "Siavash", "Soheil", "Soroush", "Vardan", "Yaghoub", "Yar", "Zubin"]
    last_names = ["Abedzadeh", "Adl", "Afkari", "Akhtar", "Al-Hashimi", "Alaei", "Alamouti", "Alimardani", "Alinejad", "Anvari", "Araki", "Arbab", "Arvin", "Arya", "Astarabadi", "Ayari", "Azimi", "Bahrami", "Bakhshi", "Bakhtiar", "Balkhi", "Banai", "Behnegar", "Behzadi", "Beiranvand", "Boroumand", "Bukhari", "Bushehri", "Choheili", "Dabbaghi", "Dabir ", "Daivari", "Dalili", "Danaeifard", "Daneshvar", "Darvish", "Daryabegi", "Davani", "Dehlavi", "Dehnavi", "Dirbaz", "Ebrahimi", "Eftekhari", "Emani", "Entezami", "Esfahani", "Esmaeilzadeh", "Faghiri", "Farahmand", "Farrukhi", "Farzan", "Feyzi", "Fotouhi", "Ghahreman", "Ghahremani", "Gharabaghi", "Ghasemi", "Ghelichkhani", "Ghodsi", "Gholipour", "Ghoreishi", "Gilani", "Golpaygani", "Golshiri", "Gul", "Haghighi", "Hagigat", "Hajati", "Hakimi", "Hatami", "Hedayati", "Hemami", "Humayun", "Irandoost", "Iravani", "Izadi", "Jafarzadeh", "Jahani", "Jalayer", "Kadivar", "Kamali", "Kamangar", "Kashani", "Keshmiri", "Khansari", "Khatibi", "Khavari", "Khiabani", "Khonsari", "Khorrami", "Khudsiani", "Kirmani", "Kordestani", "Kuchak", "Laghmani", "Lajevardi", "Lashgari", "Latifi", "Mahabadi", "Mahdavi_Damghani", "Mahjoub", "Makhmalbaf", "Masoud", "Massoud", "Masud", "Mehr", "Mehrabi", "Mobasseri", "Moghaddam", "Mohajerani", "Monshipour", "Moridi", "Motahhari", "Najafi", "Nalbandian", "Namjoo", "Nasseri", "Navabi", "Nawaz", "Nazari", "Niavarani", "Nilforoushan", "Pejman", "Pouya", "Rafati", "Rafiee", "Raisi", "Rajabian", "Ramezani", "Raminfar", "Razavi", "Rekabi", "Rouhani", "Saatchi", "Saberi", "Sadeghi", "Sadr", "Safavi", "Seghatoleslam", "Sepehr", "Shabani", "Shafaei", "Shahlaei", "Shahrokhi", "Shahzad", "Shakarimi", "Shams", "Shamsi", "Sharifi", "Al-Sijistani", "Sorouri", "Soroush", "Taghavi", "Tahami", "Taleghani", "Taslimi", "Tavakkoli", "Tirmizi", "Toloui", "Torkan", "Vafaei", "Vatankhah", "Veisi", "Yaghoub", "Yazdani", "Yeganeh", "Yousefi", "Zadeh", "Zandi", "Zangeneh", "Zarepour", "Zarghami"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"


def generate_random_phone():
    country_code = "+98"  # Customize the country code if needed
    fix_operator = ["905", "935", "936", "937", "912", "911", "910", "913", "914", "915", "916", "917", "918", "919"]
    number = f"{fix_operator[random.randint(0, len(fix_operator) - 1)]} {random.randint(100, 999)} {random.randint(1000, 9999)}"
    return f"{country_code} {number}"


def generate_vcard(name, phone):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
N:{name}
TEL;TYPE=CELL:{phone}
UID:{uuid.uuid4()}
END:VCARD
"""
    return vcard


def generate_vcf(file_name="contacts.vcf", number_of_contacts=100):
    with open(file_name, "w", encoding="utf-8") as file:
        for _ in range(number_of_contacts):
            name = generate_random_name()
            phone = generate_random_phone()
            vcard = generate_vcard(name, phone)
            file.write(vcard)
    print(f"Generated {number_of_contacts} contacts in {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{sys.argv[0]} <OUTPUT> <TOTAL_CONTACTS>\n[+] ex: {sys.argv[0]} random_contacts.vcf 20000")
        exit(1)
    output_file = sys.argv[1]
    total_contacts = int(sys.argv[2])
    generate_vcf(output_file, total_contacts)
