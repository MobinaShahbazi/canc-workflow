import datetime
import json
from khayyam import JalaliDatetime


def reform_info(input_obj):
    self_assessment = {}
    self_assessment['birth_month'] = input_obj['birth_month']
    self_assessment['birth_year'] = input_obj['birth_year']
    self_assessment['age'] = JalaliDatetime.now().year - input_obj['birth_year']
    self_assessment['province'] = input_obj['province']

    self_assessment['clinical_examination_history'] = input_obj['clinical_examination_history'] == "true"
    self_assessment['clinical_examination_month'] = input_obj.get('clinical_examination_month', 1)
    self_assessment['clinical_examination_year'] = input_obj.get('clinical_examination_year', 400)  # was born 1000 years ago if doesnt exist
    self_assessment['clinical_examination_result'] = input_obj.get('clinical_examination_result', '1')

    self_assessment['mammography_history'] = input_obj['mammography_history'] == "true"
    self_assessment['mammography_month'] = input_obj.get('mammography_month', 1)
    self_assessment['mammography_year'] = input_obj.get('mammography_year', 400)
    self_assessment['mammography_result'] = input_obj.get('mammography_result', '1')

    self_assessment['ultrasound_history'] = input_obj['ultrasound_history'] == "true"
    self_assessment['ultrasound_month'] = input_obj.get('ultrasound_month', 1)
    self_assessment['ultrasound_year'] = input_obj.get('ultrasound_year', 400)
    self_assessment['ultrasound_result'] = input_obj.get('ultrasound_result', '1')

    self_assessment['biopsy_history'] = input_obj['biopsy_history'] == "true"
    self_assessment['biopsy_month'] = input_obj.get('biopsy_month', 1)
    self_assessment['biopsy_year'] = input_obj.get('biopsy_year', 400)
    self_assessment['biopsy_result'] = input_obj.get('biopsy_result', '1')

    self_assessment['radiotherapy_history'] = input_obj['radiotherapy_history'] == "true"
    self_assessment['radiotherapy_month'] = input_obj.get('radiotherapy_month', 1)
    self_assessment['radiotherapy_year'] = input_obj.get('radiotherapy_year', 400)

    #  personal cancer info
    self_assessment['personal_cancer_history'] = input_obj['personal_cancer_history'] == 'true'

    #  --------------------------------breast--------------------------------
    self_assessment['personal_breast_cancer_history'] = input_obj.get('personal_breast_cancer_history', 'false') != "false"  # oniSide or twoSide
    self_assessment['personal_twoside_breast_cancer_history'] = input_obj.get('personal_breast_cancer_history', 'false') in ["oneSide", "twoSide"]  # check!!!!!!!!
    self_assessment['month_of_diagnose_by_breast_cancer'] = input_obj.get('month_of_diagnose_by_breast_cancer', 1)  # oneSide
    self_assessment['year_of_diagnose_by_breast_cancer'] = input_obj.get('year_of_diagnose_by_breast_cancer', 400)  # oneSide

    self_assessment['month_of_diagnose_by_breast_cancer_left'] = input_obj.get('month_of_diagnose_by_breast_cancer_left', 1)  # twoSide
    self_assessment['year_of_diagnose_by_breast_cancer_left'] = input_obj.get('year_of_diagnose_by_breast_cancer_left', 400)  # twoSide
    self_assessment['month_of_diagnose_by_breast_cancer_right'] = input_obj.get('month_of_diagnose_by_breast_cancer_right', 1)  # twoSide
    self_assessment['year_of_diagnose_by_breast_cancer_right'] = input_obj.get('year_of_diagnose_by_breast_cancer_right', 400)  # twoSide

    self_assessment['age_of_diagnose_by_breast_cancer'] = input_obj.get('year_of_diagnose_by_breast_cancer', 3000) - input_obj.get('birth_year')  # oneSide
    self_assessment['age_of_diagnose_by_breast_cancer_left'] = input_obj.get('year_of_diagnose_by_breast_cancer_left', 3000) - input_obj.get('birth_year')
    self_assessment['age_of_diagnose_by_breast_cancer_right'] = input_obj.get('year_of_diagnose_by_breast_cancer_right', 3000) - input_obj.get('birth_year')

    # #  --------------------------------ovary--------------------------------
    self_assessment['personal_ovary_cancer_history'] = input_obj.get('personal_ovary_cancer_history', 'false') == 'true'
    self_assessment['month_of_diagnose_by_ovary_cancer'] = input_obj.get('month_of_diagnose_by_ovary_cancer', 1)
    self_assessment['year_of_diagnose_by_ovary_cancer'] = input_obj.get('year_of_diagnose_by_ovary_cancer', 400)
    self_assessment['age_of_diagnose_by_ovary_cancer'] = input_obj.get('year_of_diagnose_by_ovary_cancer', 3000) - input_obj.get('birth_year')

    #  --------------------------------pancreatic--------------------------------
    self_assessment['personal_pancreatic_cancer_history'] = input_obj.get('personal_pancreatic_cancer_history', 'false') == 'true'
    self_assessment['month_of_diagnose_by_pancreatic_cancer'] = input_obj.get('month_of_diagnose_by_pancreatic_cancer', 1)
    self_assessment['year_of_diagnose_by_pancreatic_cancer'] = input_obj.get('year_of_diagnose_by_pancreatic_cancer', 400)
    self_assessment['age_of_diagnose_by_pancreatic_cancer'] = input_obj.get('year_of_diagnose_by_pancreatic_cancer',3000) - input_obj.get('birth_year')

    # #  --------------------------------other--------------------------------
    self_assessment['personal_other_cancer_history'] = input_obj.get('personal_other_cancer_history', 'false') == 'true'
    self_assessment['month_of_diagnose_by_other_cancer'] = input_obj.get('month_of_diagnose_by_other_cancer', 1)
    self_assessment['year_of_diagnose_by_other_cancer'] = input_obj.get('year_of_diagnose_by_other_cancer', 400)


    #  familial cancer info
    self_assessment['familial_cancer_history'] = input_obj['familial_cancer_history'] == 'true'
    deg = {
        't1': 1,
        't2': 2,
        't3': 3,
    }

    # #  --------------------------------breast--------------------------------
    self_assessment['familial_breast_cancer_history'] = input_obj.get('familial_breast_cancer_history', 'false') == 'true'
    self_assessment['familial_breast_cancer_list'] = []
    if input_obj.get('familial_breast_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_breast_cancer_list', []):
            if entry.get('familial_breast_cancer_side') == "oneSide":
                self_assessment['familial_breast_cancer_list'].append(
                    {
                        'side': entry.get('familial_breast_cancer_side'),
                        'degree': deg[entry.get('familial_breast_cancer_degree')],
                        'age_of_diagnose': entry.get('familial_breast_cancer_age')
                    }
                )
            elif entry.get('familial_breast_cancer_side') == "twoSide":
                self_assessment['familial_breast_cancer_list'].append(
                    {
                        'side': entry.get('familial_breast_cancer_side'),
                        'degree': deg[entry.get('familial_breast_cancer_degree')],
                        'age_of_diagnose_right': entry.get('familial_breast_cancer_age_right'),
                        'age_of_diagnose_left': entry.get('familial_breast_cancer_age_left')
                    }
                )
    #  --------------------------------ovary--------------------------------
    self_assessment['familial_ovary_cancer_history'] = input_obj.get('familial_ovary_cancer_history', 'false') == 'true'
    self_assessment['familial_ovary_cancer_list'] = []
    if input_obj.get('familial_ovary_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_ovary_cancer_list', []):
            self_assessment['familial_ovary_cancer_list'].append(
                {
                    'degree': deg[entry.get('familial_ovary_cancer_degree')],
                    'age_of_diagnose': entry.get('familial_ovary_cancer_age')
                }
            )
    #  --------------------------------pancreatic--------------------------------
    self_assessment['familial_pancreatic_cancer_history'] = input_obj.get('familial_pancreatic_cancer_history', 'false') == 'true'
    self_assessment['familial_pancreatic_cancer_list'] = []
    if input_obj.get('familial_pancreatic_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_pancreatic_cancer_list', []):
            self_assessment['familial_pancreatic_cancer_list'].append(
                {
                    'degree': deg[entry.get('familial_pancreatic_cancer_degree')],
                    'age_of_diagnose': entry.get('familial_pancreatic_cancer_age')
                }
            )
    #  --------------------------------prostate--------------------------------
    self_assessment['familial_prostate_cancer_history'] = input_obj.get('familial_prostate_cancer_history', 'false') == 'true'
    self_assessment['familial_prostate_cancer_list'] = []
    if input_obj.get('familial_prostate_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_prostate_cancer_list', []):
            self_assessment['familial_prostate_cancer_list'].append(
                {
                    'degree': deg[entry.get('familial_prostate_cancer_degree')],
                    'age_of_diagnose': entry.get('familial_prostate_cancer_age')
                }
            )
    #  --------------------------------men_breast--------------------------------
    self_assessment['familial_men_breast_cancer_history'] = input_obj.get('familial_men_breast_cancer_history', 'false') == 'true'
    self_assessment['familial_men_breast_cancer_list'] = []
    if input_obj.get('familial_men_breast_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_men_breast_cancer_list', []):
            self_assessment['familial_men_breast_cancer_list'].append(
                {
                    'degree': deg[entry.get('familial_men_breast_cancer_degree')],
                    'age_of_diagnose': entry.get('familial_men_breast_cancer_age')
                }
            )
    #  --------------------------------other--------------------------------
    self_assessment['familial_other_cancer_history'] = input_obj.get('familial_other_cancer_history', 'false') == 'true'
    self_assessment['familial_other_cancer_list'] = []
    if input_obj.get('familial_other_cancer_history', 'false') == 'true':
        for entry in input_obj.get('familial_other_cancer_list', []):
            self_assessment['familial_other_cancer_list'].append(
                {
                    'degree': deg[entry.get('familial_other_cancer_degree')],
                    'age_of_diagnose': entry.get('familial_other_cancer_age')
                }
            )

    if input_obj['biopsy_history'] == 'true' and input_obj['biopsy_result'] == '4':
        threshold_age = input_obj['biopsy_year'] - input_obj['birth_year']
    else:
        threshold_age = 1000

    self_assessment['threshold_age'] = threshold_age

    self_assessment['self_assessment_month'] = JalaliDatetime.now().month
    self_assessment['self_assessment_year'] = JalaliDatetime.now().year


    self_assessment['q18'] = input_obj['q18']
    self_assessment['q19'] = input_obj['q19']
    self_assessment['q20'] = input_obj['q20']
    self_assessment['q21'] = input_obj['q21']
    self_assessment['q22'] = input_obj['q22']
    self_assessment['q23'] = input_obj['q23']

    self_assessment['history_a'] = False
    self_assessment['history_b'] = False
    self_assessment['history_c'] = False
    self_assessment['history_d'] = False
    self_assessment['history_e'] = False
    self_assessment['history_f4'] = False
    self_assessment['history_f5'] = False
    self_assessment['history_g'] = False

    self_assessment['age_a'] = 1000
    self_assessment['bool_b'] = False
    self_assessment['age_c'] = 1000
    self_assessment['age_d'] = 1000
    self_assessment['age_e'] = 1000
    self_assessment['age_f'] = 1000

    total_brest_cancer_number = len(self_assessment.get('familial_breast_cancer_list', []))
    if self_assessment['personal_breast_cancer_history'] == 'true':
        total_brest_cancer_number += 1
    self_assessment['total_brest_cancer_number'] = total_brest_cancer_number

    total_cancer_number = len(self_assessment.get('familial_breast_cancer_list', [])) + len(self_assessment.get('familial_ovary_cancer_list', [])) + len(self_assessment.get('familial_pancreatic_cancer_list', [])) + len(self_assessment.get('familial_prostate_cancer_list', [])) + len(self_assessment.get('familial_men_breast_cancer_list', [])) + len(self_assessment.get('familial_other_cancer_list', []))
    if self_assessment['personal_breast_cancer_history'] == 'true':
        total_cancer_number += 1
    if self_assessment['personal_ovary_cancer_history'] == 'true':
        total_cancer_number += 1
    if self_assessment['personal_pancreatic_cancer_history'] == 'true':
        total_cancer_number += 1
    if self_assessment['personal_other_cancer_history'] == 'true':
        total_cancer_number += 1
    self_assessment['total_cancer_number'] = total_cancer_number

    return self_assessment
