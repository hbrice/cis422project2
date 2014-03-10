import dj_database_url

TEST_DATABASES = {
    'default': dj_database_url.config(env='TEST_DATABASE_URL')
}

# replace path below to point to HerokuTestSuiteRunner class
TEST_RUNNER = './lunarshiftapp/test_suite_runner.py'# 'python.path.to.test_suite_runner.HerokuTestSuiteRunner'
