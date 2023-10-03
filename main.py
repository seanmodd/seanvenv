from Foundation import *
from Contacts import *
import datetime





# Initialize the store and request access
store = CNContactStore.alloc().init()
keys_to_fetch = [CNContactIdentifierKey, "modificationDate", CNContactDatesKey]
predicate = CNContact.predicateForContactsMatchingName_("Aaftetlysaumma")
contacts, error = store.unifiedContactsMatchingPredicate_keysToFetch_error_(predicate, keys_to_fetch, None)

# Check if we have at least one contact
if contacts:
    contact = contacts[0]
    # Fetch existing date_modified custom field, if exists
    custom_dates = [x for x in contact.dates() if x.label() == "date_modified"]
    
    # Convert the modification date to datetime object
    modification_date_str = contact.valueForKey_("modificationDate")
    modification_date = datetime.datetime.strptime(modification_date_str, "%Y-%m-%d %H:%M:%S %z")
    
    # Convert the datetime object to string
    modification_date_str = modification_date.strftime("%Y-%m-%d %H:%M:%S %z")
    
    # Update or create the custom field
    if custom_dates:
        date = custom_dates[0]
        date.setValue_(modification_date_str)
    else:
        custom_date = CNLabeledValue.alloc().initWithLabel_value_("date_modified", modification_date_str)
        contact.setDates_([custom_date])

    # Save the updated contact
    save_request = CNSaveRequest.alloc().init()
    save_request.updateContact_(contact)


# Initialize the store and request access
store = CNContactStore.alloc().init()
keys_to_fetch = [CNContactIdentifierKey, "modificationDate", CNContactDatesKey]
predicate = CNContact.predicateForContactsMatchingName_("Aaftetlysaumma")
contacts, error = store.unifiedContactsMatchingPredicate_keysToFetch_error_(predicate, keys_to_fetch, None)

# Check if we have at least one contact
if contacts:
    contact = contacts[0]
    # Fetch existing date_modified custom field, if exists
    custom_dates = [x for x in contact.dates() if x.label() == "date_modified"]
    
    # Convert the modification date to datetime object
    modification_date_str = contact.valueForKey_("modificationDate")
    modification_date = datetime.datetime.strptime(modification_date_str, "%Y-%m-%d %H:%M:%S %z")
    
    # Convert the datetime object to string
    modification_date_str = modification_date.strftime("%Y-%m-%d %H:%M:%S %z")
    
    # Update or create the custom field
    if custom_dates:
        date = custom_dates[0]
        date.setValue_(modification_date_str)
    else:
        custom_date = CNLabeledValue.alloc().initWithLabel_value_("date_modified", modification_date_str)
        contact.setDates_([custom_date])

    # Save the updated contact

# Initialize the store and request access
store = CNContactStore.alloc().init()
keys_to_fetch = [CNContactIdentifierKey, "modificationDate", CNContactDatesKey]
predicate = CNContact.predicateForContactsMatchingName_("Aaftetlysaumma")
contacts, error = store.unifiedContactsMatchingPredicate_keysToFetch_error_(predicate, keys_to_fetch, None)

# Check if we have at least one contact
if contacts:
    contact = contacts[0]
    # Fetch existing date_modified custom field, if exists
    custom_dates = [x for x in contact.dates() if x.label() == "date_modified"]
    
    # Convert the modification date to datetime object
    modification_date_str = contact.valueForKey_("modificationDate")
    modification_date = datetime.datetime.strptime(modification_date_str, "%Y-%m-%d %H:%M:%S %z")
    
    # Convert the datetime object to string
    modification_date_str = modification_date.strftime("%Y-%m-%d %H:%M:%S %z")
    
    # Update or create the custom field
    if custom_dates:
        date = custom_dates[0]
        date.setValue_(modification_date_str)
    else:
        custom_date = CNLabeledValue.alloc().initWithLabel_value_("date_modified", modification_date_str)
        contact.setDates_([custom_date])

    # Save the updated contact
    save_request = CNSaveRequest.alloc().init()
    save_request.updateContact_(contact)
    store.executeSaveRequest_error_(save_request, None)

# q: what's the capital of italy?
# a: rome

# q: what's the capital of france?
# a: paris

# q: what's the capital of germany?
# a: berlin

# q: what's the capital of spain?
# a: madrid

# q: what's the capital of portugal?
# a: lisbon

# q: what's the capital of belgium?
# a: brussels

# q: what file type is this file?
# a: text

# q: what code language is in this file above?
# a: python

# q: why did you state that this file type is text if it's actually python?
# a: because python is a type of text

# q: is the file type text or python?
# a: python


