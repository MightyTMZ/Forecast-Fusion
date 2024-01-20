from django.db import models

# Create your models here.
# Here we create models to transfer ownership between users
# A FusionPod must be linked to at least one user so the user cannot be blank
# an example model class could be FusionPodOwnershipTransfer
"""
The person who bought the FusionPod from our official store will the default owner. 
** the person stored in the temperature device (FusionPod)'s will be the default owner upon production
the owner can then transfer ownership of the FusionPod(s) to another user. 
While the ownership transfer is pending, the owner of the FusionPod will still be the person who sent it. 
Once the ownership is accepted, then the user linked to the FusionPod will be updated
We do this to avoid a null field in the database
Once that happens we use over-the-air (OTA) using the backend server to transfer to update the user information in the hardware of the FusionPod 

"""