#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:
#
# Author:
#
# Created:     09/07/2020
# Copyright:   (c)  2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from unittest import TestLoader, TestSuite
import HtmlTestRunner

import profil_Admin_FI_navbar, profil_Admin_EdF, profil_Admin_Statistiques, profil_Admin_AnalyseSitupasse, profil_Admin_adminMetier

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H%M%S")

#profil admin
Admin_nvbar_FI = TestLoader().loadTestsFromTestCase(profil_Admin_FI_navbar.FicheInc)
Admin_edf = TestLoader().loadTestsFromTestCase(profil_Admin_EdF.EcartDeFrequence)
Admin_analyseSitupasse = TestLoader().loadTestsFromTestCase(profil_Admin_AnalyseSitupasse.AnalyseSituationPassee)
Admin_statistique = TestLoader().loadTestsFromTestCase(profil_Admin_Statistiques.Statistiques)
Admin_admin_metier = TestLoader().loadTestsFromTestCase(profil_Admin_adminMetier.Administration_Metier)

suite = TestSuite([Admin_nvbar_FI, Admin_edf, Admin_analyseSitupasse, Admin_statistique, Admin_admin_metier])

h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport"+str(dt_string), add_timestamp=False).run(suite)