from logo import logo

print(logo)

auction_dict = []


def blind_auction(name_person, bid_person, ):
    new_bid = {
        "name": name_person,
        "bid": bid_person
    }
    auction_dict.append(new_bid)


next_person = True

while next_person:
    name_p = input("What is your name?: ")
    bid_p = input("What's your bid?: $")
    next_p = input("Are there any other bidders? Type (yes) or (no).\n")
    if next_p == "no":
        next_person = False

    blind_auction(name_person=name_p, bid_person=bid_p)

max_bid = 0
person_with_max_bid = ""

for dict_auc in auction_dict:
    int_bid = int(dict_auc["bid"])
    if int_bid >= max_bid:
        max_bid = int_bid
        person_with_max_bid = dict_auc["name"]

print(f"The winner is {person_with_max_bid} with a bid of ${max_bid}")
