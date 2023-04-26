from Application import Application
from Client import Client
from CreditCard import CreditCard
from DebitCard import DebitCard
from Dispensing import Dispensing
from Drug import Drug
from Free import Free
from Pharmacy import Pharmacy
from Phone import Phone
from Prescriptive import Prescriptive
from Provider import Provider

application = Application(["Edwin", "James", "Louis"])
client = Client("Juan", "Perez", "05/12/2004", 1, 12345, "Street 1")
credit_card = CreditCard(123, "", "12/10/2025")
debit_card = DebitCard(456, "", "12/10/2025")
dispensing = Dispensing(35000, "Acetaminophen 500mg", "18/02/2023", "30/12/2030", "20/03/2026")
drug = Drug(42000, "Acetaminophen 500mg", "18/02/2023")
free = Free(12000, "Acetaminophen 500mg", "18/02/2023", "30/12/2030", "20/03/2026")
pharmacy = Pharmacy()
phone = Phone()
prescriptive = Prescriptive(50000, "Acetaminophen 500mg", "18/02/2023", "30/12/2030", "20/03/2026")
provider = Provider(["mk", "mk2", "mk3"])

print("\n", application.copies_number,
      "\n", client.name, 
      "\n", credit_card.card_number, 
      "\n", debit_card.card_number,
      "\n", dispensing.name,
      "\n", drug.name,
      "\n", free.name, 
      "\n", pharmacy, 
      "\n", phone, 
      "\n", prescriptive.name, 
      "\n", provider.article)