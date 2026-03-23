# def analyze_password(
#     password,
#     min_length=8,
#     require_digit=True,
#     require_upper=True,
#     require_symbol=False,
#     banned_words=None
# ):
#     if banned_words is None:
#         banned_words = ['heslo', 'password', '1234']
#
#     symbols = "!@#$%^&*()-_=+[]{};:,.?"
#     missing_rules = []
#
#     active_rules = 0
#     passed_rules = 0
#
#     # minimální délka
#     active_rules += 1
#     if len(password) >= min_length:
#         passed_rules += 1
#     else:
#         missing_rules.append("min_length")
#
#     # číslice
#     if require_digit:
#         active_rules += 1
#         if any(char.isdigit() for char in password):
#             passed_rules += 1
#         else:
#             missing_rules.append("digit")
#
#     # velké písmeno
#     if require_upper:
#         active_rules += 1
#         if any(char.isupper() for char in password):
#             passed_rules += 1
#         else:
#             missing_rules.append("upper")
#
#     # symbol
#     if require_symbol:
#         active_rules += 1
#         if any(char in symbols for char in password):
#             passed_rules += 1
#         else:
#             missing_rules.append("symbol")
#
#     # zakázaná slova
#     active_rules += 1
#     password_lower = password.lower()
#     if any(word.lower() in password_lower for word in banned_words):
#         missing_rules.append("banned_word")
#     else:
#         passed_rules += 1
#
#     score_percent = int((passed_rules / active_rules) * 100)
#     is_strong = len(missing_rules) == 0
#
#     return is_strong, score_percent, missing_rules
#
#
# print(analyze_password(
#     "Eva_18062012!",
#     require_digit=True,
#     require_upper=True,
#     require_symbol=True,
#     banned_words=None,
#     min_length=8
# ))

######################################################























