#!/usr/bin/env python3
"""Regression tests: false-positive tickers, event identity and token boundaries."""
import unittest

from youtube_title_relevance import company_in_title, event_relevant, groups_relevant, has_phrase


def event(entity, ticker, terms, entity_type="company"):
    return dict(entity=entity, ticker=ticker, entity_type=entity_type,
                youtube_event_terms=terms)


class TitleRelevanceTests(unittest.TestCase):
    def test_token_boundary(self):
        self.assertTrue(has_phrase("BP shares slump", "BP"))
        self.assertFalse(has_phrase("CBP report", "BP"))
        self.assertFalse(has_phrase("hardware", "war"))
        self.assertTrue(has_phrase("台积电上涨", "台积电"))

    def test_bp_health_must_not_count(self):
        bp = event("BP PLC", "BP", ["BP", "Gulf", "hurricane"])
        self.assertFalse(event_relevant("Check your BP: doctor explains blood pressure", bp))
        self.assertFalse(event_relevant("I got the emperor conduit BP", bp))
        self.assertFalse(event_relevant("BP stocks jump on unrelated news", bp))
        self.assertTrue(event_relevant("BP halts oil production in Gulf of Mexico after hurricane", bp))

    def test_microsoft_unrelated_video_must_not_count(self):
        ms = event("MICROSOFT CORP", "MSFT", ["Microsoft", "Chevron", "power"])
        self.assertFalse(event_relevant("Microsoft Built a Magnetic USB-C Port!", ms))
        self.assertFalse(event_relevant("Microsoft Stock Analysis: How High?", ms))
        self.assertFalse(event_relevant("Nvidia Apple MSFT stocks roundup", ms))
        self.assertTrue(event_relevant("Microsoft Chevron announce 20-year data center power deal", ms))

    def test_broad_fallback_company_only_not_event(self):
        ts = event("TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD", "TSM",
                   ["GlobalFoundries", "TSMC", "interposer", "packaging"])
        self.assertFalse(event_relevant("TSMC hits record third quarter revenue", ts))
        self.assertFalse(event_relevant("Taiwan Semiconductor Stock Analysis", ts))
        self.assertTrue(event_relevant("TSMC GlobalFoundries interposer deal for AI chips", ts))

    def test_company_and_event_for_starbucks(self):
        sb = event("STARBUCKS CORP", "SBUX", ["Starbucks", "Chipotle", "takeover"])
        self.assertFalse(event_relevant("Chipotle jumps on takeover rumours", sb))
        self.assertTrue(event_relevant("Starbucks reportedly considers Chipotle takeover", sb))

    def test_generic_event_terms_need_two(self):
        dal = event("DELTA AIR LINES, INC.", "DAL",
                    ["earnings", "guidance", "fuel", "profit"])
        self.assertFalse(event_relevant("Delta Earnings Preview", dal))
        self.assertTrue(event_relevant("Delta airline earnings fall as fuel costs surge", dal))

    def test_cjk_and_ticker_entity_focus(self):
        self.assertFalse(groups_relevant("Why I monitor my BP daily",
                                         [["BP", "BP PLC"]], "BP PLC", "BP"))
        self.assertTrue(groups_relevant("BP oil and energy earnings drop",
                                        [["BP", "BP PLC"]], "BP PLC", "BP"))
        self.assertTrue(groups_relevant("台积电先进封装订单", [["TSMC", "台积电"]],
                                        "TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD", "TSM"))
        self.assertFalse(groups_relevant("Apple pie recipe", [["Apple"]], "APPLE INC.", "AAPL"))
        self.assertTrue(groups_relevant("Apple iPhone 18 production cut", [["Apple"]], "APPLE INC.", "AAPL"))

    def test_macro_and_technical_alias(self):
        rate = event("Federal Reserve / Rates", None, ["Shelton", "Treasury", "Bessent"], "macro")
        self.assertFalse(event_relevant("Bessent makes unrelated remarks", rate))
        self.assertTrue(event_relevant("Shelton joins Bessent as Treasury adviser", rate))
        self.assertTrue(event_relevant("NVIDIA's Critical Bug Fix", event(
            "NVIDIA CORP", "NVDA", ["NVIDIA", "GPU", "vulnerability"])))


if __name__ == "__main__":
    unittest.main()
