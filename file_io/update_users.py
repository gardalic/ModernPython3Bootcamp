"""update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated."""
'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
import csv
