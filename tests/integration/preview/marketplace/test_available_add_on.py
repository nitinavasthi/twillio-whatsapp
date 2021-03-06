# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AvailableAddOnTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.marketplace.available_add_ons(sid="XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/marketplace/AvailableAddOns/XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "VoiceBase High Accuracy Transcription",
                "description": "Automatic Transcription and Keyword Extract...",
                "pricing_type": "per minute",
                "configuration_schema": {
                    "type": "object",
                    "properties": {
                        "bad_words": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "bad_words"
                    ]
                },
                "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "extensions": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions"
                }
            }
            '''
        ))

        actual = self.client.preview.marketplace.available_add_ons(sid="XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.marketplace.available_add_ons.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/marketplace/AvailableAddOns',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "available_add_ons": [
                    {
                        "sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "VoiceBase High Accuracy Transcription",
                        "description": "Automatic Transcription and Keyword Extract...",
                        "pricing_type": "per minute",
                        "configuration_schema": {
                            "type": "object",
                            "properties": {
                                "bad_words": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "bad_words"
                            ]
                        },
                        "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "extensions": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://preview.twilio.com/marketplace/AvailableAddOns?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/marketplace/AvailableAddOns?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "available_add_ons"
                }
            }
            '''
        ))

        actual = self.client.preview.marketplace.available_add_ons.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "available_add_ons": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://preview.twilio.com/marketplace/AvailableAddOns?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/marketplace/AvailableAddOns?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "available_add_ons"
                }
            }
            '''
        ))

        actual = self.client.preview.marketplace.available_add_ons.list()

        self.assertIsNotNone(actual)
