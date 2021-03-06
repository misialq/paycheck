from setuptools import setup, find_packages

setup(
    name='paycheck',
    version='0.0.3',
    author='Ben Kaehler',
    author_email='kaehler@gmail.com',
    description='Tools for testing q2-clawback',
    scripts=['paycheck/assets/run_traceable_dada_paired.R'],
    license='BSD-3-Clause',
    packages=find_packages(),
    package_data={'paycheck.tests': ['data/*']},
    entry_points={
        'console_scripts':
        ['paycheck_simulate=paycheck.simulate:simulate_all_samples',
         'pick_up_the_check=paycheck.simulate:simulate_missed_samples',
         'paycheck_cv=paycheck.cross_validate:cross_validate',
         'paycheck_shannon=paycheck.shannon:shannon',
         'paycheck_diversity=paycheck.shannon:diversity',
         'paycheck_cv_for_weights='
         'paycheck.cross_validate:cross_validate_for_weights',
         'paycheck_cv_average='
         'paycheck.cross_validate:cross_validate_average',
         'paycheck_generate_folds='
         'paycheck.cross_validate:generate_folds',
         'paycheck_cv_classifier='
         'paycheck.cross_validate:cross_validate_classifier']
    }
)
