## Sign Out
Signing out of an account removes a users account from the device they are logged in to. Users will not be able to access their account on that device until they log in again.

### Auto-logout
Automated, time-based sign out is likely to lead to users losing decryption keys so we do not want to consider introducing automated signout at this time.

### Placement
Sign out is a destructive action and as such should not be easy to do. However, if a user has made the decision to sign out of their app, it should not be hard to do. 
* Users should be able to find Sign Out from Settings. 
* Users should not be able to access Sign Out directly from the home screen.

**September 29, 2022**
Currently, all but our Android app have Sign Out in a place that does not follow this Prodcut Strategy. We will need to consider and update the designs of our product when makes sense - not as a matter of urgency. 
There are open issues in all our repo's that request moving this button: These will be closed, quoting this strategy once it has been reviewed internally.
