parliment = ["Adilabad (ST)",
"Bhuvangiri",
"Chevella",
"Hyderabad",
"Karimnagar",
"Khammam",
"Mahaboobabad (ST)"
"Mahbubnagar",
"Malkajgiri",
"Medak",
"Nagarkurnool (SC)",
"Nallagonda",
"Nizamabad",
"Peddapalle (SC)",
"Secunderabad",
"Warangal (SC)",
"Zaheerabad"]

for i in range(len(parliment)):
    res = parliment[i]+"|"+parliment[i]
    parliment[i]=res
print(parliment)
