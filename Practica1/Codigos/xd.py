import re
patronTupla= r"\((?:[a-zA-Z0-9]+(?:,[a-zA-Z0-9]+)*)\)(?:,\((?:[a-zA-Z0-9]+(?:,[a-zA-Z0-9]+)*)\))*"
linea = "(1,2),(3,4),(5,6)"

patronComillas = r"\"(?:[a-zA-Z0-9]+(?:,[a-zA-Z0-9]+)*)\"(?:,\"(?:[a-zA-Z0-9]+(?:,[a-zA-Z0-9]+)*)\")*"
linea2 = "\"1,2\",\"3,4\",\"5,6\""

if re.fullmatch(patronTupla, linea):
    print("Matched tupla")
if re.fullmatch(patronComillas, linea2):
    print("Matched comillas")
