import requests
import json


# 인증 정보
data = {
    'grant_type': 'client_credentials',
    'client_id': 'l7d5b3a151ec87415f8159c79324057eb7',
    'client_secret': '9962a2fa6b994452859644acbc4d9362'
}

# access token 얻기

acc_url= "https://apis-sandbox.fedex.com/track/v1/associatedshipments"
response = requests.post(acc_url, data=data)

# 응답 검증
if response.status_code == 200:
    access_token = response.json()['access_token']
else:
    print('Error: ', response.json())


headers = {
    'Content-Type': 'application/json',
    'X-locale': 'en_US',
    #여기서 왜 안되는지 모르겠네 
    'Authorization': f'Bearer {access_token}'
}




url = 'https://apis-sandbox.fedex.com/rate/v1/rates/quotes'

Payload = {
  "accountNumber": {
    "value": "895953296"
  },
  "rateRequestControlParameters": {
    "returnTransitTimes": False,
    "servicesNeededOnRateFailure": True,
    "variableOptions": "FREIGHT_GUARANTEE",
    "rateSortOrder": "SERVICENAMETRADITIONAL"
  },
  "requestedShipment": {
    "shipper": {
      "address": {
        "streetLines": [
          "1550 Union Blvd",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "TN",
        "postalCode": "65247",
        "countryCode": "US",
        "residential": False
      }
    },
    "recipient": {
      "address": {
        "streetLines": [
          "1550 Union Blvd",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "TN",
        "postalCode": "65247",
        "countryCode": "US",
        "residential": False
      }
    },
    "serviceType": "STANDARD_OVERNIGHT",
    "emailNotificationDetail": {
      "recipients": [
        {
          "emailAddress": "string",
          "notificationEventType": [
            "ON_DELIVERY"
          ],
          "smsDetail": {
            "phoneNumber": "string",
            "phoneNumberCountryCode": "string"
          },
          "notificationFormatType": "HTML",
          "emailNotificationRecipientType": "BROKER",
          "notificationType": "EMAIL",
          "locale": "string"
        }
      ],
      "personalMessage": "string",
      "PrintedReference": {
        "printedReferenceType": "BILL_OF_LADING",
        "value": "string"
      }
    },
    "preferredCurrency": "USD",
    "rateRequestType": [
      "ACCOUNT",
      "LIST"
    ],
    "shipDateStamp": "2019-09-05",
    "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
    "requestedPackageLineItems": [
      {
        "subPackagingType": "BAG",
        "groupPackageCount": 1,
        "contentRecord": [
          {
            "itemNumber": "string",
            "receivedQuantity": 0,
            "description": "string",
            "partNumber": "string"
          }
        ],
        "declaredValue": {
          "amount": "100",
          "currency": "USD"
        },
        "weight": {
          "units": "LB",
          "value": 22
        },
        "dimensions": {
          "length": 10,
          "width": 8,
          "height": 2,
          "units": "IN"
        },
        "variableHandlingChargeDetail": {
          "rateType": "ACCOUNT",
          "percentValue": 0,
          "rateLevelType": "BUNDLED_RATE",
          "fixedValue": {
            "amount": "100",
            "currency": "USD"
          },
          "rateElementBasis": "NET_CHARGE"
        },
        "packageSpecialServices": {
          "specialServiceTypes": [
            "DANGEROUS_GOODS"
          ],
          "signatureOptionType": [
            "NO_SIGNATURE_REQUIRED"
          ],
          "alcoholDetail": {
            "alcoholRecipientType": "LICENSEE",
            "shipperAgreementType": "Retailer"
          },
          "dangerousGoodsDetail": {
            "offeror": "Offeror Name",
            "accessibility": "ACCESSIBLE",
            "emergencyContactNumber": "3268545905",
            "options": [
              "BATTERY"
            ],
            "containers": [
              {
                "offeror": "Offeror Name",
                "hazardousCommodities": [
                  {
                    "quantity": {
                      "quantityType": "GROSS",
                      "amount": 0,
                      "units": "LB"
                    },
                    "innerReceptacles": [
                      {
                        "quantity": {
                          "quantityType": "GROSS",
                          "amount": 0,
                          "units": "LB"
                        }
                      }
                    ],
                    "options": {
                      "labelTextOption": "Override",
                      "customerSuppliedLabelText": "LabelText"
                    },
                    "description": {
                      "sequenceNumber": 0,
                      "processingOptions": [
                        "INCLUDE_SPECIAL_PROVISIONS"
                      ],
                      "subsidiaryClasses": "subsidiaryClass",
                      "labelText": "labelText",
                      "technicalName": "technicalName",
                      "packingDetails": {
                        "packingInstructions": "instruction",
                        "cargoAircraftOnly": False
                      },
                      "authorization": "Authorization Information",
                      "reportableQuantity": False,
                      "percentage": 10,
                      "id": "ID",
                      "packingGroup": "DEFAULT",
                      "properShippingName": "ShippingName",
                      "hazardClass": "hazardClass"
                    }
                  }
                ],
                "numberOfContainers": 10,
                "containerType": "Copper Box",
                "emergencyContactNumber": {
                  "areaCode": "202",
                  "extension": "3245",
                  "countryCode": "US",
                  "personalIdentificationNumber": "9545678",
                  "localNumber": "23456"
                },
                "packaging": {
                  "count": 20,
                  "units": "Liter"
                },
                "packingType": "ALL_PACKED_IN_ONE",
                "radioactiveContainerClass": "EXCEPTED_PACKAGE"
              }
            ],
            "packaging": {
              "count": 20,
              "units": "Liter"
            }
          },
          "packageCODDetail": {
            "codCollectionAmount": {
              "amount": 12.45,
              "currency": "USD"
            },
            "codCollectionType": "ANY"
          },
          "pieceCountVerificationBoxCount": 0,
          "batteryDetails": [
            {
              "material": "LITHIUM_METAL",
              "regulatorySubType": "IATA_SECTION_II",
              "packing": "CONTAINED_IN_EQUIPMENT"
            }
          ],
          "dryIceWeight": {
            "units": "LB",
            "value": 10
          }
        }
      }
    ],
    "documentShipment": False,
    "variableHandlingChargeDetail": {
      "rateType": "ACCOUNT",
      "percentValue": 0,
      "rateLevelType": "BUNDLED_RATE",
      "fixedValue": {
        "amount": "100",
        "currency": "USD"
      },
      "rateElementBasis": "NET_CHARGE"
    },
    "packagingType": "YOUR_PACKAGING",
    "totalPackageCount": 3,
    "totalWeight": 87.5,
    "shipmentSpecialServices": {
      "returnShipmentDetail": {
        "returnType": "PRINT_RETURN_LABEL"
      },
      "deliveryOnInvoiceAcceptanceDetail": {
        "recipient": {
          "accountNumber": {
            "value": 123456789
          },
          "address": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 30"
            ],
            "countryCode": "US"
          },
          "contact": {
            "companyName": "FedEx",
            "faxNumber": "9013577890",
            "personName": "John Taylor",
            "phoneNumber": "9013577890"
          }
        }
      },
      "internationalTrafficInArmsRegulationsDetail": {
        "licenseOrExemptionNumber": "432345"
      },
      "pendingShipmentDetail": {
        "pendingShipmentType": "EMAIL",
        "processingOptions": {
          "options": [
            "ALLOW_MODIFICATIONS"
          ]
        },
        "recommendedDocumentSpecification": {
          "types": [
            "ANTIQUE_STATEMENT_EUROPEAN_UNION"
          ]
        },
        "emailLabelDetail": {
          "recipients": [
            {
              "emailAddress": "string",
              "optionsRequested": {
                "options": [
                  "PRODUCE_PAPERLESS_SHIPPING_FORMAT"
                ]
              },
              "role": "SHIPMENT_COMPLETOR",
              "locale": {
                "country": "string",
                "language": "string"
              }
            }
          ],
          "message": "string"
        },
        "documentReferences": [
          {
            "documentType": "CERTIFICATE_OF_ORIGIN",
            "customerReference": "string",
            "description": "ShippingDocumentSpecification",
            "documentId": "98123"
          }
        ],
        "expirationTimeStamp": "2012-12-31",
        "shipmentDryIceDetail": {
          "totalWeight": {
            "units": "LB",
            "value": 10
          },
          "packageCount": 12
        }
      },
      "holdAtLocationDetail": {
        "locationId": "YBZA",
        "locationContactAndAddress": {
          "address": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "38127",
            "countryCode": "US",
            "residential": False
          },
          "contact": {
            "personName": "person name",
            "emailAddress": "email address",
            "phoneNumber": "phone number",
            "phoneExtension": "phone extension",
            "companyName": "company name",
            "faxNumber": "fax number"
          }
        },
        "locationType": "FEDEX_ONSITE"
      },
      "shipmentCODDetail": {
        "addTransportationChargesDetail": {
          "rateType": "ACCOUNT",
          "rateLevelType": "BUNDLED_RATE",
          "chargeLevelType": "CURRENT_PACKAGE",
          "chargeType": "COD_SURCHARGE"
        },
        "codRecipient": {
          "accountNumber": {
            "value": 123456789
          }
        },
        "remitToName": "FedEx",
        "codCollectionType": "ANY",
        "financialInstitutionContactAndAddress": {
          "address": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "38127",
            "countryCode": "US",
            "residential": False
          },
          "contact": {
            "personName": "person name",
            "emailAddress": "email address",
            "phoneNumber": "phone number",
            "phoneExtension": "phone extension",
            "companyName": "company name",
            "faxNumber": "fax number"
          }
        },
        "returnReferenceIndicatorType": "INVOICE"
      },
      "shipmentDryIceDetail": {
        "totalWeight": {
          "units": "LB",
          "value": 10
        },
        "packageCount": 12
      },
      "internationalControlledExportDetail": {
        "type": "DEA_036"
      },
      "homeDeliveryPremiumDetail": {
        "phoneNumber": {
          "areaCode": "areaCode",
          "extension": "extension",
          "countryCode": "countryCode",
          "personalIdentificationNumber": "personalIdentificationNumber",
          "localNumber": "localNumber"
        },
        "shipTimestamp": "2020-04-24",
        "homedeliveryPremiumType": "APPOINTMENT"
      },
      "specialServiceTypes": [
        "BROKER_SELECT_OPTION"
      ]
    },
    "customsClearanceDetail": {
      "brokers": [
        {
          "broker": {
            "accountNumber": {
              "value": 123456789
            },
            "address": None,
            "contact": None
          },
          "type": "EXPORT",
          "brokerCommitTimestamp": "2019-07-22",
          "brokerCommitDayOfWeek": "SUNDAY",
          "brokerLocationId": "brokerLocationId",
          "brokerAddress": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "90210",
            "countryCode": "US",
            "residential": False,
            "classification": "residential",
            "geographicCoordinates": "geographicCoordinates",
            "urbanizationCode": "code",
            "countryName": "India"
          },
          "brokerToDestinationDays": 10
        }
      ],
      "commercialInvoice": {
        "shipmentPurpose": "GIFT"
      },
      "freightOnValue": "CARRIER_RISK",
      "dutiesPayment": {
        "payor": {
          "responsibleParty": {
            "address": {
              "streetLines": [
                "10 FedEx Parkway",
                "Suite 302"
              ],
              "city": "Beverly Hills",
              "stateOrProvinceCode": "CA",
              "postalCode": "90210",
              "countryCode": "US",
              "residential": False
            },
            "contact": {
              "personName": "John Taylor",
              "emailAddress": "sample@company.com",
              "phoneNumber": "1234567890",
              "phoneExtension": "phone extension",
              "companyName": "Fedex",
              "faxNumber": "fax number"
            },
            "accountNumber": {
              "value": "123456789"
            }
          }
        },
        "paymentType": "SENDER"
      },
      "commodities": [
        {
          "description": "DOCUMENTS",
          "weight": {
            "units": "LB",
            "value": 22
          },
          "quantity": 1,
          "customsValue": {
            "amount": "100",
            "currency": "USD"
          },
          "unitPrice": {
            "amount": "100",
            "currency": "USD"
          },
          "numberOfPieces": 1,
          "countryOfManufacture": "US",
          "quantityUnits": "PCS",
          "name": "DOCUMENTS",
          "harmonizedCode": "080211",
          "partNumber": "P1"
        }
      ]
    },
    "groupShipment": True,
    "serviceTypeDetail": {
      "carrierCode": "FDXE",
      "description": "string",
      "serviceName": "string",
      "serviceCategory": "string"
    },
    "smartPostInfoDetail": {
      "ancillaryEndorsement": "ADDRESS_CORRECTION",
      "hubId": "5531",
      "indicia": "MEDIA_MAIL",
      "specialServices": "USPS_DELIVERY_CONFIRMATION"
    },
    "expressFreightDetail": {
      "bookingConfirmationNumber": "string",
      "shippersLoadAndCount": 0
    },
    "groundShipment": False
  },
  "carrierCodes": [
    "FDXE"
  ]
}



try:
    response = requests.post(url, data=Payload, headers=headers)
    print("코드: ", response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)
