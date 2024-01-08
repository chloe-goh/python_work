guests = ['Ann', 'Beth', 'Cindy', 'Dilon']
guestlist = f"Hi {guests[2]}, you're invited to dinner at my place tonight!"
# print(guestlist)

unavailable = 'Cindy'
guests.remove(unavailable)
print(guests)
print(f"\n {unavailable} is not able to make it for dinner tonight.")
print(guestlist)