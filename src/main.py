#!/usr/bin/env python

if __name__ == '__main__':
    print('Hello world!')


    # Pull appointments from (GET) <mind-body>/public/v{version}/appointment/staffappointments
'''
{
  "PaginationResponse": {
    "RequestedLimit": 0,
    "RequestedOffset": 0,
    "PageSize": 0,
    "TotalResults": 0
  },
  "Appointments": [
    {
      "GenderPreference": "None",
      "Duration": 0,
      "ProviderId": "string",
      "Id": 0,
      "Status": "None",
      "StartDateTime": "2024-01-25T19:39:11.588Z",
      "EndDateTime": "2024-01-25T19:39:11.588Z",
      "Notes": "string",
      "PartnerExternalId": "string",
      "StaffRequested": true,
      "ProgramId": 0,
      "SessionTypeId": 0,
      "LocationId": 0,
      "StaffId": 0,
      "ClientId": "string",
      "FirstAppointment": true,
      "IsWaitlist": true,
      "WaitlistEntryId": 0,
      "ClientServiceId": 0,
      "Resources": [
        {
          "Id": 0,
          "Name": "string"
        }
      ],
      "AddOns": [
        {
          "Id": 0,
          "Name": "string",
          "StaffId": 0,
          "TypeId": 0
        }
      ],
      "OnlineDescription": "string"
    }
  ]
}
'''

# Pull appointments from Athena Health (GET) https://api.preview.platform.athenahealth.com/v1/{contextId}/1/fhir/dstu2/Appointment

