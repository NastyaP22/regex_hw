from pprint import pprint

import csv
import re

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for contact in contacts_list[1:]:
  fio = " ".join(contact[:3])
  fio_split = fio.split()
  id = 0
  for el in fio_split:
    contact[id] = el
    id += 1

dict = {}
for index, contact in enumerate(contacts_list[1:]):
  fi = " ".join(contact[:2])
  dict[index] = fi

fi_contacts_list = []
for fi in dict.values():
  fi_contacts_list.append(fi)

unique_contacts = set(fi_contacts_list)

doubles_list = []
for contact in unique_contacts:
  if fi_contacts_list.count(contact) > 1:
    doubles_list.append(contact)

for double_client in doubles_list:
  ids = []
  for contact in contacts_list:
    if contact[:2] == double_client.split():
      ids.append(contacts_list.index(contact))
  contacts_dicts = []
  for id in ids:
    contacts_dict = {'id': id, 0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
    contacts_dicts.append(contacts_dict)
    ind = 0
    for el in contacts_list[id]:
      contacts_dict[ind] = el
      ind += 1
  for index, el in enumerate(contacts_list[contacts_dicts[0]['id']]):
    if el == '':
      if contacts_dicts[0][index] != '':
        contacts_list[contacts_dicts[0]['id']][index] = contacts_dicts[0][index]
      else:
        contacts_list[contacts_dicts[0]['id']][index] = contacts_dicts[1][index]

for double in doubles_list:
  for contact in contacts_list:
    if double == " ".join(contact[:2]) and contact[5] == '':
      id = contacts_list.index(contact)
  del contacts_list[id]

pattern = r"(\+7|8)\s*[\(]*(\d{3})[\)\-]*\s*(\d{3})[\-]*(\d{2})[\-]*(\d{2})\s*\(*([доб.]*)\s*(\d+)*\)*"
replace = r"+7(\2)\3-\4-\5 \6\7"

for contact in contacts_list:
  for id, el in enumerate(contact):
    contact[id] = re.sub(pattern, replace, el)
  contact[5] = contact[5] = contact[5].strip()

pprint(contacts_list)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)